from .core import ParserContext, Parser, ParseError
from typing import Callable, TypeVar

T = TypeVar("T", covariant=True)


def stringable_parser_decorator(f):
    def wrapper(*args, **kwargs):
        class Parser:
            def __call__(self, ctx: ParserContext):
                return f(*args, **kwargs)(ctx)

            def __repr__(self):
                return f.__name__ + "(" + ", ".join(map(repr, args)) + ")"

            def __eq__(self, other: object) -> bool:
                return repr(self) == repr(other)

        return Parser()

    return wrapper


def named(name: str) -> Callable[[Parser[T]], Parser[T]]:
    def inner(parser: Parser[T]):
        class Parser:
            def __call__(self, ctx: ParserContext):
                try:
                    return parser(ctx)
                except ParseError as e:
                    raise ParseError(f"Expected {name}", ctx)

            def __repr__(self):
                return name

            def __eq__(self, other: object) -> bool:
                return repr(self) == repr(other)

        return Parser()

    return inner
