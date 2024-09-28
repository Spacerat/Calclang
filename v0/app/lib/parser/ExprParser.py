# Generated from ExprParser.g4 by ANTLR 4.13.2
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
        4,1,32,128,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,0,5,0,30,8,0,10,0,12,0,33,9,0,1,0,5,0,36,8,0,10,0,12,0,39,9,
        0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,5,3,49,8,3,10,3,12,3,52,9,3,1,
        4,1,4,3,4,56,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,3,5,73,8,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,
        8,85,8,8,3,8,87,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,109,8,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,123,8,9,10,9,12,9,126,9,9,1,
        9,0,1,18,10,0,2,4,6,8,10,12,14,16,18,0,7,2,1,8,8,29,29,1,0,16,17,
        1,0,24,25,1,0,21,22,1,0,14,15,1,0,12,13,2,0,1,1,3,3,139,0,23,1,0,
        0,0,2,42,1,0,0,0,4,44,1,0,0,0,6,46,1,0,0,0,8,55,1,0,0,0,10,72,1,
        0,0,0,12,74,1,0,0,0,14,76,1,0,0,0,16,86,1,0,0,0,18,108,1,0,0,0,20,
        22,5,29,0,0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,
        0,0,24,31,1,0,0,0,25,23,1,0,0,0,26,27,3,10,5,0,27,28,7,0,0,0,28,
        30,1,0,0,0,29,26,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,
        0,32,37,1,0,0,0,33,31,1,0,0,0,34,36,5,29,0,0,35,34,1,0,0,0,36,39,
        1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,37,1,0,0,0,
        40,41,5,0,0,1,41,1,1,0,0,0,42,43,3,8,4,0,43,3,1,0,0,0,44,45,5,26,
        0,0,45,5,1,0,0,0,46,50,3,4,2,0,47,49,3,4,2,0,48,47,1,0,0,0,49,52,
        1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,7,1,0,0,0,52,50,1,0,0,0,53,
        56,3,6,3,0,54,56,5,27,0,0,55,53,1,0,0,0,55,54,1,0,0,0,56,9,1,0,0,
        0,57,58,3,8,4,0,58,59,5,6,0,0,59,60,3,18,9,0,60,73,1,0,0,0,61,73,
        3,18,9,0,62,63,3,18,9,0,63,64,7,1,0,0,64,65,3,18,9,0,65,73,1,0,0,
        0,66,67,3,8,4,0,67,68,5,20,0,0,68,69,3,8,4,0,69,73,1,0,0,0,70,73,
        5,31,0,0,71,73,5,32,0,0,72,57,1,0,0,0,72,61,1,0,0,0,72,62,1,0,0,
        0,72,66,1,0,0,0,72,70,1,0,0,0,72,71,1,0,0,0,73,11,1,0,0,0,74,75,
        5,26,0,0,75,13,1,0,0,0,76,77,7,2,0,0,77,15,1,0,0,0,78,87,3,2,1,0,
        79,87,5,23,0,0,80,81,7,3,0,0,81,87,3,14,7,0,82,84,3,14,7,0,83,85,
        3,12,6,0,84,83,1,0,0,0,84,85,1,0,0,0,85,87,1,0,0,0,86,78,1,0,0,0,
        86,79,1,0,0,0,86,80,1,0,0,0,86,82,1,0,0,0,87,17,1,0,0,0,88,89,6,
        9,-1,0,89,109,3,16,8,0,90,91,5,9,0,0,91,92,3,18,9,0,92,93,5,10,0,
        0,93,109,1,0,0,0,94,95,3,16,8,0,95,96,5,11,0,0,96,97,3,16,8,0,97,
        109,1,0,0,0,98,99,3,16,8,0,99,100,5,28,0,0,100,101,3,16,8,0,101,
        109,1,0,0,0,102,103,3,16,8,0,103,104,5,28,0,0,104,105,3,16,8,0,105,
        106,5,28,0,0,106,107,3,16,8,0,107,109,1,0,0,0,108,88,1,0,0,0,108,
        90,1,0,0,0,108,94,1,0,0,0,108,98,1,0,0,0,108,102,1,0,0,0,109,124,
        1,0,0,0,110,111,10,6,0,0,111,112,7,4,0,0,112,123,3,18,9,7,113,114,
        10,2,0,0,114,115,7,5,0,0,115,123,3,18,9,3,116,117,10,1,0,0,117,118,
        5,2,0,0,118,123,3,18,9,2,119,120,10,7,0,0,120,121,7,6,0,0,121,123,
        3,12,6,0,122,110,1,0,0,0,122,113,1,0,0,0,122,116,1,0,0,0,122,119,
        1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,19,1,
        0,0,0,126,124,1,0,0,0,11,23,31,37,50,55,72,84,86,108,122,124
    ]

class ExprParser ( Parser ):

    grammarFileName = "ExprParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'in'", "'and'", "<INVALID>", "'or'", 
                     "'not'", "'='", "','", "';'", "'('", "')'", "'to'", 
                     "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'['", "']'", 
                     "'~'", "'$'", "'\\u00A3'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'..'" ]

    symbolicNames = [ "<INVALID>", "IN", "AND", "THEN", "OR", "NOT", "EQ", 
                      "COMMA", "SEMI", "LPAREN", "RPAREN", "TO", "PLUS", 
                      "MINUS", "TIMES", "DIVIDE", "GREATER_THAN", "LESS_THAN", 
                      "LSQPAREN", "RSQPAREN", "VERSUS", "DOLLAR", "POUND", 
                      "SLASH_DATE", "INT", "FLOAT", "WORD", "BRACKET_ID", 
                      "DOTS", "NL", "WS_SKIP", "SINGLE_COMMENT", "MULTILINE_COMMENT" ]

    RULE_program = 0
    RULE_id = 1
    RULE_word = 2
    RULE_words = 3
    RULE_basicId = 4
    RULE_stat = 5
    RULE_unit = 6
    RULE_numericLiteral = 7
    RULE_simpleExpr = 8
    RULE_expr = 9

    ruleNames =  [ "program", "id", "word", "words", "basicId", "stat", 
                   "unit", "numericLiteral", "simpleExpr", "expr" ]

    EOF = Token.EOF
    IN=1
    AND=2
    THEN=3
    OR=4
    NOT=5
    EQ=6
    COMMA=7
    SEMI=8
    LPAREN=9
    RPAREN=10
    TO=11
    PLUS=12
    MINUS=13
    TIMES=14
    DIVIDE=15
    GREATER_THAN=16
    LESS_THAN=17
    LSQPAREN=18
    RSQPAREN=19
    VERSUS=20
    DOLLAR=21
    POUND=22
    SLASH_DATE=23
    INT=24
    FLOAT=25
    WORD=26
    BRACKET_ID=27
    DOTS=28
    NL=29
    WS_SKIP=30
    SINGLE_COMMENT=31
    MULTILINE_COMMENT=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.statements = None # StatContext

        def EOF(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.EOF)
            else:
                return self.getToken(ExprParser.EOF, i)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NL)
            else:
                return self.getToken(ExprParser.NL, i)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.SEMI)
            else:
                return self.getToken(ExprParser.SEMI, i)

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
            self.state = 23
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 20
                    self.match(ExprParser.NL) 
                self.state = 25
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6708789760) != 0):
                self.state = 26
                localctx.statements = self.stat()
                self.state = 27
                _la = self._input.LA(1)
                if not(((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & 1073742337) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 34
                self.match(ExprParser.NL)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(ExprParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.basicId()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(ExprParser.WORD, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_word

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWord" ):
                listener.enterWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWord" ):
                listener.exitWord(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWord" ):
                return visitor.visitWord(self)
            else:
                return visitor.visitChildren(self)




    def word(self):

        localctx = ExprParser.WordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_word)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(ExprParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WordsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_words

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WordListContext(WordsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.WordsContext
            super().__init__(parser)
            self.first = None # WordContext
            self.rest = None # WordContext
            self.copyFrom(ctx)

        def word(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.WordContext)
            else:
                return self.getTypedRuleContext(ExprParser.WordContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWordList" ):
                listener.enterWordList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWordList" ):
                listener.exitWordList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWordList" ):
                return visitor.visitWordList(self)
            else:
                return visitor.visitChildren(self)



    def words(self):

        localctx = ExprParser.WordsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_words)
        try:
            localctx = ExprParser.WordListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            localctx.first = self.word()
            self.state = 50
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 47
                    localctx.rest = self.word() 
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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

        def words(self):
            return self.getTypedRuleContext(ExprParser.WordsContext,0)


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
        self.enterRule(localctx, 8, self.RULE_basicId)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                localctx = ExprParser.RawIdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.words()
                pass
            elif token in [27]:
                localctx = ExprParser.BracketIdContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 54
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


    class CommentContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SINGLE_COMMENT(self):
            return self.getToken(ExprParser.SINGLE_COMMENT, 0)
        def MULTILINE_COMMENT(self):
            return self.getToken(ExprParser.MULTILINE_COMMENT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
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
        self.enterRule(localctx, 10, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = ExprParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                localctx.target = self.basicId()
                self.state = 58
                self.match(ExprParser.EQ)
                self.state = 59
                localctx.expression = self.expr(0)
                pass

            elif la_ == 2:
                localctx = ExprParser.StatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                localctx.expression = self.expr(0)
                pass

            elif la_ == 3:
                localctx = ExprParser.InequalityContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                localctx.lhs = self.expr(0)
                self.state = 63
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 64
                localctx.rhs = self.expr(0)
                pass

            elif la_ == 4:
                localctx = ExprParser.VersusContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 66
                localctx.lhs = self.basicId()
                self.state = 67
                self.match(ExprParser.VERSUS)
                self.state = 68
                localctx.rhs = self.basicId()
                pass

            elif la_ == 5:
                localctx = ExprParser.CommentContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 70
                self.match(ExprParser.SINGLE_COMMENT)
                pass

            elif la_ == 6:
                localctx = ExprParser.CommentContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 71
                self.match(ExprParser.MULTILINE_COMMENT)
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

        def WORD(self):
            return self.getToken(ExprParser.WORD, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(ExprParser.WORD)
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
            self.state = 76
            _la = self._input.LA(1)
            if not(_la==24 or _la==25):
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
        self.enterRule(localctx, 16, self.RULE_simpleExpr)
        self._la = 0 # Token type
        try:
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27]:
                localctx = ExprParser.IdentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.id_()
                pass
            elif token in [23]:
                localctx = ExprParser.DateContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(ExprParser.SLASH_DATE)
                pass
            elif token in [21, 22]:
                localctx = ExprParser.CurrencyValueContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                localctx.symbol = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    localctx.symbol = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 81
                localctx.amount = self.numericLiteral()
                pass
            elif token in [24, 25]:
                localctx = ExprParser.ValueContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 82
                localctx.value = self.numericLiteral()
                self.state = 84
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 83
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


    class UnitConvertContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.expression = None # ExprContext
            self.exprUnit = None # UnitContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def IN(self):
            return self.getToken(ExprParser.IN, 0)
        def THEN(self):
            return self.getToken(ExprParser.THEN, 0)
        def unit(self):
            return self.getTypedRuleContext(ExprParser.UnitContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnitConvert" ):
                listener.enterUnitConvert(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnitConvert" ):
                listener.exitUnitConvert(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnitConvert" ):
                return visitor.visitUnitConvert(self)
            else:
                return visitor.visitChildren(self)


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
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = ExprParser.SimpleContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 89
                self.simpleExpr()
                pass

            elif la_ == 2:
                localctx = ExprParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 90
                self.match(ExprParser.LPAREN)
                self.state = 91
                self.expr(0)
                self.state = 92
                self.match(ExprParser.RPAREN)
                pass

            elif la_ == 3:
                localctx = ExprParser.RangeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 94
                localctx.bottom = self.simpleExpr()
                self.state = 95
                self.match(ExprParser.TO)
                self.state = 96
                localctx.top = self.simpleExpr()
                pass

            elif la_ == 4:
                localctx = ExprParser.RangeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 98
                localctx.bottom = self.simpleExpr()
                self.state = 99
                self.match(ExprParser.DOTS)
                self.state = 100
                localctx.top = self.simpleExpr()
                pass

            elif la_ == 5:
                localctx = ExprParser.RangeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 102
                localctx.bottom = self.simpleExpr()
                self.state = 103
                self.match(ExprParser.DOTS)
                self.state = 104
                localctx.mid = self.simpleExpr()
                self.state = 105
                self.match(ExprParser.DOTS)
                self.state = 106
                localctx.top = self.simpleExpr()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 124
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 122
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.BinopContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 110
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 111
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 112
                        localctx.rhs = self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.BinopContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 113
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 114
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 115
                        localctx.rhs = self.expr(3)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.BinopContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 116
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 117
                        localctx.op = self.match(ExprParser.AND)
                        self.state = 118
                        localctx.rhs = self.expr(2)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.UnitConvertContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.expression = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 119
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 120
                        _la = self._input.LA(1)
                        if not(_la==1 or _la==3):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 121
                        localctx.exprUnit = self.unit()
                        pass

             
                self.state = 126
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
        self._predicates[9] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         




