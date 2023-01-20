from __future__ import annotations
from typing import Any, Tuple, Callable, TypeVar, List, Optional
from .core import Parser, ParserContext, Result, ParseError
from .token import Token, StringToken

from .decorators import stringable_parser_decorator, named
import re
from .utils import countAtPos

T = TypeVar("T", covariant=True)
T1 = TypeVar("T1")
T2 = TypeVar("T2")
T3 = TypeVar("T3")
U = TypeVar("U")


def restOfLine() -> Parser[StringToken]:
    def pRestOfLine(ctx: ParserContext):
        pos = ctx.text.find("\n", ctx.pos)
        if pos == -1:
            pos = len(ctx.text)
        return Result(
            Token.string(ctx.text[ctx.pos : pos], ctx.pos),
            ctx.advance(pos - ctx.pos + 1),
        )

    return pRestOfLine


@stringable_parser_decorator
def string(s: str) -> Parser[StringToken]:
    """A parser that matches the given string"""

    def pString(ctx: ParserContext):
        if ctx.text.startswith(s, ctx.pos):
            return Result(Token.string(s, ctx.pos), ctx.advance(len(s)))
        raise ParseError(f"Expected '{s}'", ctx)

    return pString


@stringable_parser_decorator
def anyOf(*parsers: Parser[Any]) -> Parser[Any]:
    """A parser that matches any one of the given parsers"""

    def pAnyOf(ctx: ParserContext):
        for p in parsers:
            try:
                return p(ctx)
            except ParseError:
                pass
        raise ParseError(f"Expected any of {list(parsers)}", ctx)

    return pAnyOf


def skip(p: Parser[T]) -> Parser[None]:
    """A parser that matches the given parser and then returns None"""

    def pSkip(ctx: ParserContext):
        result = p(ctx)
        return Result(None, result.context)

    return pSkip


@stringable_parser_decorator
def regex(r: str) -> Parser[StringToken]:
    def pRegex(ctx: ParserContext):
        match = re.match(r, ctx.text[ctx.pos :])
        if match:
            return Result(
                Token.string(match.group(0), ctx.pos), ctx.advance(len(match.group(0)))
            )
        raise ParseError(f"Expected regex '{r}'", ctx)

    return pRegex


ws = regex(r"[ \t]*")


newlines = regex(r"\n+")


@stringable_parser_decorator
def wsAfter(p: Parser[T]) -> Parser[T]:
    """A parser that matches the given parser and then skips any whitespace"""

    def pWsAfter(ctx: ParserContext):
        result = p(ctx)
        return Result(result.value, ws(result.context).context)

    return pWsAfter


@stringable_parser_decorator
def rawTriple(
    parser1: Parser[T1], parser2: Parser[T2], parser3: Parser[T3]
) -> Parser[Tuple[T1, T2, T3]]:
    """A parser that matches the given parsers in sequence"""

    def pRawTriple(ctx: ParserContext):
        result1 = parser1(ctx)
        result2 = parser2(result1.context)
        result3 = parser3(result2.context)
        return Result((result1.value, result2.value, result3.value), result3.context)

    return pRawTriple


@stringable_parser_decorator
def triple(
    parser1: Parser[T1], parser2: Parser[T2], parser3: Parser[T3]
) -> Parser[Tuple[T1, T2, T3]]:
    """A parser that matches the given parsers in sequence, with optional whitespace between them"""
    return rawTriple(wsAfter(parser1), wsAfter(parser2), parser3)


@stringable_parser_decorator
def rawPair(parser1: Parser[T1], parser2: Parser[T2]) -> Parser[Tuple[T1, T2]]:
    """A parser that matches the given parsers in sequence, without whitespace between them"""

    def pRawPair(ctx: ParserContext):
        result1 = parser1(ctx)
        result2 = parser2(result1.context)
        return Result((result1.value, result2.value), result2.context)

    return pRawPair


@stringable_parser_decorator
def pair(parser1: Parser[T1], parser2: Parser[T2]) -> Parser[Tuple[T1, T2]]:
    """A parser that matches the given parsers in sequence, with optional whitespace between them"""
    return rawPair(wsAfter(parser1), parser2)


@stringable_parser_decorator
def sequence(
    parsers: List[Parser[T | Any]], *, separator: Parser[Any] | None = None
) -> Parser[List[T]]:
    """A parser that matches the given parsers in sequence"""

    def pSequence(ctx: ParserContext):
        results = []
        for idx, p in enumerate(parsers):
            result = p(ctx)
            results.append(result.value)
            ctx = result.context
            if separator and idx < len(parsers) - 1:
                ctx = separator(result.context).context
        return Result(results, ctx)

    return pSequence


@stringable_parser_decorator
def zeroOrMore(p: Parser[T]) -> Parser[List[T]]:
    """A parser that matches the given parser zero or more times"""

    def pZeroOrMore(ctx: ParserContext):
        results = []
        while True:
            try:
                result = p(ctx)
                results.append(result.value)
                ctx = result.context
            except ParseError:
                break
        return Result(results, ctx)

    return pZeroOrMore


@stringable_parser_decorator
def optional(p: Parser[T]) -> Parser[Optional[T]]:
    """A parser that matches the given parser, or nothing"""

    def pOptional(ctx: ParserContext):
        try:
            result = p(ctx)
            return Result(result.value, result.context)
        except ParseError:
            return Result(None, ctx)

    return pOptional


def lazyParser(f: Callable[[], Parser[T]]) -> Parser[T]:
    """A decorator that allows a parser to be defined recursively"""

    def pLazyParser(context: ParserContext) -> Result[T]:
        return f()(context)

    return pLazyParser


@stringable_parser_decorator
def oneOrMore(p: Parser[T]) -> Parser[List[T]]:
    """A parser that matches one or more instances of the given parser"""

    def pOneOrMore(ctx: ParserContext):
        result = p(ctx)
        rest = zeroOrMore(p)(result.context)
        return Result([result.value] + rest.value, rest.context)

    return pOneOrMore


def oneOrMoreSeparated(p: Parser[T], separator: Parser[Any]) -> Parser[List[T]]:
    """A parser that matches one or more instances of the given parser, separated by the given separator"""

    def pOneOrMoreSequence(ctx: ParserContext):
        result = p(ctx)
        rest = zeroOrMore(right(separator, p))(result.context)
        return Result([result.value] + rest.value, rest.context)

    return pOneOrMoreSequence


def transform(p: Parser[T], f: Callable[[T], U]) -> Parser[U]:
    """Transform the result of a parser"""

    def pTransform(ctx: ParserContext):
        result = p(ctx)
        return Result(f(result.value), result.context)

    return pTransform


def tokenTransform(p: Parser[Token[T]], f: Callable[[T], U]) -> Parser[Token[U]]:
    """Transform the result of a parser that returns a token into another parser that returns a token"""

    def pTokenTransform(ctx: ParserContext):
        result = p(ctx)
        return Result(
            Token(
                text=result.value.text,
                value=f(result.value.value),
                pos=ctx.pos,
            ),
            result.context,
        )

    return pTokenTransform


def transformer(transformer: Callable[[T], U]) -> Callable[[Parser[T]], Parser[U]]:
    """A dectorator that turns a function into a parser transformer"""

    def decorator(parser: Parser[T]) -> Parser[U]:
        return transform(parser, transformer)

    return decorator


@stringable_parser_decorator
def bracketed(p: Parser[T]) -> Parser[T]:
    def pBracketed(ctx: ParserContext):
        result = triple(string("("), p, string(")"))(ctx)
        return Result(result.value[1], result.context)

    return pBracketed


@stringable_parser_decorator
def left(p: Parser[T], p2: Parser[Any]) -> Parser[T]:
    """A parser that matches the given parsers in sequence, but only returns the first result"""

    def pLeft(ctx: ParserContext):
        result = pair(p, p2)(ctx)
        return Result(result.value[0], result.context)

    return pLeft


@stringable_parser_decorator
def right(p: Parser[Any], p2: Parser[T]) -> Parser[T]:
    """A parser that matches the given parsers in sequence, but only returns the second result"""

    def pRight(ctx: ParserContext):
        result = pair(p, p2)(ctx)
        return Result(result.value[1], result.context)

    return pRight


intParser = named("integer")(tokenTransform(regex(r"\d+"), int))
floatParser = named("float")(tokenTransform(regex(r"\d+\.\d+"), float))
