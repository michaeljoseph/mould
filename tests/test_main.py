import subprocess
import sys


def test_should_invoke_main(monkeypatch, tmpdir):
    monkeypatch.setenv('PYTHONPATH', '.')

    response = subprocess.check_output([
        sys.executable,
        '-m',
        'mould',
        'tests/files/example-project',
        str(tmpdir)
    ], input=b'exit\n')

    decoded_response = response.decode('utf-8')
    expected_output = [
        'Reading from tests/files/example-project '
        'and writing to {}'.format(str(tmpdir)),

        'Enter a pattern to search for '
        '(quit, or ctrl-c when done): '
    ]

    assert '\n'.join(expected_output) == decoded_response
