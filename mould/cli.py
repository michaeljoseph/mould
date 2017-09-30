import json

import click

from . import mould
from . import read_directory
from .transform import preview


@click.command()
@click.argument('source', type=click.Path(exists=True))
@click.argument('destination', type=click.Path())
@click.option('--debug', is_flag=True, default=False, help='Debug mode.')
@click.option('--dry-run', is_flag=True, default=False, help='Dry run.')
def main(source, destination, debug, dry_run):

    click.secho(
        'Reading from {} and writing to {}'.format(source, destination),
        fg='green',
    )

    source_files = read_directory(source)

    replacements = {}

    done = False
    while not done:
        try:
            pattern = click.prompt(click.style(
                'Enter a pattern to search for '
                '(quit, or ctrl-c when done)',
                fg='green'))
            if pattern in ['quit', 'exit']:
                raise click.Abort

            click.echo(
                preview(
                    source_files,
                    {
                        pattern: '<temporary-name>'
                    },
                )
            )

            name = click.prompt(
                click.style(
                    'Give this pattern a name (or enter to discard)',
                    fg='green'
                ),
                default='',
                show_default=False
            )

            if name:
                replacements[pattern] = name

            if replacements:
                click.secho(
                    'Current replacements {}'.format(json.dumps(replacements)),
                    fg='yellow'
                )
        except click.Abort:
            done = True

    if replacements:
        click.confirm(click.style(
            'Confirm moulding {} to {}, with replacements:\n{}\n'.format(
                source,
                destination,
                json.dumps(replacements)),
            fg='yellow'
        ))

        if not dry_run:
            mould(
                source,
                replacements,
                destination,
            )
