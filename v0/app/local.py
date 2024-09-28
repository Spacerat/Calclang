import sys
from lib.language.analysis import DistributionOutput, analyse_result
from lib.language.parse import parse_file
from pprint import pprint
import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument('path', type=click.Path(exists=True))
def analyse(path):
    if last_result := parse_file(path).execute().last_result:
        if analysis := analyse_result(last_result):
            print(f"Analysis for {analysis.name}\n")
            for output in analysis.outputs:
                if not isinstance(output, DistributionOutput):
                    pprint(output)

@cli.command()
@click.argument('path', type=click.Path(exists=True))
def parse(path):
    if parsed := parse_file(path):
        pprint(parsed)

if __name__ == '__main__':
    cli()