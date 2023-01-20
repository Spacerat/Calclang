from __future__ import annotations

from typing import Tuple, List, Union

from combinators.combinators import (
    Token,
    transformer,
)

from combinators.decorators import named
from .ast import Literal, BinOp, Term, Variable, Assignment, Program, Statement


@transformer
def binOpTransformer(value: Tuple[Term, Token[str], Term]) -> BinOp:
    return BinOp(left=value[0], op=value[1], right=value[2])


@transformer
def assignmentTransformer(value: Tuple[Variable, Token[str], Term]) -> Assignment:
    return Assignment(left=value[0], equals=value[1], right=value[2])


@transformer
def statementTransformer(value: Term) -> Statement:
    return Statement(value)


@transformer
def variableTransformer(value: Token[str]) -> Variable:
    return Variable(name=value)


@transformer
def literalTransformer(value: Tuple[Token[float], Token[str] | None]) -> Literal:
    return Literal(value=value[0], unit=value[1])


@transformer
def programTransformer(value: List[Union[Assignment, Statement]]) -> Program:
    return Program(
        assignments=[
            assignment
            for assignment in value
            if isinstance(assignment, (Assignment, Statement))
        ]
    )
