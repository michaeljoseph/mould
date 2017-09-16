import difflib

import click


def replace_directory_entries(directory_entries, replacements, preview=False):
    replaced_entries = []

    for directory_entry in directory_entries:
        entry = dict(directory_entry)

        for search, replace in replacements.items():
            replace = '{{cookiecutter.' + replace + '}}'
            entry['path'] = entry['path'].replace(search, replace)

            for file_record in entry['files']:
                old_path = file_record['path']
                file_record['path'] = file_record['path'].replace(
                    search,
                    replace
                )

                if not file_record['binary']:
                    before = file_record['content']
                    file_record['content'] = file_record['content'].replace(
                        search,
                        replace
                    )
                    if preview:
                        click.echo_via_pager('\n'.join(
                            difflib.unified_diff(
                                before.splitlines(),
                                file_record['content'].splitlines(),
                                fromfile=old_path,
                                tofile=file_record['path'],
                                lineterm='',
                            )
                        ))

        replaced_entries.append(entry)

    return replaced_entries
