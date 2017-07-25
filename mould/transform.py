def replace_directory_entries(directory_entries, replacements):
    replaced_entries = []

    for directory_entry in directory_entries:
        entry = dict(directory_entry)

        for search, replace in replacements.items():
            entry['path'] = entry['path'].replace(search, replace)

        for file_record in entry['files']:
            for search, replace in replacements.items():
                file_record['path'] = file_record['path'].replace(
                    search,
                    replace
                )

                if not file_record['binary']:
                    file_record['content'] = file_record['content'].replace(
                        search,
                        replace
                    )

        replaced_entries.append(entry)

    return replaced_entries
