import os

from mould import read_directory


def test_read_directory():
    expected_directories = [
        'example-project',
        'example-project/foo',
        'example-project/foo/bar',
        'example-project/foo/bar/baz',
        'example-project/proj',
    ]

    directories = [
        directory['path']
        for directory in read_directory('tests/files/example-project')
    ]
    assert sorted(expected_directories) == sorted(directories)


def test_read_directory_excludes_git():
    os.mkdir('tests/files/example-project/.git')

    expected_directories = [
        'example-project',
        'example-project/foo',
        'example-project/foo/bar',
        'example-project/foo/bar/baz',
        'example-project/proj',
    ]

    directories = [
        directory['path']
        for directory in read_directory('tests/files/example-project')
    ]
    assert sorted(expected_directories) == sorted(directories)
    os.rmdir('tests/files/example-project/.git')


def test_read_directory_files():
    expected_files = {
        'example-project': [
            'example-project/README.md',
            'example-project/file.bin'
        ],
        'example-project/foo': [],
        'example-project/foo/bar': [],
        'example-project/foo/bar/baz': [
            'example-project/foo/bar/baz/sample.txt'
        ],
        'example-project/proj': [
        ],
    }

    directory_entries = read_directory('tests/files/example-project')
    for directory in directory_entries:
        files = [f['path'] for f in directory['files']]
        assert sorted(expected_files[directory['path']]) == sorted(files)


def test_read_directory_types():
    expected_files = {
        'example-project/README.md': False,
        'example-project/file.bin': True,
        'example-project/foo/bar/baz/sample.txt': False,
    }

    directory_entries = read_directory('tests/files/example-project')

    for directory in directory_entries:
        for f in directory['files']:
            assert expected_files[f['path']] == f['binary'], f


def test_read_directory_content():
    import io
    expected_content = {
        'example-project/README.md': (
            u'# example-project\n\n'
            'This is an Example Project\n\nBy user@example.com\n'
        ),
        'example-project/file.bin': io.open(
            'tests/files/example-project/file.bin',
            mode='rb'
        ).read(),
        'example-project/foo/bar/baz/sample.txt': u'some text\n',
        'example-project/proj/.gitkeep': u'',
    }

    directory_entries = read_directory('tests/files/example-project')

    for directory in directory_entries:
        for f in directory['files']:
            assert expected_content[f['path']] == f['content'], f
