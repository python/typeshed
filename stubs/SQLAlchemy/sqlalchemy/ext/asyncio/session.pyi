from typing import Any

from .base import ReversibleProxy, StartableContext

class AsyncSession(ReversibleProxy):
    dispatch: Any
    bind: Any
    binds: Any
    sync_session_class: Any
    sync_session: Any
    def __init__(self, bind: Any | None = ..., binds: Any | None = ..., sync_session_class: Any | None = ..., **kw) -> None: ...
    async def refresh(self, instance, attribute_names: Any | None = ..., with_for_update: Any | None = ...): ...
    async def run_sync(self, fn, *arg, **kw): ...
    async def execute(
        self, statement, params: Any | None = ..., execution_options=..., bind_arguments: Any | None = ..., **kw
    ): ...
    async def scalar(
        self, statement, params: Any | None = ..., execution_options=..., bind_arguments: Any | None = ..., **kw
    ): ...
    async def scalars(
        self, statement, params: Any | None = ..., execution_options=..., bind_arguments: Any | None = ..., **kw
    ): ...
    async def get(
        self,
        entity,
        ident,
        options: Any | None = ...,
        populate_existing: bool = ...,
        with_for_update: Any | None = ...,
        identity_token: Any | None = ...,
    ): ...
    async def stream(
        self, statement, params: Any | None = ..., execution_options=..., bind_arguments: Any | None = ..., **kw
    ): ...
    async def stream_scalars(
        self, statement, params: Any | None = ..., execution_options=..., bind_arguments: Any | None = ..., **kw
    ): ...
    async def delete(self, instance): ...
    async def merge(self, instance, load: bool = ..., options: Any | None = ...): ...
    async def flush(self, objects: Any | None = ...) -> None: ...
    def get_transaction(self): ...
    def get_nested_transaction(self): ...
    def get_bind(self, mapper: Any | None = ..., clause: Any | None = ..., bind: Any | None = ..., **kw): ...
    async def connection(self, **kw): ...
    def begin(self, **kw): ...
    def begin_nested(self, **kw): ...
    async def rollback(self): ...
    async def commit(self): ...
    async def close(self): ...
    @classmethod
    async def close_all(self): ...
    async def __aenter__(self): ...
    async def __aexit__(self, type_, value, traceback) -> None: ...

class _AsyncSessionContextManager:
    async_session: Any
    def __init__(self, async_session) -> None: ...
    trans: Any
    async def __aenter__(self): ...
    async def __aexit__(self, type_, value, traceback) -> None: ...

class AsyncSessionTransaction(ReversibleProxy, StartableContext):
    session: Any
    nested: Any
    sync_transaction: Any
    def __init__(self, session, nested: bool = ...) -> None: ...
    @property
    def is_active(self): ...
    async def rollback(self) -> None: ...
    async def commit(self) -> None: ...
    async def start(self, is_ctxmanager: bool = ...): ...
    async def __aexit__(self, type_, value, traceback) -> None: ...

def async_object_session(instance): ...
def async_session(session): ...
