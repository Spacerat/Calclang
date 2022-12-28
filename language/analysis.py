from .calc_ast import ProgramResults, AnyResult
import seaborn as sns
import matplotlib.pyplot as plt


def display(results: ProgramResults):
    result = results.last_result
    if not result:
        return

    if isinstance(result.value, (int, float)):
        title = result.name()
        print(f"{title}: {result.value}")
    else:
        plot_result(result)


def plot_result(result: AnyResult):
    title = result.name()

    plt.subplot(2, 1, 1)
    plt.title(f"Cumulative distribution of {title}")
    sns.histplot(result.value, kde=True, stat="percent", cumulative=True)
    plt.grid()
    plt.subplot(2, 1, 2)
    plt.title(f"Distribution of {title}")
    sns.histplot(result.value, kde=True, stat="percent")
    plt.tight_layout()
    plt.show()
