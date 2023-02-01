from _typeshed import Incomplete
from typing import Any

from ...engine import AdaptedConnection
from .pymysql import MySQLDialect_pymysql

class AsyncAdapt_asyncmy_cursor:
    server_side: bool
    await_: Any
    def __init__(self, adapt_connection) -> None: ...
    @property
    def description(self): ...
    @property
    def rowcount(self): ...
    @property
    def arraysize(self): ...
    @arraysize.setter
    def arraysize(self, value) -> None: ...
    @property
    def lastrowid(self): ...
    def close(self) -> None: ...
    def execute(self, operation, parameters: Incomplete | None = ...): ...
    def executemany(self, operation, seq_of_parameters): ...
    def setinputsizes(self, *inputsizes) -> None: ...
    def __iter__(self): ...
    def fetchone(self): ...
    def fetchmany(self, size: Incomplete | None = ...): ...
    def fetchall(self): ...

class AsyncAdapt_asyncmy_ss_cursor(AsyncAdapt_asyncmy_cursor):
    server_side: bool
    await_: Any
    def __init__(self, adapt_connection) -> None: ...
    def close(self) -> None: ...
    def fetchone(self): ...
    def fetchmany(self, size: Incomplete | None = ...): ...
    def fetchall(self): ...

class AsyncAdapt_asyncmy_connection(AdaptedConnection):
    await_: Any
    dbapi: Any
    def __init__(self, dbapi, connection) -> None: ...
    def ping(self, reconnect): ...
    def character_set_name(self): ...
    def autocommit(self, value) -> None: ...
    def cursor(self, server_side: bool = ...): ...
    def rollback(self) -> None: ...
    def commit(self) -> None: ...
    def close(self) -> None: ...

class AsyncAdaptFallback_asyncmy_connection(AsyncAdapt_asyncmy_connection):
    await_: Any

class AsyncAdapt_asyncmy_dbapi:
    asyncmy: Any
    pymysql: Any
    paramstyle: str
    def __init__(self, asyncmy: Any) -> None: ...
    def connect(self, *arg, **kw): ...

class MySQLDialect_asyncmy(MySQLDialect_pymysql):
    driver: str
    supports_statement_cache: bool
    supports_server_side_cursors: bool
    is_async: bool
    @classmethod
    def dbapi(cls): ...
    @classmethod
    def get_pool_class(cls, url): ...
    def create_connect_args(self, url): ...
    def is_disconnect(self, e, connection, cursor): ...
    def get_driver_connection(self, connection): ...

dialect = MySQLDialect_asyncmy
