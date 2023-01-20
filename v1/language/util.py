from antlr4 import CommonTokenStream, InputStream, FileStream
from parser.CalcLexer import CalcLexer
from parser.CalcParser import CalcParser
from .lexer.visitor import Visitor


def parse(input_stream: InputStream):
    lexer = CalcLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CalcParser(stream)

    tree = parser.program()
    visitor = Visitor()
    return visitor.visit(tree)  # type: ignore


def parse_string(data: str):
    return parse(InputStream(data))


def parse_file(path: str):
    return parse(FileStream(path))
