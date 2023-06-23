from _typeshed import Incomplete
from collections.abc import Iterable
from re import Pattern
from typing_extensions import TypeAlias

from .connections import _Literal

_Arguments: TypeAlias = dict[str, _Literal] | dict[bytes, _Literal] | Iterable[_Literal]

RE_INSERT_VALUES: Pattern[str]

class BaseCursor:
    from ._exceptions import (
        DatabaseError as DatabaseError,
        DataError as DataError,
        Error as Error,
        IntegrityError as IntegrityError,
        InterfaceError as InterfaceError,
        InternalError as InternalError,
        MySQLError as MySQLError,
        NotSupportedError as NotSupportedError,
        OperationalError as OperationalError,
        ProgrammingError as ProgrammingError,
        Warning as Warning,
    )

    max_stmt_length: Incomplete
    connection: Incomplete
    description: Incomplete
    description_flags: Incomplete
    rowcount: int
    arraysize: int
    lastrowid: Incomplete
    rownumber: Incomplete
    def __init__(self, connection) -> None: ...
    def close(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *exc_info: object) -> None: ...
    def nextset(self): ...
    def setinputsizes(self, *args) -> None: ...
    def setoutputsizes(self, *args) -> None: ...
    def execute(self, query, args: Incomplete | None = None): ...
    def mogrify(self, query: str | bytes, args: _Arguments | None = None) -> str: ...
    def executemany(self, query: str, args: Iterable[_Arguments]) -> int | None: ...
    def callproc(self, procname, args=()): ...
    def __iter__(self): ...

class CursorStoreResultMixIn:
    rownumber: Incomplete
    def fetchone(self): ...
    def fetchmany(self, size: Incomplete | None = None): ...
    def fetchall(self): ...
    def scroll(self, value, mode: str = "relative") -> None: ...
    def __iter__(self): ...

class CursorUseResultMixIn:
    rownumber: Incomplete
    def fetchone(self): ...
    def fetchmany(self, size: Incomplete | None = None): ...
    def fetchall(self): ...
    def __iter__(self): ...
    def next(self): ...
    __next__: Incomplete

class CursorTupleRowsMixIn: ...
class CursorDictRowsMixIn: ...
class Cursor(CursorStoreResultMixIn, CursorTupleRowsMixIn, BaseCursor): ...
class DictCursor(CursorStoreResultMixIn, CursorDictRowsMixIn, BaseCursor): ...
class SSCursor(CursorUseResultMixIn, CursorTupleRowsMixIn, BaseCursor): ...
class SSDictCursor(CursorUseResultMixIn, CursorDictRowsMixIn, BaseCursor): ...
