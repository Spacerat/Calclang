lexer grammar ExprLexer;

IN: 'in';
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
VERSUS: '~';

DOLLAR: '$';
POUND: '£';

SLASH_DATE:
	(([0-2][0-9]) | ('3' [0-1])) '/' ('0' [0-9] | '11' '12') '/' [0-9][0-9] (
		[0-9][0-9]
	)?;

INT: (MINUS? [1-9][0-9]* | '0');
FLOAT: INT [.] INT;

WORD: [a-zA-Z_][a-zA-Z_0-9]*;

BRACKET_ID: '\'' (~['])* '\'';

DOTS: '..';

NL: [\r\n]+;
// SPACE: ' '+;
WS_SKIP: [ \t\r\n\f]+ -> channel(HIDDEN);

// TODO: can we do comments normally?

SINGLE_COMMENT: '#' (~('\r' | '\n'))*; // -> channel(HIDDEN);
MULTILINE_COMMENT: '/*' .*? '*/'; // -> channel(HIDDEN);
