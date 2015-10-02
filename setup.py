#!/usr/bin/env python
# coding: utf-8

import sys
from distutils.core import setup

if sys.version_info < (3, 2, 0):
    sys.stderr.write('ERROR: You need Python 3.2 or later '
                     'to install the typing package.\n')
    exit(1)

version = '3.5.0'
description = 'Type Hints for Python'
long_description = '''\
Typing -- Type Hints for Python

This is a backport of the standard library typing module to Python
versions older than 3.5.

Typing defines a standard notation for Python function and variable
type annotations. The notation can be used for documenting code in a
concise, standard format, and it has been designed to also be used by
static and runtime type checkers, static analyzers, IDEs and other
tools.
'''

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Python Software Foundation License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Topic :: Software Development',
]

setup(name='typing',
      version=version,
      description=description,
      long_description=long_description,
      author=u'Guido van Rossum, Jukka Lehtosalo, Łukasz Langa',
      author_email='jukka.lehtosalo@iki.fi',
      url='https://docs.python.org/3.5/library/typing.html',
      license='PSF',
      keywords='typing function annotations type hints hinting checking '
               'checker typehints typehinting typechecking backport',
      package_dir={'': 'src'},
      py_modules=['typing'],
      classifiers=classifiers)
