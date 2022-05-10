from collections.abc import Mapping
from typing import Any, overload
from typing_extensions import Literal

from ..engine import Engine
from ..engine.url import URL
from ..ext.asyncio import AsyncEngine

class ConnectionKiller:
    proxy_refs: Any
    testing_engines: Any
    dbapi_connections: Any
    def __init__(self) -> None: ...
    def add_pool(self, pool) -> None: ...
    def add_engine(self, engine, scope) -> None: ...
    def rollback_all(self) -> None: ...
    def checkin_all(self) -> None: ...
    def close_all(self) -> None: ...
    def prepare_for_drop_tables(self, connection) -> None: ...
    def after_test(self) -> None: ...
    def after_test_outside_fixtures(self, test) -> None: ...
    def stop_test_class_inside_fixtures(self) -> None: ...
    def stop_test_class_outside_fixtures(self) -> None: ...
    def final_cleanup(self) -> None: ...
    def assert_all_closed(self) -> None: ...

testing_reaper: Any

def assert_conns_closed(fn, *args, **kw) -> None: ...
def rollback_open_connections(fn, *args, **kw) -> None: ...
def close_first(fn, *args, **kw) -> None: ...
def close_open_connections(fn, *args, **kw) -> None: ...
def all_dialects(exclude: Any | None = ...) -> None: ...

class ReconnectFixture:
    dbapi: Any
    connections: Any
    is_stopped: bool
    def __init__(self, dbapi) -> None: ...
    def __getattr__(self, key): ...
    def connect(self, *args, **kwargs): ...
    def shutdown(self, stop: bool = ...) -> None: ...
    def restart(self) -> None: ...

def reconnecting_engine(url: Any | None = ..., options: Any | None = ...): ...
@overload
def testing_engine(  # type: ignore[misc]
    url: URL | str | None = ...,
    options: Mapping[str, Any] | None = ...,
    future: Any | None = ...,
    asyncio: Literal[False] = ...,
    transfer_staticpool: bool = ...,
) -> Engine: ...
@overload
def testing_engine(
    url: URL | str | None = ...,
    options: Mapping[str, Any] | None = ...,
    future: Any | None = ...,
    asyncio: Literal[True] = ...,
    transfer_staticpool: bool = ...,
) -> AsyncEngine: ...
def mock_engine(dialect_name: Any | None = ...): ...

class DBAPIProxyCursor:
    engine: Any
    connection: Any
    cursor: Any
    def __init__(self, engine, conn, *args, **kwargs) -> None: ...
    def execute(self, stmt, parameters: Any | None = ..., **kw): ...
    def executemany(self, stmt, params, **kw): ...
    def __iter__(self): ...
    def __getattr__(self, key): ...

class DBAPIProxyConnection:
    conn: Any
    engine: Any
    cursor_cls: Any
    def __init__(self, engine, cursor_cls) -> None: ...
    def cursor(self, *args, **kwargs): ...
    def close(self) -> None: ...
    def __getattr__(self, key): ...

def proxying_engine(conn_cls=..., cursor_cls=...): ...
