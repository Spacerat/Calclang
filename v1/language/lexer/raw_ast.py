from __future__ import annotations
from dataclasses import dataclass
from typing import List, Union
from utils.aggregating_visitor import SourceContext


@dataclass
class Word:
    value: str
    ctx: SourceContext


@dataclass
class Parens:
    value: Expression
    ctx: SourceContext


Expression = List[Union[Word, Parens]]


@dataclass
class RawAssignment:
    target: List[str]
    expression: Expression
    ctx: SourceContext


@dataclass
class RawStatement:
    expression: Expression
    ctx: SourceContext
