# Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at <https://github.com/michaeljoseph/mould/issues>.

If you are reporting a bug, please include:

-   Your operating system name and version.
-   Any details about your local setup that might be helpful in
    troubleshooting.
-   Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" is
open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with
"feature" is open to whoever wants to implement it.

### Write Documentation

We could always use more documentation, whether as part of the official
mould docs, in docstrings, or even on the web in blog posts and articles.

### Submit Feedback

The best way to send feedback is to file an issue at
<https://github.com/michaeljoseph/mould/issues>.

If you are proposing a feature:

-   Explain in detail how it would work.
-   Keep the scope as narrow as possible, to make it easier to
    implement.
-   Remember that this is a volunteer-driven project, and that
    contributions are welcome :)

## Documentation

[API Documentation][(https://mould.readthedocs.io)]

## Development Setup

Install development requirements:

    pip install -r requirements.txt

Tests can then be run with:

    pytest

Lint the project with:

    flake8 mould tests setup.py

## API documentation

Generate the documentation with:

    make -C docs html

To monitor changes to Python files and execute the tests
automatically, use [pytest-watch](https://github.com/joeyespo/pytest-watch):

    ptw

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1.  The pull request should include tests.
2.  If the pull request adds functionality, the docs should be updated.
    Put your new functionality into a function with a docstring, and add
    the feature to the list in README.md.
3.  Check <https://travis-ci.org/michaeljoseph/mould/pull_requests> and make sure that
    the tests pass for all supported Python versions.
