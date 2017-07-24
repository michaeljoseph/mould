from mould import replace_directory_entries


def test_replace_directory_entries():
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

    expected_entries = [
        {
            'files': [
                {
                    'content': b'\x03\xf3',
                    'binary': True,
                    'path': '{{cookiecutter.repo_name}}/file.bin',
                },
                {
                    'content': (
                        u'# {{cookiecutter.repo_name}}\n\n'
                        'This is an Example Project\n\n'
                        'By user@example.com\n'
                    ),
                    'binary': False,
                    'path': '{{cookiecutter.repo_name}}/README.md',
                }
            ],
            'path': '{{cookiecutter.repo_name}}',
        },
        {
            'files': [],
            'path': '{{cookiecutter.repo_name}}/foo',
        },
        {
            'files': [],
            'path': '{{cookiecutter.repo_name}}/foo/bar',
        },
        {
            'files': [
                {
                    'content': u'some text\n',
                    'binary': False,
                    'path': (
                        '{{cookiecutter.repo_name}}/'
                        'foo/bar/baz/sample.txt'
                    ),
                }
            ],
            'path': '{{cookiecutter.repo_name}}/foo/bar/baz',
        },
        {
            'files': [],
            'path': '{{cookiecutter.repo_name}}/proj',
        }
    ]

    replacements = {
        'example-project': '{{cookiecutter.repo_name}}',
    }

    assert (
        expected_entries ==
        replace_directory_entries(directory_entries, replacements)
    )
