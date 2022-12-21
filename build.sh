#! /usr/bin/env bash

antlr4 -Dlanguage=Python3 ExprParser.g4 ExprLexer.g4 -visitor -o parser
