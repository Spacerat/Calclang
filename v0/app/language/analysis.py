from .calc_ast import (
    AssignmentResult,
    StatementResult,
    InequalityResult,
    AnyResult,
    Operator,
)
import numpy as np
from typing import List, Literal, Union, cast
from .pint_stubs import Quantity
from pydantic.dataclasses import dataclass
from pydantic import BaseModel


number = Union[float, int]


@dataclass(frozen=True)
class ValueOutput:
    value: int | float
    unit: str
    name: str | None = None
    typename: Literal["value"] = "value"


@dataclass(frozen=True)
class VarOutput:
    name: str
    unit: str
    typename: Literal["var"] = "var"


@dataclass(frozen=True)
class ValueInequalityOutput:
    lhs: ValueOutput
    rhs: ValueOutput
    op: Operator
    result: bool
    typename: Literal["inequality"] = "inequality"


@dataclass(frozen=True)
class MeasureOutput:
    kind: Literal["median", "mean", "minimum", "maximum"]
    value: int | float
    unit: str
    name: str
    typename: Literal["measure"] = "measure"


@dataclass(frozen=True)
class InequalityProbabilityOutput:
    distribution: VarOutput
    threshold: ValueOutput
    op: Operator
    probability: float
    typename: Literal["inequality_probability"] = "inequality_probability"


@dataclass(frozen=True)
class DistributionElement:
    hist: List[float]
    bins: List[float]
    label: str | None = None
    # TODO: replace label with name/unit
    color: str | None = None


@dataclass(frozen=True)
class DistributionOutput:
    title: str
    distribution: VarOutput
    dists: List[DistributionElement]
    typename: Literal["distribution"] = "distribution"


@dataclass
class Percentile:
    percentile: float
    value: float


@dataclass(frozen=True)
class PercentilesOutput:
    distribution: VarOutput
    unit: str
    percentiles: List[Percentile]
    typename: Literal["percentiles"] = "percentiles"


Output = (
    ValueOutput
    | MeasureOutput
    | DistributionOutput
    | ValueInequalityOutput
    | InequalityProbabilityOutput
    | PercentilesOutput
)

OutputValue = Union[int, float, np.ndarray]


class Analysis(BaseModel):
    name: str
    outputs: List[Output]


@dataclass(frozen=True)
class Analyses:
    outputs: List[Analysis]


def invert_inequality(op: Operator) -> Operator:
    # NOTE: this would ideally support >= and <= but
    # we don't support them for now
    match op:
        case "<":
            return ">"
        case ">":
            return "<"


def analyse_result(result: AnyResult | None) -> Analysis | None:
    # XXX: we can't do this right until we get units right!
    match result:
        case StatementResult(_, value) | AssignmentResult(_, _, value):
            if value is None:
                return None

            if isinstance(value.m, (float, int)):
                return Analysis(
                    name=result.name(),
                    outputs=[
                        ValueOutput(
                            name=result.name(), value=value.m, unit=str(value.u)
                        )
                    ],
                )

            if isinstance(value.m, np.ndarray):
                return Analysis(
                    name=result.name(),
                    outputs=make_distribution_analysis(value, result.name()),
                )

        case InequalityResult(text, lhs, rhs, op) as result:
            if lhs is None or rhs is None:
                return
            lhs_name = result.lhs_name()
            rhs_name = result.rhs_name()

            if isinstance(lhs.m, (int, float)) and isinstance(rhs.m, np.ndarray):
                lhs, rhs = rhs, lhs
                lhs_name, rhs_name = rhs_name, lhs_name
                op = invert_inequality(op)

            if isinstance(lhs.m, np.ndarray) and isinstance(rhs.m, np.ndarray):
                print("Inequalities between distributions not yet supported")

            if isinstance(lhs.m, (int, float)) and isinstance(rhs.m, (int, float)):
                return Analysis(
                    name=text,
                    outputs=[
                        make_inequality_values_analysis(
                            lhs, lhs_name, rhs, rhs_name, op
                        ),
                    ],
                )

            if isinstance(lhs.m, np.ndarray) and isinstance(rhs.m, (int, float)):
                return Analysis(
                    name=lhs_name,
                    outputs=make_inequality_analysis(lhs, lhs_name, rhs, rhs_name, op),
                )


def make_inequality_analysis(
    data: Quantity[np.ndarray],
    data_name: str,
    threshold: Quantity[number],
    threshold_name: str,
    op: Operator,
) -> List[Output]:
    return (
        [
            make_inequality_probability_analysis(
                data, data_name, threshold, threshold_name, op
            )
        ]
        + make_measure_analyses(data, data_name)
        + [make_percentiles_analysis(data, data_name)]
        + [make_inequality_distribution_analysis(data, data_name, threshold, op)]
    )


def make_inequality_probability_analysis(
    data: Quantity[np.ndarray],
    data_name: str,
    threshold: Quantity[number],
    threshold_name: str,
    op: Operator,
) -> InequalityProbabilityOutput:
    threshold_unit = str(data.u) if threshold.unitless else str(threshold.u)

    if op == "<":
        return InequalityProbabilityOutput(
            distribution=VarOutput(name=data_name, unit=str(data.u)),
            threshold=ValueOutput(
                value=threshold.m, unit=threshold_unit, name=threshold_name
            ),
            op=op,
            probability=np.mean(data.m < threshold.m, dtype=float),
        )
    if op == ">":
        return InequalityProbabilityOutput(
            distribution=VarOutput(name=data_name, unit=str(data.u)),
            threshold=ValueOutput(
                value=threshold.m, unit=threshold_unit, name=threshold_name
            ),
            op=op,
            probability=np.mean(data.m > threshold.m, dtype=float),
        )


def fmt_unit(unit: str) -> str:
    # TODO: remove when we send unit/name separately instead
    if unit == "dimensionless":
        return ""
    return f" {unit}"


def make_inequality_distribution_analysis(
    data: Quantity[np.ndarray],
    data_name: str,
    threshold: Quantity[number],
    op: Operator,
):
    threshold_unit = str(data.u) if threshold.unitless else str(threshold.u)
    threhsold_name = f"{threshold.m:n}{fmt_unit(threshold_unit)}"

    distribution = VarOutput(name=data_name, unit=str(data.u))
    hist, bins = np.histogram(data.m, bins="auto", density=True)
    hist = cumulative(hist)

    lcol, rcol = "salmon", "chartreuse"
    if op == "<":
        lcol, rcol = rcol, lcol

    if threshold < min(data.m):
        return DistributionOutput(
            title="Cumulative distribution",
            distribution=distribution,
            dists=[
                DistributionElement(
                    hist=hist.tolist(),
                    bins=bins.tolist(),
                    label=f"{data_name} > {threhsold_name}",
                    color=rcol,
                ),
            ],
        )

    if threshold > max(data.m):
        return DistributionOutput(
            title="Cumulative distribution",
            distribution=distribution,
            dists=[
                DistributionElement(
                    hist=hist.tolist(),
                    bins=bins.tolist(),
                    label=f"{data_name} < {threhsold_name}",
                    color=lcol,
                )
            ],
        )

    thresh_idx = np.argmax(bins > threshold)

    return DistributionOutput(
        title="Cumulative distribution",
        distribution=distribution,
        dists=[
            DistributionElement(
                hist=hist[: thresh_idx - 1].tolist(),
                bins=bins[:thresh_idx].tolist(),
                label=f"{data_name} < {threhsold_name}",
                color=lcol,
            ),
            DistributionElement(
                hist=hist[thresh_idx - 1 :].tolist(),
                bins=bins[thresh_idx - 1 :].tolist(),
                label=f"{data_name} > {threhsold_name}",
                color=rcol,
            ),
        ],
    )


def make_inequality_values_analysis(
    lhs: Quantity[number],
    lhs_name: str,
    rhs: Quantity[number],
    rhs_name: str,
    op: Operator,
) -> ValueInequalityOutput:

    result = lhs < rhs if op == "<" else lhs > rhs

    return ValueInequalityOutput(
        lhs=ValueOutput(value=lhs.m, unit=str(lhs.u), name=lhs_name),
        rhs=ValueOutput(value=rhs.m, unit=str(rhs.u), name=rhs_name),
        op=op,
        result=result,
    )


def cumulative(hist: np.ndarray):
    hist = np.cumsum(hist)
    hist = 100 * hist / max(hist)
    return hist


def make_distribution_analysis(
    value: Quantity[np.ndarray], value_name: str
) -> List[Output]:
    unit = str(value.u)
    hist, bins = np.histogram(value.m, bins="auto", density=True)
    hist = cumulative(hist)

    return (
        make_measure_analyses(value, value_name)
        + [make_percentiles_analysis(value, value_name)]
        + [
            DistributionOutput(
                title="Cumulative distribution",
                distribution=VarOutput(name=value_name, unit=unit),
                dists=[DistributionElement(hist=hist.tolist(), bins=bins.tolist())],
            )
        ]
    )


def make_percentiles_analysis(value: Quantity[np.ndarray], value_name: str) -> Output:
    unit = str(value.u)
    percentile_locations = [5, 10, 25, 50, 75, 90, 95]
    percentiles = np.percentile(value.m, percentile_locations)
    return PercentilesOutput(
        distribution=VarOutput(name=value_name, unit=unit),
        unit=unit,
        percentiles=[
            Percentile(percentile=percentile, value=value)
            for percentile, value in zip(percentile_locations, percentiles)
        ],
    )


def make_measure_analyses(value: Quantity[np.ndarray], value_name: str) -> List[Output]:
    mean = cast(Quantity[float], np.mean(value))
    minimum = cast(Quantity[float], np.min(value))
    maximum = cast(Quantity[float], np.max(value))

    return [
        MeasureOutput(
            kind="minimum", value=minimum.m, name=value_name, unit=str(mean.u)
        ),
        MeasureOutput(kind="mean", value=mean.m, name=value_name, unit=str(mean.u)),
        MeasureOutput(
            kind="maximum", value=maximum.m, name=value_name, unit=str(mean.u)
        ),
    ]
