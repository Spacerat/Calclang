from __future__ import annotations
from typing import Tuple, Literal
from dataclasses import dataclass


@dataclass
class Assignment:
    name: Tuple[str]
    value: Expression


@dataclass
class Statement:
    value: Expression


@dataclass
class Reference:
    name: Tuple[str]


@dataclass
class LiteralValue:
    value: float
    unit: str = None


@dataclass
class Parens:
    value: Expression


@dataclass
class Unknown:
    text: str


@dataclass
class Operator:
    name: Literal["+", "-", "*", "/"]


Expression = Reference | LiteralValue | Parens
