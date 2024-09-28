import sys
from language.parse import parse_file
from pprint import pprint


def main(path):
    pprint(parse_file(path))


if __name__ == "__main__":
    main(sys.argv[1])