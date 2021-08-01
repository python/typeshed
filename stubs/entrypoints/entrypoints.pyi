import sys
from typing import Any, Dict, Generic, Iterator, List, Sequence, Text, Tuple, Type, TypeVar

if sys.version_info >= (3, 0):
    from configparser import ConfigParser
else:
    from ConfigParser import ConfigParser

if sys.version_info >= (3, 8):
    from re import Pattern
else:
    from typing import Pattern

_T = TypeVar("_T")

entry_point_pattern: Pattern[Text]
file_in_zip_pattern: Pattern[Text]

class BadEntryPoint(Exception):
    epstr: Text
    def __init__(self, epstr: Text) -> None: ...
    @staticmethod
    def err_to_warnings() -> Iterator[None]: ...

class NoSuchEntryPoint(Exception):
    group: Text
    name: Text
    def __init__(self, group: Text, name: Text) -> None: ...

class EntryPoint(Generic[_T]):
    _E = TypeVar("_E", bound="EntryPoint[_T]")
    name: Text
    module_name: Text
    object_name: Text
    extras: Sequence[Text] | None
    distro: Distribution | None
    def __init__(
        self,
        name: Text,
        module_name: Text,
        object_name: Text,
        extras: Sequence[Text] | None = ...,
        distro: Distribution | None = ...,
    ) -> None: ...
    def load(self) -> _T: ...
    @classmethod
    def from_string(cls: Type[_E], epstr: Text, name: Text, distro: Distribution | None = ...) -> _E: ...

class Distribution:
    name: Text
    version: Text
    def __init__(self, name: Text, version: Text) -> None: ...

def iter_files_distros(
    path: Sequence[Text] | None = ..., repeated_distro: Text = ...
) -> Iterator[Tuple[ConfigParser, Distribution | None]]: ...
def get_single(group: Text, name: Text, path: Sequence[Text] | None = ...) -> EntryPoint[_T]: ...
def get_group_named(group: Text, path: Sequence[Text] | None = ...) -> Dict[str, EntryPoint[Any]]: ...
def get_group_all(group: Text, path: Sequence[Text] | None = ...) -> List[EntryPoint[Any]]: ...
