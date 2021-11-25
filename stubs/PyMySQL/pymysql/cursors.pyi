from typing import Any, Iterable, Iterator, Text, Tuple, TypeVar

from .connections import Connection

_SelfT = TypeVar("_SelfT")

class Cursor:
    connection: Connection[Any]
    description: Tuple[Text, ...]
    rownumber: int
    rowcount: int
    arraysize: int
    messages: Any
    errorhandler: Any
    lastrowid: int
    def __init__(self, connection: Connection[Any]) -> None: ...
    def __del__(self) -> None: ...
    def close(self) -> None: ...
    def setinputsizes(self, *args) -> None: ...
    def setoutputsizes(self, *args) -> None: ...
    def nextset(self) -> bool | None: ...
    def mogrify(self, query: Text, args: object = ...) -> str: ...
    def execute(self, query: Text, args: object = ...) -> int: ...
    def executemany(self, query: Text, args: Iterable[object]) -> int | None: ...
    def callproc(self, procname: Text, args: Iterable[Any] = ...) -> Any: ...
    def scroll(self, value: int, mode: Text = ...) -> None: ...
    def __enter__(self: _SelfT) -> _SelfT: ...
    def __exit__(self, *exc_info: Any) -> None: ...
    # Methods returning result tuples are below.
    def fetchone(self) -> Tuple[Any, ...] | None: ...
    def fetchmany(self, size: int | None = ...) -> Tuple[Tuple[Any, ...], ...]: ...
    def fetchall(self) -> Tuple[Tuple[Any, ...], ...]: ...
    def __iter__(self) -> Iterator[Tuple[Any, ...]]: ...

class DictCursorMixin:
    dict_type: Any  # TODO: add support if someone needs this
    def fetchone(self) -> dict[Text, Any] | None: ...
    def fetchmany(self, size: int | None = ...) -> Tuple[dict[Text, Any], ...]: ...
    def fetchall(self) -> Tuple[dict[Text, Any], ...]: ...
    def __iter__(self) -> Iterator[dict[Text, Any]]: ...

class SSCursor(Cursor):
    def fetchall(self) -> list[Tuple[Any, ...]]: ...
    def fetchall_unbuffered(self) -> Iterator[Tuple[Any, ...]]: ...
    def scroll(self, value: int, mode: Text = ...) -> None: ...

class DictCursor(DictCursorMixin, Cursor): ...

class SSDictCursor(DictCursorMixin, SSCursor):
    def fetchall_unbuffered(self) -> Iterator[dict[Text, Any]]: ...
