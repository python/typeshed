import sys
from collections.abc import Iterable
from os import PathLike
from typing import AnyStr, TypeVar, overload

__all__ = ["filter", "fnmatch", "fnmatchcase", "translate"]
if sys.version_info >= (3, 14):
    __all__ += ["filterfalse"]

_PathT_str = TypeVar("_PathT_str", bound=str | PathLike[str])
_PathT_bytes = TypeVar("_PathT_bytes", bound=bytes | PathLike[bytes])

def fnmatch(name: AnyStr | PathLike[AnyStr], pat: AnyStr | PathLike[AnyStr]) -> bool: ...
def fnmatchcase(name: AnyStr, pat: AnyStr) -> bool: ...

@overload
def filter(names: Iterable[_PathT_str], pat: str | PathLike[str]) -> list[_PathT_str]: ...
@overload
def filter(names: Iterable[_PathT_bytes], pat: bytes | PathLike[bytes]) -> list[_PathT_bytes]: ...

def translate(pat: str) -> str: ...

if sys.version_info >= (3, 14):
    @overload
    def filterfalse(names: Iterable[_PathT_str], pat: str | PathLike[str]) -> list[_PathT_str]: ...
    @overload
    def filterfalse(names: Iterable[_PathT_bytes], pat: bytes | PathLike[bytes]) -> list[_PathT_bytes]: ...
