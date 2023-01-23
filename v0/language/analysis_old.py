from .calc_ast import (
    ProgramResults,
    AssignmentResult,
    StatementResult,
    InequalityResult,
    VersusResult,
)
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import babel.numbers

from IPython.display import display as ipdisplay, Markdown


def display(results: ProgramResults):
    result = results.last_result
    if not result:
        return

    if isinstance(result, (StatementResult, AssignmentResult)):
        display_basic_result(result)

    elif isinstance(result, InequalityResult):
        display_inequality_result(result)

    elif isinstance(result, VersusResult):
        display_versus_result(result)


def display_inequality_result(result: InequalityResult):
    lhs = result.lhs
    rhs = result.rhs
    op = result.op
    if isinstance(lhs.m, (int, float)) and isinstance(rhs.m, np.ndarray):
        lhs, rhs = rhs, lhs

    if isinstance(lhs.m, np.ndarray) and isinstance(rhs.m, np.ndarray):
        print("Inequalities between distributions not yet supported")

    elif isinstance(lhs.m, (int, float)) and isinstance(rhs.m, (int, float)):
        if op == ">":
            statement = "is" if lhs > rhs else "is not"
            print(f"{lhs} {statement} greater than {rhs}")
        if op == "<":
            statement = "is" if lhs < rhs else "is not"
            print(f"{lhs} {statement} less than {rhs}")

    elif isinstance(lhs.m, np.ndarray) and isinstance(rhs.m, (int, float)):
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

        greater = op == ">"
        name = result.name()

        split_hist(
            lhs.m, ax=ax1, threshold=rhs, greater=greater, cumulative=True, name=name
        )

        split_hist(
            lhs.m, ax=ax2, threshold=rhs, greater=greater, cumulative=False, name=name
        )

        proba = np.mean(lhs.m > rhs if greater else lhs.m < rhs)

        fig.suptitle(f"P ( {result.text} ) = {proba:.0%}")

        human_text = result.text.replace("<", "under").replace(">", "over")

        format_plots(ax1, ax2, name, lhs.u)

        printmd(f"**Probability of '{human_text}'**: {proba:.2%}")
        printmd(f"**Mean {name}**: {fmt_value(np.mean(lhs))}")
        printmd(f"**Median {name}**: {fmt_value(np.median(lhs))}")

        fig.tight_layout()
        plt.show()


def display_versus_result(result: VersusResult):
    lhs = result.lhs
    rhs = result.rhs

    if isinstance(lhs.m, (int, float)) or isinstance(rhs.m, (int, float)):
        print("Comparison to single numbers not supported")

    g = sns.jointplot(y=lhs.m, x=rhs.m, kind="hex")
    g.plot_joint(sns.regplot, scatter=False, color="red")
    left_name, right_name = result.text.split(" vs ")
    plt.xlabel(label(right_name, rhs.u))
    plt.ylabel(label(left_name, lhs.u))


def format_plots(ax1, ax2, name, unit=None):
    ax1.grid()
    ax1.set_ylabel("Cumulative probability")

    ax2.set_ylabel("Probability density")
    ax2.set_yticklabels([])

    ax2.set_xlabel(label(name, unit))


def label(name, unit=None):
    if unit and str(unit) != "dimensionless":
        return f"{name} ({unit})"
    else:
        return name


def display_basic_result(result: StatementResult | AssignmentResult):
    value = result.value
    title = result.name()

    if isinstance(value.m, (int, float)):
        print(f"{title}: {result.value}")

    elif isinstance(value.m, np.ndarray):

        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
        fig.suptitle(title)

        sns.histplot(value.m, stat="percent", cumulative=True, ax=ax1)

        sns.histplot(value.m, stat="percent", ax=ax2)

        format_plots(ax1, ax2, result.name(), value.u)

        fig.tight_layout()

        printmd(f"**Mean {result.name()}**: {fmt_value(np.mean(value))}")
        printmd(f"**Median {result.name()}**: {fmt_value(np.median(value))}")

        plt.show()
    else:
        print(f"Unknown type {value.m.__class__}")


def fmt_value(value):
    if value.dimensionless:
        return f"{value.m:n}"

    if value.u in ("USD", "GBP"):
        return babel.numbers.format_currency(value.m, str(value.u), locale="EN_US")

    return f"{value:n}"


def split_hist(data, *, ax, threshold, greater, cumulative, name):

    hist, bins = np.histogram(data, bins="auto", density=True)

    if cumulative:
        hist = np.cumsum(hist)
        hist = 100 * hist / max(hist)

    lcol, rcol = "salmon", "chartreuse"
    if not greater:
        lcol, rcol = rcol, lcol

    if threshold < min(data):
        ax.hist(
            bins[:-1],
            bins,
            weights=hist,
            color=rcol,
            label=f"{name} > {threshold.m}",
        )
    elif threshold > max(data):
        ax.hist(
            bins[:-1],
            bins,
            weights=hist,
            color=lcol,
            label=f"{name} < {threshold.m}",
        )
    else:
        thresh_idx = np.argmax(bins > threshold)

        ax.hist(
            bins[: thresh_idx - 1],
            bins[:thresh_idx],  # type: ignore
            weights=hist[: thresh_idx - 1],
            color=lcol,
            label=f"{name} < {threshold.m}",
        )

        ax.hist(
            bins[thresh_idx - 1 : -1],
            bins[thresh_idx - 1 :],  # type: ignore
            weights=hist[thresh_idx - 1 :],
            color=rcol,
            label=f"{name} > {threshold.m}",
        )

    ax.legend()


def printmd(md: str):
    ipdisplay(Markdown(md))
