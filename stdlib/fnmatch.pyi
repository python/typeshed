import sys
from _typeshed import AnyOrLiteralStr
from collections.abc import Iterable
from os import PathLike
from typing import AnyStr, overload

__all__ = ["filter", "fnmatch", "fnmatchcase", "translate"]
if sys.version_info >= (3, 14):
    __all__ += ["filterfalse"]

def fnmatch(name: AnyOrLiteralStr | PathLike[AnyStr], pat: AnyOrLiteralStr | PathLike[AnyStr]) -> bool: ...
def fnmatchcase(name: AnyStr, pat: AnyStr) -> bool: ...
@overload
def filter(names: Iterable[AnyOrLiteralStr], pat: AnyOrLiteralStr) -> list[AnyOrLiteralStr]: ...
@overload
def filter(names: Iterable[AnyOrLiteralStr | PathLike[AnyStr]], pat: AnyOrLiteralStr | PathLike[AnyStr]) -> list[AnyStr]: ...
def translate(pat: str) -> str: ...

if sys.version_info >= (3, 14):
    @overload
    def filterfalse(names: Iterable[AnyOrLiteralStr], pat: AnyOrLiteralStr) -> list[AnyOrLiteralStr]: ...
    @overload
    def filterfalse(names: Iterable[AnyOrLiteralStr | PathLike[AnyStr]], pat: AnyOrLiteralStr | PathLike[AnyStr]) -> list[AnyStr]:
        ...
