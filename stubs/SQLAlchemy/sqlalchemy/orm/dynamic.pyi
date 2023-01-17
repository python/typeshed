from _typeshed import Incomplete
from typing import Any, Generic, TypeVar

from . import attributes, strategies
from .query import Query

_T = TypeVar("_T")

class DynaLoader(strategies.AbstractRelationshipLoader):
    logger: Any
    is_class_level: bool
    def init_class_attribute(self, mapper) -> None: ...

class DynamicAttributeImpl(attributes.AttributeImpl):
    uses_objects: bool
    default_accepts_scalar_loader: bool
    supports_population: bool
    collection: bool
    dynamic: bool
    order_by: Any
    target_mapper: Any
    query_class: Any
    def __init__(
        self, class_, key, typecallable, dispatch, target_mapper, order_by, query_class: Incomplete | None = ..., **kw
    ) -> None: ...
    def get(self, state, dict_, passive=...): ...
    def get_collection(self, state, dict_, user_data: Incomplete | None = ..., passive=...): ...
    def fire_append_event(self, state, dict_, value, initiator, collection_history: Incomplete | None = ...) -> None: ...
    def fire_remove_event(self, state, dict_, value, initiator, collection_history: Incomplete | None = ...) -> None: ...
    def set(
        self,
        state,
        dict_,
        value,
        initiator: Incomplete | None = ...,
        passive=...,
        check_old: Incomplete | None = ...,
        pop: bool = ...,
        _adapt: bool = ...,
    ) -> None: ...
    def delete(self, *args, **kwargs) -> None: ...
    def set_committed_value(self, state, dict_, value) -> None: ...
    def get_history(self, state, dict_, passive=...): ...
    def get_all_pending(self, state, dict_, passive=...): ...
    def append(self, state, dict_, value, initiator, passive=...) -> None: ...
    def remove(self, state, dict_, value, initiator, passive=...) -> None: ...
    def pop(self, state, dict_, value, initiator, passive=...) -> None: ...

class DynamicCollectionAdapter:
    data: Any
    def __init__(self, data) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...

class AppenderMixin:
    query_class: Any
    instance: Any
    attr: Any
    def __init__(self, attr, state) -> None: ...
    session: Any
    def __getitem__(self, index): ...
    def count(self): ...
    def extend(self, iterator) -> None: ...
    def append(self, item) -> None: ...
    def remove(self, item) -> None: ...

class AppenderQuery(AppenderMixin, Query[_T], Generic[_T]): ...

def mixin_user_query(cls): ...

class CollectionHistory:
    unchanged_items: Any
    added_items: Any
    deleted_items: Any
    def __init__(self, attr, state, apply_to: Incomplete | None = ...) -> None: ...
    @property
    def added_plus_unchanged(self): ...
    @property
    def all_items(self): ...
    def as_history(self): ...
    def indexed(self, index): ...
    def add_added(self, value) -> None: ...
    def add_removed(self, value) -> None: ...