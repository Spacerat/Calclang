from .parser import literal, expression, program
from .ast import Literal, BinOp, Variable, Program, Assignment, Statement
from combinators.test_helpers import check_passes, check_fails
from combinators.token import Token, TaggedToken
from combinators.parse import parse
from pprint import pprint


def test_literal():
    check_passes(literal, "1.5", Literal(Token.float(1.5, pos=0), None))

    check_passes(
        literal, "1.5 days", Literal(Token.float(1.5, pos=0), Token.string("days", 4))
    )


def test_expresion():
    check_passes(
        expression,
        "10 * 12.6 + 15 * 19",
        BinOp(
            left=BinOp(
                left=Literal(value=Token.int(10, pos=0), unit=None),
                op=Token.string("*", pos=3),
                right=Literal(value=Token(text="12.6", value=12.6, pos=5), unit=None),
            ),
            op=Token(text="+", value="+", pos=10),
            right=BinOp(
                left=Literal(value=Token.int(15, pos=12), unit=None),
                op=Token.string("*", pos=15),
                right=Literal(value=Token.int(19, pos=17), unit=None),
            ),
        ),
    )


def test_expression_with_units():
    check_passes(
        expression,
        "10 days + 3 hours",
        BinOp(
            left=Literal(value=Token.int(10, pos=0), unit=Token.string("days", 3)),
            op=Token(text="+", value="+", pos=8),
            right=Literal(value=Token.int(3, pos=10), unit=Token.string("hours", 12)),
        ),
    )


def test_expression_with_variable():
    check_passes(
        expression,
        "foo bar + baz",
        BinOp(
            Variable(Token.string("foo bar", 0)),
            Token.string("+", 8),
            Variable(Token.string("baz", 10)),
        ),
    )


def test_range():
    check_passes(
        expression,
        "9 + 10 to 20 * 2",
        BinOp(
            left=Literal(value=Token.int(9, pos=0), unit=None),
            op=Token(text="+", value="+", pos=2),
            right=BinOp(
                left=BinOp(
                    left=Literal(value=Token.int(10, pos=4), unit=None),
                    op=Token.string("to", pos=7),
                    right=Literal(value=Token.int(20, pos=10), unit=None),
                ),
                op=Token.string("*", pos=13),
                right=Literal(value=Token.int(2, pos=15), unit=None),
            ),
        ),
    )


def test_consecutive_ops_fail():
    check_fails(expression, "10 + + 20", "Expected expression at 6")


def test_expression_doesnt_eat_newlines():
    text = "1 + 2\n\n\n"
    result = parse(expression, text)
    assert result.context.pos == 5


def test_program():
    check_passes(
        program,
        "foo = 10\nbar = 20\nfoo + bar",
        Program(
            assignments=[
                Assignment(
                    left=Variable(name=Token(text="foo", value="foo", pos=0)),
                    equals=Token(text="=", value="=", pos=4),
                    right=Literal(value=Token(text="10", value=10, pos=6), unit=None),
                ),
                Assignment(
                    left=Variable(name=Token(text="bar", value="bar", pos=9)),
                    equals=Token(text="=", value="=", pos=13),
                    right=Literal(value=Token(text="20", value=20, pos=15), unit=None),
                ),
                Statement(
                    term=BinOp(
                        left=Variable(name=Token(text="foo", value="foo", pos=18)),
                        op=Token(text="+", value="+", pos=22),
                        right=Variable(name=Token(text="bar", value="bar", pos=24)),
                    )
                ),
            ]
        ),
    )


def test_program_tokens():
    text = "foo = 10\nbar = 20\nfoo + bar"
    result = parse(program, text)

    assert result.value.tokens() == [
        TaggedToken(text="foo", value="foo", pos=0, tag="variable"),
        TaggedToken(text="=", value="=", pos=4, tag="equals"),
        TaggedToken(text="10", value=10, pos=6, tag="literal_value"),
        TaggedToken(text="bar", value="bar", pos=9, tag="variable"),
        TaggedToken(text="=", value="=", pos=13, tag="equals"),
        TaggedToken(text="20", value=20, pos=15, tag="literal_value"),
        TaggedToken(text="foo", value="foo", pos=18, tag="variable"),
        TaggedToken(text="+", value="+", pos=22, tag="operator"),
        TaggedToken(text="bar", value="bar", pos=24, tag="variable"),
    ]
