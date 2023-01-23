from .analysis import (
    ValueOutput,
    MeasureOutput,
    DistributionOutput,
    InequalityProbabilityOutput,
    ValueInequalityOutput,
    Analysis,
    Output,
)

import matplotlib.pyplot as plt
from IPython.core.display import Markdown
from IPython.display import display as ipdisplay


def display_analysis(analysis: Analysis | None):
    if analysis is None:
        return

    for output in analysis.outputs:
        display_output(output, analysis.name)


def display_output(output: Output, analysis_name: str):
    # unit = "" if unit == "dimensionless" else f"({unit})"
    match output:
        case ValueOutput(value, unit, name):
            printmd(f"**{name}**: {value} {unit}")
        case MeasureOutput(kind, value, unit):
            printmd(f"**{kind} of {analysis_name}**: {value:n} {unit}")
        case DistributionOutput(_, _, _) as output:
            display_distribution_output(output)
        case ValueInequalityOutput(lhs, rhs, op, result):
            op_name = "greater than" if op == ">" else "less than"
            result_name = "is" if result else "is not"
            printmd(
                f"**{analysis_name}**: {lhs.value:n} {lhs.unit} {result_name} {op_name} {rhs.value:n} {rhs.unit}"
            )
        case InequalityProbabilityOutput(distribution, threshold, op, probability):
            op_name = "greater than" if op == ">" else "less than"
            printmd(
                f"**Probability of {distribution.name} ({distribution.unit}) {op_name} {threshold.value:n} ({threshold.unit})**: {probability:.2%}"
            )
        case _:
            printmd(f"**{analysis_name}**: {output}")


def display_distribution_output(output: DistributionOutput):
    dists = output.dists

    _, ax = plt.subplots()
    for dist in dists:
        ax.hist(
            dist.bins[:-1],
            dist.bins,
            weights=dist.hist,
            label=dist.label,
            color=dist.color,
        )
    ax.set_title(output.title)
    ax.set_xlabel(f"{output.distribution.name} {output.distribution.unit}")
    if any(x.label is not None for x in dists):
        ax.legend()
    plt.show()


def printmd(md: str):
    ipdisplay(Markdown(md))
