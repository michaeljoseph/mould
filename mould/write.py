import io
import os

import click


def write_directory(directory_entries, target_directory):
    """
    :param directory_entries: DirectoryEntry instances
    :param target_directory: The directory to write the mould to
    :return:
    """

    if not os.path.exists(target_directory):
        os.mkdir(target_directory)
        click.secho(
            'Creating {} directory'.format(target_directory),
            fg='green'
        )
    else:
        # TODO: handle existing git target directory
        click.secho(
            '{} already exists, overwriting contents'.format(target_directory),
            fg='red'
        )

    for directory_entry in directory_entries:
        dir_to_create = os.path.join(target_directory, directory_entry['path'])
        click.secho(
            'creating {}'.format(dir_to_create),
            fg='blue'
        )

        if not os.path.exists(dir_to_create):
            os.mkdir(dir_to_create)

        for file_entry in directory_entry['files']:
            file_to_create = os.path.join(target_directory, file_entry['path'])
            click.secho(
                'writing {}'.format(file_to_create),
                fg='blue'
            )

            mode = 'w{}'.format('b' if file_entry['binary'] else 't')
            with io.open(file_to_create, mode=mode) as fh:
                fh.write(file_entry['content'])
