from pprint import pprint
from language.parser import program
from combinators.parse import parse


def main():
    while True:
        text = input(">")
        result = parse(program, text)
        pprint(result.value)


if __name__ == "__main__":
    main()
