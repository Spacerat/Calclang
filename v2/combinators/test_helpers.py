from typing import List, Tuple
from pprint import pprint

from .combinators import ParserContext
from .parse import parse


def check_fails(parser, string, expected_message):
    try:
        parse(parser, string)
    except Exception as e:
        assert str(e) == expected_message


def check_passes(
    parser,
    string,
    expected_result,
    *,
    expected_pos=None,
    expected_references: List[Tuple[str]] | None = None,
):
    resultValue, resultContext = parse(parser, string)
    pprint(resultValue)
    assert resultValue == expected_result
    assert resultContext == ParserContext(
        text=string,
        pos=expected_pos or len(string),
        references=expected_references or [],
    )
