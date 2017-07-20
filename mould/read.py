import io
import os
from binaryornot import check


def read_directory(project_directory):
    directory_entries = []
    exclude_directories = ['.git']

    project_parent_directory = os.path.normpath(
        os.path.join(project_directory, os.pardir)
    )

    for root, dirs, files in os.walk(project_directory):

        directory = {
            'path': os.path.relpath(root, project_parent_directory),
            'files': [],
        }

        for exclude_dir in exclude_directories:
            if exclude_dir in dirs:
                dirs.remove(exclude_dir)

        for file_path in files:
            file_path = os.path.join(root, file_path)

            is_binary, content = _read_file(file_path)

            directory['files'].append({
                'path': os.path.relpath(file_path, project_parent_directory),
                'binary': is_binary,
                'content': content,
            })

        directory_entries.append(directory)

    return directory_entries


def _read_file(file_path):
    is_binary = check.is_binary(file_path)

    mode = 'r{}'.format('b' if is_binary else 't')

    return is_binary, io.open(file_path, mode=mode).read()
