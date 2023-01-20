from __future__ import annotations

from typing import Any, TypeVar

from combinators.combinators import (
    Parser,
    anyOf,
    bracketed,
    floatParser,
    oneOrMore,
    oneOrMoreSeparated,
    intParser,
    lazyParser,
    optional,
    regex,
    pair,
    triple,
    newlines,
    string,
    left,
)

from combinators.decorators import named


from .transformers import (
    binOpTransformer,
    assignmentTransformer,
    statementTransformer,
    variableTransformer,
    literalTransformer,
    programTransformer,
)

T = TypeVar("T")
U = TypeVar("U")


word = regex(r"\w+")
words = regex(r"\w+( +\w+)*")  # too broad?

number = anyOf(floatParser, intParser)

unit = anyOf(
    string("days"),
    string("hours"),
)


literal = literalTransformer(anyOf(pair(number, optional(unit))))


mulOp = anyOf(string("*"), string("/"))
addOp = anyOf(string("+"), string("-"))

numberRange = binOpTransformer(triple(literal, string("to"), literal))

variable = variableTransformer(words)


@named("expression")
@lazyParser
def expression() -> Parser[Any]:
    return anyOf(
        binOpTransformer(triple(term, addOp, term)),
        term,
    )


@named("term")
@lazyParser
def term() -> Parser[Any]:
    return anyOf(
        binOpTransformer(triple(factor, mulOp, factor)),
        factor,
    )


@named("factor")
@lazyParser
def factor() -> Parser[Any]:
    return anyOf(numberRange, bracketed(expression), literal, variable)


statement = statementTransformer(expression)

assignment = assignmentTransformer(triple(variable, string("="), expression))

program = programTransformer(oneOrMoreSeparated(anyOf(assignment, statement), newlines))
