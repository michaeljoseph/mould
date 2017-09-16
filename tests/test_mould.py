from mould import mould

from . import is_same


def test_mould(tmpdir):
    output_directory = tmpdir

    mould(
        'tests/files/example-project',
        {
            'example-project': 'repo_name',
        },
        str(output_directory)
    )

    assert output_directory.join('{{cookiecutter.repo_name}}').exists()

    expected_readme = (
        u'# {{cookiecutter.repo_name}}\n\n'
        'This is an Example Project\n\n'
        'By user@example.com\n'
    )

    assert (
        expected_readme ==
        output_directory.join('{{cookiecutter.repo_name}}')
        .join('README.md')
        .read_text('utf-8')
    )
