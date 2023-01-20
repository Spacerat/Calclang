from .core import Parser, Result, ParserContext
from typing import TypeVar

T = TypeVar("T")


def parse(parser: Parser[T], text: str) -> Result[T]:
    return parser(ParserContext(text, 0))
