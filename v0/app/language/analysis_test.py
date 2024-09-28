from .calc_ast import StatementResult
import numpy as np

from .analysis import (
    analyse_result,
    Analysis,
    ValueOutput,
    MeasureOutput,
    PercentilesOutput,
    DistributionOutput
)
from .units import units
from pprint import pprint


def test_analyse_result_statement():
    result = StatementResult("x", 1 * units.dimensionless)
    expected_output = ValueOutput(1, "dimensionless", "x", "value")
    expected = Analysis(name="x", outputs=[expected_output])
    assert analyse_result(result) == expected


def test_analyse_result_distribution():
    result = StatementResult("x", np.array([1, 2, 3]) * units.dimensionless)

    analysis = analyse_result(result)

    assert analysis is not None
    assert analysis.name == "x"
    # assert analysis.unit == "dimensionless"
    assert len(analysis.outputs) == 5
    assert analysis.outputs[0] == MeasureOutput("minimum", 1, "dimensionless", "x", "measure")
    assert analysis.outputs[1] == MeasureOutput("mean", 2, "dimensionless", "x", "measure")
    assert analysis.outputs[2] == MeasureOutput("maximum", 3, "dimensionless", "x", "measure")
    assert isinstance(analysis.outputs[3], PercentilesOutput)
    assert isinstance(analysis.outputs[4], DistributionOutput)

