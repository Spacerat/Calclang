from dataclasses import dataclass
from typing import Dict, Union, List
import numpy as np
from itertools import groupby
import networkx as nx
from .ExecContext import ExecContext
from .results import ProgramResults, AssignmentResult, StatementResult


@dataclass
class Unknown:
    text: str


@dataclass
class ID:
    name: str

    def get_deps(self) -> List[str]:
        return [self.name]

    def execute(self, ctx: ExecContext):
        return ctx.values[self.name]


@dataclass
class Assignment:
    text: str
    target: ID
    expression: "Expression"

    def get_deps(self) -> List[str]:
        return self.expression.get_deps()

    def execute(self, ctx: ExecContext):
        return AssignmentResult(
            self.text, self.target.name, self.expression.execute(ctx)
        )


@dataclass
class Statement:
    text: str
    expression: "Expression"

    def get_deps(self) -> List[str]:
        return self.expression.get_deps()

    def execute(self, ctx: ExecContext):
        return StatementResult(self.text, self.expression.execute(ctx))


@dataclass
class Value:
    literal: int | float
    unit: str

    def get_deps(self) -> List[str]:
        return []

    def execute(self, ctx: ExecContext):
        return self.literal


@dataclass
class BinOp:
    lhs: "Expression"
    op: str
    rhs: "Expression"

    def get_deps(self) -> List[str]:
        return self.lhs.get_deps() + self.rhs.get_deps()

    def execute(self, ctx: ExecContext):
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

    def execute(self, ctx: ExecContext):
        bottom = self.bottom.execute(ctx)
        top = self.top.execute(ctx)
        if bottom > top:
            bottom, top = top, bottom
        return np.random.rand(100000) * (top - bottom) + bottom


Expression = BinOp | Value | Range | ID


@dataclass
class Program:
    statements: Union[Assignment, Statement]

    def execute(self):
        """
        Perf notes:
        - ideally, use numpy/etc to compute in bulk
        """

        ctx = ExecContext({}, nx.DiGraph())
        results = []

        assignments: Dict[str, Assignment] = {}

        for cls, v in groupby(filter(None, self.statements), key=lambda x: x.__class__):
            if cls == Assignment:
                # Set up the dependency graph
                for assignment in v:
                    ctx.add_assignment(assignment.target.name, assignment.get_deps())
                    assignments[assignment.target.name] = assignment

            if cls == Statement:
                # Recompute new values
                for node in ctx.get_invalid_nodes_from_leaves():
                    ctx.values[node] = assignments[node].execute(ctx).value

                results.extend(statement.execute(ctx) for statement in v)
        return ProgramResults(list(filter(None, results)), ctx, results[-1])
