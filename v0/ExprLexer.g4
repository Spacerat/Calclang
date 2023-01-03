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
GREATER_THAN: '>';
LESS_THAN: '<';
LSQPAREN: '[';
RSQPAREN: ']';
VERSUS: 'vs';

DOLLAR: '$';
POUND: '£';

DAYS: 'day' 's'?;
BUSINESS_DAYS: 'business ' DAYS;
WEEKS: 'week' 's'?;
HOURS: 'hour' 's'?;
MINUTES: 'minute' 's'?;
SECONDS: 'second' 's'?;
YEARS: 'year' 's'?;

SLASH_DATE:
	(([0-2][0-9]) | ('3' [0-1])) '/' ('0' [0-9] | '11' '12') '/' [0-9][0-9] (
		[0-9][0-9]
	)?;

INT: (MINUS? [1-9][0-9]* | '0');
FLOAT: INT [.] INT;
ID: [a-zA-Z_][a-zA-Z_0-9]*;
BRACKET_ID: '\'' (~['])* '\'';

DOTS: '..';

WS: [ \t\r\n\f]+ -> skip;
NL: [\r\n]+;