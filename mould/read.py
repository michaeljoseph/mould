import io
import os
from binaryornot import check

from .gitignore import read_ignore, remove_ignores


def read_directory(project_directory):
    directory_entries = []

    project_parent_directory = os.path.normpath(
        os.path.join(project_directory, os.pardir)
    )

    ignore_path = os.path.join(project_directory, '.gitignore')
    ignore_list = []
    if os.path.exists(ignore_path):
        ignore_list = read_ignore(read_file(ignore_path))

    for root, dirs, files in os.walk(project_directory):

        directory_path = os.path.relpath(root, project_parent_directory)

        if '.git' in directory_path:
            dirs[:] = []
            continue

        directory = {
            'path': directory_path,
            'files': [],
        }

        if ignore_list:
            files = remove_ignores(files, ignore_list)

        for file_path in files:
            if file_path.startswith('.'):
                continue

            file_path = os.path.join(root, file_path)

            content = read_file(file_path)
            is_binary = check.is_binary(file_path)

            directory['files'].append({
                'path': os.path.relpath(file_path, project_parent_directory),
                'binary': is_binary,
                'content': content,
            })

        directory_entries.append(directory)

    return directory_entries


def read_file(file_path):
    is_binary = check.is_binary(file_path)
    mode = 'r{}'.format('b' if is_binary else 't')
    return io.open(file_path, mode=mode).read()
