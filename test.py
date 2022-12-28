import sys
from language.parse import parse_file
from language.analysis import display


def main(path):
    display(parse_file(path).execute())


if __name__ == "__main__":
    main(sys.argv[1])
