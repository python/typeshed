from _typeshed import SupportsWrite
from collections.abc import Iterable, Iterator
from typing import Any, Union
from typing_extensions import Literal, TypeAlias

__version__: str

QUOTE_ALL: Literal[1]
QUOTE_MINIMAL: Literal[0]
QUOTE_NONE: Literal[3]
QUOTE_NONNUMERIC: Literal[2]

class Error(Exception): ...

class Dialect:
    delimiter: str
    quotechar: str | None
    escapechar: str | None
    doublequote: bool
    skipinitialspace: bool
    lineterminator: str
    quoting: int
    strict: int
    def __init__(self) -> None: ...

_DialectLike: TypeAlias = Union[str, Dialect, type[Dialect]]

class _reader(Iterator[list[str]]):
    @property
    def dialect(self) -> Dialect: ...
    line_num: int
    def __next__(self) -> list[str]: ...

class _writer:
    @property
    def dialect(self) -> Dialect: ...
    def writerow(self, row: Iterable[Any]) -> Any: ...
    def writerows(self, rows: Iterable[Iterable[Any]]) -> None: ...

def writer(
    csvfile: SupportsWrite[str],
    dialect: _DialectLike = ...,
    *,
    delimiter: str = ...,
    quotechar: str | None = ...,
    escapechar: str | None = ...,
    skipinitialspace: bool = ...,
    lineterminator: str = ...,
    quoting: int = ...,
    strict: int = ...,
) -> _writer: ...
def reader(
    csvfile: Iterable[str],
    dialect: _DialectLike = ...,
    *,
    delimiter: str = ...,
    quotechar: str | None = ...,
    escapechar: str | None = ...,
    skipinitialspace: bool = ...,
    lineterminator: str = ...,
    quoting: int = ...,
    strict: int = ...,
) -> _reader: ...
def register_dialect(
    name: str,
    dialect: Any = ...,
    *,
    delimiter: str = ...,
    quotechar: str | None = ...,
    escapechar: str | None = ...,
    skipinitialspace: bool = ...,
    lineterminator: str = ...,
    quoting: int = ...,
    strict: int = ...,
) -> None: ...
def unregister_dialect(name: str) -> None: ...
def get_dialect(name: str) -> Dialect: ...
def list_dialects() -> list[str]: ...
def field_size_limit(new_limit: int = ...) -> int: ...
