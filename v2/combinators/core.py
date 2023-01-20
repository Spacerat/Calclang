from __future__ import annotations
from typing import Any, Tuple, Callable, Generic, TypeVar, List, Optional
from dataclasses import dataclass, replace, field as dataclass_field
from typing import NamedTuple

T = TypeVar("T", covariant=True)


class Result(NamedTuple, Generic[T]):
    value: T
    context: ParserContext


@dataclass
class ParserContext:
    text: str
    pos: int
    deferredEvaluationContexts: List[List[DeferredEvaluation[Any]]] = dataclass_field(
        default_factory=list
    )
    references: List[Tuple[str]] = dataclass_field(default_factory=list)

    def advance(self, num_chars: int):
        return replace(self, pos=min(self.pos + num_chars, len(self.text)))

    def withPushDeferredContext(self):
        return replace(
            self,
            deferredEvaluationContexts=[[]] + self.deferredEvaluationContexts,
        )

    def withPopDeferredContext(self):
        return replace(
            self, deferredEvaluationContexts=self.deferredEvaluationContexts[1:]
        )

    def withDeferredEvaluation(self, deferredEvaluation: DeferredEvaluation[Any]):
        first = self.deferredEvaluationContexts[0]
        rest = self.deferredEvaluationContexts[1:]

        newStack = [[deferredEvaluation] + first] + rest

        return replace(
            self,
            deferredEvaluationContexts=newStack,
        )

    def withPos(self, pos: int):
        return replace(self, pos=pos)

    def withReference(self, value: Tuple[str]):
        return replace(self, references=[value] + self.references)


Parser = Callable[[ParserContext], Result[T]]


@dataclass
class DeferredEvaluation(Generic[T]):
    pos: int
    parser: Parser[T]
    result: T | None = None


class ParseError(Exception):
    def __init__(self, message: str, ctx: ParserContext):
        self.message = message
        self.ctx = ctx

    def __str__(self):
        return f"{self.message} at {self.ctx.pos}"
