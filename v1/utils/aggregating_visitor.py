from antlr4 import ParseTreeVisitor

from dataclasses import dataclass

@dataclass
class SourceContext:
    start: int
    stop: int
    text: str

class AggregatingVisitor(ParseTreeVisitor):
    def aggregateResult(self, aggregate, nextResult):
        match aggregate, nextResult:
            case None, None:
                return None
            case None, item:
                return [item]
            case agg, None:
                return agg
            case agg, item:
                return agg + [item]

    def visitChildren(self, ctx):
        result = super().visitChildren(ctx)
        if result is None or (len(result) == 1 and result[0] is None):
            return ctx.getText()

        if len(result) == 1:
            return result[0]

        return result

    def get_source_context(self, ctx):
        token_source = ctx.start.getTokenSource()
        input_stream = token_source.inputStream
        start, stop = ctx.start.start, ctx.stop.stop
        return SourceContext(start, stop, input_stream.getText(start, stop))
