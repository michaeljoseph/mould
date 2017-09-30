from mould.gitignore import remove_ignores


def test_python_extension_glob_is_ignored():
    paths = [
        'write.py',
        'write.pyc',
    ]
    ignore_list = [
        '*.py[cod]'
    ]
    assert ['write.py'] == remove_ignores(paths, ignore_list)
