from .parse import parse_string
from .analysis import display
from .calc_ast import ExecContext
from .errors import ProgramNameError


def run(data: str, context: ExecContext | None = None):
    try:
        result = parse_string(data).execute(context)
    except ProgramNameError as name:
        print(f"'{name}' is not defined")
        return context
    else:
        display(result)
        return result.context
