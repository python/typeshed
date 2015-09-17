# typeshed

## About

Typeshed models function types for the Python standard library
and Python builtins, as well as third party packages.

This data can e.g. be used for static analysis, type checking or type inference.

## Format

Each Python module is represented by a `.pyi` "stub". This is a normal Python
file (i.e., it can be interpreted by Python 3), except all the methods are empty.
Python function annotations ([PEP 3107](https://www.python.org/dev/peps/pep-3107/))
are used to describe the types the function has.
See [PEP 484](http://www.python.org/dev/peps/pep-0484/) for the exact syntax
of the stub files.

## Directory structure

### Builtins vs stdlib

Python ships with a set of built-in modules, i.e., modules that are baked into
the Python executable. For a specific Python build, you can use
`sys.builtin_module_names` to query which modules are built in. Also, you
can determine whether a module is a built-in module by doing
`import module; import.__file__`. If `__file__` exists, the module is not
built in. Typeshed stores built-in modules in the "builtins/" directory.
Examples for built-in modules: sys, array, math, signal.

There are other modules that ship with Python, but are not linked into the
Python binary. E.g. os.py, glob.py, zipfile.py. (But also some C extensions
like datetime)
These modules are stored in the stdlib/ directory.

Note that built-in modules have higher precedence in the import path than stdlib
modules.  The former are implicitly prepended to the start of your PYTHONPATH,
whereas the latter are implicitly appended to it.

### Version numbers

We store stubs for both Python 2 as well as Python 3. We also distinguish
between minor versions (E.g. 3.2 <-> 3.3). To accomplish not having to duplicate
modules that are the same between all minor versions, we have e.g. a top-level
directory 3/ that contains all the stubs for Python 3. More specialized stubs
go into e.g. 3.3/ and supersede the more generic stubs in 3/. (And, if needed,
a directory 3.3.1/ would be able to supersede stubs in 3.3/).
Modules that are the same under both Python 2 and Python 3 go into 2and3/.

### Example

Directory       | Contents
-------------   | -------------
builtins/2and3/ | Builtin stubs for Python 2 and Python 3
builtins/2/     | Builtin stubs for Python 2
...             | ...
builtins/2.7/   | Builtin stubs for Python 2.7
builtins/3/     | Builtin stubs for Python 3
...             | ...
builtins/3.3/   | Builtin stubs for Python 3.3 (replacing generic stubs in 3/)
stdlib/2and3/   | Standard library stubs for Python 2 and Python 3
stdlib/2.7/     | Standard library stubs for Python 2.7
...             | ...
stdlib/2.7.6/   | Standard library stubs specialized for Python 2.7.6

## Example

The below is an excerpt from the types for the `datetime` module.

```
MAXYEAR = ...  # type: int
MINYEAR = ...  # type: int
__doc__ = ...  # type: str
__file__ = ...  # type: str
__name__ = ...  # type: str
__package__ = ...  # type: None

class date(object):
    def __init__(self, year: int, month: int, day: int): ...
    @classmethod
    def fromtimestamp(cls, timestamp: int or float) -> date: ...
    @classmethod
    def fromordinal(cls, ordinal: int) -> date: ...
    @classmethod
    def today(self) -> date: ...
    def ctime(self) -> str: ...
    def weekday(self) -> int: ...
```

## Contributions

We're welcoming contributions (pull requests) for types of third party
packages. They'll go under {2.7,3}/dist-packages/.

