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


    # Enter a parse tree produced by ExprParser#id.
    def enterId(self, ctx:ExprParser.IdContext):
        pass

    # Exit a parse tree produced by ExprParser#id.
    def exitId(self, ctx:ExprParser.IdContext):
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


    # Enter a parse tree produced by ExprParser#sequenceAssignment.
    def enterSequenceAssignment(self, ctx:ExprParser.SequenceAssignmentContext):
        pass

    # Exit a parse tree produced by ExprParser#sequenceAssignment.
    def exitSequenceAssignment(self, ctx:ExprParser.SequenceAssignmentContext):
        pass


    # Enter a parse tree produced by ExprParser#statement.
    def enterStatement(self, ctx:ExprParser.StatementContext):
        pass

    # Exit a parse tree produced by ExprParser#statement.
    def exitStatement(self, ctx:ExprParser.StatementContext):
        pass


    # Enter a parse tree produced by ExprParser#inequality.
    def enterInequality(self, ctx:ExprParser.InequalityContext):
        pass

    # Exit a parse tree produced by ExprParser#inequality.
    def exitInequality(self, ctx:ExprParser.InequalityContext):
        pass


    # Enter a parse tree produced by ExprParser#versus.
    def enterVersus(self, ctx:ExprParser.VersusContext):
        pass

    # Exit a parse tree produced by ExprParser#versus.
    def exitVersus(self, ctx:ExprParser.VersusContext):
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


    # Enter a parse tree produced by ExprParser#ident.
    def enterIdent(self, ctx:ExprParser.IdentContext):
        pass

    # Exit a parse tree produced by ExprParser#ident.
    def exitIdent(self, ctx:ExprParser.IdentContext):
        pass


    # Enter a parse tree produced by ExprParser#date.
    def enterDate(self, ctx:ExprParser.DateContext):
        pass

    # Exit a parse tree produced by ExprParser#date.
    def exitDate(self, ctx:ExprParser.DateContext):
        pass


    # Enter a parse tree produced by ExprParser#currencyValue.
    def enterCurrencyValue(self, ctx:ExprParser.CurrencyValueContext):
        pass

    # Exit a parse tree produced by ExprParser#currencyValue.
    def exitCurrencyValue(self, ctx:ExprParser.CurrencyValueContext):
        pass


    # Enter a parse tree produced by ExprParser#value.
    def enterValue(self, ctx:ExprParser.ValueContext):
        pass

    # Exit a parse tree produced by ExprParser#value.
    def exitValue(self, ctx:ExprParser.ValueContext):
        pass


    # Enter a parse tree produced by ExprParser#parens.
    def enterParens(self, ctx:ExprParser.ParensContext):
        pass

    # Exit a parse tree produced by ExprParser#parens.
    def exitParens(self, ctx:ExprParser.ParensContext):
        pass


    # Enter a parse tree produced by ExprParser#range.
    def enterRange(self, ctx:ExprParser.RangeContext):
        pass

    # Exit a parse tree produced by ExprParser#range.
    def exitRange(self, ctx:ExprParser.RangeContext):
        pass


    # Enter a parse tree produced by ExprParser#simple.
    def enterSimple(self, ctx:ExprParser.SimpleContext):
        pass

    # Exit a parse tree produced by ExprParser#simple.
    def exitSimple(self, ctx:ExprParser.SimpleContext):
        pass


    # Enter a parse tree produced by ExprParser#binop.
    def enterBinop(self, ctx:ExprParser.BinopContext):
        pass

    # Exit a parse tree produced by ExprParser#binop.
    def exitBinop(self, ctx:ExprParser.BinopContext):
        pass


    # Enter a parse tree produced by ExprParser#sequenceId.
    def enterSequenceId(self, ctx:ExprParser.SequenceIdContext):
        pass

    # Exit a parse tree produced by ExprParser#sequenceId.
    def exitSequenceId(self, ctx:ExprParser.SequenceIdContext):
        pass


    # Enter a parse tree produced by ExprParser#sequenceIndexAtId.
    def enterSequenceIndexAtId(self, ctx:ExprParser.SequenceIndexAtIdContext):
        pass

    # Exit a parse tree produced by ExprParser#sequenceIndexAtId.
    def exitSequenceIndexAtId(self, ctx:ExprParser.SequenceIndexAtIdContext):
        pass


    # Enter a parse tree produced by ExprParser#sequenceIndexAbsolute.
    def enterSequenceIndexAbsolute(self, ctx:ExprParser.SequenceIndexAbsoluteContext):
        pass

    # Exit a parse tree produced by ExprParser#sequenceIndexAbsolute.
    def exitSequenceIndexAbsolute(self, ctx:ExprParser.SequenceIndexAbsoluteContext):
        pass


    # Enter a parse tree produced by ExprParser#sequenceIndexRelative.
    def enterSequenceIndexRelative(self, ctx:ExprParser.SequenceIndexRelativeContext):
        pass

    # Exit a parse tree produced by ExprParser#sequenceIndexRelative.
    def exitSequenceIndexRelative(self, ctx:ExprParser.SequenceIndexRelativeContext):
        pass



del ExprParser