from _typeshed import SupportsRead
from collections.abc import Iterable, Mapping, Sequence
from re import Pattern
from typing import Any, TypeVar, overload
from typing_extensions import TypeAlias

from Xlib._typing import SupportsComparisons
from Xlib.display import Display
from Xlib.support.lock import _DummyLock

_T = TypeVar("_T")
_C = TypeVar("_C", bound=SupportsComparisons)

_DB: TypeAlias = dict[str, tuple[_DB, ...]]
# This can be a bit annoying due to dict invariance, so making a parameter-specific alias
_DB_Param: TypeAlias = dict[str, Any]

comment_re: Pattern[str]
resource_spec_re: Pattern[str]
value_escape_re: Pattern[str]
resource_parts_re: Pattern[str]
NAME_MATCH: int
CLASS_MATCH: int
WILD_MATCH: int
MATCH_SKIP: int

class OptionError(Exception): ...

class ResourceDB:
    db: _DB
    lock: _DummyLock
    def __init__(
        self,
        file: bytes | SupportsRead[str] | None = ...,
        string: str | None = ...,
        resources: Iterable[tuple[str, object]] | None = ...,
    ) -> None: ...
    def insert_file(self, file: bytes | SupportsRead[str]) -> None: ...
    def insert_string(self, data: str) -> None: ...
    def insert_resources(self, resources: Iterable[tuple[str, object]]) -> None: ...
    def insert(self, resource: str, value: object) -> None: ...
    def __getitem__(self, keys_tuple: tuple[str, str]) -> Any: ...
    @overload
    def get(self, res: str, cls: str, default: None = ...) -> Any: ...
    @overload
    def get(self, res: str, cls: str, default: _T) -> _T: ...
    def update(self, db: ResourceDB) -> None: ...
    def output(self) -> str: ...
    def getopt(self, name: str, argv: Sequence[str], opts: Mapping[str, Option]) -> Sequence[str]: ...

def bin_insert(list: list[_C], element: _C) -> None: ...
def update_db(dest: _DB_Param, src: _DB_Param) -> None: ...
def copy_group(group: tuple[_DB_Param, ...]) -> tuple[_DB, ...]: ...
def copy_db(db: _DB_Param) -> _DB: ...
def output_db(prefix: str, db: _DB_Param) -> str: ...
def output_escape(value: object) -> str: ...

class Option:
    def parse(self, name: str, db: ResourceDB, args: Sequence[_T]) -> Sequence[_T]: ...

class NoArg(Option):
    specifier: str
    value: object
    def __init__(self, specifier: str, value: object) -> None: ...

class IsArg(Option):
    specifier: str
    def __init__(self, specifier: str) -> None: ...

class SepArg(Option):
    specifier: str
    def __init__(self, specifier: str) -> None: ...

class ResArgClass(Option):
    def parse(self, name: str, db: ResourceDB, args: Sequence[str]) -> Sequence[str]: ...  # type: ignore[override]

ResArg: ResArgClass

class SkipArgClass(Option): ...

SkipArg: SkipArgClass

class SkipLineClass(Option): ...

SkipLine: SkipLineClass

class SkipNArgs(Option):
    count: int
    def __init__(self, count: int) -> None: ...

def get_display_opts(
    options: Mapping[str, Option], argv: Sequence[str] = ...
) -> tuple[Display, str, ResourceDB, Sequence[str]]: ...

stdopts: dict[str, SepArg | NoArg | ResArgClass]
