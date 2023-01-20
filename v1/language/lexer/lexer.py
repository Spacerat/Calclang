from typing import List, Tuple, Dict, Set, Iterable
from .raw_ast import RawAssignment, RawStatement, Expression
from itertools import groupby
from .tokens import (
    Reference,
    LiteralValue,
    Parens,
    Unknown,
    Operator,
    Assignment,
    Statement,
)
import re

Assignments = Dict[Tuple[str], Expression]


def is_valid_init(unit: str) -> bool:
    # return true if unit matches 'months'/'days' etc with optional plural, using regex
    return re.match(r"^(months|days|years)s?$", unit) is not None


def interpret_words(words: List[str], assignments: Set[Tuple[str]]) -> Expression:
    # TODO: refactor to some kind of plugin architecture

    if tuple(words) in assignments:
        return Reference(name=tuple(words))

    if len(words) == 2:
        # Try to interpret as a value with a unit
        try:
            if is_valid_init(words[1]):
                return LiteralValue(float(words[0]), unit=words[1])
            return
        except ValueError:
            pass

    if len(words) == 1:
        word = words[0]

        # Try to interpret as an operator
        if word in ("+", "-", "*", "/", "to", "<", ">"):
            return Operator(name=word)

        # Try to interpret as a number
        try:
            # TODO: support currency
            return LiteralValue(float(word))
        except ValueError:
            pass

        # Try to interpret as a date

        # Return an unknown token
        return Unknown(word)

    return None


def process_words(
    words: List[str], assignments: Set[Tuple[str]]
) -> Iterable[Expression]:
    if not words:
        return
    # Try to consume as many words as possible. If there is no valid interpretation, try to consume one less word
    for i in range(len(words), 0, -1):
        result = interpret_words(words[:i], assignments)
        if result is not None:
            yield result
            yield from process_words(words[i:], assignments)
            return


def process_expression(expression: Expression, assignments: Set[Tuple[str]]):
    # Each expression element is a list of words, or sub-expressions
    # print("---")
    # print("expression", expression)
    groupby_key = lambda x: isinstance(x, list)

    for is_list, group in groupby(expression, groupby_key):
        if is_list:
            # When encountering a sub-expression, recurse
            yield from (Parens(list(process_expression(x, assignments))) for x in group)
        else:
            yield from process_words(list(group), assignments)


def process_assignments(assignments: Assignments):
    # For each assignment, we need to:
    # 1. Process its expressions.
    # 2. Replace the assignment's value with the processed expression

    assignment_names = set(assignments.keys())
    for key, value in assignments.items():
        yield Assignment(key, list(process_expression(value, assignment_names)))


def process_statement(expression: Expression, assignments: Assignments):
    return Statement(list(process_expression(expression, set(assignments.keys()))))


def lex(list: List[RawAssignment | RawStatement | None]):
    assignments: Dict[Tuple[str], Expression] = {}
    new_assignments: Dict[Tuple[str], Expression] = {}

    for item in filter(None, list + [RawStatement([])]):
        match item:
            case RawAssignment(target, expression):
                assignments[tuple(target)] = expression
                new_assignments[tuple(target)] = expression
            case RawStatement(expression):
                yield from process_assignments(new_assignments)
                yield process_statement(expression, assignments)
                new_assignments = {}
