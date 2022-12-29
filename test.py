import sys
from language.parse import parse_file
from language.analysis import display
from pprint import pprint


def main(path):
    # display(parse_file(path).execute())
    pprint(parse_file(path))


if __name__ == "__main__":
    main(sys.argv[1])
