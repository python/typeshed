from typing import Any

from ..engine.util import TransactionalContext
from ..util import memoized_property, MemoizedSlots

class _SessionClassMethods:
    @classmethod
    def close_all(cls) -> None: ...
    @classmethod
    def identity_key(cls, *args, **kwargs): ...
    @classmethod
    def object_session(cls, instance): ...

class ORMExecuteState(MemoizedSlots):
    session: Any
    statement: Any
    parameters: Any
    local_execution_options: Any
    execution_options: Any
    bind_arguments: Any
    def __init__(
        self, session, statement, parameters, execution_options, bind_arguments, compile_state_cls, events_todo
    ) -> None: ...
    def invoke_statement(
        self,
        statement: Any | None = ...,
        params: Any | None = ...,
        execution_options: Any | None = ...,
        bind_arguments: Any | None = ...,
    ): ...
    @property
    def bind_mapper(self): ...
    @property
    def all_mappers(self): ...
    @property
    def is_orm_statement(self): ...
    @property
    def is_select(self): ...
    @property
    def is_insert(self): ...
    @property
    def is_update(self): ...
    @property
    def is_delete(self): ...
    def update_execution_options(self, **opts) -> None: ...
    @property
    def lazy_loaded_from(self): ...
    @property
    def loader_strategy_path(self): ...
    @property
    def is_column_load(self): ...
    @property
    def is_relationship_load(self): ...
    @property
    def load_options(self): ...
    @property
    def update_delete_options(self): ...
    @property
    def user_defined_options(self): ...

class SessionTransaction(TransactionalContext):
    session: Any
    nested: Any
    def __init__(self, session, parent: Any | None = ..., nested: bool = ..., autobegin: bool = ...) -> None: ...
    @property
    def parent(self): ...
    @property
    def is_active(self): ...
    def connection(self, bindkey, execution_options: Any | None = ..., **kwargs): ...
    def prepare(self) -> None: ...
    def commit(self, _to_root: bool = ...): ...
    def rollback(self, _capture_exception: bool = ..., _to_root: bool = ...): ...
    def close(self, invalidate: bool = ...) -> None: ...

class Session(_SessionClassMethods):
    identity_map: Any
    bind: Any
    future: Any
    hash_key: Any
    autoflush: Any
    expire_on_commit: Any
    enable_baked_queries: Any
    autocommit: bool
    twophase: Any
    def __init__(
        self,
        bind: Any | None = ...,
        autoflush: bool = ...,
        future: bool = ...,
        expire_on_commit: bool = ...,
        autocommit: bool = ...,
        twophase: bool = ...,
        binds: Any | None = ...,
        enable_baked_queries: bool = ...,
        info: Any | None = ...,
        query_cls: Any | None = ...,
    ) -> None: ...
    connection_callable: Any
    def __enter__(self): ...
    def __exit__(self, type_, value, traceback) -> None: ...
    @property
    def transaction(self): ...
    def in_transaction(self): ...
    def in_nested_transaction(self): ...
    def get_transaction(self): ...
    def get_nested_transaction(self): ...
    @memoized_property
    def info(self): ...
    def begin(self, subtransactions: bool = ..., nested: bool = ..., _subtrans: bool = ...): ...
    def begin_nested(self): ...
    def rollback(self) -> None: ...
    def commit(self) -> None: ...
    def prepare(self) -> None: ...
    def connection(
        self, bind_arguments: Any | None = ..., close_with_result: bool = ..., execution_options: Any | None = ..., **kw
    ): ...
    def execute(
        self,
        statement,
        params: Any | None = ...,
        execution_options=...,
        bind_arguments: Any | None = ...,
        _parent_execute_state: Any | None = ...,
        _add_event: Any | None = ...,
        **kw,
    ): ...
    def scalar(self, statement, params: Any | None = ..., execution_options=..., bind_arguments: Any | None = ..., **kw): ...
    def scalars(self, statement, params: Any | None = ..., execution_options=..., bind_arguments: Any | None = ..., **kw): ...
    def close(self) -> None: ...
    def invalidate(self) -> None: ...
    def expunge_all(self) -> None: ...
    def bind_mapper(self, mapper, bind) -> None: ...
    def bind_table(self, table, bind) -> None: ...
    def get_bind(
        self,
        mapper: Any | None = ...,
        clause: Any | None = ...,
        bind: Any | None = ...,
        _sa_skip_events: Any | None = ...,
        _sa_skip_for_implicit_returning: bool = ...,
    ): ...
    def query(self, *entities, **kwargs): ...
    @property
    def no_autoflush(self) -> None: ...
    def refresh(self, instance, attribute_names: Any | None = ..., with_for_update: Any | None = ...) -> None: ...
    def expire_all(self) -> None: ...
    def expire(self, instance, attribute_names: Any | None = ...) -> None: ...
    def expunge(self, instance) -> None: ...
    def add(self, instance, _warn: bool = ...) -> None: ...
    def add_all(self, instances) -> None: ...
    def delete(self, instance) -> None: ...
    def get(
        self,
        entity,
        ident,
        options: Any | None = ...,
        populate_existing: bool = ...,
        with_for_update: Any | None = ...,
        identity_token: Any | None = ...,
    ): ...
    def merge(self, instance, load: bool = ..., options: Any | None = ...): ...
    def enable_relationship_loading(self, obj) -> None: ...
    def __contains__(self, instance): ...
    def __iter__(self): ...
    def flush(self, objects: Any | None = ...) -> None: ...
    def bulk_save_objects(
        self, objects, return_defaults: bool = ..., update_changed_only: bool = ..., preserve_order: bool = ...
    ): ...
    def bulk_insert_mappings(self, mapper, mappings, return_defaults: bool = ..., render_nulls: bool = ...) -> None: ...
    def bulk_update_mappings(self, mapper, mappings) -> None: ...
    def is_modified(self, instance, include_collections: bool = ...): ...
    @property
    def is_active(self): ...
    @property
    def dirty(self): ...
    @property
    def deleted(self): ...
    @property
    def new(self): ...

class sessionmaker(_SessionClassMethods):
    kw: Any
    class_: Any
    def __init__(
        self,
        bind: Any | None = ...,
        class_=...,
        autoflush: bool = ...,
        autocommit: bool = ...,
        expire_on_commit: bool = ...,
        info: Any | None = ...,
        **kw,
    ) -> None: ...
    def begin(self): ...
    def __call__(self, **local_kw): ...
    def configure(self, **new_kw) -> None: ...

def close_all_sessions() -> None: ...
def make_transient(instance) -> None: ...
def make_transient_to_detached(instance) -> None: ...
def object_session(instance): ...
