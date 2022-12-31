from dataclasses import dataclass, field
from typing import Dict, Union, List, Optional, Iterator, Literal
import numpy as np
import networkx as nx


Numeric = int | float | np.ndarray


@dataclass
class ExecContext:
    values: Dict[str, Optional[Numeric]] = field(default_factory=dict)
    graph: nx.DiGraph = field(default_factory=nx.DiGraph)
    assignments: Dict[str, "Assignment"] = field(default_factory=dict)
    # sequenceAssignments: Dic

    indexValues: List[int] = field(default_factory=list)

    def copy(self):
        return ExecContext(
            values=self.values.copy(),
            graph=self.graph.copy(),
            assignments=self.assignments.copy(),
        )

    def withIndexValues(self, values: List[int]):
        return ExecContext(
            values=self.values,
            graph=self.graph,
            assignments=self.assignments,
            indexValues=values,
        )

    # TODO: make immutable?
    def add_assignment(self, target: str, assignment: "Assignment"):
        # Do nothing if the assignment is unchanged

        curr_assignment = self.assignments.get(target)
        if curr_assignment and curr_assignment.text == assignment.text:
            return

        # invalidate the target and everything which depends on it

        deps = assignment.get_deps(self)
        self.values[target] = None

        if target in self.graph:
            for node in nx.ancestors(self.graph, target):
                self.values[node] = None

            # replace this assignment's dependencies

            for successor in list(self.graph.successors(target)):
                self.graph.remove_edge(target, successor)

        # Add the new assignment and all of its dependencies

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
            print(f"{name} is not defined")
            return None

    def get_invalid_nodes_from_leaves(self) -> Iterator[str]:
        for node in nx.topological_sort(self.graph.reverse(copy=False)):
            if node in self.values and self.values[node] is None:
                yield node

    def recompute(self):
        if self.has_assigned:
            for node in self.get_invalid_nodes_from_leaves():
                if node in self.assignments:
                    self.values[node] = self.assignments[node].execute(self).value

    def get_highest_node(self, from_nodes):
        subgraph = subgraph_dag_from_nodes(self.graph, from_nodes)
        return next(nx.topological_sort(subgraph))


@dataclass
class StatementResult:
    text: str
    value: Optional[Numeric]

    def name(self):
        return self.text


@dataclass
class AssignmentResult:
    text: str
    target: str
    value: Optional[Numeric]

    def name(self):
        return self.target


@dataclass
class InequalityResult:
    text: str
    lhs: Optional[Numeric]
    rhs: Optional[Numeric]
    op: Literal[">"] | Literal["<"]

    def name(self):
        # HACK
        # should get text from children directly instead
        return (self.text.split("<") if self.op == "<" else self.text.split(">"))[
            0
        ].strip()


AnyResult = StatementResult | AssignmentResult | InequalityResult


@dataclass
class ProgramResults:
    results: List[AnyResult]
    context: "ExecContext"

    @property
    def last_result(self):
        return self.results[-1] if self.results else None


@dataclass
class Unknown:
    text: str


@dataclass
class Id:
    name: str

    def get_deps(self, ctx: ExecContext) -> List[str]:
        return [self.name]

    def execute(self, ctx: "ExecContext"):
        return ctx.get_value(self.name)


@dataclass
class SequenceIndexId:
    name: str


@dataclass
class SequenceIndexRelative:
    name: str
    op: Literal["-", "+"]
    offset: int


@dataclass
class SequenceIndexAbsolute:
    index: int


SequenceIndex = SequenceIndexId | SequenceIndexRelative | SequenceIndexRelative


@dataclass
class SequenceId:
    name: str
    indexes: List[SequenceIndex]


@dataclass
class Assignment:
    text: str
    target: Id
    expression: "Expression"

    def get_deps(self, ctx: ExecContext) -> List[str]:
        return self.expression.get_deps(ctx)

    def execute(self, ctx: "ExecContext"):
        return AssignmentResult(
            self.text, self.target.name, self.expression.execute(ctx)
        )


@dataclass
class SequenceAssignment:
    text: str
    target: SequenceId
    expression: "Expression"

    def get_deps(self, ctx: ExecContext) -> List[str]:
        return self.expression.get_deps(ctx)

    def execute(self, ctx: "ExecContext"):
        return AssignmentResult(
            self.text, self.target.name, self.expression.execute(ctx)
        )


@dataclass
class Inequality:
    text: str
    lhs: "Expression"
    op: str
    rhs: "Expression"

    def get_deps(self, ctx: ExecContext) -> List[str]:
        return self.lhs.get_deps(ctx) + self.rhs.get_deps(ctx)

    def execute(self, ctx: "ExecContext"):
        if self.op not in ("<", ">"):
            raise Exception("Invalid inequality operator")

        return InequalityResult(
            self.text, self.lhs.execute(ctx), self.rhs.execute(ctx), self.op
        )


@dataclass
class Statement:
    text: str
    expression: "Expression"

    def get_deps(self, ctx: ExecContext) -> List[str]:
        return self.expression.get_deps(ctx)

    def execute(self, ctx: "ExecContext"):
        return StatementResult(self.text, self.expression.execute(ctx))


@dataclass
class Value:
    literal: int | float
    unit: str

    def get_deps(self, ctx: ExecContext) -> List[str]:
        return []

    def execute(self, ctx: "ExecContext"):
        return self.literal


@dataclass
class BinOp:
    lhs: "Expression"
    op: str
    rhs: "Expression"

    def get_deps(self, ctx: ExecContext) -> List[str]:
        return self.lhs.get_deps(ctx) + self.rhs.get_deps(ctx)

    def default_val(self, val):
        if val is not None:
            return val
        if self.op in ("+", "-"):
            return 0
        if self.op in ("*", "/"):
            return 1

    def execute(self, ctx: "ExecContext"):
        lhs = self.default_val(self.lhs.execute(ctx))
        rhs = self.default_val(self.rhs.execute(ctx))

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

    def get_deps(self, ctx: ExecContext) -> List[str]:
        try:
            return self.bottom.get_deps(ctx) + self.top.get_deps(ctx)
        except:
            print(self.bottom)
            print(self.top)
            raise

    def execute(self, ctx: "ExecContext") -> np.ndarray:
        bottom = self.bottom.execute(ctx)
        top = self.top.execute(ctx)
        if bottom > top:
            bottom, top = top, bottom
        return np.random.rand(100000) * (top - bottom) + bottom


Expression = BinOp | Value | Range | Id


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
            if isinstance(statement, (Statement, Inequality)):
                ctx.recompute()
                results.append(statement.execute(ctx))

        if not results and new_assignments:
            ctx.recompute()
            top = ctx.get_highest_node(new_assignments)
            results = [ctx.assignments[top].execute(ctx)]

        return ProgramResults(list(filter(None, results)), ctx)


def subgraph_dag_from_nodes(g, nodes):
    all_nodes = set()
    for node in nodes:
        all_nodes.update(nx.ancestors(g, node))
        all_nodes.update(nx.descendants(g, node))
        all_nodes.add(node)
    return nx.subgraph(g, all_nodes)
