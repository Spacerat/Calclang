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
        4,1,38,108,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,2,1,2,1,3,1,3,3,3,33,8,3,1,4,1,4,1,4,1,4,3,4,39,8,4,1,4,1,4,
        3,4,43,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,53,8,4,1,5,1,5,1,
        6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,65,8,7,3,7,67,8,7,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,3,8,89,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,
        8,103,8,8,10,8,12,8,106,9,8,1,8,0,1,16,9,0,2,4,6,8,10,12,14,16,0,
        6,1,0,17,18,1,0,24,30,1,0,32,33,1,0,22,23,1,0,15,16,1,0,13,14,117,
        0,21,1,0,0,0,2,26,1,0,0,0,4,28,1,0,0,0,6,32,1,0,0,0,8,52,1,0,0,0,
        10,54,1,0,0,0,12,56,1,0,0,0,14,66,1,0,0,0,16,88,1,0,0,0,18,20,3,
        8,4,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,
        24,1,0,0,0,23,21,1,0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,27,5,9,0,
        0,27,3,1,0,0,0,28,29,3,6,3,0,29,5,1,0,0,0,30,33,5,34,0,0,31,33,5,
        35,0,0,32,30,1,0,0,0,32,31,1,0,0,0,33,7,1,0,0,0,34,35,3,6,3,0,35,
        36,5,7,0,0,36,38,3,16,8,0,37,39,3,2,1,0,38,37,1,0,0,0,38,39,1,0,
        0,0,39,53,1,0,0,0,40,42,3,16,8,0,41,43,3,2,1,0,42,41,1,0,0,0,42,
        43,1,0,0,0,43,53,1,0,0,0,44,45,3,16,8,0,45,46,7,0,0,0,46,47,3,16,
        8,0,47,53,1,0,0,0,48,49,3,6,3,0,49,50,5,21,0,0,50,51,3,6,3,0,51,
        53,1,0,0,0,52,34,1,0,0,0,52,40,1,0,0,0,52,44,1,0,0,0,52,48,1,0,0,
        0,53,9,1,0,0,0,54,55,7,1,0,0,55,11,1,0,0,0,56,57,7,2,0,0,57,13,1,
        0,0,0,58,67,3,4,2,0,59,67,5,31,0,0,60,61,7,3,0,0,61,67,3,12,6,0,
        62,64,3,12,6,0,63,65,3,10,5,0,64,63,1,0,0,0,64,65,1,0,0,0,65,67,
        1,0,0,0,66,58,1,0,0,0,66,59,1,0,0,0,66,60,1,0,0,0,66,62,1,0,0,0,
        67,15,1,0,0,0,68,69,6,8,-1,0,69,89,3,14,7,0,70,71,5,10,0,0,71,72,
        3,16,8,0,72,73,5,11,0,0,73,89,1,0,0,0,74,75,3,14,7,0,75,76,5,12,
        0,0,76,77,3,14,7,0,77,89,1,0,0,0,78,79,3,14,7,0,79,80,5,36,0,0,80,
        81,3,14,7,0,81,89,1,0,0,0,82,83,3,14,7,0,83,84,5,36,0,0,84,85,3,
        14,7,0,85,86,5,36,0,0,86,87,3,14,7,0,87,89,1,0,0,0,88,68,1,0,0,0,
        88,70,1,0,0,0,88,74,1,0,0,0,88,78,1,0,0,0,88,82,1,0,0,0,89,104,1,
        0,0,0,90,91,10,7,0,0,91,92,7,4,0,0,92,103,3,16,8,8,93,94,10,3,0,
        0,94,95,7,5,0,0,95,103,3,16,8,4,96,97,10,2,0,0,97,98,5,3,0,0,98,
        103,3,16,8,3,99,100,10,1,0,0,100,101,5,4,0,0,101,103,3,16,8,2,102,
        90,1,0,0,0,102,93,1,0,0,0,102,96,1,0,0,0,102,99,1,0,0,0,103,106,
        1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,17,1,0,0,0,106,104,1,
        0,0,0,10,21,32,38,42,52,64,66,88,102,104
    ]

class ExprParser ( Parser ):

    grammarFileName = "ExprParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'and'", "<INVALID>", 
                     "'or'", "'not'", "'='", "','", "';'", "'('", "')'", 
                     "'to'", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'['", 
                     "']'", "'~'", "'$'", "'\\u00A3'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'..'" ]

    symbolicNames = [ "<INVALID>", "SINGLE_COMMENT", "MULTILINE_COMMENT", 
                      "AND", "THEN", "OR", "NOT", "EQ", "COMMA", "SEMI", 
                      "LPAREN", "RPAREN", "TO", "PLUS", "MINUS", "TIMES", 
                      "DIVIDE", "GREATER_THAN", "LESS_THAN", "LSQPAREN", 
                      "RSQPAREN", "VERSUS", "DOLLAR", "POUND", "DAYS", "BUSINESS_DAYS", 
                      "WEEKS", "HOURS", "MINUTES", "SECONDS", "YEARS", "SLASH_DATE", 
                      "INT", "FLOAT", "ID", "BRACKET_ID", "DOTS", "WS", 
                      "NL" ]

    RULE_program = 0
    RULE_terminate = 1
    RULE_id = 2
    RULE_basicId = 3
    RULE_stat = 4
    RULE_unit = 5
    RULE_numericLiteral = 6
    RULE_simpleExpr = 7
    RULE_expr = 8

    ruleNames =  [ "program", "terminate", "id", "basicId", "stat", "unit", 
                   "numericLiteral", "simpleExpr", "expr" ]

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
    GREATER_THAN=17
    LESS_THAN=18
    LSQPAREN=19
    RSQPAREN=20
    VERSUS=21
    DOLLAR=22
    POUND=23
    DAYS=24
    BUSINESS_DAYS=25
    WEEKS=26
    HOURS=27
    MINUTES=28
    SECONDS=29
    YEARS=30
    SLASH_DATE=31
    INT=32
    FLOAT=33
    ID=34
    BRACKET_ID=35
    DOTS=36
    WS=37
    NL=38

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
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 66584577024) != 0:
                self.state = 18
                localctx.statements = self.stat()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
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
            self.state = 26
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

        def basicId(self):
            return self.getTypedRuleContext(ExprParser.BasicIdContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)




    def id_(self):

        localctx = ExprParser.IdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.basicId()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BasicIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_basicId

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RawIdContext(BasicIdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.BasicIdContext
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


    class BracketIdContext(BasicIdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.BasicIdContext
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



    def basicId(self):

        localctx = ExprParser.BasicIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_basicId)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                localctx = ExprParser.RawIdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(ExprParser.ID)
                pass
            elif token in [35]:
                localctx = ExprParser.BracketIdContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 31
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



    class InequalityContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
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

        def GREATER_THAN(self):
            return self.getToken(ExprParser.GREATER_THAN, 0)
        def LESS_THAN(self):
            return self.getToken(ExprParser.LESS_THAN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInequality" ):
                listener.enterInequality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInequality" ):
                listener.exitInequality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInequality" ):
                return visitor.visitInequality(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.target = None # BasicIdContext
            self.expression = None # ExprContext
            self.copyFrom(ctx)

        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)
        def basicId(self):
            return self.getTypedRuleContext(ExprParser.BasicIdContext,0)

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


    class VersusContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.lhs = None # BasicIdContext
            self.rhs = None # BasicIdContext
            self.copyFrom(ctx)

        def VERSUS(self):
            return self.getToken(ExprParser.VERSUS, 0)
        def basicId(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.BasicIdContext)
            else:
                return self.getTypedRuleContext(ExprParser.BasicIdContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVersus" ):
                listener.enterVersus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVersus" ):
                listener.exitVersus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVersus" ):
                return visitor.visitVersus(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = ExprParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = ExprParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                localctx.target = self.basicId()
                self.state = 35
                self.match(ExprParser.EQ)
                self.state = 36
                localctx.expression = self.expr(0)
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 37
                    self.terminate()


                pass

            elif la_ == 2:
                localctx = ExprParser.StatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                localctx.expression = self.expr(0)
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 41
                    self.terminate()


                pass

            elif la_ == 3:
                localctx = ExprParser.InequalityContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                localctx.lhs = self.expr(0)
                self.state = 45
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 46
                localctx.rhs = self.expr(0)
                pass

            elif la_ == 4:
                localctx = ExprParser.VersusContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                localctx.lhs = self.basicId()
                self.state = 49
                self.match(ExprParser.VERSUS)
                self.state = 50
                localctx.rhs = self.basicId()
                pass


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

        def YEARS(self):
            return self.getToken(ExprParser.YEARS, 0)

        def WEEKS(self):
            return self.getToken(ExprParser.WEEKS, 0)

        def DAYS(self):
            return self.getToken(ExprParser.DAYS, 0)

        def HOURS(self):
            return self.getToken(ExprParser.HOURS, 0)

        def MINUTES(self):
            return self.getToken(ExprParser.MINUTES, 0)

        def SECONDS(self):
            return self.getToken(ExprParser.SECONDS, 0)

        def BUSINESS_DAYS(self):
            return self.getToken(ExprParser.BUSINESS_DAYS, 0)

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
            self.state = 54
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 2130706432) != 0):
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
            self.state = 56
            _la = self._input.LA(1)
            if not(_la==32 or _la==33):
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


    class SimpleExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_simpleExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DateContext(SimpleExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.SimpleExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SLASH_DATE(self):
            return self.getToken(ExprParser.SLASH_DATE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDate" ):
                listener.enterDate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDate" ):
                listener.exitDate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDate" ):
                return visitor.visitDate(self)
            else:
                return visitor.visitChildren(self)


    class IdentContext(SimpleExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.SimpleExprContext
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


    class CurrencyValueContext(SimpleExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.SimpleExprContext
            super().__init__(parser)
            self.symbol = None # Token
            self.amount = None # NumericLiteralContext
            self.copyFrom(ctx)

        def numericLiteral(self):
            return self.getTypedRuleContext(ExprParser.NumericLiteralContext,0)

        def DOLLAR(self):
            return self.getToken(ExprParser.DOLLAR, 0)
        def POUND(self):
            return self.getToken(ExprParser.POUND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCurrencyValue" ):
                listener.enterCurrencyValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCurrencyValue" ):
                listener.exitCurrencyValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCurrencyValue" ):
                return visitor.visitCurrencyValue(self)
            else:
                return visitor.visitChildren(self)


    class ValueContext(SimpleExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.SimpleExprContext
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



    def simpleExpr(self):

        localctx = ExprParser.SimpleExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_simpleExpr)
        self._la = 0 # Token type
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34, 35]:
                localctx = ExprParser.IdentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.id_()
                pass
            elif token in [31]:
                localctx = ExprParser.DateContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(ExprParser.SLASH_DATE)
                pass
            elif token in [22, 23]:
                localctx = ExprParser.CurrencyValueContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                localctx.symbol = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==22 or _la==23):
                    localctx.symbol = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 61
                localctx.amount = self.numericLiteral()
                pass
            elif token in [32, 33]:
                localctx = ExprParser.ValueContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 62
                localctx.value = self.numericLiteral()
                self.state = 64
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 63
                    localctx.valueUnit = self.unit()


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


    class RangeContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.bottom = None # SimpleExprContext
            self.top = None # SimpleExprContext
            self.mid = None # SimpleExprContext
            self.copyFrom(ctx)

        def TO(self):
            return self.getToken(ExprParser.TO, 0)
        def simpleExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.SimpleExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.SimpleExprContext,i)

        def DOTS(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.DOTS)
            else:
                return self.getToken(ExprParser.DOTS, i)

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


    class SimpleContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def simpleExpr(self):
            return self.getTypedRuleContext(ExprParser.SimpleExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple" ):
                listener.enterSimple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple" ):
                listener.exitSimple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple" ):
                return visitor.visitSimple(self)
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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = ExprParser.SimpleContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 69
                self.simpleExpr()
                pass

            elif la_ == 2:
                localctx = ExprParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 70
                self.match(ExprParser.LPAREN)
                self.state = 71
                self.expr(0)
                self.state = 72
                self.match(ExprParser.RPAREN)
                pass

            elif la_ == 3:
                localctx = ExprParser.RangeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 74
                localctx.bottom = self.simpleExpr()
                self.state = 75
                self.match(ExprParser.TO)
                self.state = 76
                localctx.top = self.simpleExpr()
                pass

            elif la_ == 4:
                localctx = ExprParser.RangeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 78
                localctx.bottom = self.simpleExpr()
                self.state = 79
                self.match(ExprParser.DOTS)
                self.state = 80
                localctx.top = self.simpleExpr()
                pass

            elif la_ == 5:
                localctx = ExprParser.RangeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 82
                localctx.bottom = self.simpleExpr()
                self.state = 83
                self.match(ExprParser.DOTS)
                self.state = 84
                localctx.mid = self.simpleExpr()
                self.state = 85
                self.match(ExprParser.DOTS)
                self.state = 86
                localctx.top = self.simpleExpr()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 104
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 102
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.BinopContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 90
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 91
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 92
                        localctx.rhs = self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.BinopContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 93
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 94
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 95
                        localctx.rhs = self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.BinopContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 96
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 97
                        localctx.op = self.match(ExprParser.AND)
                        self.state = 98
                        localctx.rhs = self.expr(3)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.BinopContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 99
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 100
                        localctx.op = self.match(ExprParser.THEN)
                        self.state = 101
                        localctx.rhs = self.expr(2)
                        pass

             
                self.state = 106
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
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




