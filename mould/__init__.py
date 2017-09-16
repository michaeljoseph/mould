"""Create a cookiecutter template from an existing project directory"""
import io
import json
import os

from .read import read_directory
from .transform import replace_directory_entries
from .write import write_directory

__author__ = 'Michael Joseph'
__email__ = 'michaeljoseph@gmail.com'
__url__ = 'https://github.com/michaeljoseph/mould'
__version__ = '0.0.1'

__all__ = ['read_directory', 'replace_directory_entries', 'write_directory']


def mould(source_directory, replacements, output_directory):

    write_directory(
        replace_directory_entries(
            read_directory(source_directory),
            replacements
        ),
        output_directory
    )

    cookiecutter_json = os.path.join(output_directory, 'cookiecutter.json')
    io.open(cookiecutter_json, 'wt').write(
        unicode(json.dumps({
            value: key
            for key, value in replacements.items()
        }))
    )
