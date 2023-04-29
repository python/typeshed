from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any, Generic, NamedTuple, TypeVar
from typing_extensions import ParamSpec

from ..sql import base as sql_base, roles, traversals
from ..util import memoized_property
from . import interfaces
from .base import (
    ATTR_EMPTY as ATTR_EMPTY,
    ATTR_WAS_SET as ATTR_WAS_SET,
    CALLABLES_OK as CALLABLES_OK,
    DEFERRED_HISTORY_LOAD as DEFERRED_HISTORY_LOAD,
    INIT_OK as INIT_OK,
    LOAD_AGAINST_COMMITTED as LOAD_AGAINST_COMMITTED,
    NEVER_SET as NEVER_SET,
    NO_AUTOFLUSH as NO_AUTOFLUSH,
    NO_CHANGE as NO_CHANGE,
    NO_RAISE as NO_RAISE,
    NO_VALUE as NO_VALUE,
    NON_PERSISTENT_OK as NON_PERSISTENT_OK,
    PASSIVE_CLASS_MISMATCH as PASSIVE_CLASS_MISMATCH,
    PASSIVE_NO_FETCH as PASSIVE_NO_FETCH,
    PASSIVE_NO_FETCH_RELATED as PASSIVE_NO_FETCH_RELATED,
    PASSIVE_NO_INITIALIZE as PASSIVE_NO_INITIALIZE,
    PASSIVE_NO_RESULT as PASSIVE_NO_RESULT,
    PASSIVE_OFF as PASSIVE_OFF,
    PASSIVE_ONLY_PERSISTENT as PASSIVE_ONLY_PERSISTENT,
    PASSIVE_RETURN_NO_VALUE as PASSIVE_RETURN_NO_VALUE,
    RELATED_OBJECT_OK as RELATED_OBJECT_OK,
    SQL_OK as SQL_OK,
)

_T = TypeVar("_T")
_P = ParamSpec("_P")

class NoKey(str): ...

NO_KEY: Any

class QueryableAttribute(
    interfaces._MappedAttribute,
    interfaces.InspectionAttr,
    interfaces.PropComparator[Any],
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
        impl: Incomplete | None = None,
        comparator: Incomplete | None = None,
        of_type: Incomplete | None = None,
        extra_criteria=(),
    ) -> None: ...
    def __reduce__(self): ...
    def get_history(self, instance, passive=...): ...
    @memoized_property
    def info(self): ...
    @memoized_property
    def parent(self): ...
    @memoized_property
    def expression(self): ...
    def __clause_element__(self): ...
    def adapt_to_entity(self, adapt_to_entity): ...
    def of_type(self, entity): ...
    def and_(self, *other): ...
    def label(self, name): ...
    def operate(self, op: Callable[_P, _T], *other: _P.args, **kwargs: _P.kwargs) -> _T: ...
    def reverse_operate(self, op: Callable[..., _T], other, **kwargs) -> _T: ...
    def hasparent(self, state, optimistic: bool = False): ...
    def __getattr__(self, key: str): ...
    @memoized_property
    def property(self): ...

class Mapped(QueryableAttribute, Generic[_T]):
    def __get__(self, instance, owner) -> None: ...
    def __set__(self, instance, value) -> None: ...
    def __delete__(self, instance) -> None: ...

class InstrumentedAttribute(Mapped[Any]):
    inherit_cache: bool
    def __set__(self, instance, value) -> None: ...
    def __delete__(self, instance) -> None: ...
    def __get__(self, instance, owner): ...

class _HasEntityNamespace(NamedTuple):
    entity_namespace: Any

class HasEntityNamespace(_HasEntityNamespace):
    is_mapper: bool
    is_aliased_class: bool

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
    def __eq__(self, other) -> bool: ...
    @property
    def key(self): ...
    def hasparent(self, state): ...

Event = AttributeEvent

class AttributeImpl:
    class_: Any
    key: Any
    callable_: Any
    dispatch: Any
    trackparent: bool
    parent_token: Any
    send_modified_events: Any
    is_equal: Any
    accepts_scalar_loader: bool
    load_on_unexpire: Any
    def __init__(
        self,
        class_,
        key,
        callable_,
        dispatch,
        trackparent: bool = False,
        compare_function: Incomplete | None = None,
        active_history: bool = False,
        parent_token: Incomplete | None = None,
        load_on_unexpire: bool = True,
        send_modified_events: bool = True,
        accepts_scalar_loader: bool | None = None,
        **kwargs,
    ) -> None: ...
    @property
    def active_history(self) -> bool: ...
    @active_history.setter
    def active_history(self, value: bool) -> None: ...
    def hasparent(self, state, optimistic: bool = False): ...
    def sethasparent(self, state, parent_state, value) -> None: ...
    def get_history(self, state, dict_, passive=...) -> None: ...
    def get_all_pending(self, state, dict_, passive=...) -> None: ...
    def get(self, state, dict_, passive=...): ...
    def append(self, state, dict_, value, initiator, passive=...) -> None: ...
    def remove(self, state, dict_, value, initiator, passive=...) -> None: ...
    def pop(self, state, dict_, value, initiator, passive=...) -> None: ...
    def set(
        self, state, dict_, value, initiator, passive=..., check_old: Incomplete | None = None, pop: bool = False
    ) -> None: ...
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
    def set(
        self, state, dict_, value, initiator, passive=..., check_old: Incomplete | None = None, pop: bool = False
    ) -> None: ...
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
    def set(
        self, state, dict_, value, initiator, passive=..., check_old: Incomplete | None = None, pop: bool = False
    ) -> None: ...
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
        typecallable: Incomplete | None = None,
        trackparent: bool = False,
        copy_function: Incomplete | None = None,
        compare_function: Incomplete | None = None,
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
        initiator: Incomplete | None = None,
        passive=...,
        check_old: Incomplete | None = None,
        pop: bool = False,
        _adapt: bool = True,
    ) -> None: ...
    def set_committed_value(self, state, dict_, value): ...
    def get_collection(self, state, dict_, user_data: Incomplete | None = None, passive=...): ...

def backref_listeners(attribute, key, uselist): ...

class _History(NamedTuple):
    added: Incomplete
    unchanged: Incomplete
    deleted: Incomplete

class History(_History):
    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...
    def empty(self): ...
    def sum(self): ...
    def non_deleted(self): ...
    def non_added(self): ...
    def has_changes(self) -> bool: ...
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
def has_parent(cls, obj, key, optimistic: bool = False): ...
def register_attribute(class_, key, **kw): ...
def register_attribute_impl(
    class_,
    key,
    uselist: bool = False,
    callable_: Incomplete | None = None,
    useobject: bool = False,
    impl_class: Incomplete | None = None,
    backref: Incomplete | None = None,
    **kw,
): ...
def register_descriptor(
    class_, key, comparator: Incomplete | None = None, parententity: Incomplete | None = None, doc: Incomplete | None = None
): ...
def unregister_attribute(class_, key) -> None: ...
def init_collection(obj, key): ...
def init_state_collection(state, dict_, key): ...
def set_committed_value(instance, key, value) -> None: ...
def set_attribute(instance, key, value, initiator: Incomplete | None = None) -> None: ...
def get_attribute(instance, key): ...
def del_attribute(instance, key) -> None: ...
def flag_modified(instance, key) -> None: ...
def flag_dirty(instance) -> None: ...
