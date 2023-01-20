# Generated from CalcLexer.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,49,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,0,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,2,1,2,1,3,1,3,1,4,4,4,34,8,4,11,4,12,4,35,1,5,4,5,39,8,5,11,
        5,12,5,40,1,5,1,5,1,6,4,6,46,8,6,11,6,12,6,47,0,0,7,1,1,3,2,5,3,
        7,4,9,5,11,6,13,7,1,0,3,2,0,10,10,13,13,4,0,9,10,12,13,32,32,40,
        41,3,0,9,9,12,12,32,32,52,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,
        7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,1,15,1,0,0,0,3,26,
        1,0,0,0,5,28,1,0,0,0,7,30,1,0,0,0,9,33,1,0,0,0,11,38,1,0,0,0,13,
        45,1,0,0,0,15,16,5,47,0,0,16,17,5,47,0,0,17,21,1,0,0,0,18,20,8,0,
        0,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,24,
        1,0,0,0,23,21,1,0,0,0,24,25,6,0,0,0,25,2,1,0,0,0,26,27,5,61,0,0,
        27,4,1,0,0,0,28,29,5,40,0,0,29,6,1,0,0,0,30,31,5,41,0,0,31,8,1,0,
        0,0,32,34,8,1,0,0,33,32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,
        1,0,0,0,36,10,1,0,0,0,37,39,7,2,0,0,38,37,1,0,0,0,39,40,1,0,0,0,
        40,38,1,0,0,0,40,41,1,0,0,0,41,42,1,0,0,0,42,43,6,5,0,0,43,12,1,
        0,0,0,44,46,7,0,0,0,45,44,1,0,0,0,46,47,1,0,0,0,47,45,1,0,0,0,47,
        48,1,0,0,0,48,14,1,0,0,0,5,0,21,35,40,47,1,6,0,0
    ]

class CalcLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SINGLE_COMMENT = 1
    EQUALS = 2
    LPAREN = 3
    RPAREN = 4
    WORD = 5
    WS = 6
    NL = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "SINGLE_COMMENT", "EQUALS", "LPAREN", "RPAREN", "WORD", "WS", 
            "NL" ]

    ruleNames = [ "SINGLE_COMMENT", "EQUALS", "LPAREN", "RPAREN", "WORD", 
                  "WS", "NL" ]

    grammarFileName = "CalcLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


