parser grammar CalcParser;

options {
	tokenVocab = CalcLexer;
}

program: lines = line* EOF;

line:
	target += word+ EQUALS expression = expr NL?	# assignment
	| expression = expr NL?							# statement
	| NL											# empty;

expr: items += element+;

word: WORD;

element:
	word						# wordElement
	| '(' expression = expr ')'	# parens;

// blah blah (boo boo (foo) roo) snoo

