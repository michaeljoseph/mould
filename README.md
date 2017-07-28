# mould

[![Build Status](https://secure.travis-ci.org/michaeljoseph/mould.png)](http://travis-ci.org/michaeljoseph/mould)
[![code coverage](https://codecov.io/gh/michaeljoseph/mould/branch/master/graph/badge.svg)](https://codecov.io/gh/michaeljoseph/mould)

## Overview

Create [cookiecutter](https://github.com/audreyr/cookiecutter) templates from an existing project or module.

## Usage

Install `mould`:

    pip install mould

Then execute the cli:

   mould

## Documentation

[API Documentation](https://mould.readthedocs.io)

## Testing

Install the development requirements:

    pip install -r requirements.txt

Run the tests:

    pytest

Lint the project:

    flake8 mould tests setup.py

## API documentation

Generate the documentation with:

    make -C docs html

To monitor changes to Python files and execute the tests
automatically, use [pytest-watch](https://github.com/joeyespo/pytest-watch):

    ptw
