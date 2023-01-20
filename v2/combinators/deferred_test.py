from .deferred import (
    addReference,
    deferred,
    deferredContext,
    DeferredEvaluation,
    reference,
    Reference,
)
from .token import Token
from .combinators import string, oneOrMore, sequence, restOfLine, anyOf, ws
from .test_helpers import check_passes


def test_deferred():
    parser = deferredContext(deferred(string("foo"), string("foo")))
    check_passes(
        parser,
        "foo",
        DeferredEvaluation(
            pos=0, parser=string("foo"), result=Token.string("foo", pos=0)
        ),
    )


def test_lazyAssignmentAndReference():
    word = oneOrMore(anyOf(string("bar"), string("foo")))
    assignment = sequence(
        [
            addReference(word),
            string("="),
            deferred(restOfLine(), anyOf(string("10"), reference())),
        ],
        separator=ws,
    )

    parser = deferredContext(oneOrMore(assignment))

    check_passes(
        parser,
        "foo = bar\nbar = 10\n",
        [
            [
                [Token.string("foo", pos=0)],
                Token.string("=", pos=4),
                DeferredEvaluation(
                    pos=6,
                    parser=anyOf(string("10"), reference()),
                    result=Reference(name=("bar",)),
                ),
            ],
            [
                [Token.string("bar", pos=10)],
                Token.string("=", pos=14),
                DeferredEvaluation(
                    pos=16,
                    parser=anyOf(string("10"), reference()),
                    result=Token.string("10", pos=16),
                ),
            ],
        ],
        expected_references=[("bar",), ("foo",)],
    )


def test_assignmentAndReference():
    parser = sequence(
        [string("foo"), addReference(sequence([string("bar")])), reference()],
        separator=ws,
    )

    check_passes(
        parser,
        "foo bar bar",
        [
            Token.string("foo", pos=0),
            [Token.string("bar", pos=4)],
            Reference(name=("bar",)),
        ],
        expected_references=[("bar",)],
    )
