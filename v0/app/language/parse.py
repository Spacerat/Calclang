from antlr4 import CommonTokenStream, InputStream, FileStream
from ..parser.ExprLexer import ExprLexer
from ..parser.ExprParser import ExprParser
from .CalcAstVisitor import CalcAstVisitor
from .calc_ast import Program


def parse(input_stream: InputStream) -> Program:
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)

    tree = parser.program()
    visitor = CalcAstVisitor()
    return visitor.visit(tree)  # type: ignore


def parse_string(data: str):
    return parse(InputStream(data))


def parse_file(path: str):
    return parse(FileStream(path))
