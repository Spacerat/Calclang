from .parse import parse_string
from .analysis_old import display
from .analysis import analyse_result, Analysis
from .calc_ast import ExecContext
from .display import display_analysis


import json


def run(data: str, context: ExecContext | None = None, debug: bool = False):
    result = parse_string(data).execute(context)

    analysis = analyse_result(result.last_result)
    display_analysis(analysis)

    if debug and analysis:
        print(json.dumps(json.loads(analysis.json()), indent=4))

    return result.context
