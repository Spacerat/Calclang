from .combinators import (
    anyOf,
    bracketed,
    floatParser,
    intParser,
    oneOrMore,
    optional,
    rawPair,
    regex,
    restOfLine,
    sequence,
    string,
    tokenTransform,
    Token,
    rawTriple,
    ws,
    wsAfter,
    newlines,
    zeroOrMore,
    oneOrMoreSeparated,
)

from .parse import parse

from .test_helpers import check_fails, check_passes


def test_string():
    parser = string("foo")
    check_passes(parser, "foo", Token.string("foo", 0))


def test_string_fail():
    parser = string("foo")
    check_fails(parser, "bar", "Expected 'foo' at 0")


def test_anyOf():
    parser = anyOf(string("foo"), string("bar"))
    check_passes(parser, "foo", Token.string("foo", 0))
    check_passes(parser, "bar", Token.string("bar", 0))


def test_anyOf_fail():
    parser = anyOf(string("foo"), string("bar"))
    check_fails(parser, "baz", "Expected any of [string('foo'), string('bar')] at 0")


def test_wsAfter():
    parser = wsAfter(string("foo"))
    check_passes(parser, "foo", Token.string("foo", 0))
    check_passes(parser, "foo ", Token.string("foo", 0))
    check_passes(parser, "foo  ", Token.string("foo", 0))


def test_triple():
    parser = rawTriple(string("foo"), string("bar"), string("baz"))
    check_passes(
        parser,
        "foobarbaz",
        (Token.string("foo", 0), Token.string("bar", 3), Token.string("baz", 6)),
    )


def test_triple_fail():
    parser = rawTriple(string("foo"), string("bar"), string("baz"))
    check_fails(parser, "foobar", "Expected 'baz' at 6")


def test_pair():
    parser = rawPair(string("foo"), string("bar"))
    check_passes(
        parser,
        "foobar",
        (Token.string("foo", 0), Token.string("bar", 3)),
    )


def test_sequence():
    parser = sequence([wsAfter(string("foo")), wsAfter(string("bar"))])
    check_passes(parser, "foo bar", [Token.string("foo", 0), Token.string("bar", 4)])


def test_zeroOrMore():
    parser = zeroOrMore(string("foo"))
    check_passes(
        parser,
        "foofoofoo",
        [
            Token.string("foo", 0),
            Token.string("foo", 3),
            Token.string("foo", 6),
        ],
    )


def test_oneOrMore():
    parser = oneOrMore(string("foo"))
    check_passes(
        parser,
        "foofoofoo",
        [
            Token.string("foo", 0),
            Token.string("foo", 3),
            Token.string("foo", 6),
        ],
    )


def test_oneOrMore_fail():
    parser = oneOrMore(string("foo"))
    check_fails(parser, "bar", "Expected 'foo' at 0")


def test_restOfLine():
    parser = sequence([string("foo"), restOfLine(), optional(string("bar"))])
    check_passes(
        parser, "foo bar", [Token.string("foo", 0), Token.string(" bar", 3), None]
    )
    check_passes(
        parser,
        "foo  \nbar",
        [Token.string("foo", 0), Token.string("  ", 3), Token.string("bar", 6)],
    )


def test_regex():
    parser = regex(r"\d+")
    check_passes(parser, "123", Token.string("123", pos=0))
    check_fails(parser, "foo", "Expected regex '\\d+' at 0")


def test_bracketed():
    parser = bracketed(string("foo"))
    check_passes(parser, "(foo)", Token.string("foo", pos=1))
    check_fails(parser, "foo", "Expected '(' at 0")
    check_fails(parser, "(foo", "Expected ')' at 4")

    check_passes(parser, "( foo )", Token.string("foo", pos=2))


def test_intParser():
    check_passes(intParser, "123", Token("123", 123, 0))
    check_fails(intParser, "foo", "Expected integer at 0")


def test_floatParser():
    check_passes(floatParser, "123.456", Token("123.456", 123.456, 0))
    check_fails(floatParser, "foo", "Expected float at 0")


def test_transform():
    parser = tokenTransform(intParser, lambda x: x * 2)
    check_passes(parser, "123", Token("123", 246, 0))


def test_ws():
    check_passes(ws, " ", Token.string(" ", 0))


def test_oneOrMoreSeparated():
    parser = oneOrMoreSeparated(string("foo"), string(","))
    check_passes(
        parser,
        "foo,foo,foo",
        [Token.string("foo", 0), Token.string("foo", 4), Token.string("foo", 8)],
    )


def test_oneOrMoreSeparated_newlines():
    parser = oneOrMoreSeparated(string("foo"), newlines)
    check_passes(
        parser,
        "foo\nfoo\nfoo",
        [Token.string("foo", 0), Token.string("foo", 4), Token.string("foo", 8)],
    )


def test_triple_doesnt_eat_newlines():
    parser = rawTriple(string("foo"), string("bar"), string("baz"))
    text = "foobarbaz\n\n\n\n"
    result = parse(parser, text)
    assert result.context.pos == 9
