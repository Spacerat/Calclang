from __future__ import annotations

from dataclasses import dataclass
from typing import Union, List, Any

from combinators.token import Token
from itertools import chain

# from typing_extensions import Protocol


# class Flyer(Protocol):
#     def fly(self) -> None:
#         """A Flyer can fly"""


@dataclass
class Literal:
    value: Token[float] | Token[int]
    unit: Token[str] | None

    def tokens(self) -> List[Token[Any]]:
        if self.unit:
            return [
                self.value.tagged("literal_value"),
                self.unit.tagged("literal_unit"),
            ]
        return [self.value.tagged("literal_value")]


@dataclass
class BinOp:
    left: Term
    op: Token[str]
    right: Term

    def tokens(self) -> List[Token[Any]]:
        return list(
            chain(
                self.left.tokens(),
                self.op.tagged("operator").tokens(),
                self.right.tokens(),
            )
        )


@dataclass
class Assignment:
    left: Variable
    equals: Token[str]
    right: Term

    def tokens(self) -> List[Token[Any]]:
        return list(
            chain(
                self.left.tokens(),
                self.equals.tagged("equals").tokens(),
                self.right.tokens(),
            )
        )


@dataclass
class Statement:
    term: Term

    def tokens(self) -> List[Token[Any]]:
        return self.term.tokens()


@dataclass
class Variable:
    name: Token[str]

    def tokens(self) -> List[Token[Any]]:
        return [self.name.tagged("variable")]


@dataclass
class Program:
    assignments: list[Assignment | Statement]

    def tokens(self) -> List[Token[Any]]:
        return list(chain.from_iterable([x.tokens() for x in self.assignments]))


Term = Union[Literal, BinOp, Variable]
