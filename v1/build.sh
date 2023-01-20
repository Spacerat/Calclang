#! /usr/bin/env bash

antlr4 -Dlanguage=Python3 CalcParser.g4 CalcLexer.g4 -visitor -o parser
