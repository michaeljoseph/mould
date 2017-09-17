import json
import click

from . import mould
from . import read_directory
from . import replace_directory_entries


@click.command()
@click.argument('source', type=click.Path(exists=True))
@click.argument('destination', type=click.Path())
@click.option('--debug', default=False, help='Debug mode.')
def main(source, destination, debug):
    click.secho(
        'Reading from {} and writing to {}'.format(source, destination),
        fg='green',
    )

    source_files = read_directory(source)

    replacements = {}

    done = False
    while not done:
        try:
            pattern = click.prompt('Enter a pattern to search for')
            if pattern in ['quit', 'exit']:
                raise click.Abort

            name = click.prompt('Name it')

            replacement = {
                pattern: name
            }

            replace_directory_entries(
                source_files,
                replacement,
                preview=True
            )

            replacements.update(replacement)

        except click.Abort:
            done = True

    click.prompt(click.style(
        'Moulding with replacements {}'.format(json.dumps(replacements)),
        fg='yellow'
    ))

    mould(
        source,
        replacements,
        destination,
    )
