# Generated from ExprLexer.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,32,212,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,79,8,2,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,
        1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,16,
        1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,
        1,22,1,22,3,22,127,8,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        3,22,137,8,22,1,22,1,22,1,22,1,22,1,22,3,22,144,8,22,1,23,3,23,147,
        8,23,1,23,1,23,5,23,151,8,23,10,23,12,23,154,9,23,1,23,3,23,157,
        8,23,1,24,1,24,1,24,1,24,1,25,1,25,5,25,165,8,25,10,25,12,25,168,
        9,25,1,26,1,26,5,26,172,8,26,10,26,12,26,175,9,26,1,26,1,26,1,27,
        1,27,1,27,1,28,4,28,183,8,28,11,28,12,28,184,1,29,4,29,188,8,29,
        11,29,12,29,189,1,29,1,29,1,30,1,30,5,30,196,8,30,10,30,12,30,199,
        9,30,1,31,1,31,1,31,1,31,5,31,205,8,31,10,31,12,31,208,9,31,1,31,
        1,31,1,31,1,206,0,32,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,
        10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,
        21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,
        32,1,0,11,1,0,48,50,1,0,48,57,1,0,48,49,1,0,49,57,2,0,44,44,48,57,
        1,0,46,46,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,1,
        0,39,39,2,0,10,10,13,13,3,0,9,10,12,13,32,32,224,0,1,1,0,0,0,0,3,
        1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,
        0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,
        0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,
        0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,
        0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,
        0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,
        0,0,0,1,65,1,0,0,0,3,68,1,0,0,0,5,78,1,0,0,0,7,80,1,0,0,0,9,83,1,
        0,0,0,11,87,1,0,0,0,13,89,1,0,0,0,15,91,1,0,0,0,17,93,1,0,0,0,19,
        95,1,0,0,0,21,97,1,0,0,0,23,100,1,0,0,0,25,102,1,0,0,0,27,104,1,
        0,0,0,29,106,1,0,0,0,31,108,1,0,0,0,33,110,1,0,0,0,35,112,1,0,0,
        0,37,114,1,0,0,0,39,116,1,0,0,0,41,118,1,0,0,0,43,120,1,0,0,0,45,
        126,1,0,0,0,47,156,1,0,0,0,49,158,1,0,0,0,51,162,1,0,0,0,53,169,
        1,0,0,0,55,178,1,0,0,0,57,182,1,0,0,0,59,187,1,0,0,0,61,193,1,0,
        0,0,63,200,1,0,0,0,65,66,5,105,0,0,66,67,5,110,0,0,67,2,1,0,0,0,
        68,69,5,97,0,0,69,70,5,110,0,0,70,71,5,100,0,0,71,4,1,0,0,0,72,73,
        5,116,0,0,73,74,5,104,0,0,74,75,5,101,0,0,75,79,5,110,0,0,76,77,
        5,45,0,0,77,79,5,62,0,0,78,72,1,0,0,0,78,76,1,0,0,0,79,6,1,0,0,0,
        80,81,5,111,0,0,81,82,5,114,0,0,82,8,1,0,0,0,83,84,5,110,0,0,84,
        85,5,111,0,0,85,86,5,116,0,0,86,10,1,0,0,0,87,88,5,61,0,0,88,12,
        1,0,0,0,89,90,5,44,0,0,90,14,1,0,0,0,91,92,5,59,0,0,92,16,1,0,0,
        0,93,94,5,40,0,0,94,18,1,0,0,0,95,96,5,41,0,0,96,20,1,0,0,0,97,98,
        5,116,0,0,98,99,5,111,0,0,99,22,1,0,0,0,100,101,5,43,0,0,101,24,
        1,0,0,0,102,103,5,45,0,0,103,26,1,0,0,0,104,105,5,42,0,0,105,28,
        1,0,0,0,106,107,5,47,0,0,107,30,1,0,0,0,108,109,5,62,0,0,109,32,
        1,0,0,0,110,111,5,60,0,0,111,34,1,0,0,0,112,113,5,91,0,0,113,36,
        1,0,0,0,114,115,5,93,0,0,115,38,1,0,0,0,116,117,5,126,0,0,117,40,
        1,0,0,0,118,119,5,36,0,0,119,42,1,0,0,0,120,121,5,163,0,0,121,44,
        1,0,0,0,122,123,7,0,0,0,123,127,7,1,0,0,124,125,5,51,0,0,125,127,
        7,2,0,0,126,122,1,0,0,0,126,124,1,0,0,0,127,128,1,0,0,0,128,136,
        5,47,0,0,129,130,5,48,0,0,130,137,7,1,0,0,131,132,5,49,0,0,132,133,
        5,49,0,0,133,134,1,0,0,0,134,135,5,49,0,0,135,137,5,50,0,0,136,129,
        1,0,0,0,136,131,1,0,0,0,137,138,1,0,0,0,138,139,5,47,0,0,139,140,
        7,1,0,0,140,143,7,1,0,0,141,142,7,1,0,0,142,144,7,1,0,0,143,141,
        1,0,0,0,143,144,1,0,0,0,144,46,1,0,0,0,145,147,3,25,12,0,146,145,
        1,0,0,0,146,147,1,0,0,0,147,148,1,0,0,0,148,152,7,3,0,0,149,151,
        7,4,0,0,150,149,1,0,0,0,151,154,1,0,0,0,152,150,1,0,0,0,152,153,
        1,0,0,0,153,157,1,0,0,0,154,152,1,0,0,0,155,157,5,48,0,0,156,146,
        1,0,0,0,156,155,1,0,0,0,157,48,1,0,0,0,158,159,3,47,23,0,159,160,
        7,5,0,0,160,161,3,47,23,0,161,50,1,0,0,0,162,166,7,6,0,0,163,165,
        7,7,0,0,164,163,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,167,
        1,0,0,0,167,52,1,0,0,0,168,166,1,0,0,0,169,173,5,39,0,0,170,172,
        8,8,0,0,171,170,1,0,0,0,172,175,1,0,0,0,173,171,1,0,0,0,173,174,
        1,0,0,0,174,176,1,0,0,0,175,173,1,0,0,0,176,177,5,39,0,0,177,54,
        1,0,0,0,178,179,5,46,0,0,179,180,5,46,0,0,180,56,1,0,0,0,181,183,
        7,9,0,0,182,181,1,0,0,0,183,184,1,0,0,0,184,182,1,0,0,0,184,185,
        1,0,0,0,185,58,1,0,0,0,186,188,7,10,0,0,187,186,1,0,0,0,188,189,
        1,0,0,0,189,187,1,0,0,0,189,190,1,0,0,0,190,191,1,0,0,0,191,192,
        6,29,0,0,192,60,1,0,0,0,193,197,5,35,0,0,194,196,8,9,0,0,195,194,
        1,0,0,0,196,199,1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,62,1,
        0,0,0,199,197,1,0,0,0,200,201,5,47,0,0,201,202,5,42,0,0,202,206,
        1,0,0,0,203,205,9,0,0,0,204,203,1,0,0,0,205,208,1,0,0,0,206,207,
        1,0,0,0,206,204,1,0,0,0,207,209,1,0,0,0,208,206,1,0,0,0,209,210,
        5,42,0,0,210,211,5,47,0,0,211,64,1,0,0,0,15,0,78,126,136,143,146,
        150,152,156,166,173,184,189,197,206,1,0,1,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IN = 1
    AND = 2
    THEN = 3
    OR = 4
    NOT = 5
    EQ = 6
    COMMA = 7
    SEMI = 8
    LPAREN = 9
    RPAREN = 10
    TO = 11
    PLUS = 12
    MINUS = 13
    TIMES = 14
    DIVIDE = 15
    GREATER_THAN = 16
    LESS_THAN = 17
    LSQPAREN = 18
    RSQPAREN = 19
    VERSUS = 20
    DOLLAR = 21
    POUND = 22
    SLASH_DATE = 23
    INT = 24
    FLOAT = 25
    WORD = 26
    BRACKET_ID = 27
    DOTS = 28
    NL = 29
    WS_SKIP = 30
    SINGLE_COMMENT = 31
    MULTILINE_COMMENT = 32

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'in'", "'and'", "'or'", "'not'", "'='", "','", "';'", "'('", 
            "')'", "'to'", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'['", 
            "']'", "'~'", "'$'", "'\\u00A3'", "'..'" ]

    symbolicNames = [ "<INVALID>",
            "IN", "AND", "THEN", "OR", "NOT", "EQ", "COMMA", "SEMI", "LPAREN", 
            "RPAREN", "TO", "PLUS", "MINUS", "TIMES", "DIVIDE", "GREATER_THAN", 
            "LESS_THAN", "LSQPAREN", "RSQPAREN", "VERSUS", "DOLLAR", "POUND", 
            "SLASH_DATE", "INT", "FLOAT", "WORD", "BRACKET_ID", "DOTS", 
            "NL", "WS_SKIP", "SINGLE_COMMENT", "MULTILINE_COMMENT" ]

    ruleNames = [ "IN", "AND", "THEN", "OR", "NOT", "EQ", "COMMA", "SEMI", 
                  "LPAREN", "RPAREN", "TO", "PLUS", "MINUS", "TIMES", "DIVIDE", 
                  "GREATER_THAN", "LESS_THAN", "LSQPAREN", "RSQPAREN", "VERSUS", 
                  "DOLLAR", "POUND", "SLASH_DATE", "INT", "FLOAT", "WORD", 
                  "BRACKET_ID", "DOTS", "NL", "WS_SKIP", "SINGLE_COMMENT", 
                  "MULTILINE_COMMENT" ]

    grammarFileName = "ExprLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


