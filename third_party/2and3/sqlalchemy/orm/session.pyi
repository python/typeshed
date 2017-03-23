# Stubs for sqlalchemy.orm.session (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .. import exc as sa_exc
from ..sql import util as sql_util
from . import state as statelib

class _SessionClassMethods:
    @classmethod
    def close_all(cls): ...
    @classmethod
    def identity_key(cls, orm_util, *args, **kwargs): ...
    @classmethod
    def object_session(cls, instance): ...

class SessionTransaction:
    session = ...  # type: Any
    nested = ...  # type: Any
    def __init__(self, session, parent: Optional[Any] = ..., nested: bool = ...) -> None: ...
    @property
    def parent(self): ...
    @property
    def is_active(self): ...
    def connection(self, bindkey, execution_options: Optional[Any] = ..., **kwargs): ...
    def prepare(self): ...
    def commit(self): ...
    def rollback(self, _capture_exception: bool = ...): ...
    def close(self, invalidate: bool = ...): ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback): ...

class Session(_SessionClassMethods):
    public_methods = ...  # type: Any
    identity_map = ...  # type: Any
    bind = ...  # type: Any
    transaction = ...  # type: Any
    hash_key = ...  # type: Any
    autoflush = ...  # type: Any
    autocommit = ...  # type: Any
    expire_on_commit = ...  # type: Any
    twophase = ...  # type: Any
    def __init__(self, bind: Optional[Any] = ..., autoflush: bool = ..., expire_on_commit: bool = ..., _enable_transaction_accounting: bool = ..., autocommit: bool = ..., twophase: bool = ..., weak_identity_map: bool = ..., binds: Optional[Any] = ..., extension: Optional[Any] = ..., info: Optional[Any] = ..., query_cls: Any = ...) -> None: ...
    connection_callable = ...  # type: Any
    def info(self): ...
    def begin(self, subtransactions: bool = ..., nested: bool = ...): ...
    def begin_nested(self): ...
    def rollback(self): ...
    def commit(self): ...
    def prepare(self): ...
    def connection(self, mapper: Optional[Any] = ..., clause: Optional[Any] = ..., bind: Optional[Any] = ..., close_with_result: bool = ..., execution_options: Optional[Any] = ..., **kw): ...
    def execute(self, clause, params: Optional[Any] = ..., mapper: Optional[Any] = ..., bind: Optional[Any] = ..., **kw): ...
    def scalar(self, clause, params: Optional[Any] = ..., mapper: Optional[Any] = ..., bind: Optional[Any] = ..., **kw): ...
    def close(self): ...
    def invalidate(self): ...
    def expunge_all(self): ...
    def bind_mapper(self, mapper, bind): ...
    def bind_table(self, table, bind): ...
    def get_bind(self, mapper: Optional[Any] = ..., clause: Optional[Any] = ...): ...
    def query(self, *entities, **kwargs): ...
    @property
    def no_autoflush(self): ...
    def refresh(self, instance, attribute_names: Optional[Any] = ..., lockmode: Optional[Any] = ...): ...
    def expire_all(self): ...
    def expire(self, instance, attribute_names: Optional[Any] = ...): ...
    def prune(self): ...
    def expunge(self, instance): ...
    def add(self, instance, _warn: bool = ...): ...
    def add_all(self, instances): ...
    def delete(self, instance): ...
    def merge(self, instance, load: bool = ...): ...
    def enable_relationship_loading(self, obj): ...
    def __contains__(self, instance): ...
    def __iter__(self): ...
    def flush(self, objects: Optional[Any] = ...): ...
    def bulk_save_objects(self, objects, return_defaults: bool = ..., update_changed_only: bool = ...): ...
    def bulk_insert_mappings(self, mapper, mappings, return_defaults: bool = ..., render_nulls: bool = ...): ...
    def bulk_update_mappings(self, mapper, mappings): ...
    def is_modified(self, instance, include_collections: bool = ..., passive: bool = ...): ...
    @property
    def is_active(self): ...
    @property
    def dirty(self): ...
    @property
    def deleted(self): ...
    @property
    def new(self): ...

class sessionmaker(_SessionClassMethods):
    kw = ...  # type: Any
    class_ = ...  # type: Any
    def __init__(self, bind: Optional[Any] = ..., class_: Any = ..., autoflush: bool = ..., autocommit: bool = ..., expire_on_commit: bool = ..., info: Optional[Any] = ..., **kw) -> None: ...
    def __call__(self, **local_kw): ...
    def configure(self, **new_kw): ...

# Names in __all__ with no definition:
#   SessionExtension
