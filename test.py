import sys
from antlr4 import FileStream
from language.calc_ast import Program
from language.parse import parse


def main(argv):
    input_stream = FileStream(argv)

    program: Program = parse(input_stream)

    result = program.execute().lastResult

    title = result.text

    if isinstance(result.value, (int, float)):
        print(f"{title}: {result.value}")

    else:

        plot_result(title, result)


def plot_result(title, result):
    import seaborn as sns
    import matplotlib.pyplot as plt

    plt.subplot(2, 1, 1)
    plt.title(f"Cumulative distribution of {title}")
    sns.histplot(result.value, kde=True, stat="percent", cumulative=True)
    plt.grid()
    plt.subplot(2, 1, 2)
    plt.title(f"Distribution of {title}")
    sns.histplot(result.value, kde=True, stat="percent")
    plt.tight_layout()
    plt.show()

    # plt.hist(result.value, density=True, bins="auto")
    # plt.title(title)
    # plt.xlabel(f"value of {title}")
    # plt.ylabel("Probability density")
    # plt.show()


if __name__ == "__main__":
    main(sys.argv[1])
