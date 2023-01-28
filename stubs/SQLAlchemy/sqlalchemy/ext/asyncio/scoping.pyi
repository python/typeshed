from _typeshed import Incomplete
from typing import Any

from ...orm.scoping import ScopedSessionMixin
from ...util import memoized_property

class async_scoped_session(ScopedSessionMixin):
    session_factory: Any
    registry: Any
    def __init__(self, session_factory, scopefunc) -> None: ...
    async def remove(self) -> None: ...
    # proxied from Session
    @classmethod
    async def close_all(cls): ...
    @classmethod
    def identity_key(cls, *args, **kwargs): ...
    @classmethod
    def object_session(cls, instance): ...
    bind: Any
    identity_map: Any
    autoflush: Any
    def __contains__(self, instance) -> bool: ...
    def __iter__(self): ...
    def add(self, instance, _warn: bool = ...) -> None: ...
    def add_all(self, instances) -> None: ...
    def begin(self, **kw): ...
    def begin_nested(self, **kw): ...
    async def close(self): ...
    async def commit(self): ...
    async def connection(self, **kw): ...
    async def delete(self, instance): ...
    async def execute(
        self, statement, params: Incomplete | None = ..., execution_options=..., bind_arguments: Incomplete | None = ..., **kw
    ): ...
    def expire(self, instance, attribute_names: Incomplete | None = ...) -> None: ...
    def expire_all(self) -> None: ...
    def expunge(self, instance) -> None: ...
    def expunge_all(self) -> None: ...
    async def flush(self, objects: Incomplete | None = ...) -> None: ...
    async def get(
        self,
        entity,
        ident,
        options: Incomplete | None = ...,
        populate_existing: bool = ...,
        with_for_update: Incomplete | None = ...,
        identity_token: Incomplete | None = ...,
    ): ...
    def get_bind(self, mapper: Incomplete | None = ..., clause: Incomplete | None = ..., bind: Incomplete | None = ..., **kw): ...
    def is_modified(self, instance, include_collections: bool = ...) -> bool: ...
    async def merge(self, instance, load: bool = ..., options: Incomplete | None = ...): ...
    async def refresh(self, instance, attribute_names: Incomplete | None = ..., with_for_update: Incomplete | None = ...): ...
    async def rollback(self): ...
    async def scalar(
        self, statement, params: Incomplete | None = ..., execution_options=..., bind_arguments: Incomplete | None = ..., **kw
    ): ...
    async def scalars(
        self, statement, params: Incomplete | None = ..., execution_options=..., bind_arguments: Incomplete | None = ..., **kw
    ): ...
    async def stream(
        self, statement, params: Incomplete | None = ..., execution_options=..., bind_arguments: Incomplete | None = ..., **kw
    ): ...
    async def stream_scalars(
        self, statement, params: Incomplete | None = ..., execution_options=..., bind_arguments: Incomplete | None = ..., **kw
    ): ...
    @property
    def dirty(self): ...
    @property
    def deleted(self): ...
    @property
    def new(self): ...
    @property
    def is_active(self) -> bool: ...
    @property
    def no_autoflush(self) -> None: ...
    @memoized_property
    def info(self): ...
