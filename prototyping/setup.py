#!/usr/bin/env python
# coding: utf-8

import sys
from distutils.core import setup

if sys.version_info < (2, 7, 0) or (3,) < sys.version_info < (3, 2, 0):
    sys.stderr.write('ERROR: You need either Python2 2.7 or later '
                     'or Python3 3.2 or later '
                     'to install the typing package.\n')
    exit(1)

version = '3.5.0b1'
description = 'Type Hints for Python'
long_description = '''
Typing -- Type Hints for Python

This is a backport of the standard library typing module to Python
versions older than 3.5.

Typing defines a standard notation for Python function and variable
type annotations. The notation can be used for documenting code in a
concise, standard format, and it has been designed to also be used by
static and runtime type checkers, static analyzers, IDEs and other
tools.
'''.lstrip()

package_dir = {2: 'python2', 3: '.'}[sys.version_info.major]
classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: POSIX',
    'Programming Language :: Python :: 2.7',
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
      url='http://docs.python.org/dev/library/typing.html#typing',
      license='PSF',
      keywords='typing function annotations type hints hinting checking '
               'checker typehints typehinting typechecking backport',
      platforms=['POSIX', 'Windows'],
      package_dir={'': package_dir},
      py_modules=['typing'],
      classifiers=classifiers)
