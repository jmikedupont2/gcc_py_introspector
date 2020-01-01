#!/usr/bin/env python
"""Packaging logic for introspector."""
from distutils.core import setup
import os
import sys


import setuptools

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))  # noqa

requires = [
    # We document the reasoning for using ranges here:
    # http://flake8.pycqa.org/en/latest/faq.html#why-does-flake8-use-ranges-for-its-dependencies
    # And in which releases we will update those ranges here:
    # http://flake8.pycqa.org/en/latest/internal/releases.html#releasing-flake8
    "entrypoints >= 0.3.0, < 0.4.0",
    "pyflakes >= 2.1.0, < 2.2.0",
    "pycodestyle >= 2.5.0, < 2.6.0",
    "mccabe >= 0.6.0, < 0.7.0",
    "ply",
    'click'
]

extras_require = {
    ":python_version<'3.4'": ['enum34'],
    ":python_version<'3.5'": ['typing'],
    ":python_version<'3.2'": ['configparser', 'functools32'],
}

if int(setuptools.__version__.split('.')[0]) < 18:
    extras_require = {}
    if sys.version_info < (3, 4):
        requires.append('enum34')
    if sys.version_info < (3, 2):
        requires.append('configparser')

setup(
    name="gcc.py.introspector",
    version="0.1",
    description="Python Parsing of GCC Tree Dump Utilities",
    long_description="gcc .tu dump file processing utility",
    author="James Michael DuPont",
    author_email="jamesmikedupont@gmail.com",
    scripts=["src/gcc/tree/gcc-tu-reader.py"],
    url="https://www.python.org/sigs/distutils-sig/",
    packages=["gcc.tree"],
    package_dir={"": "src"},
    install_requires=requires,
    extras_require=extras_require,

)
