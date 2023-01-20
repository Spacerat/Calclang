from parser.CalcParserVisitor import CalcParserVisitor, ParseTreeVisitor
from parser.CalcParser import CalcParser
from .raw_ast import RawAssignment, RawStatement
from utils.aggregating_visitor import AggregatingVisitor


class Visitor(CalcParserVisitor, AggregatingVisitor):
    def visitAssignment(self, ctx: CalcParser.AssignmentContext):
        target = [self.visit(x) for x in ctx.target]
        expression = self.visit(ctx.expression)
        return RawAssignment(target=target, expression=expression)

    def visitStatement(self, ctx: CalcParser.StatementContext):
        return RawStatement(self.visit(ctx.expression))

    def visitExpr(self, ctx: CalcParser.ExprContext):
        return [self.visit(x) for x in ctx.items]

    def visitParens(self, ctx: CalcParser.ParensContext):
        return self.visit(ctx.expression)

    def visitWord(self, ctx: CalcParser.WordContext):
        return ctx.getText()

    def visitEmpty(self, ctx: CalcParser.EmptyContext):
        return None
