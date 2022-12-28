from .parse import parse_string
from .analysis import display
from .calc_ast import ExecContext


def run(data: str, context: ExecContext | None = None):
    result = parse_string(data).execute(context)
    display(result)
    return result.context
