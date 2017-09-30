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


def test_baked_mould(tmpdir, cookies):
    """Project to template; generated template == project"""
    output_directory = tmpdir

    mould(
        'tests/files/example-project',
        {
            'example-project': 'repo_name',
        },
        str(output_directory)
    )

    result = cookies.bake(
        template=str(output_directory),
        extra_context={'repo_name': 'example-project'}
    )

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'example-project'
    assert result.project.isdir()

    assert is_same('tests/files/example-project', str(result.project))


def test_bake_custom_project(tmpdir, cookies):
    """Generate project; mould generated result"""
    template = tmpdir.ensure('cookiecutter-template', dir=True)
    template.join('cookiecutter.json').write(
        '{"repo_name": "example-project"}'
    )

    repo_dir = template.ensure('{{cookiecutter.repo_name}}', dir=True)
    repo_dir.join('README.rst').write('{{cookiecutter.repo_name}}')

    result = cookies.bake(
        template=str(template),
    )

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'example-project'
    assert result.project.isdir()

    output_directory = tmpdir.ensure(
        'moulded-cookiecutter-template',
        dir=True
    )
    mould(
        str(result.project),
        {
            'example-project': 'repo_name',
        },
        str(output_directory)
    )

    assert is_same(
        str(output_directory),
        str(template)
    )
