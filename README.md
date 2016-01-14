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

## Syntax example

The below is an excerpt from the types for the `datetime` module.

```
MAXYEAR = ...  # type: int
MINYEAR = ...  # type: int
__doc__ = ...  # type: str
__file__ = ...  # type: str
__name__ = ...  # type: str
__package__ = ...  # type: None

class date(object):
    def __init__(self, year: int, month: int, day: int) -> None: ...
    @classmethod
    def fromtimestamp(cls, timestamp: int or float) -> date: ...
    @classmethod
    def fromordinal(cls, ordinal: int) -> date: ...
    @classmethod
    def today(self) -> date: ...
    def ctime(self) -> str: ...
    def weekday(self) -> int: ...
```

## Directory structure

### stdlib

This contains stubs for modules the Python standard library -- which
includes pure Python modules, dynamically loaded extension modules,
hard-linked extension modules, and the builtins.

### third_party

Modules that are not shipped with Python but have a type description in Python
go into `third_party`. Since these modules can behave differently for different
versions of Python, `third_party` has version subdirectories, just like
`stdlib`.

We're welcoming contributions (pull requests) for type definitions of
third party packages.

### Version directories

We store stubs for both Python 2 as well as Python 3. We also distinguish
between minor versions (E.g. 3.2 <-> 3.3). To accomplish not having to duplicate
modules that are the same between all minor versions, we have e.g. a top-level
directory 3/ that contains all the stubs for Python 3. More specialized stubs
go into e.g. 3.3/ and supersede the more generic stubs in 3/.
Modules that are the same under both Python 2 and Python 3 go into 2and3/.
Note that the only supported version of Python 2 is 2.7.

### Combining multiple versions in a single file

According to PEP 484, type checkers are expected to understand simple
version and platform checks. So the following syntax is legal in a `pyi`:

```
if sys.version_info[0] >= 3:
    # Python 3 specific definitions
else:
    # Python 2 specific definitions
```

This can be used for modules in 2and3/ that only have minor changes between
Python 2 and Python 3. If the difference between versions is more drastic, it
can make more sense to have seperate files in 2.x/ and 3.x/.
