# Generated from ExprParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#program.
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#id.
    def visitId(self, ctx:ExprParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#word.
    def visitWord(self, ctx:ExprParser.WordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#wordList.
    def visitWordList(self, ctx:ExprParser.WordListContext):
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


    # Visit a parse tree produced by ExprParser#inequality.
    def visitInequality(self, ctx:ExprParser.InequalityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#versus.
    def visitVersus(self, ctx:ExprParser.VersusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#comment.
    def visitComment(self, ctx:ExprParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#unit.
    def visitUnit(self, ctx:ExprParser.UnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#numericLiteral.
    def visitNumericLiteral(self, ctx:ExprParser.NumericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ident.
    def visitIdent(self, ctx:ExprParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#date.
    def visitDate(self, ctx:ExprParser.DateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#currencyValue.
    def visitCurrencyValue(self, ctx:ExprParser.CurrencyValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#value.
    def visitValue(self, ctx:ExprParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#unitConvert.
    def visitUnitConvert(self, ctx:ExprParser.UnitConvertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parens.
    def visitParens(self, ctx:ExprParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#range.
    def visitRange(self, ctx:ExprParser.RangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#simple.
    def visitSimple(self, ctx:ExprParser.SimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#binop.
    def visitBinop(self, ctx:ExprParser.BinopContext):
        return self.visitChildren(ctx)



del ExprParser