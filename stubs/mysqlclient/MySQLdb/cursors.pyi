from typing import Any

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

RE_INSERT_VALUES: Any

class BaseCursor:
    max_stmt_length: Any
    connection: Any
    description: Any
    description_flags: Any
    rowcount: int
    arraysize: int
    lastrowid: Any
    rownumber: Any
    def __init__(self, connection) -> None: ...
    def close(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *exc_info) -> None: ...
    def nextset(self): ...
    def setinputsizes(self, *args) -> None: ...
    def setoutputsizes(self, *args) -> None: ...
    def execute(self, query, args: Any | None = ...): ...
    def executemany(self, query: str, args: list) -> int: ...
    def callproc(self, procname, args=...): ...
    def __iter__(self): ...

class CursorStoreResultMixIn:
    rownumber: Any
    def fetchone(self): ...
    def fetchmany(self, size: Any | None = ...): ...
    def fetchall(self): ...
    def scroll(self, value, mode: str = ...) -> None: ...
    def __iter__(self): ...

class CursorUseResultMixIn:
    rownumber: Any
    def fetchone(self): ...
    def fetchmany(self, size: Any | None = ...): ...
    def fetchall(self): ...
    def __iter__(self): ...
    def next(self): ...
    __next__: Any

class CursorTupleRowsMixIn: ...
class CursorDictRowsMixIn: ...
class Cursor(CursorStoreResultMixIn, CursorTupleRowsMixIn, BaseCursor): ...
class DictCursor(CursorStoreResultMixIn, CursorDictRowsMixIn, BaseCursor): ...
class SSCursor(CursorUseResultMixIn, CursorTupleRowsMixIn, BaseCursor): ...
class SSDictCursor(CursorUseResultMixIn, CursorDictRowsMixIn, BaseCursor): ...
