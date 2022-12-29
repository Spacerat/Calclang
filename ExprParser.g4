parser grammar ExprParser;
options {
	tokenVocab = ExprLexer;
}

program: statements = stat* EOF;

terminate: ';';

id: basicId | sequenceId;

basicId: ID # rawId | BRACKET_ID # bracketId;

stat:
	target = basicId '=' expression = expr terminate?		# assignment
	| target = sequenceId '=' expression = expr terminate?	# sequenceAssignment
	| expression = expr terminate?							# statement
	| lhs = expr op = (GREATER_THAN | LESS_THAN) rhs = expr	# inequality;

rangeSpec: '(' kind = ID ')';

unit: WEEKS | DAYS | HOURS | MINUTES;

numericLiteral: INT | FLOAT;

expr:
	id												# ident
	| symbol = (DOLLAR | POUND) amount = FLOAT		# currencyValue
	| value = numericLiteral valueUnit = unit?		# value
	| '(' expr ')'									# parens
	| lhs = expr op = (TIMES | DIVIDE) rhs = expr	# binop
	| bottom = expr TO top = expr rangeSpec?		# range
	| lhs = expr op = (PLUS | MINUS) rhs = expr		# binop
	| lhs = expr op = AND rhs = expr				# binop
	| lhs = expr op = THEN rhs = expr				# binop;

/* Sequences */

/*
 e.g. account[0] = 0 ; account[day] = account[day - 1] + 1 to 100 ;
 */
sequenceId:
	name = basicId LSQPAREN args += sequenceIndex (
		COMMA args += sequenceIndex
	)* RSQPAREN;

sequenceIndex:
	seqId = ID											# sequenceIndexAtId
	| seqIdx = INT										# sequenceIndexAbsolute
	| seqId = ID op = (PLUS | MINUS) seqOffset = INT	# sequenceIndexRelative;
