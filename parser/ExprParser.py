# Generated from ExprParser.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,28,86,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,1,0,1,1,1,1,1,2,1,
        2,3,2,29,8,2,1,3,1,3,1,3,1,3,3,3,35,8,3,1,3,1,3,3,3,39,8,3,3,3,41,
        8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,3,7,55,8,7,1,
        7,1,7,1,7,1,7,3,7,61,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,3,7,79,8,7,5,7,81,8,7,10,7,12,7,84,9,7,1,
        7,0,1,14,8,0,2,4,6,8,10,12,14,0,5,1,0,17,18,1,0,19,22,1,0,23,24,
        1,0,15,16,1,0,13,14,91,0,19,1,0,0,0,2,24,1,0,0,0,4,28,1,0,0,0,6,
        40,1,0,0,0,8,42,1,0,0,0,10,46,1,0,0,0,12,48,1,0,0,0,14,60,1,0,0,
        0,16,18,3,6,3,0,17,16,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,
        1,0,0,0,20,22,1,0,0,0,21,19,1,0,0,0,22,23,5,0,0,1,23,1,1,0,0,0,24,
        25,5,9,0,0,25,3,1,0,0,0,26,29,5,25,0,0,27,29,5,26,0,0,28,26,1,0,
        0,0,28,27,1,0,0,0,29,5,1,0,0,0,30,31,3,4,2,0,31,32,5,7,0,0,32,34,
        3,14,7,0,33,35,3,2,1,0,34,33,1,0,0,0,34,35,1,0,0,0,35,41,1,0,0,0,
        36,38,3,14,7,0,37,39,3,2,1,0,38,37,1,0,0,0,38,39,1,0,0,0,39,41,1,
        0,0,0,40,30,1,0,0,0,40,36,1,0,0,0,41,7,1,0,0,0,42,43,5,10,0,0,43,
        44,7,0,0,0,44,45,5,11,0,0,45,9,1,0,0,0,46,47,7,1,0,0,47,11,1,0,0,
        0,48,49,7,2,0,0,49,13,1,0,0,0,50,51,6,7,-1,0,51,61,3,4,2,0,52,54,
        3,12,6,0,53,55,3,10,5,0,54,53,1,0,0,0,54,55,1,0,0,0,55,61,1,0,0,
        0,56,57,5,10,0,0,57,58,3,14,7,0,58,59,5,11,0,0,59,61,1,0,0,0,60,
        50,1,0,0,0,60,52,1,0,0,0,60,56,1,0,0,0,61,82,1,0,0,0,62,63,10,5,
        0,0,63,64,7,3,0,0,64,81,3,14,7,6,65,66,10,3,0,0,66,67,7,4,0,0,67,
        81,3,14,7,4,68,69,10,2,0,0,69,70,5,3,0,0,70,81,3,14,7,3,71,72,10,
        1,0,0,72,73,5,4,0,0,73,81,3,14,7,2,74,75,10,4,0,0,75,76,5,12,0,0,
        76,78,3,14,7,0,77,79,3,8,4,0,78,77,1,0,0,0,78,79,1,0,0,0,79,81,1,
        0,0,0,80,62,1,0,0,0,80,65,1,0,0,0,80,68,1,0,0,0,80,71,1,0,0,0,80,
        74,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,15,1,0,0,
        0,84,82,1,0,0,0,10,19,28,34,38,40,54,60,78,80,82
    ]

class ExprParser ( Parser ):

    grammarFileName = "ExprParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'and'", "<INVALID>", 
                     "'or'", "'not'", "'='", "','", "';'", "'('", "')'", 
                     "'to'", "'+'", "'-'", "'*'", "'/'", "'linear'", "'gaussian'" ]

    symbolicNames = [ "<INVALID>", "SINGLE_COMMENT", "MULTILINE_COMMENT", 
                      "AND", "THEN", "OR", "NOT", "EQ", "COMMA", "SEMI", 
                      "LPAREN", "RPAREN", "TO", "PLUS", "MINUS", "TIMES", 
                      "DIVIDE", "LINEAR", "GAUSSIAN", "DAYS", "WEEKS", "HOURS", 
                      "MINUTES", "INT", "FLOAT", "ID", "BRACKET_ID", "WS", 
                      "NL" ]

    RULE_program = 0
    RULE_terminate = 1
    RULE_id = 2
    RULE_stat = 3
    RULE_rangeSpec = 4
    RULE_unit = 5
    RULE_numericLiteral = 6
    RULE_expr = 7

    ruleNames =  [ "program", "terminate", "id", "stat", "rangeSpec", "unit", 
                   "numericLiteral", "expr" ]

    EOF = Token.EOF
    SINGLE_COMMENT=1
    MULTILINE_COMMENT=2
    AND=3
    THEN=4
    OR=5
    NOT=6
    EQ=7
    COMMA=8
    SEMI=9
    LPAREN=10
    RPAREN=11
    TO=12
    PLUS=13
    MINUS=14
    TIMES=15
    DIVIDE=16
    LINEAR=17
    GAUSSIAN=18
    DAYS=19
    WEEKS=20
    HOURS=21
    MINUTES=22
    INT=23
    FLOAT=24
    ID=25
    BRACKET_ID=26
    WS=27
    NL=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.statements = None # StatContext

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 125830144) != 0:
                self.state = 16
                localctx.statements = self.stat()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(ExprParser.SEMI, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_terminate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminate" ):
                listener.enterTerminate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminate" ):
                listener.exitTerminate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminate" ):
                return visitor.visitTerminate(self)
            else:
                return visitor.visitChildren(self)




    def terminate(self):

        localctx = ExprParser.TerminateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_terminate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(ExprParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_id

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RawIdContext(IdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.IdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRawId" ):
                listener.enterRawId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRawId" ):
                listener.exitRawId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRawId" ):
                return visitor.visitRawId(self)
            else:
                return visitor.visitChildren(self)


    class BracketIdContext(IdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.IdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BRACKET_ID(self):
            return self.getToken(ExprParser.BRACKET_ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBracketId" ):
                listener.enterBracketId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBracketId" ):
                listener.exitBracketId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBracketId" ):
                return visitor.visitBracketId(self)
            else:
                return visitor.visitChildren(self)



    def id_(self):

        localctx = ExprParser.IdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_id)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                localctx = ExprParser.RawIdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.match(ExprParser.ID)
                pass
            elif token in [26]:
                localctx = ExprParser.BracketIdContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(ExprParser.BRACKET_ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignmentContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.target = None # IdContext
            self.expression = None # ExprContext
            self.copyFrom(ctx)

        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)
        def id_(self):
            return self.getTypedRuleContext(ExprParser.IdContext,0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def terminate(self):
            return self.getTypedRuleContext(ExprParser.TerminateContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)


    class StatementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.expression = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def terminate(self):
            return self.getTypedRuleContext(ExprParser.TerminateContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = ExprParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = ExprParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                localctx.target = self.id_()
                self.state = 31
                self.match(ExprParser.EQ)
                self.state = 32
                localctx.expression = self.expr(0)
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 33
                    self.terminate()


                pass

            elif la_ == 2:
                localctx = ExprParser.StatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                localctx.expression = self.expr(0)
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 37
                    self.terminate()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def LINEAR(self):
            return self.getToken(ExprParser.LINEAR, 0)

        def GAUSSIAN(self):
            return self.getToken(ExprParser.GAUSSIAN, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_rangeSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRangeSpec" ):
                listener.enterRangeSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRangeSpec" ):
                listener.exitRangeSpec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRangeSpec" ):
                return visitor.visitRangeSpec(self)
            else:
                return visitor.visitChildren(self)




    def rangeSpec(self):

        localctx = ExprParser.RangeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_rangeSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(ExprParser.LPAREN)
            self.state = 43
            _la = self._input.LA(1)
            if not(_la==17 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 44
            self.match(ExprParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WEEKS(self):
            return self.getToken(ExprParser.WEEKS, 0)

        def DAYS(self):
            return self.getToken(ExprParser.DAYS, 0)

        def HOURS(self):
            return self.getToken(ExprParser.HOURS, 0)

        def MINUTES(self):
            return self.getToken(ExprParser.MINUTES, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_unit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnit" ):
                listener.enterUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnit" ):
                listener.exitUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnit" ):
                return visitor.visitUnit(self)
            else:
                return visitor.visitChildren(self)




    def unit(self):

        localctx = ExprParser.UnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_unit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumericLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def FLOAT(self):
            return self.getToken(ExprParser.FLOAT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_numericLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericLiteral" ):
                listener.enterNumericLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericLiteral" ):
                listener.exitNumericLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericLiteral" ):
                return visitor.visitNumericLiteral(self)
            else:
                return visitor.visitChildren(self)




    def numericLiteral(self):

        localctx = ExprParser.NumericLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_numericLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            _la = self._input.LA(1)
            if not(_la==23 or _la==24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class IdentContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def id_(self):
            return self.getTypedRuleContext(ExprParser.IdContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdent" ):
                listener.enterIdent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdent" ):
                listener.exitIdent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdent" ):
                return visitor.visitIdent(self)
            else:
                return visitor.visitChildren(self)


    class RangeContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.bottom = None # ExprContext
            self.top = None # ExprContext
            self.copyFrom(ctx)

        def TO(self):
            return self.getToken(ExprParser.TO, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def rangeSpec(self):
            return self.getTypedRuleContext(ExprParser.RangeSpecContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange" ):
                listener.enterRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange" ):
                listener.exitRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange" ):
                return visitor.visitRange(self)
            else:
                return visitor.visitChildren(self)


    class ValueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.value = None # NumericLiteralContext
            self.valueUnit = None # UnitContext
            self.copyFrom(ctx)

        def numericLiteral(self):
            return self.getTypedRuleContext(ExprParser.NumericLiteralContext,0)

        def unit(self):
            return self.getTypedRuleContext(ExprParser.UnitContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)


    class BinopContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.lhs = None # ExprContext
            self.op = None # Token
            self.rhs = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def TIMES(self):
            return self.getToken(ExprParser.TIMES, 0)
        def DIVIDE(self):
            return self.getToken(ExprParser.DIVIDE, 0)
        def PLUS(self):
            return self.getToken(ExprParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(ExprParser.MINUS, 0)
        def AND(self):
            return self.getToken(ExprParser.AND, 0)
        def THEN(self):
            return self.getToken(ExprParser.THEN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinop" ):
                listener.enterBinop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinop" ):
                listener.exitBinop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinop" ):
                return visitor.visitBinop(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25, 26]:
                localctx = ExprParser.IdentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 51
                self.id_()
                pass
            elif token in [23, 24]:
                localctx = ExprParser.ValueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                localctx.value = self.numericLiteral()
                self.state = 54
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 53
                    localctx.valueUnit = self.unit()


                pass
            elif token in [10]:
                localctx = ExprParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 56
                self.match(ExprParser.LPAREN)
                self.state = 57
                self.expr(0)
                self.state = 58
                self.match(ExprParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 82
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 80
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.BinopContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 62
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 63
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 64
                        localctx.rhs = self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.BinopContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 65
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 66
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 67
                        localctx.rhs = self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.BinopContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 68
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 69
                        localctx.op = self.match(ExprParser.AND)
                        self.state = 70
                        localctx.rhs = self.expr(3)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.BinopContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 71
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 72
                        localctx.op = self.match(ExprParser.THEN)
                        self.state = 73
                        localctx.rhs = self.expr(2)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.RangeContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.bottom = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 74
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 75
                        self.match(ExprParser.TO)
                        self.state = 76
                        localctx.top = self.expr(0)
                        self.state = 78
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                        if la_ == 1:
                            self.state = 77
                            self.rangeSpec()


                        pass

             
                self.state = 84
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         




