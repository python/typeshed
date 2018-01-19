import sys
from typing import Any, Optional, TypeVar, Union, Pattern, Tuple

T = TypeVar('T', bound='Version')

class Version:
    def __init__(self, vstring: Optional[str] = None) -> None: ...
    def __repr__(self) -> str: ...

    if sys.version_info >= (3,):
        def __eq__(self: T, other: Union[T, str]) -> bool: ...
        def __lt__(self: T, other: Union[T, str]) -> bool: ...
        def __le__(self: T, other: Union[T, str]) -> bool: ...
        def __gt__(self: T, other: Union[T, str]) -> bool: ...
        def __ge__(self: T, other: Union[T, str]) -> bool: ...

    # Methods part of the 'Version' interface, but not implemented
    # within the class itself

    def parse(self: T, vstring: str) -> T: ...
    def __str__(self) -> str: ...
    if sys.version_info >= (3,):
        def _cmp(self: T, other: Union[T, str]) -> bool: ...
    else:
        def __cmp__(self: T, other: Union[T, str]) -> bool: ...
    

class StrictVersion(Version):
    version_re: Pattern[str]
    version: Tuple[int, int, int]
    prerelease: Optional[Tuple[str, int]]


class LooseVersion(Version):
    component_re: Pattern[str]
    vstring: str
    version: Tuple[Union[str, int], ...]

