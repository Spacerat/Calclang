from .calc_ast import ProgramResults, AnyResult
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def display(results: ProgramResults):
    result = results.last_result
    if not result:
        return

    if isinstance(result.value, (int, float)):
        title = result.name()
        print(f"{title}: {result.value}")
    elif isinstance(result.value, np.ndarray):
        plot_result(result)


def plot_result(result: AnyResult):
    title = result.name()
    value = result.value
    if not isinstance(value, np.ndarray):
        return

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    fig.suptitle(title)

    ax1.set_title("Cumulative distribution")
    sns.histplot(value, kde=True, stat="percent", cumulative=True, ax=ax1)
    ax1.grid()

    ax2.set_title(f"Distribution")
    sns.histplot(value, kde=True, stat="percent", ax=ax2)

    fig.tight_layout()
    plt.show()

    print(f"Average (mean): {np.mean(value):n}")
    print(f"Average (median): {np.median(value):n}")
