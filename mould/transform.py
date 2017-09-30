import difflib


def replace_directory_entries(directory_entries, replacements):
    """
    Perform `replacements` substitutions on `DirectoryEntry` instances.

    Also mention the cookiecutter thing?
    https://docs.python.org/3.3/library/stdtypes.html#str.replace

    Specifically the path elements
    :param directory_entries:
    :param replacements: A dict where the key is the [value of the needle]
                         and the value
    :return:
    """
    replaced_entries = []

    for directory_entry in directory_entries:
        # make a copy of the current entry
        directory = dict(directory_entry)

        for search, replace in replacements.items():
            # transform the value into a cookiecutter variable
            replace = '{{cookiecutter.' + replace + '}}'

            # replace directory path names
            directory['path'] = directory['path'].replace(search, replace)

            for file_record in directory['files']:
                # transform the file path
                file_record['path'] = file_record['path'].replace(
                    search,
                    replace
                )

                # don't try to run replace on binary files
                is_text_file = not file_record['binary']
                if is_text_file:
                    # transform the file content
                    file_record['content'] = file_record['content'].replace(
                        search,
                        replace
                    )

        replaced_entries.append(directory)

    return replaced_entries


def preview(directory_entries, replacements):
    preview_content = []

    for directory_entry in directory_entries:
        # make a copy of the current entry
        directory = dict(directory_entry)

        for search, replace in replacements.items():
            # transform the value into a cookiecutter variable
            replace = '{{cookiecutter.' + replace + '}}'

            # replace directory path names
            # directory['path'] = directory['path'].replace(search, replace)

            for file_record in directory['files']:
                # save current path for diff
                old_path = file_record['path']

                # transform the file path
                new_path = old_path.replace(
                    search,
                    replace
                )

                # don't try to run replace on binary files
                is_text_file = not file_record['binary']
                if is_text_file:
                    # save current content for diff
                    old_content = file_record['content']

                    # transform the file content
                    new_content = old_content.replace(
                        search,
                        replace
                    )

                    preview_content.append('\n'.join(difflib.unified_diff(
                        old_content.splitlines(),
                        new_content.splitlines(),
                        fromfile=old_path,
                        tofile=new_path,
                        lineterm='',
                    )))

    return '\n'.join(preview_content)
