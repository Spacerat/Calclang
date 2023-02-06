from __future__ import annotations
from typing import Protocol, TypeVar, Iterator, Generic
import numpy as np

TNumeric = TypeVar("TNumeric", int, float, np.ndarray)


class Unit(Protocol):
    """Stub for pint.Unit"""


class Quantity(np.ndarray, Generic[TNumeric]):
    """Stub for pint.Quantity"""

    # This is a complete hack, lol!

    m: TNumeric
    u: Unit

    def to(self, other: Unit) -> Quantity[TNumeric]:
        ...

    def __mul__(self, other: Unit) -> Quantity[TNumeric]:
        ...

    def __iter__(self) -> Iterator[TNumeric]:
        ...

    def __lt__(self, other: Quantity[TNumeric]) -> bool:
        ...

    def __gt__(self, other: Quantity[TNumeric]) -> bool:
        ...

    @property
    def unitless(self) -> bool:
        ...
