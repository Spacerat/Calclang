# Generated from CalcParser.g4 by ANTLR 4.11.1
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
        4,1,7,50,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,4,1,20,8,1,11,1,12,1,21,1,1,1,1,1,1,
        3,1,27,8,1,1,1,1,1,3,1,31,8,1,1,1,3,1,34,8,1,1,2,4,2,37,8,2,11,2,
        12,2,38,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,48,8,4,1,4,0,0,5,0,2,4,6,
        8,0,0,52,0,13,1,0,0,0,2,33,1,0,0,0,4,36,1,0,0,0,6,40,1,0,0,0,8,47,
        1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,15,1,0,0,0,13,11,1,0,0,0,
        13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,0,16,17,5,0,0,1,17,1,1,0,
        0,0,18,20,3,6,3,0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,
        1,0,0,0,22,23,1,0,0,0,23,24,5,2,0,0,24,26,3,4,2,0,25,27,5,7,0,0,
        26,25,1,0,0,0,26,27,1,0,0,0,27,34,1,0,0,0,28,30,3,4,2,0,29,31,5,
        7,0,0,30,29,1,0,0,0,30,31,1,0,0,0,31,34,1,0,0,0,32,34,5,7,0,0,33,
        19,1,0,0,0,33,28,1,0,0,0,33,32,1,0,0,0,34,3,1,0,0,0,35,37,3,8,4,
        0,36,35,1,0,0,0,37,38,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,5,1,
        0,0,0,40,41,5,5,0,0,41,7,1,0,0,0,42,48,3,6,3,0,43,44,5,3,0,0,44,
        45,3,4,2,0,45,46,5,4,0,0,46,48,1,0,0,0,47,42,1,0,0,0,47,43,1,0,0,
        0,48,9,1,0,0,0,7,13,21,26,30,33,38,47
    ]

class CalcParser ( Parser ):

    grammarFileName = "CalcParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'='", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "SINGLE_COMMENT", "EQUALS", "LPAREN", 
                      "RPAREN", "WORD", "WS", "NL" ]

    RULE_program = 0
    RULE_line = 1
    RULE_expr = 2
    RULE_word = 3
    RULE_element = 4

    ruleNames =  [ "program", "line", "expr", "word", "element" ]

    EOF = Token.EOF
    SINGLE_COMMENT=1
    EQUALS=2
    LPAREN=3
    RPAREN=4
    WORD=5
    WS=6
    NL=7

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
            self.lines = None # LineContext

        def EOF(self):
            return self.getToken(CalcParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.LineContext)
            else:
                return self.getTypedRuleContext(CalcParser.LineContext,i)


        def getRuleIndex(self):
            return CalcParser.RULE_program

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

        localctx = CalcParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 168) != 0:
                self.state = 10
                localctx.lines = self.line()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(CalcParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcParser.RULE_line

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignmentContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.LineContext
            super().__init__(parser)
            self._word = None # WordContext
            self.target = list() # of WordContexts
            self.expression = None # ExprContext
            self.copyFrom(ctx)

        def EQUALS(self):
            return self.getToken(CalcParser.EQUALS, 0)
        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)

        def NL(self):
            return self.getToken(CalcParser.NL, 0)
        def word(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.WordContext)
            else:
                return self.getTypedRuleContext(CalcParser.WordContext,i)


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


    class StatementContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.LineContext
            super().__init__(parser)
            self.expression = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)

        def NL(self):
            return self.getToken(CalcParser.NL, 0)

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


    class EmptyContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NL(self):
            return self.getToken(CalcParser.NL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmpty" ):
                listener.enterEmpty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmpty" ):
                listener.exitEmpty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmpty" ):
                return visitor.visitEmpty(self)
            else:
                return visitor.visitChildren(self)



    def line(self):

        localctx = CalcParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = CalcParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 18
                    localctx._word = self.word()
                    localctx.target.append(localctx._word)
                    self.state = 21 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==5):
                        break

                self.state = 23
                self.match(CalcParser.EQUALS)
                self.state = 24
                localctx.expression = self.expr()
                self.state = 26
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 25
                    self.match(CalcParser.NL)


                pass

            elif la_ == 2:
                localctx = CalcParser.StatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                localctx.expression = self.expr()
                self.state = 30
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 29
                    self.match(CalcParser.NL)


                pass

            elif la_ == 3:
                localctx = CalcParser.EmptyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.match(CalcParser.NL)
                pass


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
            self._element = None # ElementContext
            self.items = list() # of ElementContexts

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.ElementContext)
            else:
                return self.getTypedRuleContext(CalcParser.ElementContext,i)


        def getRuleIndex(self):
            return CalcParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = CalcParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 35
                    localctx._element = self.element()
                    localctx.items.append(localctx._element)

                else:
                    raise NoViableAltException(self)
                self.state = 38 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
            return self.getToken(CalcParser.WORD, 0)

        def getRuleIndex(self):
            return CalcParser.RULE_word

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

        localctx = CalcParser.WordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_word)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(CalcParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcParser.RULE_element

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParensContext(ElementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ElementContext
            super().__init__(parser)
            self.expression = None # ExprContext
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(CalcParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(CalcParser.RPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


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


    class WordElementContext(ElementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ElementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def word(self):
            return self.getTypedRuleContext(CalcParser.WordContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWordElement" ):
                listener.enterWordElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWordElement" ):
                listener.exitWordElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWordElement" ):
                return visitor.visitWordElement(self)
            else:
                return visitor.visitChildren(self)



    def element(self):

        localctx = CalcParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_element)
        try:
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = CalcParser.WordElementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.word()
                pass
            elif token in [3]:
                localctx = CalcParser.ParensContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(CalcParser.LPAREN)
                self.state = 44
                localctx.expression = self.expr()
                self.state = 45
                self.match(CalcParser.RPAREN)
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





