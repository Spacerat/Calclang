from typing import Any, Tuple, List
from .core import ParserContext, Parser, ParseError, Result, DeferredEvaluation
from .token import StringToken
from dataclasses import dataclass
from .combinators import sequence, string, anyOf, ws
from typing import TypeVar
from .decorators import stringable_parser_decorator

T = TypeVar("T")


def deferred(basicParser: Parser[Any], deferredParser):
    def parser(ctx: ParserContext):
        parserResult = basicParser(ctx)
        result = DeferredEvaluation(ctx.pos, deferredParser)
        ctx = parserResult.context.withDeferredEvaluation(result)
        return Result(result, ctx)

    return parser


def addReference(p: Parser[List[StringToken]]) -> Parser[List[StringToken]]:
    def parser(ctx: ParserContext):
        result = p(ctx)
        reference = tuple(x.text for x in result.value)
        ctx = result.context.withReference(reference)
        return Result(result.value, ctx)

    return parser


@dataclass
class Reference:
    name: Tuple[str]


@stringable_parser_decorator
def reference() -> Parser[Reference]:
    # Return a parser which tries to match any reference defined in the current context
    def parser(ctx: ParserContext):
        parser = anyOf(
            *[
                sequence([string(x) for x in reference], separator=ws)
                for reference in ctx.references
            ]
        )
        result = parser(ctx)
        if result:
            return Result(
                Reference(tuple(x.text for x in result.value)), result.context
            )
        raise ParseError("Expected reference", ctx)

    return parser


def deferredContext(p: Parser[T]) -> Parser[T]:
    def parser(ctx: ParserContext):
        ctx = ctx.withPushDeferredContext()
        result = p(ctx)
        deferredContext = result.context.deferredEvaluationContexts[0]
        ctx = result.context.withPopDeferredContext()

        # Evaluate all deferred evaulations in the context
        for deferredEvaluation in deferredContext:
            if deferredEvaluation.result is None:

                deferredEvaluation.result = deferredEvaluation.parser(
                    ctx.withPos(deferredEvaluation.pos)
                ).value

        return Result(result.value, ctx)

    return parser
