from _typeshed import Incomplete
from typing import Any

from ...engine import AdaptedConnection
from .base import SQLiteExecutionContext
from .pysqlite import SQLiteDialect_pysqlite

class AsyncAdapt_aiosqlite_cursor:
    server_side: bool
    await_: Any
    arraysize: int
    rowcount: int
    description: Any
    def __init__(self, adapt_connection) -> None: ...
    def close(self) -> None: ...
    lastrowid: int
    def execute(self, operation, parameters: Incomplete | None = ...) -> None: ...
    def executemany(self, operation, seq_of_parameters) -> None: ...
    def setinputsizes(self, *inputsizes) -> None: ...
    def __iter__(self): ...
    def fetchone(self): ...
    def fetchmany(self, size: Incomplete | None = ...): ...
    def fetchall(self): ...

class AsyncAdapt_aiosqlite_ss_cursor(AsyncAdapt_aiosqlite_cursor):
    server_side: bool
    def __init__(self, *arg, **kw) -> None: ...
    def close(self) -> None: ...
    def fetchone(self): ...
    def fetchmany(self, size: Incomplete | None = ...): ...
    def fetchall(self): ...

class AsyncAdapt_aiosqlite_connection(AdaptedConnection):
    await_: Any
    dbapi: Any
    def __init__(self, dbapi, connection) -> None: ...
    @property
    def isolation_level(self): ...
    @isolation_level.setter
    def isolation_level(self, value) -> None: ...
    def create_function(self, *args, **kw) -> None: ...
    def cursor(self, server_side: bool = ...): ...
    def execute(self, *args, **kw): ...
    def rollback(self) -> None: ...
    def commit(self) -> None: ...
    def close(self) -> None: ...

class AsyncAdaptFallback_aiosqlite_connection(AsyncAdapt_aiosqlite_connection):
    await_: Any

class AsyncAdapt_aiosqlite_dbapi:
    aiosqlite: Any
    sqlite: Any
    paramstyle: str
    def __init__(self, aiosqlite, sqlite) -> None: ...
    def connect(self, *arg, **kw): ...

class SQLiteExecutionContext_aiosqlite(SQLiteExecutionContext):
    def create_server_side_cursor(self): ...

class SQLiteDialect_aiosqlite(SQLiteDialect_pysqlite):
    driver: str
    supports_statement_cache: bool
    is_async: bool
    supports_server_side_cursors: bool
    @classmethod
    def dbapi(cls): ...
    @classmethod
    def get_pool_class(cls, url): ...
    def is_disconnect(self, e, connection, cursor): ...
    def get_driver_connection(self, connection): ...

dialect = SQLiteDialect_aiosqlite