from language.util import parse_string
from pprint import pprint
from language.lexer.lexer import lex

result = parse_string(
    """
a to b = 10

blah = 3 + a to b     + c to d 

c = 2
d = 6
"""
)

for result in lex(result):
    pprint(result)
