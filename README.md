# typeshed

## About

Typeshed models function types for the Python standard library
and Python builtins.

This data can e.g. be used for static analysis, type checking or type inference.

## Format

Each Python module is represented by a `.py` "stub". This is a normal Python
file (i.e., it can be interpreted by Python 3), except all the methods are empty.
Python function annotations ([PEP 3107](https://www.python.org/dev/peps/pep-3107/))
are used to describe the types the function has.
See [PEP 484](http://www.python.org/dev/peps/pep-0484/) for the exact syntax
of the stub files.

## Example

The below is an excerpt from the types for the `datetime` module.

```
MAXYEAR = Undefined(int)
MINYEAR = Undefined(int)
__doc__ = Undefined(str)
__file__ = Undefined(str)
__name__ = Undefined(str)
__package__ = Undefined(None)

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

