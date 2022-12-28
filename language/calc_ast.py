from dataclasses import dataclass, field
from typing import Dict, Union, List, Optional, Iterator
import numpy as np
import networkx as nx
from .errors import ProgramNameError


Literal = int | float | np.ndarray


@dataclass
class StatementResult:
    text: str
    value: Optional[Literal]

    def name(self):
        return self.text


@dataclass
class AssignmentResult:
    text: str
    target: str
    value: Optional[Literal]

    def name(self):
        return self.target


AnyResult = StatementResult | AssignmentResult


@dataclass
class ProgramResults:
    results: List[StatementResult | AssignmentResult]
    context: "ExecContext"

    @property
    def last_result(self):
        return self.results[-1] if self.results else None


@dataclass
class Unknown:
    text: str


@dataclass
class ID:
    name: str

    def get_deps(self) -> List[str]:
        return [self.name]

    def execute(self, ctx: "ExecContext"):
        return ctx.get_value(self.name)


@dataclass
class Assignment:
    text: str
    target: ID
    expression: "Expression"

    def get_deps(self) -> List[str]:
        return self.expression.get_deps()

    def execute(self, ctx: "ExecContext"):
        return AssignmentResult(
            self.text, self.target.name, self.expression.execute(ctx)
        )


@dataclass
class Statement:
    text: str
    expression: "Expression"

    def get_deps(self) -> List[str]:
        return self.expression.get_deps()

    def execute(self, ctx: "ExecContext"):
        return StatementResult(self.text, self.expression.execute(ctx))


@dataclass
class Value:
    literal: int | float
    unit: str

    def get_deps(self) -> List[str]:
        return []

    def execute(self, ctx: "ExecContext"):
        return self.literal


@dataclass
class BinOp:
    lhs: "Expression"
    op: str
    rhs: "Expression"

    def get_deps(self) -> List[str]:
        return self.lhs.get_deps() + self.rhs.get_deps()

    def execute(self, ctx: "ExecContext"):
        lhs = self.lhs.execute(ctx)
        rhs = self.rhs.execute(ctx)

        if self.op == "+":
            return lhs + rhs
        if self.op == "-":
            return lhs - rhs
        if self.op == "*":
            return lhs * rhs
        if self.op == "/":
            return lhs / rhs
        raise RuntimeError(f"unknown operator {self.op}")


@dataclass
class Range:
    bottom: "Expression"
    top: "Expression"

    def get_deps(self) -> List[str]:
        return self.bottom.get_deps() + self.top.get_deps()

    def execute(self, ctx: "ExecContext") -> np.ndarray:
        bottom = self.bottom.execute(ctx)
        top = self.top.execute(ctx)
        if bottom > top:
            bottom, top = top, bottom
        return np.random.rand(100000) * (top - bottom) + bottom


Expression = BinOp | Value | Range | ID


@dataclass
class Program:
    statements: List[Union[Assignment, Statement]]

    def execute(self, ctx: Optional["ExecContext"] = None):
        """
        Perf notes:
        - ideally, use numpy/etc to compute in bulk
        """

        ctx = ExecContext() if ctx is None else ctx.copy()

        if not self.statements:
            return ProgramResults([], ctx)

        results = []
        new_assignments = set()

        for statement in self.statements:
            if isinstance(statement, Assignment):
                ctx.add_assignment(statement.target.name, statement)
                new_assignments.add(statement.target.name)
            if isinstance(statement, Statement):
                ctx.recompute()
                results.append(statement.execute(ctx))

        if not results and new_assignments:
            top = ctx.get_highest_node(new_assignments)
            ctx.recompute()
            results = [ctx.assignments[top].execute(ctx)]

        return ProgramResults(list(filter(None, results)), ctx)


from dataclasses import dataclass
from typing import Dict, List
import networkx as nx


@dataclass
class ExecContext:
    values: Dict[str, Optional[Literal]] = field(default_factory=dict)
    graph: nx.DiGraph = field(default_factory=nx.DiGraph)
    assignments: Dict[str, Assignment] = field(default_factory=dict)

    def copy(self):
        return ExecContext(
            values=self.values.copy(),
            graph=self.graph.copy(),
            assignments=self.assignments.copy(),
        )

    def add_assignment(self, target: str, assignment: Assignment):
        # invalidate the target and everything which depends on it

        deps = assignment.get_deps()
        self.values[target] = None

        if target in self.graph:
            for node in nx.ancestors(self.graph, target):
                self.values[node] = None

            # replace this assignment's dependencies
            for successor in list(self.graph.successors(target)):
                self.graph.remove_edge(target, successor)

        self.graph.add_node(target)
        for dep in deps:
            self.graph.add_edge(target, dep)

        self.assignments[target] = assignment

    @property
    def has_assigned(self) -> bool:
        return any(v is None for v in self.values.values())

    def get_value(self, name: str):
        try:
            return self.values[name]
        except KeyError:
            raise ProgramNameError(name)

    def get_invalid_nodes_from_leaves(self) -> Iterator[str]:
        for node in nx.topological_sort(self.graph.reverse(copy=False)):
            try:
                if self.get_value(node) is None:
                    yield node
            except KeyError:
                raise ProgramNameError(node)

    def recompute(self):
        if self.has_assigned:
            for node in self.get_invalid_nodes_from_leaves():
                self.values[node] = self.assignments[node].execute(self).value

    def get_highest_node(self, from_nodes):
        subgraph_dag_from_nodes(self.graph, from_nodes)
        return next(nx.topological_sort(self.graph))


def subgraph_dag_from_nodes(g, nodes):
    all_nodes = set()
    for node in nodes:
        all_nodes.update(nx.ancestors(g, node))
        all_nodes.update(nx.descendants(g, node))
        all_nodes.add(node)
    return nx.subgraph(g, all_nodes)
