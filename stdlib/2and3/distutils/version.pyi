import sys
from abc import abstractmethod
from typing import Optional, Pattern, Text, Tuple, TypeVar, Union

_T = TypeVar("_T", bound=Version)

class Version:
    def __repr__(self) -> str: ...
    if sys.version_info >= (3,):
        def __eq__(self, other: object) -> bool: ...
        def __lt__(self: _T, other: Union[_T, str]) -> bool: ...
        def __le__(self: _T, other: Union[_T, str]) -> bool: ...
        def __gt__(self: _T, other: Union[_T, str]) -> bool: ...
        def __ge__(self: _T, other: Union[_T, str]) -> bool: ...
    @abstractmethod
    def __init__(self, vstring: Optional[Text] = ...) -> None: ...
    @abstractmethod
    def parse(self: _T, vstring: Text) -> _T: ...
    @abstractmethod
    def __str__(self) -> str: ...
    if sys.version_info >= (3,):
        @abstractmethod
        def _cmp(self: _T, other: Union[_T, str]) -> bool: ...
    else:
        @abstractmethod
        def __cmp__(self: _T, other: Union[_T, str]) -> bool: ...

class StrictVersion(Version):
    version_re: Pattern[str]
    version: Tuple[int, int, int]
    prerelease: Optional[Tuple[Text, int]]
    def __init__(self, vstring: Optional[Text] = ...) -> None: ...
    def parse(self: _T, vstring: Text) -> _T: ...
    def __str__(self) -> str: ...
    if sys.version_info >= (3,):
        def _cmp(self: _T, other: Union[_T, str]) -> bool: ...
    else:
        def __cmp__(self: _T, other: Union[_T, str]) -> bool: ...

class LooseVersion(Version):
    component_re: Pattern[str]
    vstring: Text
    version: Tuple[Union[Text, int], ...]
    def __init__(self, vstring: Optional[Text] = ...) -> None: ...
    def parse(self: _T, vstring: Text) -> _T: ...
    def __str__(self) -> str: ...
    if sys.version_info >= (3,):
        def _cmp(self: _T, other: Union[_T, str]) -> bool: ...
    else:
        def __cmp__(self: _T, other: Union[_T, str]) -> bool: ...
