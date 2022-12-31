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
        4,1,34,127,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,1,1,1,2,1,2,3,2,35,8,2,1,3,1,3,3,3,39,8,3,1,4,1,
        4,1,4,1,4,3,4,45,8,4,1,4,1,4,1,4,1,4,3,4,51,8,4,1,4,1,4,3,4,55,8,
        4,1,4,1,4,1,4,1,4,3,4,61,8,4,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,
        1,8,1,8,1,8,1,8,1,8,3,8,77,8,8,1,8,1,8,1,8,1,8,3,8,83,8,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,101,
        8,8,5,8,103,8,8,10,8,12,8,106,9,8,1,9,1,9,1,9,1,9,1,9,5,9,113,8,
        9,10,9,12,9,116,9,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,3,10,125,8,
        10,1,10,0,1,16,11,0,2,4,6,8,10,12,14,16,18,20,0,6,1,0,17,18,1,0,
        23,28,1,0,29,30,1,0,21,22,1,0,15,16,1,0,13,14,137,0,25,1,0,0,0,2,
        30,1,0,0,0,4,34,1,0,0,0,6,38,1,0,0,0,8,60,1,0,0,0,10,62,1,0,0,0,
        12,66,1,0,0,0,14,68,1,0,0,0,16,82,1,0,0,0,18,107,1,0,0,0,20,124,
        1,0,0,0,22,24,3,8,4,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,
        25,26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,29,5,0,0,1,29,1,1,0,
        0,0,30,31,5,9,0,0,31,3,1,0,0,0,32,35,3,6,3,0,33,35,3,18,9,0,34,32,
        1,0,0,0,34,33,1,0,0,0,35,5,1,0,0,0,36,39,5,31,0,0,37,39,5,32,0,0,
        38,36,1,0,0,0,38,37,1,0,0,0,39,7,1,0,0,0,40,41,3,6,3,0,41,42,5,7,
        0,0,42,44,3,16,8,0,43,45,3,2,1,0,44,43,1,0,0,0,44,45,1,0,0,0,45,
        61,1,0,0,0,46,47,3,18,9,0,47,48,5,7,0,0,48,50,3,16,8,0,49,51,3,2,
        1,0,50,49,1,0,0,0,50,51,1,0,0,0,51,61,1,0,0,0,52,54,3,16,8,0,53,
        55,3,2,1,0,54,53,1,0,0,0,54,55,1,0,0,0,55,61,1,0,0,0,56,57,3,16,
        8,0,57,58,7,0,0,0,58,59,3,16,8,0,59,61,1,0,0,0,60,40,1,0,0,0,60,
        46,1,0,0,0,60,52,1,0,0,0,60,56,1,0,0,0,61,9,1,0,0,0,62,63,5,10,0,
        0,63,64,5,31,0,0,64,65,5,11,0,0,65,11,1,0,0,0,66,67,7,1,0,0,67,13,
        1,0,0,0,68,69,7,2,0,0,69,15,1,0,0,0,70,71,6,8,-1,0,71,83,3,4,2,0,
        72,73,7,3,0,0,73,83,3,14,7,0,74,76,3,14,7,0,75,77,3,12,6,0,76,75,
        1,0,0,0,76,77,1,0,0,0,77,83,1,0,0,0,78,79,5,10,0,0,79,80,3,16,8,
        0,80,81,5,11,0,0,81,83,1,0,0,0,82,70,1,0,0,0,82,72,1,0,0,0,82,74,
        1,0,0,0,82,78,1,0,0,0,83,104,1,0,0,0,84,85,10,5,0,0,85,86,7,4,0,
        0,86,103,3,16,8,6,87,88,10,3,0,0,88,89,7,5,0,0,89,103,3,16,8,4,90,
        91,10,2,0,0,91,92,5,3,0,0,92,103,3,16,8,3,93,94,10,1,0,0,94,95,5,
        4,0,0,95,103,3,16,8,2,96,97,10,4,0,0,97,98,5,12,0,0,98,100,3,16,
        8,0,99,101,3,10,5,0,100,99,1,0,0,0,100,101,1,0,0,0,101,103,1,0,0,
        0,102,84,1,0,0,0,102,87,1,0,0,0,102,90,1,0,0,0,102,93,1,0,0,0,102,
        96,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,17,
        1,0,0,0,106,104,1,0,0,0,107,108,3,6,3,0,108,109,5,19,0,0,109,114,
        3,20,10,0,110,111,5,8,0,0,111,113,3,20,10,0,112,110,1,0,0,0,113,
        116,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,117,1,0,0,0,116,
        114,1,0,0,0,117,118,5,20,0,0,118,19,1,0,0,0,119,125,5,31,0,0,120,
        125,5,29,0,0,121,122,5,31,0,0,122,123,7,5,0,0,123,125,5,29,0,0,124,
        119,1,0,0,0,124,120,1,0,0,0,124,121,1,0,0,0,125,21,1,0,0,0,14,25,
        34,38,44,50,54,60,76,82,100,102,104,114,124
    ]

class ExprParser ( Parser ):

    grammarFileName = "ExprParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'and'", "<INVALID>", 
                     "'or'", "'not'", "'='", "','", "';'", "'('", "')'", 
                     "'to'", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'['", 
                     "']'", "'$'", "'\\u00A3'" ]

    symbolicNames = [ "<INVALID>", "SINGLE_COMMENT", "MULTILINE_COMMENT", 
                      "AND", "THEN", "OR", "NOT", "EQ", "COMMA", "SEMI", 
                      "LPAREN", "RPAREN", "TO", "PLUS", "MINUS", "TIMES", 
                      "DIVIDE", "GREATER_THAN", "LESS_THAN", "LSQPAREN", 
                      "RSQPAREN", "DOLLAR", "POUND", "DAYS", "WEEKS", "HOURS", 
                      "MINUTES", "SECONDS", "YEARS", "INT", "FLOAT", "ID", 
                      "BRACKET_ID", "WS", "NL" ]

    RULE_program = 0
    RULE_terminate = 1
    RULE_id = 2
    RULE_basicId = 3
    RULE_stat = 4
    RULE_rangeSpec = 5
    RULE_unit = 6
    RULE_numericLiteral = 7
    RULE_expr = 8
    RULE_sequenceId = 9
    RULE_sequenceIndex = 10

    ruleNames =  [ "program", "terminate", "id", "basicId", "stat", "rangeSpec", 
                   "unit", "numericLiteral", "expr", "sequenceId", "sequenceIndex" ]

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
    DOLLAR=21
    POUND=22
    DAYS=23
    WEEKS=24
    HOURS=25
    MINUTES=26
    SECONDS=27
    YEARS=28
    INT=29
    FLOAT=30
    ID=31
    BRACKET_ID=32
    WS=33
    NL=34

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
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 8059356160) != 0:
                self.state = 22
                localctx.statements = self.stat()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
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
            self.state = 30
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


        def sequenceId(self):
            return self.getTypedRuleContext(ExprParser.SequenceIdContext,0)


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
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.basicId()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.sequenceId()
                pass


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
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                localctx = ExprParser.RawIdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.match(ExprParser.ID)
                pass
            elif token in [32]:
                localctx = ExprParser.BracketIdContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 37
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



    class SequenceAssignmentContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.target = None # SequenceIdContext
            self.expression = None # ExprContext
            self.copyFrom(ctx)

        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)
        def sequenceId(self):
            return self.getTypedRuleContext(ExprParser.SequenceIdContext,0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def terminate(self):
            return self.getTypedRuleContext(ExprParser.TerminateContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequenceAssignment" ):
                listener.enterSequenceAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequenceAssignment" ):
                listener.exitSequenceAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequenceAssignment" ):
                return visitor.visitSequenceAssignment(self)
            else:
                return visitor.visitChildren(self)


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



    def stat(self):

        localctx = ExprParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = ExprParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                localctx.target = self.basicId()
                self.state = 41
                self.match(ExprParser.EQ)
                self.state = 42
                localctx.expression = self.expr(0)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 43
                    self.terminate()


                pass

            elif la_ == 2:
                localctx = ExprParser.SequenceAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                localctx.target = self.sequenceId()
                self.state = 47
                self.match(ExprParser.EQ)
                self.state = 48
                localctx.expression = self.expr(0)
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 49
                    self.terminate()


                pass

            elif la_ == 3:
                localctx = ExprParser.StatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                localctx.expression = self.expr(0)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 53
                    self.terminate()


                pass

            elif la_ == 4:
                localctx = ExprParser.InequalityContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                localctx.lhs = self.expr(0)
                self.state = 57
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 58
                localctx.rhs = self.expr(0)
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
            self.kind = None # Token

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

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
        self.enterRule(localctx, 10, self.RULE_rangeSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(ExprParser.LPAREN)
            self.state = 63
            localctx.kind = self.match(ExprParser.ID)
            self.state = 64
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
        self.enterRule(localctx, 12, self.RULE_unit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 528482304) != 0):
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
        self.enterRule(localctx, 14, self.RULE_numericLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            _la = self._input.LA(1)
            if not(_la==29 or _la==30):
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


    class CurrencyValueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31, 32]:
                localctx = ExprParser.IdentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 71
                self.id_()
                pass
            elif token in [21, 22]:
                localctx = ExprParser.CurrencyValueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 72
                localctx.symbol = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    localctx.symbol = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 73
                localctx.amount = self.numericLiteral()
                pass
            elif token in [29, 30]:
                localctx = ExprParser.ValueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 74
                localctx.value = self.numericLiteral()
                self.state = 76
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 75
                    localctx.valueUnit = self.unit()


                pass
            elif token in [10]:
                localctx = ExprParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 78
                self.match(ExprParser.LPAREN)
                self.state = 79
                self.expr(0)
                self.state = 80
                self.match(ExprParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 104
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 102
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.BinopContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 84
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 85
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 86
                        localctx.rhs = self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.BinopContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 87
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 88
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 89
                        localctx.rhs = self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.BinopContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 90
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 91
                        localctx.op = self.match(ExprParser.AND)
                        self.state = 92
                        localctx.rhs = self.expr(3)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.BinopContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 93
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 94
                        localctx.op = self.match(ExprParser.THEN)
                        self.state = 95
                        localctx.rhs = self.expr(2)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.RangeContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.bottom = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 96
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 97
                        self.match(ExprParser.TO)
                        self.state = 98
                        localctx.top = self.expr(0)
                        self.state = 100
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                        if la_ == 1:
                            self.state = 99
                            self.rangeSpec()


                        pass

             
                self.state = 106
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class SequenceIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # BasicIdContext
            self._sequenceIndex = None # SequenceIndexContext
            self.args = list() # of SequenceIndexContexts

        def LSQPAREN(self):
            return self.getToken(ExprParser.LSQPAREN, 0)

        def RSQPAREN(self):
            return self.getToken(ExprParser.RSQPAREN, 0)

        def basicId(self):
            return self.getTypedRuleContext(ExprParser.BasicIdContext,0)


        def sequenceIndex(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.SequenceIndexContext)
            else:
                return self.getTypedRuleContext(ExprParser.SequenceIndexContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_sequenceId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequenceId" ):
                listener.enterSequenceId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequenceId" ):
                listener.exitSequenceId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequenceId" ):
                return visitor.visitSequenceId(self)
            else:
                return visitor.visitChildren(self)




    def sequenceId(self):

        localctx = ExprParser.SequenceIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_sequenceId)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            localctx.name = self.basicId()
            self.state = 108
            self.match(ExprParser.LSQPAREN)
            self.state = 109
            localctx._sequenceIndex = self.sequenceIndex()
            localctx.args.append(localctx._sequenceIndex)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 110
                self.match(ExprParser.COMMA)
                self.state = 111
                localctx._sequenceIndex = self.sequenceIndex()
                localctx.args.append(localctx._sequenceIndex)
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 117
            self.match(ExprParser.RSQPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SequenceIndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_sequenceIndex

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SequenceIndexAtIdContext(SequenceIndexContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.SequenceIndexContext
            super().__init__(parser)
            self.seqId = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequenceIndexAtId" ):
                listener.enterSequenceIndexAtId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequenceIndexAtId" ):
                listener.exitSequenceIndexAtId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequenceIndexAtId" ):
                return visitor.visitSequenceIndexAtId(self)
            else:
                return visitor.visitChildren(self)


    class SequenceIndexAbsoluteContext(SequenceIndexContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.SequenceIndexContext
            super().__init__(parser)
            self.seqIdx = None # Token
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequenceIndexAbsolute" ):
                listener.enterSequenceIndexAbsolute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequenceIndexAbsolute" ):
                listener.exitSequenceIndexAbsolute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequenceIndexAbsolute" ):
                return visitor.visitSequenceIndexAbsolute(self)
            else:
                return visitor.visitChildren(self)


    class SequenceIndexRelativeContext(SequenceIndexContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.SequenceIndexContext
            super().__init__(parser)
            self.seqId = None # Token
            self.op = None # Token
            self.seqOffset = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def INT(self):
            return self.getToken(ExprParser.INT, 0)
        def PLUS(self):
            return self.getToken(ExprParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(ExprParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequenceIndexRelative" ):
                listener.enterSequenceIndexRelative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequenceIndexRelative" ):
                listener.exitSequenceIndexRelative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequenceIndexRelative" ):
                return visitor.visitSequenceIndexRelative(self)
            else:
                return visitor.visitChildren(self)



    def sequenceIndex(self):

        localctx = ExprParser.SequenceIndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_sequenceIndex)
        self._la = 0 # Token type
        try:
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = ExprParser.SequenceIndexAtIdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                localctx.seqId = self.match(ExprParser.ID)
                pass

            elif la_ == 2:
                localctx = ExprParser.SequenceIndexAbsoluteContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                localctx.seqIdx = self.match(ExprParser.INT)
                pass

            elif la_ == 3:
                localctx = ExprParser.SequenceIndexRelativeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 121
                localctx.seqId = self.match(ExprParser.ID)
                self.state = 122
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 123
                localctx.seqOffset = self.match(ExprParser.INT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         




