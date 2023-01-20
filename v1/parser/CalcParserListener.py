# Generated from CalcParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalcParser import CalcParser
else:
    from CalcParser import CalcParser

# This class defines a complete listener for a parse tree produced by CalcParser.
class CalcParserListener(ParseTreeListener):

    # Enter a parse tree produced by CalcParser#program.
    def enterProgram(self, ctx:CalcParser.ProgramContext):
        pass

    # Exit a parse tree produced by CalcParser#program.
    def exitProgram(self, ctx:CalcParser.ProgramContext):
        pass


    # Enter a parse tree produced by CalcParser#assignment.
    def enterAssignment(self, ctx:CalcParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CalcParser#assignment.
    def exitAssignment(self, ctx:CalcParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CalcParser#statement.
    def enterStatement(self, ctx:CalcParser.StatementContext):
        pass

    # Exit a parse tree produced by CalcParser#statement.
    def exitStatement(self, ctx:CalcParser.StatementContext):
        pass


    # Enter a parse tree produced by CalcParser#empty.
    def enterEmpty(self, ctx:CalcParser.EmptyContext):
        pass

    # Exit a parse tree produced by CalcParser#empty.
    def exitEmpty(self, ctx:CalcParser.EmptyContext):
        pass


    # Enter a parse tree produced by CalcParser#expr.
    def enterExpr(self, ctx:CalcParser.ExprContext):
        pass

    # Exit a parse tree produced by CalcParser#expr.
    def exitExpr(self, ctx:CalcParser.ExprContext):
        pass


    # Enter a parse tree produced by CalcParser#word.
    def enterWord(self, ctx:CalcParser.WordContext):
        pass

    # Exit a parse tree produced by CalcParser#word.
    def exitWord(self, ctx:CalcParser.WordContext):
        pass


    # Enter a parse tree produced by CalcParser#wordElement.
    def enterWordElement(self, ctx:CalcParser.WordElementContext):
        pass

    # Exit a parse tree produced by CalcParser#wordElement.
    def exitWordElement(self, ctx:CalcParser.WordElementContext):
        pass


    # Enter a parse tree produced by CalcParser#parens.
    def enterParens(self, ctx:CalcParser.ParensContext):
        pass

    # Exit a parse tree produced by CalcParser#parens.
    def exitParens(self, ctx:CalcParser.ParensContext):
        pass



del CalcParser