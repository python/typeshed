# typeshed

## About

Typeshed models function types for the Python standard library
and Python builtins.

This data can e.g. be used for static analysis, type checking or type inference.

## Format

Each Python module is represented by a `.py` "stub". This is a normal Python
file (i.e., it can be interpreted by Python 3), except all the methods are empty.
Python function annotations ([PEP 3107](https://www.python.org/dev/peps/pep-3107/))
and Python type annotaitons ([PEP 484](http://www.python.org/dev/peps/pep-484/))
are used to describe the types the function has.

## Example

The below is an excerpt from the types for the `datetime` module.

```
MAXYEAR = int()
MINYEAR = int()
__doc__ = str()
__file__ = str()
__name__ = str()
__package__ = None

class date(object):
    def __init__(self, year: int, month: int, day: int): pass
    @classmethod
    def fromtimestamp(cls, timestamp: int or float) -> date: pass
    @classmethod
    def fromordinal(cls, ordinal: int) -> date: pass
    @classmethod
    def today(self) -> date: pass
    def ctime(self) -> str: pass
    def weekday(self) -> int: pass
```

