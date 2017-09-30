def read_ignore(ignore_content):
    return [
        ignore_line
        for ignore_line in ignore_content.split()
        if not ignore_line.startswith('#')
    ]


def remove_ignores(file_paths, ignore_list):
    """
    Remove files that match gitignore patterns
    :param file_paths:
    :param ignore_list:
    :return:
    """
    # https://stackoverflow.com/a/25230908/5549
    from fnmatch import fnmatch
    matches = []
    for ignore in ignore_list:
        file_paths = [
            n for n
            in file_paths
            if n.startswith('#') or not fnmatch(n, ignore)
        ]
        matches.extend(file_paths)
    return matches
