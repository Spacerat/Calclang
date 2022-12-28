parser grammar ExprParser;
options {
	tokenVocab = ExprLexer;
}

program: statements = stat* EOF;

terminate: ';';

id: ID # rawId | BRACKET_ID # bracketId;

stat:
	target = id '=' expression = expr terminate?			# assignment
	| expression = expr terminate?							# statement
	| lhs = expr op = (GREATER_THAN | LESS_THAN) rhs = expr	# inequality;

rangeSpec: '(' (LINEAR | GAUSSIAN) ')';

unit: WEEKS | DAYS | HOURS | MINUTES;

numericLiteral: INT | FLOAT;

expr:
	id												# ident
	| value = numericLiteral valueUnit = unit?		# value
	| '(' expr ')'									# parens
	| lhs = expr op = (TIMES | DIVIDE) rhs = expr	# binop
	| bottom = expr TO top = expr rangeSpec?		# range
	| lhs = expr op = (PLUS | MINUS) rhs = expr		# binop
	| lhs = expr op = AND rhs = expr				# binop
	| lhs = expr op = THEN rhs = expr				# binop;
