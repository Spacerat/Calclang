from __future__ import annotations
from dataclasses import dataclass, field
from typing import (
    Dict,
    Union,
    List,
    Optional,
    Iterator,
    Literal,
    Tuple,
    Optional,
)
from pprint import pprint
import numpy as np
import networkx as nx
from .units import units
from case_insensitive_dict import CaseInsensitiveDict

from .pint_stubs import Quantity

SIM_SIZE = 300_000


""" Dictionary which treats all keys as lower clase"""


@dataclass(frozen=True)
class ExecContext:
    values: CaseInsensitiveDict[str, Optional[Quantity]] = field(
        default_factory=CaseInsensitiveDict
    )
    graph: nx.DiGraph = field(default_factory=nx.DiGraph)
    assignments: CaseInsensitiveDict[str, "Assignment"] = field(
        default_factory=CaseInsensitiveDict
    )

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
        target = target.lower()
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
                successor = successor.lower()
                self.graph.remove_edge(target, successor)

        # Add the new assignment and all of its dependencies

        self.graph.add_node(target)
        for dep in deps:
            self.graph.add_edge(target, dep.lower())

        self.assignments[target] = assignment

    @property
    def has_assigned(self) -> bool:
        return any(v is None for v in self.values.values())

    def get_value(self, name: str) -> None | Quantity:
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


@dataclass(frozen=True)
class StatementResult:
    text: str
    value: Optional[Quantity]

    def name(self):
        return self.text


@dataclass(frozen=True)
class AssignmentResult:
    text: str
    target: str
    value: Optional[Quantity]

    def name(self):
        return self.target


Operator = Literal[">"] | Literal["<"]


@dataclass(frozen=True)
class InequalityResult:
    text: str
    lhs: Optional[Quantity]
    rhs: Optional[Quantity]
    op: Operator

    def names(self):
        # HACK
        # should get text from children directly instead
        return self.text.split("<") if self.op == "<" else self.text.split(">")

    def lhs_name(self):
        return self.names()[0].strip()

    def rhs_name(self):
        return self.names()[1].strip()


@dataclass(frozen=True)
class VersusResult:
    text: str
    lhs: Optional[Quantity]
    rhs: Optional[Quantity]

    def name(self):
        return self.text


AnyResult = StatementResult | AssignmentResult | InequalityResult | VersusResult


@dataclass(frozen=True)
class ProgramResults:
    statementResults: List[AnyResult]
    context: "ExecContext"

    @property
    def last_result(self):
        return self.statementResults[-1] if self.statementResults else None


@dataclass(frozen=True)
class Unknown:
    text: str


@dataclass(frozen=True)
class Id:
    name: str

    def get_deps(self, ctx: ExecContext) -> List[str]:
        return [self.name]

    def execute(self, ctx: "ExecContext") -> None | Quantity:
        return ctx.get_value(self.name)


@dataclass(frozen=True)
class SequenceIndexId:
    name: str


@dataclass(frozen=True)
class SequenceIndexRelative:
    name: str
    op: Literal["-", "+"]
    offset: int


@dataclass(frozen=True)
class SequenceIndexAbsolute:
    index: int


SequenceIndex = SequenceIndexId | SequenceIndexRelative | SequenceIndexRelative


@dataclass(frozen=True)
class SequenceId:
    name: str
    indexes: List[SequenceIndex]


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
class Versus:
    text: str
    lhs: "Expression"
    rhs: "Expression"

    def get_deps(self, ctx: ExecContext) -> List[str]:
        return self.lhs.get_deps(ctx) + self.rhs.get_deps(ctx)

    def execute(self, ctx: "ExecContext"):
        return VersusResult(self.text, self.lhs.execute(ctx), self.rhs.execute(ctx))


@dataclass(frozen=True)
class Statement:
    text: str
    expression: "Expression"

    def get_deps(self, ctx: ExecContext) -> List[str]:
        return self.expression.get_deps(ctx)

    def execute(self, ctx: "ExecContext"):
        return StatementResult(self.text, self.expression.execute(ctx))


@dataclass(frozen=True)
class Value:
    literal: int | float
    unit: str

    def get_deps(self, ctx: ExecContext) -> List[str]:
        return []

    def execute(self, ctx: "ExecContext") -> None | Quantity:
        # return self.literal
        if self.unit:
            return self.literal * units[self.unit]
        else:
            return self.literal * units.dimensionless


@dataclass(frozen=True)
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
            return 0 * units.dimensionless
        if self.op in ("*", "/"):
            return 1 * units.dimensionless

    def execute(self, ctx: "ExecContext") -> None | Quantity:
        lhs = self.default_val(self.lhs.execute(ctx))
        rhs = self.default_val(self.rhs.execute(ctx))

        if self.op in ("-", "+"):
            # Currently unclear whether this is a good idea
            lhs, rhs = infer_units(lhs, rhs)

        if self.op == "+":
            return lhs + rhs
        if self.op == "-":
            return lhs - rhs
        if self.op == "*":
            return lhs * rhs
        if self.op == "/":
            return lhs / rhs
        raise RuntimeError(f"unknown operator {self.op}")


@dataclass(frozen=True)
class UnitConvert:
    expression: "Expression"
    unit: str

    def get_deps(self, ctx: ExecContext) -> List[str]:
        return self.expression.get_deps(ctx)

    def execute(self, ctx: "ExecContext") -> None | Quantity:
        val = self.expression.execute(ctx)
        if val:
            return val.to(units[self.unit])


@dataclass(frozen=True)
class Range:
    bottom: "Expression"
    top: "Expression"
    mid: Optional["Expression"]

    def get_deps(self, ctx: ExecContext) -> List[str]:
        return (
            self.bottom.get_deps(ctx)
            + self.top.get_deps(ctx)
            + (self.mid.get_deps(ctx) if self.mid else [])
        )

    def execute(self, ctx: "ExecContext") -> None | Quantity[np.ndarray]:
        return self.triangular(ctx) if self.mid else self.uniform(ctx)

    def triangular(self, ctx: "ExecContext") -> None | Quantity[np.ndarray]:
        bottom = self.bottom.execute(ctx)
        top = self.top.execute(ctx)
        mid = self.mid.execute(ctx)

        bottom, top = infer_units(bottom, top)
        mid, top = infer_units(mid, top)

        return (
            np.random.triangular(
                left=bottom.m,
                mode=in_unit_of(mid, of=bottom).m,
                right=in_unit_of(top, of=bottom).m,
                size=SIM_SIZE,
            )
            * bottom.u
        )

    def uniform(self, ctx: "ExecContext") -> None | Quantity[np.ndarray]:
        bottom = self.bottom.execute(ctx)
        top = self.top.execute(ctx)

        bottom, top = infer_units(bottom, top)

        if bottom > top:
            bottom, top = top, bottom

        return (
            np.random.uniform(
                low=bottom.m,
                high=in_unit_of(top, of=bottom).m,
                size=SIM_SIZE,
            )
            * bottom.u
        )


def in_unit_of(value, *, of):
    return of * 0 + value


Expression = BinOp | Value | Range | Id


def infer_units(lhs: Quantity, rhs: Quantity) -> Tuple[Quantity, Quantity]:
    match (lhs.unitless, rhs.unitless):
        case (True, False):
            return (lhs * rhs.u, rhs)
        case (False, True):
            return (lhs, rhs * lhs.u)
    return (lhs, rhs)


@dataclass(frozen=True)
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

            if isinstance(statement, (Statement, Inequality, Versus)):
                ctx.recompute()
                results.append(statement.execute(ctx))

        if not results and new_assignments:
            ctx.recompute()
            top = ctx.get_highest_node(new_assignments)
            results = [ctx.assignments[top].execute(ctx)]

        return ProgramResults(statementResults=list(filter(None, results)), context=ctx)


def subgraph_dag_from_nodes(g, nodes):
    all_nodes = set()
    for node in nodes:
        all_nodes.update(nx.ancestors(g, node))
        all_nodes.update(nx.descendants(g, node))
        all_nodes.add(node)
    return nx.subgraph(g, all_nodes)
