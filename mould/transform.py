def replace_directory_entries(directory_entries, replacements):
    replaced_entries = []
    replace_keys = ['path', 'content']

    for directory_entry in directory_entries:
        entry = dict(directory_entry)

        for search, replace in replacements.items():
            entry['path'] = entry['path'].replace(search, replace)

        for file_record in entry['files']:
            for search, replace in replacements.items():
                for replace_key in replace_keys:
                    replace_candidate = file_record[replace_key]
                    if replace_candidate:
                        file_record[replace_key] = replace_candidate.replace(
                            search,
                            replace
                        )

        replaced_entries.append(entry)

    return replaced_entries
