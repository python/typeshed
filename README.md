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

We store stubs for both Python 2 as well as Python 3. We also distinguish
between minor versions (E.g. 3.2 <-> 3.3). To accomplish not having to duplicate
modules that are the same between all minor versions, we have e.g. a top-level
directory 3/ that contains all the stubs for Python 3. More specialized stubs
go into e.g. 3.3/ and supersede the more generic stubs in 3/. (And, if needed,
a directory 3.3.1/ would be able to supersede stubs in 3.3/):

Directory     | Contents
------------- | -------------
2.7/          | Stubs for Python 2.7
3/            | Stubs for Python 3
3.3/          | Some specialized stubs for Python 3.3 (replacing generic stubs in 3/)

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

