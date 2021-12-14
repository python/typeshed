from typing import Any, Generic, NamedTuple, TypeVar

from ..sql import base as sql_base, roles, traversals
from . import interfaces

_T = TypeVar("_T")

class NoKey(str): ...

NO_KEY: Any

class QueryableAttribute(
    interfaces._MappedAttribute,
    interfaces.InspectionAttr,
    interfaces.PropComparator,
    traversals.HasCopyInternals,
    roles.JoinTargetRole,
    roles.OnClauseRole,
    sql_base.Immutable,
    sql_base.MemoizedHasCacheKey,
):
    is_attribute: bool
    __visit_name__: str
    class_: Any
    key: Any
    impl: Any
    comparator: Any
    def __init__(
        self,
        class_,
        key,
        parententity,
        impl: Any | None = ...,
        comparator: Any | None = ...,
        of_type: Any | None = ...,
        extra_criteria=...,
    ) -> None: ...
    def __reduce__(self): ...
    def get_history(self, instance, passive=...): ...
    def info(self): ...
    def parent(self): ...
    def expression(self): ...
    def __clause_element__(self): ...
    def adapt_to_entity(self, adapt_to_entity): ...
    def of_type(self, entity): ...
    def and_(self, *other): ...
    def label(self, name): ...
    def operate(self, op, *other, **kwargs): ...
    def reverse_operate(self, op, other, **kwargs): ...
    def hasparent(self, state, optimistic: bool = ...): ...
    def __getattr__(self, key): ...
    def property(self): ...

class Mapped(QueryableAttribute, Generic[_T]):
    def __get__(self, instance, owner) -> None: ...
    def __set__(self, instance, value) -> None: ...
    def __delete__(self, instance) -> None: ...

class InstrumentedAttribute(Mapped):
    inherit_cache: bool
    def __set__(self, instance, value) -> None: ...
    def __delete__(self, instance) -> None: ...
    def __get__(self, instance, owner): ...

class HasEntityNamespace(NamedTuple):
    entity_namespace: Any

def create_proxied_attribute(descriptor): ...

OP_REMOVE: Any
OP_APPEND: Any
OP_REPLACE: Any
OP_BULK_REPLACE: Any
OP_MODIFIED: Any

class AttributeEvent:
    impl: Any
    op: Any
    parent_token: Any
    def __init__(self, attribute_impl, op) -> None: ...
    def __eq__(self, other): ...
    @property
    def key(self): ...
    def hasparent(self, state): ...

Event = AttributeEvent

class AttributeImpl:
    class_: Any
    key: Any
    callable_: Any
    dispatch: Any
    trackparent: Any
    parent_token: Any
    send_modified_events: Any
    is_equal: Any
    accepts_scalar_loader: Any
    load_on_unexpire: Any
    def __init__(
        self,
        class_,
        key,
        callable_,
        dispatch,
        trackparent: bool = ...,
        compare_function: Any | None = ...,
        active_history: bool = ...,
        parent_token: Any | None = ...,
        load_on_unexpire: bool = ...,
        send_modified_events: bool = ...,
        accepts_scalar_loader: Any | None = ...,
        **kwargs,
    ) -> None: ...
    active_history: Any
    def hasparent(self, state, optimistic: bool = ...): ...
    def sethasparent(self, state, parent_state, value) -> None: ...
    def get_history(self, state, dict_, passive=...) -> None: ...
    def get_all_pending(self, state, dict_, passive=...) -> None: ...
    def get(self, state, dict_, passive=...): ...
    def append(self, state, dict_, value, initiator, passive=...) -> None: ...
    def remove(self, state, dict_, value, initiator, passive=...) -> None: ...
    def pop(self, state, dict_, value, initiator, passive=...) -> None: ...
    def set(self, state, dict_, value, initiator, passive=..., check_old: Any | None = ..., pop: bool = ...) -> None: ...
    def get_committed_value(self, state, dict_, passive=...): ...
    def set_committed_value(self, state, dict_, value): ...

class ScalarAttributeImpl(AttributeImpl):
    default_accepts_scalar_loader: bool
    uses_objects: bool
    supports_population: bool
    collection: bool
    dynamic: bool
    def __init__(self, *arg, **kw) -> None: ...
    def delete(self, state, dict_) -> None: ...
    def get_history(self, state, dict_, passive=...): ...
    def set(self, state, dict_, value, initiator, passive=..., check_old: Any | None = ..., pop: bool = ...) -> None: ...
    def fire_replace_event(self, state, dict_, value, previous, initiator): ...
    def fire_remove_event(self, state, dict_, value, initiator) -> None: ...
    @property
    def type(self) -> None: ...

class ScalarObjectAttributeImpl(ScalarAttributeImpl):
    default_accepts_scalar_loader: bool
    uses_objects: bool
    supports_population: bool
    collection: bool
    def delete(self, state, dict_) -> None: ...
    def get_history(self, state, dict_, passive=...): ...
    def get_all_pending(self, state, dict_, passive=...): ...
    def set(self, state, dict_, value, initiator, passive=..., check_old: Any | None = ..., pop: bool = ...) -> None: ...
    def fire_remove_event(self, state, dict_, value, initiator) -> None: ...
    def fire_replace_event(self, state, dict_, value, previous, initiator): ...

class CollectionAttributeImpl(AttributeImpl):
    default_accepts_scalar_loader: bool
    uses_objects: bool
    supports_population: bool
    collection: bool
    dynamic: bool
    copy: Any
    collection_factory: Any
    def __init__(
        self,
        class_,
        key,
        callable_,
        dispatch,
        typecallable: Any | None = ...,
        trackparent: bool = ...,
        copy_function: Any | None = ...,
        compare_function: Any | None = ...,
        **kwargs,
    ) -> None: ...
    def get_history(self, state, dict_, passive=...): ...
    def get_all_pending(self, state, dict_, passive=...): ...
    def fire_append_event(self, state, dict_, value, initiator): ...
    def fire_append_wo_mutation_event(self, state, dict_, value, initiator): ...
    def fire_pre_remove_event(self, state, dict_, initiator) -> None: ...
    def fire_remove_event(self, state, dict_, value, initiator) -> None: ...
    def delete(self, state, dict_) -> None: ...
    def append(self, state, dict_, value, initiator, passive=...) -> None: ...
    def remove(self, state, dict_, value, initiator, passive=...) -> None: ...
    def pop(self, state, dict_, value, initiator, passive=...) -> None: ...
    def set(
        self,
        state,
        dict_,
        value,
        initiator: Any | None = ...,
        passive=...,
        check_old: Any | None = ...,
        pop: bool = ...,
        _adapt: bool = ...,
    ) -> None: ...
    def set_committed_value(self, state, dict_, value): ...
    def get_collection(self, state, dict_, user_data: Any | None = ..., passive=...): ...

def backref_listeners(attribute, key, uselist): ...

class History:
    def __bool__(self): ...
    __nonzero__: Any
    def empty(self): ...
    def sum(self): ...
    def non_deleted(self): ...
    def non_added(self): ...
    def has_changes(self): ...
    def as_state(self): ...
    @classmethod
    def from_scalar_attribute(cls, attribute, state, current): ...
    @classmethod
    def from_object_attribute(cls, attribute, state, current, original=...): ...
    @classmethod
    def from_collection(cls, attribute, state, current): ...

HISTORY_BLANK: Any

def get_history(obj, key, passive=...): ...
def get_state_history(state, key, passive=...): ...
def has_parent(cls, obj, key, optimistic: bool = ...): ...
def register_attribute(class_, key, **kw): ...
def register_attribute_impl(
    class_,
    key,
    uselist: bool = ...,
    callable_: Any | None = ...,
    useobject: bool = ...,
    impl_class: Any | None = ...,
    backref: Any | None = ...,
    **kw,
): ...
def register_descriptor(class_, key, comparator: Any | None = ..., parententity: Any | None = ..., doc: Any | None = ...): ...
def unregister_attribute(class_, key) -> None: ...
def init_collection(obj, key): ...
def init_state_collection(state, dict_, key): ...
def set_committed_value(instance, key, value) -> None: ...
def set_attribute(instance, key, value, initiator: Any | None = ...) -> None: ...
def get_attribute(instance, key): ...
def del_attribute(instance, key) -> None: ...
def flag_modified(instance, key) -> None: ...
def flag_dirty(instance) -> None: ...
