import sys
from typing import List
from antlr4 import FileStream, CommonTokenStream
from parser.ExprLexer import ExprLexer
from parser.ExprParser import ExprParser
from language.visitor import MyVisitor
from language.calc_ast import Program, ProgramResults

from pprint import pprint


def main(argv):
    input_stream = FileStream(argv)

    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.program()
    visitor = MyVisitor()

    program: Program = visitor.visit(tree)

    results: List[ProgramResults] = []

    for _ in range(0, 100000):
        results.append(program.execute())

    values = [result.lastResult.value for result in results]
    import matplotlib.pyplot as plt

    plt.hist(values, density=True, bins="auto")
    plt.title(results[-1].statements[-1].text)
    plt.show()


if __name__ == "__main__":
    main(sys.argv[1])
