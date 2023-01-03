from .calc_ast import (
    ProgramResults,
    AssignmentResult,
    StatementResult,
    InequalityResult,
    AnyResult,
)
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from typing import List

from dataclasses import dataclass


@dataclass
class ValueOutput:
    name: str
    value: int | float


Output = ValueOutput


@dataclass
class Analysis:
    outputs: List[Output]


@dataclass
class Analyses:
    outputs: List[Analysis]


def analyse_results(results: ProgramResults) -> Analyses | None:
    # For now, only return the final result

    if results.last_result is None:
        return None

    return Analyses([analyse_result(results.last_result)])


def analyse_result(result: AnyResult) -> Analysis:
    # XXX: we can't do this right until we get units right!
    match result:
        case StatementResult(_, value) | AssignmentResult(
            _, _, value
        ) as result if isinstance(value, (float, int)):
            return Analysis([ValueOutput(result.name(), value)])

    return Analysis([])
