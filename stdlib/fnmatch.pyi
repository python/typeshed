import sys
from collections.abc import Iterable
from os import PathLike
from typing import Any, AnyStr, TypeVar

__all__ = ["filter", "fnmatch", "fnmatchcase", "translate"]
if sys.version_info >= (3, 14):
    __all__ += ["filterfalse"]

_PathT = TypeVar("_PathT", str | PathLike[str], bytes | PathLike[bytes])

def fnmatch(name: AnyStr | PathLike[AnyStr], pat: AnyStr | PathLike[AnyStr]) -> bool: ...
def fnmatchcase(name: AnyStr, pat: AnyStr) -> bool: ...
def filter(names: Iterable[_PathT], pat: _PathT) -> list[_PathT]: ...
def translate(pat: str) -> str: ...

if sys.version_info >= (3, 14):
    def filterfalse(names: Iterable[_PathT], pat: _PathT) -> list[_PathT]: ...
