import sys
from _typeshed import AnyOrLiteralStr
from collections.abc import Iterable
from os import PathLike
from typing import AnyStr

__all__ = ["filter", "fnmatch", "fnmatchcase", "translate"]
if sys.version_info >= (3, 14):
    __all__ += ["filterfalse"]

def fnmatch(name: AnyOrLiteralStr | PathLike[AnyStr], pat: AnyOrLiteralStr | PathLike[AnyStr]) -> bool: ...
def fnmatchcase(name: AnyStr, pat: AnyStr) -> bool: ...
def filter(names: Iterable[AnyOrLiteralStr | PathLike[AnyStr]], pat: AnyOrLiteralStr | PathLike[AnyStr]) -> list[AnyStr]: ...
def translate(pat: str) -> str: ...

if sys.version_info >= (3, 14):
    def filterfalse(
        names: Iterable[AnyOrLiteralStr | PathLike[AnyStr]], pat: AnyOrLiteralStr | PathLike[AnyStr]
    ) -> list[AnyStr]: ...
