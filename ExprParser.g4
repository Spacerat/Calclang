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
	| lhs = expr op = (GREATER_THAN | LESS_THAN) rhs = expr	# inequality
	// versus could also use expr in theory but starting with just basicId for easier chart titles
	| lhs = basicId VERSUS rhs = basicId # versus;

unit: YEARS | WEEKS | DAYS | HOURS | MINUTES | SECONDS;

numericLiteral: INT | FLOAT;

simpleExpr:
	id													# ident
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

/* Sequences */

/*
 e.g. account[0] = 0 ; account[day] = account[day - 1] + 1 to 100 ;
 
 not sure if we'll actually keep this feature
 */
sequenceId:
	name = basicId LSQPAREN args += sequenceIndex (
		COMMA args += sequenceIndex
	)* RSQPAREN;

sequenceIndex:
	seqId = ID											# sequenceIndexAtId
	| seqIdx = INT										# sequenceIndexAbsolute
	| seqId = ID op = (PLUS | MINUS) seqOffset = INT	# sequenceIndexRelative;
