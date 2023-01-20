# Generated from CalcParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalcParser import CalcParser
else:
    from CalcParser import CalcParser

# This class defines a complete generic visitor for a parse tree produced by CalcParser.

class CalcParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalcParser#program.
    def visitProgram(self, ctx:CalcParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#assignment.
    def visitAssignment(self, ctx:CalcParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#statement.
    def visitStatement(self, ctx:CalcParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#empty.
    def visitEmpty(self, ctx:CalcParser.EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#expr.
    def visitExpr(self, ctx:CalcParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#word.
    def visitWord(self, ctx:CalcParser.WordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#wordElement.
    def visitWordElement(self, ctx:CalcParser.WordElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#parens.
    def visitParens(self, ctx:CalcParser.ParensContext):
        return self.visitChildren(ctx)



del CalcParser