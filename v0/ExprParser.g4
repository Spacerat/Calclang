parser grammar ExprParser;
options {
	tokenVocab = ExprLexer;
}

program: statements = stat* EOF;

terminate: ';';

id: basicId;

basicId: ID # rawId | BRACKET_ID # bracketId;

stat:
	target = basicId '=' expression = expr terminate?		# assignment
	| expression = expr terminate?							# statement
	| lhs = expr op = (GREATER_THAN | LESS_THAN) rhs = expr	# inequality
	// versus could also use expr in theory but starting with just basicId for easier chart titles
	| lhs = basicId VERSUS rhs = basicId # versus;

unit:
	YEARS
	| WEEKS
	| DAYS
	| HOURS
	| MINUTES
	| SECONDS
	| BUSINESS_DAYS;

numericLiteral: INT | FLOAT;

simpleExpr:
	id													# ident
	| SLASH_DATE										# date
	| symbol = (DOLLAR | POUND) amount = numericLiteral	# currencyValue
	| value = numericLiteral valueUnit = unit?			# value;

expr:
	simpleExpr															# simple
	| '(' expr ')'														# parens
	| lhs = expr op = (TIMES | DIVIDE) rhs = expr						# binop
	| bottom = simpleExpr TO top = simpleExpr							# range
	| bottom = simpleExpr DOTS top = simpleExpr							# range
	| bottom = simpleExpr DOTS mid = simpleExpr DOTS top = simpleExpr	# range
	| lhs = expr op = (PLUS | MINUS) rhs = expr							# binop
	| lhs = expr op = AND rhs = expr									# binop
	| lhs = expr op = THEN rhs = expr									# binop;
