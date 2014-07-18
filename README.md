# mould

[![Build Status](https://secure.travis-ci.org/michaeljoseph/mould.png)](http://travis-ci.org/michaeljoseph/mould)
[![Stories in Ready](https://badge.waffle.io/michaeljoseph/mould.png?label=ready)](https://waffle.io/michaeljoseph/mould) [![pypi version](https://badge.fury.io/py/mould.png)](http://badge.fury.io/py/mould)
[![# of downloads](https://pypip.in/d/mould/badge.png)](https://crate.io/packages/mould?version=latest)
[![code coverage](https://coveralls.io/repos/michaeljoseph/mould/badge.png?branch=master)](https://coveralls.io/r/michaeljoseph/mould?branch=master)

## Overview

Create cookiecutter templates from aisting directory

* features
* and stuff 

## Usage

Install `mould`:

    pip install mould

Then execute the sample cli:

   mould

## Documentation

[API Documentation](http://mould.rtfd.org)

## Testing

Install development requirements:

    pip install -r requirements.txt

Tests can then be run with:

    nosetests

Lint the project with:

    flake8 mould tests

## API documentation

Generate the documentation with:

    cd docs && PYTHONPATH=.. make singlehtml

To monitor changes to Python files and execute flake8 and nosetests
automatically, execute the following from the root project directory:

    stir