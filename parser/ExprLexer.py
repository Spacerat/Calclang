# Generated from ExprLexer.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,28,213,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,1,0,1,0,1,0,1,0,5,0,62,8,0,10,0,12,0,65,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,5,1,73,8,1,10,1,12,1,76,9,1,1,1,1,1,1,1,1,
        1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,93,8,3,1,4,1,4,
        1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,
        11,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,18,1,18,1,18,1,18,1,18,3,18,144,8,18,1,19,1,19,1,19,1,19,1,
        19,1,19,3,19,152,8,19,1,20,1,20,1,20,1,20,1,20,1,20,3,20,160,8,20,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,170,8,21,1,22,1,22,
        5,22,174,8,22,10,22,12,22,177,9,22,1,22,3,22,180,8,22,1,23,1,23,
        1,23,1,23,1,24,1,24,5,24,188,8,24,10,24,12,24,191,9,24,1,25,1,25,
        5,25,195,8,25,10,25,12,25,198,9,25,1,25,1,25,1,26,4,26,203,8,26,
        11,26,12,26,204,1,26,1,26,1,27,4,27,210,8,27,11,27,12,27,211,1,74,
        0,28,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,
        13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,
        24,49,25,51,26,53,27,55,28,1,0,8,2,0,10,10,13,13,1,0,49,57,1,0,48,
        57,1,0,46,46,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,
        1,0,39,39,3,0,9,10,12,13,32,32,225,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,
        0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,
        0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,
        0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,
        0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,
        0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,
        0,0,1,57,1,0,0,0,3,68,1,0,0,0,5,82,1,0,0,0,7,92,1,0,0,0,9,94,1,0,
        0,0,11,97,1,0,0,0,13,101,1,0,0,0,15,103,1,0,0,0,17,105,1,0,0,0,19,
        107,1,0,0,0,21,109,1,0,0,0,23,111,1,0,0,0,25,114,1,0,0,0,27,116,
        1,0,0,0,29,118,1,0,0,0,31,120,1,0,0,0,33,122,1,0,0,0,35,129,1,0,
        0,0,37,138,1,0,0,0,39,145,1,0,0,0,41,153,1,0,0,0,43,161,1,0,0,0,
        45,179,1,0,0,0,47,181,1,0,0,0,49,185,1,0,0,0,51,192,1,0,0,0,53,202,
        1,0,0,0,55,209,1,0,0,0,57,58,5,47,0,0,58,59,5,47,0,0,59,63,1,0,0,
        0,60,62,8,0,0,0,61,60,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,
        1,0,0,0,64,66,1,0,0,0,65,63,1,0,0,0,66,67,6,0,0,0,67,2,1,0,0,0,68,
        69,5,47,0,0,69,70,5,42,0,0,70,74,1,0,0,0,71,73,9,0,0,0,72,71,1,0,
        0,0,73,76,1,0,0,0,74,75,1,0,0,0,74,72,1,0,0,0,75,77,1,0,0,0,76,74,
        1,0,0,0,77,78,5,42,0,0,78,79,5,47,0,0,79,80,1,0,0,0,80,81,6,1,0,
        0,81,4,1,0,0,0,82,83,5,97,0,0,83,84,5,110,0,0,84,85,5,100,0,0,85,
        6,1,0,0,0,86,87,5,116,0,0,87,88,5,104,0,0,88,89,5,101,0,0,89,93,
        5,110,0,0,90,91,5,45,0,0,91,93,5,62,0,0,92,86,1,0,0,0,92,90,1,0,
        0,0,93,8,1,0,0,0,94,95,5,111,0,0,95,96,5,114,0,0,96,10,1,0,0,0,97,
        98,5,110,0,0,98,99,5,111,0,0,99,100,5,116,0,0,100,12,1,0,0,0,101,
        102,5,61,0,0,102,14,1,0,0,0,103,104,5,44,0,0,104,16,1,0,0,0,105,
        106,5,59,0,0,106,18,1,0,0,0,107,108,5,40,0,0,108,20,1,0,0,0,109,
        110,5,41,0,0,110,22,1,0,0,0,111,112,5,116,0,0,112,113,5,111,0,0,
        113,24,1,0,0,0,114,115,5,43,0,0,115,26,1,0,0,0,116,117,5,45,0,0,
        117,28,1,0,0,0,118,119,5,42,0,0,119,30,1,0,0,0,120,121,5,47,0,0,
        121,32,1,0,0,0,122,123,5,108,0,0,123,124,5,105,0,0,124,125,5,110,
        0,0,125,126,5,101,0,0,126,127,5,97,0,0,127,128,5,114,0,0,128,34,
        1,0,0,0,129,130,5,103,0,0,130,131,5,97,0,0,131,132,5,117,0,0,132,
        133,5,115,0,0,133,134,5,115,0,0,134,135,5,105,0,0,135,136,5,97,0,
        0,136,137,5,110,0,0,137,36,1,0,0,0,138,139,5,100,0,0,139,140,5,97,
        0,0,140,141,5,121,0,0,141,143,1,0,0,0,142,144,5,115,0,0,143,142,
        1,0,0,0,143,144,1,0,0,0,144,38,1,0,0,0,145,146,5,119,0,0,146,147,
        5,101,0,0,147,148,5,101,0,0,148,149,5,107,0,0,149,151,1,0,0,0,150,
        152,5,115,0,0,151,150,1,0,0,0,151,152,1,0,0,0,152,40,1,0,0,0,153,
        154,5,104,0,0,154,155,5,111,0,0,155,156,5,117,0,0,156,157,5,114,
        0,0,157,159,1,0,0,0,158,160,5,115,0,0,159,158,1,0,0,0,159,160,1,
        0,0,0,160,42,1,0,0,0,161,162,5,109,0,0,162,163,5,105,0,0,163,164,
        5,110,0,0,164,165,5,117,0,0,165,166,5,116,0,0,166,167,5,101,0,0,
        167,169,1,0,0,0,168,170,5,115,0,0,169,168,1,0,0,0,169,170,1,0,0,
        0,170,44,1,0,0,0,171,175,7,1,0,0,172,174,7,2,0,0,173,172,1,0,0,0,
        174,177,1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,180,1,0,0,0,
        177,175,1,0,0,0,178,180,5,48,0,0,179,171,1,0,0,0,179,178,1,0,0,0,
        180,46,1,0,0,0,181,182,3,45,22,0,182,183,7,3,0,0,183,184,3,45,22,
        0,184,48,1,0,0,0,185,189,7,4,0,0,186,188,7,5,0,0,187,186,1,0,0,0,
        188,191,1,0,0,0,189,187,1,0,0,0,189,190,1,0,0,0,190,50,1,0,0,0,191,
        189,1,0,0,0,192,196,5,39,0,0,193,195,8,6,0,0,194,193,1,0,0,0,195,
        198,1,0,0,0,196,194,1,0,0,0,196,197,1,0,0,0,197,199,1,0,0,0,198,
        196,1,0,0,0,199,200,5,39,0,0,200,52,1,0,0,0,201,203,7,7,0,0,202,
        201,1,0,0,0,203,204,1,0,0,0,204,202,1,0,0,0,204,205,1,0,0,0,205,
        206,1,0,0,0,206,207,6,26,0,0,207,54,1,0,0,0,208,210,7,0,0,0,209,
        208,1,0,0,0,210,211,1,0,0,0,211,209,1,0,0,0,211,212,1,0,0,0,212,
        56,1,0,0,0,14,0,63,74,92,143,151,159,169,175,179,189,196,204,211,
        1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SINGLE_COMMENT = 1
    MULTILINE_COMMENT = 2
    AND = 3
    THEN = 4
    OR = 5
    NOT = 6
    EQ = 7
    COMMA = 8
    SEMI = 9
    LPAREN = 10
    RPAREN = 11
    TO = 12
    PLUS = 13
    MINUS = 14
    TIMES = 15
    DIVIDE = 16
    LINEAR = 17
    GAUSSIAN = 18
    DAYS = 19
    WEEKS = 20
    HOURS = 21
    MINUTES = 22
    INT = 23
    FLOAT = 24
    ID = 25
    BRACKET_ID = 26
    WS = 27
    NL = 28

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'and'", "'or'", "'not'", "'='", "','", "';'", "'('", "')'", 
            "'to'", "'+'", "'-'", "'*'", "'/'", "'linear'", "'gaussian'" ]

    symbolicNames = [ "<INVALID>",
            "SINGLE_COMMENT", "MULTILINE_COMMENT", "AND", "THEN", "OR", 
            "NOT", "EQ", "COMMA", "SEMI", "LPAREN", "RPAREN", "TO", "PLUS", 
            "MINUS", "TIMES", "DIVIDE", "LINEAR", "GAUSSIAN", "DAYS", "WEEKS", 
            "HOURS", "MINUTES", "INT", "FLOAT", "ID", "BRACKET_ID", "WS", 
            "NL" ]

    ruleNames = [ "SINGLE_COMMENT", "MULTILINE_COMMENT", "AND", "THEN", 
                  "OR", "NOT", "EQ", "COMMA", "SEMI", "LPAREN", "RPAREN", 
                  "TO", "PLUS", "MINUS", "TIMES", "DIVIDE", "LINEAR", "GAUSSIAN", 
                  "DAYS", "WEEKS", "HOURS", "MINUTES", "INT", "FLOAT", "ID", 
                  "BRACKET_ID", "WS", "NL" ]

    grammarFileName = "ExprLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


