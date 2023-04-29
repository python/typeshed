from _typeshed import Incomplete
from collections.abc import Callable, Iterable
from typing import Any, ClassVar, Generic, TypeVar, overload, type_check_only
from typing_extensions import Literal

from ..orm.mapper import Mapper
from ..orm.util import CascadeOptions
from ..sql.elements import BinaryExpression
from ..sql.schema import Column
from ..util import memoized_property
from .interfaces import PropComparator, StrategizedProperty

_T = TypeVar("_T")
_OB = TypeVar("_OB", str, Column, Callable[[], Incomplete])

def remote(expr): ...
def foreign(expr): ...

class RelationshipProperty(StrategizedProperty, Generic[_OB]):
    class Comparator(PropComparator[_T], Generic[_T]):
        prop: Any
        def __init__(
            self,
            prop,
            parentmapper,
            adapt_to_entity: Incomplete | None = None,
            of_type: Incomplete | None = None,
            extra_criteria=(),
        ) -> None: ...
        def adapt_to_entity(self, adapt_to_entity): ...
        @memoized_property
        def entity(self): ...
        @memoized_property
        def mapper(self): ...
        def __clause_element__(self): ...
        def of_type(self, cls): ...
        def and_(self, *other): ...
        def in_(self, other) -> BinaryExpression: ...
        __hash__: ClassVar[None]  # type: ignore[assignment]
        def __eq__(self, other): ...
        def any(self, criterion: Incomplete | None = None, **kwargs): ...
        def has(self, criterion: Incomplete | None = None, **kwargs): ...
        def contains(self, other, **kwargs) -> BinaryExpression: ...
        def __ne__(self, other) -> BinaryExpression: ...  # type: ignore[override]
        @memoized_property
        def property(self): ...

    logger: Any
    strategy_wildcard_key: str
    inherit_cache: bool
    uselist: Any
    argument: _OB | Mapper
    secondary: Any
    primaryjoin: Any
    secondaryjoin: Any
    post_update: bool
    direction: Any
    viewonly: bool
    sync_backref: Any
    lazy: Any
    single_parent: bool
    collection_class: Any
    passive_deletes: bool | str
    cascade_backrefs: bool
    passive_updates: bool
    remote_side: Any
    enable_typechecks: bool
    query_class: Any
    innerjoin: bool
    distinct_target_key: Any
    doc: Any
    active_history: bool
    join_depth: Any
    omit_join: Any
    local_remote_pairs: Any
    bake_queries: bool
    load_on_pending: bool
    comparator_factory = Comparator
    comparator: Any
    info: Any
    strategy_key: Any
    order_by: Iterable[_OB] | _OB | Literal[False] | None
    back_populates: Any
    backref: Any
    def __init__(
        self,
        argument: _OB | Mapper,
        secondary: Incomplete | None = None,
        primaryjoin: Incomplete | None = None,
        secondaryjoin: Incomplete | None = None,
        foreign_keys: Incomplete | None = None,
        uselist: Incomplete | None = None,
        order_by: Iterable[_OB] | _OB | Literal[False] | None = False,
        backref: Incomplete | None = None,
        back_populates: Incomplete | None = None,
        overlaps: Incomplete | None = None,
        post_update: bool = False,
        cascade: Iterable[str] | str | None | Literal[False] = False,
        viewonly: bool = False,
        lazy: str = 'select',
        collection_class: Incomplete | None = None,
        passive_deletes: bool | str = False,
        passive_updates: bool = True,
        remote_side: Incomplete | None = None,
        enable_typechecks: bool = True,
        join_depth: Incomplete | None = None,
        comparator_factory: Incomplete | None = None,
        single_parent: bool = False,
        innerjoin: bool = False,
        distinct_target_key: Incomplete | None = None,
        doc: Incomplete | None = None,
        active_history: bool = False,
        cascade_backrefs: bool = True,
        load_on_pending: bool = False,
        bake_queries: bool = True,
        _local_remote_pairs: Incomplete | None = None,
        query_class: Incomplete | None = None,
        info: Incomplete | None = None,
        omit_join: Incomplete | None = None,
        sync_backref: Incomplete | None = None,
        _legacy_inactive_history_style: bool = False,
    ) -> None: ...
    def instrument_class(self, mapper) -> None: ...
    def merge(
        self, session, source_state, source_dict, dest_state, dest_dict, load, _recursive, _resolve_conflict_map
    ) -> None: ...
    def cascade_iterator(self, type_, state, dict_, visited_states, halt_on: Incomplete | None = None) -> None: ...
    @memoized_property
    def entity(self): ...
    @memoized_property
    def mapper(self): ...
    def do_init(self) -> None: ...
    @property
    def cascade(self) -> CascadeOptions: ...
    @cascade.setter
    def cascade(self, cascade: Iterable[str] | str | None) -> None: ...
    # This doesn't exist at runtime, but is present here for better typing.
    @type_check_only
    @overload
    def __get__(self, instance: None, owner) -> RelationshipProperty[Incomplete]: ...  # -> RelationshipProperty[_T_co]
    @type_check_only
    @overload
    def __get__(self, instance: object, owner): ...  # -> _T_co

class JoinCondition:
    parent_persist_selectable: Any
    parent_local_selectable: Any
    child_persist_selectable: Any
    child_local_selectable: Any
    parent_equivalents: Any
    child_equivalents: Any
    primaryjoin: Any
    secondaryjoin: Any
    secondary: Any
    consider_as_foreign_keys: Any
    prop: Any
    self_referential: bool
    support_sync: bool
    can_be_synced_fn: Any
    def __init__(
        self,
        parent_persist_selectable,
        child_persist_selectable,
        parent_local_selectable,
        child_local_selectable,
        primaryjoin: Incomplete | None = None,
        secondary: Incomplete | None = None,
        secondaryjoin: Incomplete | None = None,
        parent_equivalents: Incomplete | None = None,
        child_equivalents: Incomplete | None = None,
        consider_as_foreign_keys: Incomplete | None = None,
        local_remote_pairs: Incomplete | None = None,
        remote_side: Incomplete | None = None,
        self_referential: bool = False,
        prop: Incomplete | None = None,
        support_sync: bool = True,
        can_be_synced_fn=...,
    ): ...
    @property
    def primaryjoin_minus_local(self): ...
    @property
    def secondaryjoin_minus_local(self): ...
    @memoized_property
    def primaryjoin_reverse_remote(self): ...
    @memoized_property
    def remote_columns(self): ...
    @memoized_property
    def local_columns(self): ...
    @memoized_property
    def foreign_key_columns(self): ...
    def join_targets(
        self, source_selectable, dest_selectable, aliased, single_crit: Incomplete | None = None, extra_criteria=()
    ): ...
    def create_lazy_clause(self, reverse_direction: bool = False): ...

class _ColInAnnotations:
    name: Any
    def __init__(self, name) -> None: ...
    def __call__(self, c): ...
