from _typeshed import Incomplete
from typing import Any

from .base import ProxyComparable, StartableContext

def create_async_engine(*arg, **kw) -> AsyncEngine: ...

class AsyncConnectable: ...

class AsyncConnection(ProxyComparable, StartableContext, AsyncConnectable):
    engine: Any
    sync_engine: Any
    sync_connection: Any
    def __init__(self, async_engine, sync_connection: Incomplete | None = ...) -> None: ...
    async def start(self, is_ctxmanager: bool = ...): ...
    @property
    def connection(self) -> None: ...
    async def get_raw_connection(self): ...
    @property
    def info(self): ...
    def begin(self): ...
    def begin_nested(self): ...
    async def invalidate(self, exception: Incomplete | None = ...): ...
    async def get_isolation_level(self): ...
    async def set_isolation_level(self): ...
    def in_transaction(self): ...
    def in_nested_transaction(self): ...
    def get_transaction(self): ...
    def get_nested_transaction(self): ...
    async def execution_options(self, **opt): ...
    async def commit(self) -> None: ...
    async def rollback(self) -> None: ...
    async def close(self) -> None: ...
    async def exec_driver_sql(self, statement, parameters: Incomplete | None = ..., execution_options=...): ...
    async def stream(self, statement, parameters: Incomplete | None = ..., execution_options=...): ...
    async def execute(self, statement, parameters: Incomplete | None = ..., execution_options=...): ...
    async def scalar(self, statement, parameters: Incomplete | None = ..., execution_options=...): ...
    async def scalars(self, statement, parameters: Incomplete | None = ..., execution_options=...): ...
    async def stream_scalars(self, statement, parameters: Incomplete | None = ..., execution_options=...): ...
    async def run_sync(self, fn, *arg, **kw): ...
    def __await__(self): ...
    async def __aexit__(self, type_, value, traceback) -> None: ...
    # proxied from Connection
    dialect: Any
    @property
    def closed(self): ...
    @property
    def invalidated(self): ...
    @property
    def default_isolation_level(self): ...

class AsyncEngine(ProxyComparable, AsyncConnectable):
    class _trans_ctx(StartableContext):
        conn: Any
        def __init__(self, conn) -> None: ...
        transaction: Any
        async def start(self, is_ctxmanager: bool = ...): ...
        async def __aexit__(self, type_, value, traceback) -> None: ...
    sync_engine: Any
    def __init__(self, sync_engine) -> None: ...
    def begin(self): ...
    def connect(self): ...
    async def raw_connection(self): ...
    def execution_options(self, **opt): ...
    async def dispose(self): ...
    # proxied from Engine
    url: Any
    pool: Any
    dialect: Any
    echo: Any
    @property
    def engine(self): ...
    @property
    def name(self): ...
    @property
    def driver(self): ...
    def clear_compiled_cache(self) -> None: ...
    def update_execution_options(self, **opt) -> None: ...
    def get_execution_options(self): ...

class AsyncTransaction(ProxyComparable, StartableContext):
    connection: Any
    sync_transaction: Any
    nested: Any
    def __init__(self, connection, nested: bool = ...) -> None: ...
    @property
    def is_valid(self) -> bool: ...
    @property
    def is_active(self) -> bool: ...
    async def close(self) -> None: ...
    async def rollback(self) -> None: ...
    async def commit(self) -> None: ...
    async def start(self, is_ctxmanager: bool = ...): ...
    async def __aexit__(self, type_, value, traceback) -> None: ...
