from .calc_ast import StatementResult
import numpy as np

from .analysis import (
    analyse_result,
    Analysis,
    ValueOutput,
    MeasureOutput,
    DistributionOutput,
)
from .units import units
from pprint import pprint


def test_analyse_result_statement():
    result = StatementResult("x", 1 * units.dimensionless)
    assert analyse_result(result) == Analysis("x", "dimensionless", [ValueOutput(1)])


def test_analyse_result_distribution():
    result = StatementResult("x", np.array([1, 2, 3]) * units.dimensionless)

    analysis = analyse_result(result)

    assert analysis is not None
    assert analysis.name == "x"
    assert analysis.unit == "dimensionless"
    assert len(analysis.outputs) == 3
    assert analysis.outputs[0] == MeasureOutput("mean", 2)
    assert analysis.outputs[1] == MeasureOutput("median", 2)
    assert isinstance(analysis.outputs[2], DistributionOutput)
