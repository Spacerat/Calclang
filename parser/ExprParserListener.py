# Generated from ExprParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprParserListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#program.
    def enterProgram(self, ctx:ExprParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExprParser#program.
    def exitProgram(self, ctx:ExprParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExprParser#terminate.
    def enterTerminate(self, ctx:ExprParser.TerminateContext):
        pass

    # Exit a parse tree produced by ExprParser#terminate.
    def exitTerminate(self, ctx:ExprParser.TerminateContext):
        pass


    # Enter a parse tree produced by ExprParser#rawId.
    def enterRawId(self, ctx:ExprParser.RawIdContext):
        pass

    # Exit a parse tree produced by ExprParser#rawId.
    def exitRawId(self, ctx:ExprParser.RawIdContext):
        pass


    # Enter a parse tree produced by ExprParser#bracketId.
    def enterBracketId(self, ctx:ExprParser.BracketIdContext):
        pass

    # Exit a parse tree produced by ExprParser#bracketId.
    def exitBracketId(self, ctx:ExprParser.BracketIdContext):
        pass


    # Enter a parse tree produced by ExprParser#assignment.
    def enterAssignment(self, ctx:ExprParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ExprParser#assignment.
    def exitAssignment(self, ctx:ExprParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ExprParser#statement.
    def enterStatement(self, ctx:ExprParser.StatementContext):
        pass

    # Exit a parse tree produced by ExprParser#statement.
    def exitStatement(self, ctx:ExprParser.StatementContext):
        pass


    # Enter a parse tree produced by ExprParser#rangeSpec.
    def enterRangeSpec(self, ctx:ExprParser.RangeSpecContext):
        pass

    # Exit a parse tree produced by ExprParser#rangeSpec.
    def exitRangeSpec(self, ctx:ExprParser.RangeSpecContext):
        pass


    # Enter a parse tree produced by ExprParser#unit.
    def enterUnit(self, ctx:ExprParser.UnitContext):
        pass

    # Exit a parse tree produced by ExprParser#unit.
    def exitUnit(self, ctx:ExprParser.UnitContext):
        pass


    # Enter a parse tree produced by ExprParser#numericLiteral.
    def enterNumericLiteral(self, ctx:ExprParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by ExprParser#numericLiteral.
    def exitNumericLiteral(self, ctx:ExprParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by ExprParser#parens.
    def enterParens(self, ctx:ExprParser.ParensContext):
        pass

    # Exit a parse tree produced by ExprParser#parens.
    def exitParens(self, ctx:ExprParser.ParensContext):
        pass


    # Enter a parse tree produced by ExprParser#ident.
    def enterIdent(self, ctx:ExprParser.IdentContext):
        pass

    # Exit a parse tree produced by ExprParser#ident.
    def exitIdent(self, ctx:ExprParser.IdentContext):
        pass


    # Enter a parse tree produced by ExprParser#range.
    def enterRange(self, ctx:ExprParser.RangeContext):
        pass

    # Exit a parse tree produced by ExprParser#range.
    def exitRange(self, ctx:ExprParser.RangeContext):
        pass


    # Enter a parse tree produced by ExprParser#value.
    def enterValue(self, ctx:ExprParser.ValueContext):
        pass

    # Exit a parse tree produced by ExprParser#value.
    def exitValue(self, ctx:ExprParser.ValueContext):
        pass


    # Enter a parse tree produced by ExprParser#binop.
    def enterBinop(self, ctx:ExprParser.BinopContext):
        pass

    # Exit a parse tree produced by ExprParser#binop.
    def exitBinop(self, ctx:ExprParser.BinopContext):
        pass



del ExprParser