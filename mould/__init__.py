"""Create a cookiecutter template from an existing project directory"""
from .read import read_directory
from .transform import replace_directory_entries

__author__ = 'Michael Joseph'
__email__ = 'michaeljoseph@gmail.com'
__url__ = 'https://github.com/michaeljoseph/mould'
__version__ = '0.0.1'

__all__ = [read_directory, replace_directory_entries]
