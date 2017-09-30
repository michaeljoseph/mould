from click.testing import CliRunner
from mould.cli import main


def test_cli(tmpdir):
    runner = CliRunner()
    result = runner.invoke(
        main,
        ['tests/files/example-project', str(tmpdir)],
        input=u'\n'
    )

    assert result.exit_code == 0

    expected_output = [
        'Reading from tests/files/example-project '
        'and writing to {}'.format(str(tmpdir)),

        'Enter a pattern to search for '
        '(enter when done): \n'
    ]

    assert '\n'.join(expected_output) == result.output
    assert not tmpdir.join('example-project').exists()


def test_cli_makes_one_replacement(tmpdir):
    pattern = 'user@example.com'
    name = 'email'

    result = CliRunner().invoke(
        main,
        ['tests/files/example-project', str(tmpdir)],
        input=u'{}\n{}\n\ny\n'.format(pattern, name),
    )

    assert result.exit_code == 0

    assert tmpdir.join('example-project/foo/bar/baz').exists()
