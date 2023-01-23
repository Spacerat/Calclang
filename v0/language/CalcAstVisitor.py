# type: ignore

from ..parser.ExprParser import ExprParser
from ..parser.ExprParserVisitor import ExprParserVisitor


from .calc_ast import (
    Program,
    Statement,
    Assignment,
    Unknown,
    Versus,
    Range,
    BinOp,
    Id,
    Value,
    Inequality,
)

currency_units = {
    "$": "dollar",
    "£": "pound",
}


class CalcAstVisitor(ExprParserVisitor):
    def aggregateResult(self, aggregate, nextResult):
        if aggregate is None:
            return [nextResult]

        aggregate.append(nextResult)
        return aggregate

    def visitProgram(self, ctx: ExprParser.ProgramContext):
        return Program(self.visitChildren(ctx))

    def extract_original_text(self, ctx):
        token_source = ctx.start.getTokenSource()
        input_stream = token_source.inputStream
        start, stop = ctx.start.start, ctx.stop.stop
        return input_stream.getText(start, stop)

    def visitStatement(self, ctx: ExprParser.StatementContext):
        return Statement(self.extract_original_text(ctx), self.visit(ctx.expression))

    def visitAssignment(self, ctx: ExprParser.AssignmentContext):
        return Assignment(
            self.extract_original_text(ctx),
            self.visit(ctx.target),
            self.visit(ctx.expression),
        )

    def visitInequality(self, ctx: ExprParser.InequalityContext):
        return Inequality(
            self.extract_original_text(ctx),
            self.visit(ctx.lhs),
            ctx.op.text,
            self.visit(ctx.rhs),
        )

    def visitVersus(self, ctx: ExprParser.VersusContext):
        return Versus(
            self.extract_original_text(ctx),
            self.visit(ctx.lhs),
            self.visit(ctx.rhs),
        )

    def visitCurrencyValue(self, ctx: ExprParser.CurrencyValueContext):
        unit = currency_units[ctx.symbol.text]

        return Value(self.visit(ctx.amount), unit)

    def visitValue(self, ctx: ExprParser.ValueContext):
        unit = self.visit(ctx.valueUnit) if ctx.valueUnit else None
        return Value(self.visit(ctx.value), unit=unit)

    def visitNumericLiteral(self, ctx: ExprParser.NumericLiteralContext):
        return float(ctx.getText())

    def visitBinop(self, ctx: ExprParser.BinopContext):
        return BinOp(self.visit(ctx.lhs), ctx.op.text, self.visit(ctx.rhs))

    def visitRawId(self, ctx: ExprParser.RawIdContext):
        return Id(ctx.getText())

    def visitUnit(self, ctx: ExprParser.UnitContext):
        return ctx.getText()

    def visitBracketId(self, ctx: ExprParser.BracketIdContext):
        return Id(ctx.getText()[1:-1])

    def visitRange(self, ctx: ExprParser.RangeContext):
        return Range(
            bottom=self.visit(ctx.bottom),
            mid=self.visit(ctx.mid) if ctx.mid else None,
            top=self.visit(ctx.top),
        )

    def visitParens(self, ctx: ExprParser.ParensContext):
        return self.visitChildren(ctx)[1]

    def visitChildren(self, ctx):
        result = super().visitChildren(ctx)

        if result is None or (len(result) == 1 and result[0] is None):
            return Unknown(ctx.getText())

        if len(result) == 1:
            return result[0]

        return result

    def visitDate(self, ctx: ExprParser.DateContext):
        return super().visitDate(ctx)
