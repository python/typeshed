import sys
from collections.abc import Iterable
from os import PathLike
from typing import AnyStr, TypeVar

__all__ = ["filter", "fnmatch", "fnmatchcase", "translate"]
if sys.version_info >= (3, 14):
    __all__ += ["filterfalse"]

_AnyStrPathLike = TypeVar("_T", bound=str | bytes | PathLike[Any])

def fnmatch(name: AnyStr | PathLike[AnyStr], pat: AnyStr | PathLike[AnyStr]) -> bool: ...
def fnmatchcase(name: AnyStr, pat: AnyStr) -> bool: ...
def filter(names: Iterable[_AnyStrPathLike], pat: AnyStr | PathLike[AnyStr]) -> list[_AnyStrPathLike]: ...
def translate(pat: str) -> str: ...

if sys.version_info >= (3, 14):
    def filterfalse(names: Iterable[_AnyStrPathLike], pat: AnyStr | PathLike[AnyStr]) -> list[_AnyStrPathLike]: ...
