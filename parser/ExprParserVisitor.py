# Generated from ExprParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#program.
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#terminate.
    def visitTerminate(self, ctx:ExprParser.TerminateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#rawId.
    def visitRawId(self, ctx:ExprParser.RawIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bracketId.
    def visitBracketId(self, ctx:ExprParser.BracketIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assignment.
    def visitAssignment(self, ctx:ExprParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#statement.
    def visitStatement(self, ctx:ExprParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#rangeSpec.
    def visitRangeSpec(self, ctx:ExprParser.RangeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#unit.
    def visitUnit(self, ctx:ExprParser.UnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#numericLiteral.
    def visitNumericLiteral(self, ctx:ExprParser.NumericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parens.
    def visitParens(self, ctx:ExprParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ident.
    def visitIdent(self, ctx:ExprParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#range.
    def visitRange(self, ctx:ExprParser.RangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#value.
    def visitValue(self, ctx:ExprParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#binop.
    def visitBinop(self, ctx:ExprParser.BinopContext):
        return self.visitChildren(ctx)



del ExprParser