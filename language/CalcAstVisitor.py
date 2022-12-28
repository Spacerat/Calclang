# type: ignore

from parser.ExprParser import ExprParser
from parser.ExprParserVisitor import ExprParserVisitor


from .calc_ast import Program, Statement, Assignment, Unknown, Range, BinOp, ID, Value


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

    def visitValue(self, ctx: ExprParser.ValueContext):
        unit = self.visit(ctx.valueUnit) if ctx.valueUnit else None
        return Value(self.visit(ctx.value), unit)

    def visitNumericLiteral(self, ctx: ExprParser.NumericLiteralContext):
        return float(ctx.getText())

    def visitBinop(self, ctx: ExprParser.BinopContext):
        return BinOp(self.visit(ctx.lhs), ctx.op.text, self.visit(ctx.rhs))

    def visitIdent(self, ctx: ExprParser.IdentContext):
        return self.visitChildren(ctx)[0]

    def visitRawId(self, ctx: ExprParser.RawIdContext):
        return ID(ctx.getText())

    def visitBracketId(self, ctx: ExprParser.BracketIdContext):
        return ID(ctx.getText()[1:-1])

    def visitRange(self, ctx: ExprParser.RangeContext):
        return Range(self.visit(ctx.bottom), self.visit(ctx.top))

    def visitParens(self, ctx: ExprParser.ParensContext):
        return self.visitChildren(ctx)[1]

    def visitChildren(self, ctx):
        result = super().visitChildren(ctx)

        if result is None or (len(result) == 1 and result[0] is None):
            return Unknown(ctx.getText())

        return result
