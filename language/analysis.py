from .calc_ast import (
    ProgramResults,
    AssignmentResult,
    StatementResult,
    InequalityResult,
)
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


from IPython.display import display as ipdisplay, Markdown


def display(results: ProgramResults):
    result = results.last_result
    if not result:
        return

    if isinstance(result, (StatementResult, AssignmentResult)):
        display_basic_result(result)

    elif isinstance(result, InequalityResult):
        display_inequality_result(result)


def display_inequality_result(result: InequalityResult):
    lhs = result.lhs
    rhs = result.rhs
    op = result.op
    if isinstance(lhs, (int, float)) and isinstance(rhs, np.ndarray):
        lhs, rhs = rhs, lhs

    if isinstance(lhs, np.ndarray) and isinstance(rhs, np.ndarray):
        print("Inequalities between distributions not yet supported")

    elif isinstance(lhs, (int, float)) and isinstance(rhs, (int, float)):
        if op == ">":
            statement = "is" if lhs > rhs else "is not"
            print(f"{lhs} {statement} greater than {rhs}")
        if op == "<":
            statement = "is" if lhs < rhs else "is not"
            print(f"{lhs} {statement} less than {rhs}")

    elif isinstance(lhs, np.ndarray) and isinstance(rhs, (int, float)):
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

        greater = op == ">"
        name = result.name()

        split_hist(
            lhs, ax=ax1, threshold=rhs, greater=greater, cumulative=True, name=name
        )

        split_hist(
            lhs, ax=ax2, threshold=rhs, greater=greater, cumulative=False, name=name
        )

        proba = np.mean(lhs > rhs if greater else lhs < rhs)

        fig.suptitle(f"P ( {result.text} ) = {proba:.0%}")

        human_text = result.text.replace("<", "under").replace(">", "over")

        format_plots(ax1, ax2, name)

        printmd(f"**Probability of '{human_text}'**: {proba:.2%}")
        printmd(f"**Mean {name}**: {np.mean(lhs):n}")
        printmd(f"**Median {name}**: {np.median(lhs):n}")

        fig.tight_layout()
        plt.show()


def format_plots(ax1, ax2, name):
    ax1.grid()
    ax1.set_ylabel("Cumulative probability")

    ax2.set_ylabel("Probability density")
    ax2.set_yticklabels([])
    ax2.set_xlabel(name)


def display_basic_result(result: StatementResult | AssignmentResult):
    value = result.value
    title = result.name()

    if isinstance(value, (int, float)):
        print(f"{title}: {result.value}")

    elif isinstance(result.value, np.ndarray):
        if not isinstance(value, np.ndarray):
            return

        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
        fig.suptitle(title)

        sns.histplot(value, stat="percent", cumulative=True, ax=ax1)

        sns.histplot(value, stat="percent", ax=ax2)

        format_plots(ax1, ax2, result.name())

        fig.tight_layout()

        printmd(f"**Mean {result.name()}**: {np.mean(result.value):n}")
        printmd(f"**Median {result.name()}**: {np.median(result.value):n}")

        plt.show()


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
            label=f"{name} > {threshold}",
        )
    elif threshold > max(data):
        ax.hist(
            bins[:-1],
            bins,
            weights=hist,
            color=lcol,
            label=f"{name} < {threshold}",
        )
    else:
        thresh_idx = np.argmax(bins > threshold)

        ax.hist(
            bins[: thresh_idx - 1],
            bins[:thresh_idx],  # type: ignore
            weights=hist[: thresh_idx - 1],
            color=lcol,
            label=f"{name} < {threshold}",
        )

        ax.hist(
            bins[thresh_idx - 1 : -1],
            bins[thresh_idx - 1 :],  # type: ignore
            weights=hist[thresh_idx - 1 :],
            color=rcol,
            label=f"{name} > {threshold}",
        )

    ax.legend()


def printmd(md: str):
    ipdisplay(Markdown(md))
