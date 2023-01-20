from __future__ import annotations
from typing import Any, Tuple, Callable, Generic, TypeVar, List, Optional
from dataclasses import dataclass, replace

T = TypeVar("T")


@dataclass(frozen=True)
class Token(Generic[T]):
    text: str
    value: T
    pos: int

    def tokens(self) -> List[Token[Any]]:
        return [self]

    @staticmethod
    def string(value: str, pos: int) -> Token[str]:
        return Token(value, value, pos)

    @staticmethod
    def int(value: int, pos: int) -> Token[int]:
        return Token(str(value), value, pos)

    @staticmethod
    def float(value: float, pos: int) -> Token[float]:
        return Token(str(value), value, pos)

    def tagged(self, tag: str) -> Token[T]:
        return TaggedToken(self.text, self.value, self.pos, tag)


@dataclass(frozen=True)
class TaggedToken(Token):
    tag: str


StringToken = Token[str]
