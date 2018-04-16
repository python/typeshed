# -*- coding: utf-8 -*-
"""A collection of type annotations for the standard library and others.

The type annotations in question are stored in so-called "stub files".  They're
Python-like files with the .pyi file extension.  See PEP 484 for more details.

Typeshed is organized in the following directory structure:

    typeshed
    ├── __init__.py
    ├── stdlib
    │   ├── 2
    │   ├── 2and3
    │   ├── 3
    │   ├── 3.3
    │   ├── 3.4
    │   └── ...
    └── third_party
        ├── 2
        ├── 2and3
        ├── 3
        └── ...

The `stdlib` directory contains stubs for modules the Python standard library --
which includes pure Python modules, dynamically loaded extension modules,
hard-linked extension modules, and the builtins.  Modules that are not shipped
with Python but have a type description in Python go into `third_party`.

Modules with types that behave the same regardless of the Python version used
are stored in `2and3` directories.  Specific versions like `3.6` describe
modules which are not available in previous versions.  `3` is a generic
directory storing type informartion for any Python 3 version.  Stub files often
contain sections which declare compatibility with only a particular subset of
Python 3 versions.  Those sections are marked using `if sys.version_info`
checks.  See PEP 484 for more details.

To get the absolute location of the base typeshed directory in your project,
use the following:

    >>> import typeshed
    >>> typeshed.get_dir()
    '/path/to/typeshed/'

`get_dir()` works also for zipped archives.  In this case it points to
a temporary directory where typeshed was unpacked.
"""

from os.path import dirname, realpath


__all__ = ['__version__', 'get_dir']
__version__ = "18.4.0"


def get_dir():
    # type: () -> str
    """Return the absolute path to the location of typeshed as a string.

    Works also for zipped archives.  In this case it points to a temporary
    directory where typeshed was unpacked.
    """
    try:
        import pkg_resources
    except ImportError:
        return realpath(dirname(dirname(__file__)))
    else:
        return realpath(pkg_resources.resource_filename("typeshed", ""))
