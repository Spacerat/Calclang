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
        4,1,36,138,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,1,1,1,2,1,2,3,2,35,8,2,1,3,1,3,3,3,39,8,3,1,4,1,
        4,1,4,1,4,3,4,45,8,4,1,4,1,4,1,4,1,4,3,4,51,8,4,1,4,1,4,3,4,55,8,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,65,8,4,1,5,1,5,1,6,1,6,1,7,
        1,7,1,7,1,7,1,7,3,7,76,8,7,3,7,78,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,100,8,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,114,8,8,10,
        8,12,8,117,9,8,1,9,1,9,1,9,1,9,1,9,5,9,124,8,9,10,9,12,9,127,9,9,
        1,9,1,9,1,10,1,10,1,10,1,10,1,10,3,10,136,8,10,1,10,0,1,16,11,0,
        2,4,6,8,10,12,14,16,18,20,0,6,1,0,17,18,1,0,24,29,1,0,30,31,1,0,
        22,23,1,0,15,16,1,0,13,14,150,0,25,1,0,0,0,2,30,1,0,0,0,4,34,1,0,
        0,0,6,38,1,0,0,0,8,64,1,0,0,0,10,66,1,0,0,0,12,68,1,0,0,0,14,77,
        1,0,0,0,16,99,1,0,0,0,18,118,1,0,0,0,20,135,1,0,0,0,22,24,3,8,4,
        0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,
        1,0,0,0,27,25,1,0,0,0,28,29,5,0,0,1,29,1,1,0,0,0,30,31,5,9,0,0,31,
        3,1,0,0,0,32,35,3,6,3,0,33,35,3,18,9,0,34,32,1,0,0,0,34,33,1,0,0,
        0,35,5,1,0,0,0,36,39,5,32,0,0,37,39,5,33,0,0,38,36,1,0,0,0,38,37,
        1,0,0,0,39,7,1,0,0,0,40,41,3,6,3,0,41,42,5,7,0,0,42,44,3,16,8,0,
        43,45,3,2,1,0,44,43,1,0,0,0,44,45,1,0,0,0,45,65,1,0,0,0,46,47,3,
        18,9,0,47,48,5,7,0,0,48,50,3,16,8,0,49,51,3,2,1,0,50,49,1,0,0,0,
        50,51,1,0,0,0,51,65,1,0,0,0,52,54,3,16,8,0,53,55,3,2,1,0,54,53,1,
        0,0,0,54,55,1,0,0,0,55,65,1,0,0,0,56,57,3,16,8,0,57,58,7,0,0,0,58,
        59,3,16,8,0,59,65,1,0,0,0,60,61,3,16,8,0,61,62,5,21,0,0,62,63,3,
        16,8,0,63,65,1,0,0,0,64,40,1,0,0,0,64,46,1,0,0,0,64,52,1,0,0,0,64,
        56,1,0,0,0,64,60,1,0,0,0,65,9,1,0,0,0,66,67,7,1,0,0,67,11,1,0,0,
        0,68,69,7,2,0,0,69,13,1,0,0,0,70,78,3,4,2,0,71,72,7,3,0,0,72,78,
        3,12,6,0,73,75,3,12,6,0,74,76,3,10,5,0,75,74,1,0,0,0,75,76,1,0,0,
        0,76,78,1,0,0,0,77,70,1,0,0,0,77,71,1,0,0,0,77,73,1,0,0,0,78,15,
        1,0,0,0,79,80,6,8,-1,0,80,100,3,14,7,0,81,82,5,10,0,0,82,83,3,16,
        8,0,83,84,5,11,0,0,84,100,1,0,0,0,85,86,3,14,7,0,86,87,5,12,0,0,
        87,88,3,14,7,0,88,100,1,0,0,0,89,90,3,14,7,0,90,91,5,34,0,0,91,92,
        3,14,7,0,92,100,1,0,0,0,93,94,3,14,7,0,94,95,5,34,0,0,95,96,3,14,
        7,0,96,97,5,34,0,0,97,98,3,14,7,0,98,100,1,0,0,0,99,79,1,0,0,0,99,
        81,1,0,0,0,99,85,1,0,0,0,99,89,1,0,0,0,99,93,1,0,0,0,100,115,1,0,
        0,0,101,102,10,7,0,0,102,103,7,4,0,0,103,114,3,16,8,8,104,105,10,
        3,0,0,105,106,7,5,0,0,106,114,3,16,8,4,107,108,10,2,0,0,108,109,
        5,3,0,0,109,114,3,16,8,3,110,111,10,1,0,0,111,112,5,4,0,0,112,114,
        3,16,8,2,113,101,1,0,0,0,113,104,1,0,0,0,113,107,1,0,0,0,113,110,
        1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,17,1,
        0,0,0,117,115,1,0,0,0,118,119,3,6,3,0,119,120,5,19,0,0,120,125,3,
        20,10,0,121,122,5,8,0,0,122,124,3,20,10,0,123,121,1,0,0,0,124,127,
        1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,128,1,0,0,0,127,125,
        1,0,0,0,128,129,5,20,0,0,129,19,1,0,0,0,130,136,5,32,0,0,131,136,
        5,30,0,0,132,133,5,32,0,0,133,134,7,5,0,0,134,136,5,30,0,0,135,130,
        1,0,0,0,135,131,1,0,0,0,135,132,1,0,0,0,136,21,1,0,0,0,14,25,34,
        38,44,50,54,64,75,77,99,113,115,125,135
    ]

class ExprParser ( Parser ):

    grammarFileName = "ExprParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'and'", "<INVALID>", 
                     "'or'", "'not'", "'='", "','", "';'", "'('", "')'", 
                     "'to'", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'['", 
                     "']'", "'vs'", "'$'", "'\\u00A3'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'..'" ]

    symbolicNames = [ "<INVALID>", "SINGLE_COMMENT", "MULTILINE_COMMENT", 
                      "AND", "THEN", "OR", "NOT", "EQ", "COMMA", "SEMI", 
                      "LPAREN", "RPAREN", "TO", "PLUS", "MINUS", "TIMES", 
                      "DIVIDE", "GREATER_THAN", "LESS_THAN", "LSQPAREN", 
                      "RSQPAREN", "VERSUS", "DOLLAR", "POUND", "DAYS", "WEEKS", 
                      "HOURS", "MINUTES", "SECONDS", "YEARS", "INT", "FLOAT", 
                      "ID", "BRACKET_ID", "DOTS", "WS", "NL" ]

    RULE_program = 0
    RULE_terminate = 1
    RULE_id = 2
    RULE_basicId = 3
    RULE_stat = 4
    RULE_unit = 5
    RULE_numericLiteral = 6
    RULE_simpleExpr = 7
    RULE_expr = 8
    RULE_sequenceId = 9
    RULE_sequenceIndex = 10

    ruleNames =  [ "program", "terminate", "id", "basicId", "stat", "unit", 
                   "numericLiteral", "simpleExpr", "expr", "sequenceId", 
                   "sequenceIndex" ]

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
    WEEKS=25
    HOURS=26
    MINUTES=27
    SECONDS=28
    YEARS=29
    INT=30
    FLOAT=31
    ID=32
    BRACKET_ID=33
    DOTS=34
    WS=35
    NL=36

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
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 16118711296) != 0:
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
            if token in [32]:
                localctx = ExprParser.RawIdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.match(ExprParser.ID)
                pass
            elif token in [33]:
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


    class VersusContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.lhs = None # ExprContext
            self.rhs = None # ExprContext
            self.copyFrom(ctx)

        def VERSUS(self):
            return self.getToken(ExprParser.VERSUS, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


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
            self.state = 64
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

            elif la_ == 5:
                localctx = ExprParser.VersusContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 60
                localctx.lhs = self.expr(0)
                self.state = 61
                self.match(ExprParser.VERSUS)
                self.state = 62
                localctx.rhs = self.expr(0)
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
            self.state = 66
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0):
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
            self.state = 68
            _la = self._input.LA(1)
            if not(_la==30 or _la==31):
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
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32, 33]:
                localctx = ExprParser.IdentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.id_()
                pass
            elif token in [22, 23]:
                localctx = ExprParser.CurrencyValueContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                localctx.symbol = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==22 or _la==23):
                    localctx.symbol = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 72
                localctx.amount = self.numericLiteral()
                pass
            elif token in [30, 31]:
                localctx = ExprParser.ValueContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                localctx.value = self.numericLiteral()
                self.state = 75
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 74
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
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = ExprParser.SimpleContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 80
                self.simpleExpr()
                pass

            elif la_ == 2:
                localctx = ExprParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 81
                self.match(ExprParser.LPAREN)
                self.state = 82
                self.expr(0)
                self.state = 83
                self.match(ExprParser.RPAREN)
                pass

            elif la_ == 3:
                localctx = ExprParser.RangeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 85
                localctx.bottom = self.simpleExpr()
                self.state = 86
                self.match(ExprParser.TO)
                self.state = 87
                localctx.top = self.simpleExpr()
                pass

            elif la_ == 4:
                localctx = ExprParser.RangeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 89
                localctx.bottom = self.simpleExpr()
                self.state = 90
                self.match(ExprParser.DOTS)
                self.state = 91
                localctx.top = self.simpleExpr()
                pass

            elif la_ == 5:
                localctx = ExprParser.RangeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 93
                localctx.bottom = self.simpleExpr()
                self.state = 94
                self.match(ExprParser.DOTS)
                self.state = 95
                localctx.mid = self.simpleExpr()
                self.state = 96
                self.match(ExprParser.DOTS)
                self.state = 97
                localctx.top = self.simpleExpr()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 115
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 113
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.BinopContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 101
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 102
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 103
                        localctx.rhs = self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.BinopContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 104
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 105
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 106
                        localctx.rhs = self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.BinopContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 107
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 108
                        localctx.op = self.match(ExprParser.AND)
                        self.state = 109
                        localctx.rhs = self.expr(3)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.BinopContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 110
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 111
                        localctx.op = self.match(ExprParser.THEN)
                        self.state = 112
                        localctx.rhs = self.expr(2)
                        pass

             
                self.state = 117
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
            self.state = 118
            localctx.name = self.basicId()
            self.state = 119
            self.match(ExprParser.LSQPAREN)
            self.state = 120
            localctx._sequenceIndex = self.sequenceIndex()
            localctx.args.append(localctx._sequenceIndex)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 121
                self.match(ExprParser.COMMA)
                self.state = 122
                localctx._sequenceIndex = self.sequenceIndex()
                localctx.args.append(localctx._sequenceIndex)
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
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
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = ExprParser.SequenceIndexAtIdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                localctx.seqId = self.match(ExprParser.ID)
                pass

            elif la_ == 2:
                localctx = ExprParser.SequenceIndexAbsoluteContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                localctx.seqIdx = self.match(ExprParser.INT)
                pass

            elif la_ == 3:
                localctx = ExprParser.SequenceIndexRelativeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                localctx.seqId = self.match(ExprParser.ID)
                self.state = 133
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 134
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
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




