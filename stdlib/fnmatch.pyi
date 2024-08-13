from _typeshed import GenericPath
from collections.abc import Iterable
from typing import AnyStr

__all__ = ["filter", "fnmatch", "fnmatchcase", "translate"]

def fnmatch(name: GenericPath[AnyStr], pat: AnyStr) -> bool: ...
def fnmatchcase(name: GenericPath[AnyStr], pat: AnyStr) -> bool: ...
def filter(names: Iterable[GenericPath[AnyStr]], pat: AnyStr) -> list[AnyStr]: ...
def translate(pat: str) -> str: ...
