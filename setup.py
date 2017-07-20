import re
from setuptools import setup

init_py = open('mould/__init__.py').read()
metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", init_py))
metadata['doc'] = re.findall('"""(.+)"""', init_py)[0]

setup(
    name='mould',
    version=metadata['version'],
    description=metadata['doc'],
    author=metadata['author'],
    author_email=metadata['email'],
    url=metadata['url'],
    packages=['mould'],
    include_package_data=True,
    install_requires=[
        'click < 2.1.0'
    ],
    entry_points={
        'console_scripts': [
            'mould = mould.cli:main',
        ],
    },
    license=open('LICENSE').read(),
)
