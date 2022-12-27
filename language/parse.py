from antlr4 import CommonTokenStream, InputStream
from parser.ExprLexer import ExprLexer
from parser.ExprParser import ExprParser
from language.CalcAstVisitor import CalcAstVisitor


def parse(input_stream: InputStream):
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)

    tree = parser.program()
    visitor = CalcAstVisitor()
    return visitor.visit(tree)
