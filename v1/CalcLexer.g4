lexer grammar CalcLexer;

SINGLE_COMMENT: '//' ~('\r' | '\n')* -> skip;

EQUALS: '=';
LPAREN: '(';
RPAREN: ')';

WORD: ~[ \r\n\t\f()]+;

WS: [ \t\f]+ -> skip;
NL: [\r\n]+;