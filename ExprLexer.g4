lexer grammar ExprLexer;

SINGLE_COMMENT: '//' ~('\r' | '\n')* -> skip;
MULTILINE_COMMENT: '/*' .*? '*/' -> skip;

AND: 'and';
THEN: 'then' | '->';
OR: 'or';
NOT: 'not';
EQ: '=';
COMMA: ',';
SEMI: ';';
LPAREN: '(';
RPAREN: ')';
TO: 'to';
PLUS: '+';
MINUS: '-';
TIMES: '*';
DIVIDE: '/';

LINEAR: 'linear';
GAUSSIAN: 'gaussian';

DAYS: 'day' 's'?;
WEEKS: 'week' 's'?;
HOURS: 'hour' 's'?;
MINUTES: 'minute' 's'?;

INT: [1-9][0-9]*;
FLOAT: INT [.] INT;
ID: [a-zA-Z_][a-zA-Z_0-9]*;
BRACKET_ID: '\'' (~['])* '\'';

WS: [ \t\r\n\f]+ -> skip;
NL: [\r\n]+;