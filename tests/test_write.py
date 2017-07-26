from mould import write_directory


def test_write(tmpdir):
    directory_entries = [
        {
            'files': [
                {
                    'content': b'\x03\xf3',
                    'binary': True,
                    'path': 'example-project/file.bin',
                },
                {
                    'content': (
                        u'# example-project\n\n'
                        'This is an Example Project\n\nBy user@example.com\n'
                    ),
                    'binary': False,
                    'path': 'example-project/README.md',
                }
            ],
            'path': 'example-project',
        },
        {
            'files': [],
            'path': 'example-project/foo',
        },
        {
            'files': [],
            'path': 'example-project/foo/bar',
        },
        {
            'files': [
                {
                    'content': u'some text\n',
                    'binary': False,
                    'path': 'example-project/foo/bar/baz/sample.txt',
                }
            ],
            'path': 'example-project/foo/bar/baz',
        },
        {
            'files': [],
            'path': 'example-project/proj',
        }
    ]

    write_directory(directory_entries, str(tmpdir))

    assert tmpdir.join('example-project').exists()

    bin_file = tmpdir.join('example-project').join('file.bin')
    assert bin_file.exists()
    assert (
        bin_file.read_binary() ==
        directory_entries[0]['files'][0]['content']
    )

    readme = tmpdir.join('example-project').join('README.md')
    assert readme.exists()
    assert (
        readme.read_text('utf-8') ==
        directory_entries[0]['files'][1]['content']
    )

    assert tmpdir.join('example-project/foo/bar').exists()
    assert tmpdir.join('example-project/foo/bar').isdir()

    assert tmpdir.join('example-project/foo/bar/baz').exists()
    assert tmpdir.join('example-project/foo/bar/baz').isdir()
    assert tmpdir.join('example-project/foo/bar/baz/sample.txt').isfile()
