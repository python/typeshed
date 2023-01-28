from _typeshed import Incomplete
from collections.abc import Callable, Iterable
from typing import Any, TypeVar
from typing_extensions import Literal, TypeAlias

from ..orm.mapper import (
    Mapper as Mapper,
    class_mapper as class_mapper,
    configure_mappers as configure_mappers,
    reconstructor as reconstructor,
    validates as validates,
)
from ..sql.schema import Column
from ..util.langhelpers import public_factory as public_factory
from . import exc as exc, strategy_options as strategy_options
from .attributes import (
    AttributeEvent as AttributeEvent,
    InstrumentedAttribute as InstrumentedAttribute,
    Mapped as Mapped,
    QueryableAttribute as QueryableAttribute,
)
from .context import QueryContext as QueryContext
from .decl_api import (
    DeclarativeMeta as DeclarativeMeta,
    as_declarative as as_declarative,
    declarative_base as declarative_base,
    declarative_mixin as declarative_mixin,
    declared_attr as declared_attr,
    has_inherited_table as has_inherited_table,
    registry as registry,
    synonym_for as synonym_for,
)
from .descriptor_props import CompositeProperty as CompositeProperty, SynonymProperty as SynonymProperty
from .dynamic import AppenderQuery as AppenderQuery
from .events import (
    AttributeEvents as AttributeEvents,
    InstanceEvents as InstanceEvents,
    InstrumentationEvents as InstrumentationEvents,
    MapperEvents as MapperEvents,
    QueryEvents as QueryEvents,
    SessionEvents as SessionEvents,
)
from .identity import IdentityMap as IdentityMap
from .instrumentation import ClassManager as ClassManager
from .interfaces import (
    EXT_CONTINUE as EXT_CONTINUE,
    EXT_SKIP as EXT_SKIP,
    EXT_STOP as EXT_STOP,
    MANYTOMANY as MANYTOMANY,
    MANYTOONE as MANYTOONE,
    NOT_EXTENSION as NOT_EXTENSION,
    ONETOMANY as ONETOMANY,
    InspectionAttr as InspectionAttr,
    InspectionAttrInfo as InspectionAttrInfo,
    MapperProperty as MapperProperty,
    PropComparator as PropComparator,
    UserDefinedOption as UserDefinedOption,
)
from .loading import merge_frozen_result as merge_frozen_result, merge_result as merge_result
from .properties import ColumnProperty as ColumnProperty
from .query import AliasOption as AliasOption, FromStatement as FromStatement, Query as Query
from .relationships import RelationshipProperty as RelationshipProperty, foreign as foreign, remote as remote
from .scoping import scoped_session as scoped_session
from .session import (
    ORMExecuteState as ORMExecuteState,
    Session as Session,
    SessionTransaction as SessionTransaction,
    close_all_sessions as close_all_sessions,
    make_transient as make_transient,
    make_transient_to_detached as make_transient_to_detached,
    object_session as object_session,
    sessionmaker as sessionmaker,
)
from .state import AttributeState as AttributeState, InstanceState as InstanceState
from .strategy_options import Load as Load
from .unitofwork import UOWTransaction as UOWTransaction
from .util import (
    Bundle as Bundle,
    CascadeOptions as CascadeOptions,
    LoaderCriteriaOption as LoaderCriteriaOption,
    aliased as aliased,
    join as join,
    object_mapper as object_mapper,
    outerjoin as outerjoin,
    polymorphic_union as polymorphic_union,
    was_deleted as was_deleted,
    with_parent as with_parent,
    with_polymorphic as with_polymorphic,
)

_Unused: TypeAlias = object
_OB = TypeVar("_OB", str, Column, Callable[[], Incomplete])

def create_session(bind: Incomplete | None = ..., **kwargs): ...
def with_loader_criteria(
    entity_or_base,
    where_criteria,
    loader_only: _Unused = ...,
    include_aliases: bool = ...,
    propagate_to_loaders: bool = ...,
    track_closure_variables: bool = ...,
) -> LoaderCriteriaOption: ...
def relationship(
    argument: _OB,
    secondary: Incomplete | None = ...,
    primaryjoin: Incomplete | None = ...,
    secondaryjoin: Incomplete | None = ...,
    foreign_keys: Incomplete | None = ...,
    uselist: Incomplete | None = ...,
    order_by: Iterable[_OB] | _OB | Literal[False] | None = False,
    backref: Incomplete | None = ...,
    back_populates: Incomplete | None = ...,
    overlaps: Incomplete | None = ...,
    post_update: bool = ...,
    cascade: Iterable[str] | str | None | Literal[False] = ...,
    viewonly: bool = ...,
    lazy: str = ...,
    collection_class: Incomplete | None = ...,
    passive_deletes: bool | str = ...,
    passive_updates: bool = ...,
    remote_side: Incomplete | None = ...,
    enable_typechecks: bool = ...,
    join_depth: Incomplete | None = ...,
    comparator_factory: Incomplete | None = ...,
    single_parent: bool = ...,
    innerjoin: bool = ...,
    distinct_target_key: Incomplete | None = ...,
    doc: Incomplete | None = ...,
    active_history: bool = ...,
    cascade_backrefs: bool = ...,
    load_on_pending: bool = ...,
    bake_queries: bool = ...,
    _local_remote_pairs: Incomplete | None = ...,
    query_class: Incomplete | None = ...,
    info: Incomplete | None = ...,
    omit_join: Incomplete | None = ...,
    sync_backref: Incomplete | None = ...,
    _legacy_inactive_history_style: bool = ...,
) -> RelationshipProperty[_OB]: ...
def relation(*arg, **kw): ...
def dynamic_loader(argument, **kw): ...
def column_property(*columns, **kwargs) -> ColumnProperty: ...
def composite(class_, *attrs, **kwargs) -> CompositeProperty: ...
def backref(name, **kwargs): ...
def deferred(*columns, **kw) -> ColumnProperty: ...
def query_expression(default_expr=...) -> ColumnProperty: ...
def mapper(
    class_,
    local_table: Incomplete | None = ...,
    properties: Incomplete | None = ...,
    primary_key: Incomplete | None = ...,
    non_primary: bool = ...,
    inherits: Incomplete | None = ...,
    inherit_condition: Incomplete | None = ...,
    inherit_foreign_keys: Incomplete | None = ...,
    always_refresh: bool = ...,
    version_id_col: Incomplete | None = ...,
    version_id_generator: Callable[[int], int] | Literal[False] | None = ...,
    polymorphic_on: Incomplete | None = ...,
    _polymorphic_map: Incomplete | None = ...,
    polymorphic_identity: Incomplete | None = ...,
    concrete: bool = ...,
    with_polymorphic: Incomplete | None = ...,  # noqa: F811  # False positive
    polymorphic_load: Incomplete | None = ...,
    allow_partial_pks: bool = ...,
    batch: bool = ...,
    column_prefix: Incomplete | None = ...,
    include_properties: Incomplete | None = ...,
    exclude_properties: Incomplete | None = ...,
    passive_updates: bool = ...,
    passive_deletes: bool = ...,
    confirm_deleted_rows: bool = ...,
    eager_defaults: bool = ...,
    legacy_is_orphan: bool = ...,
    _compiled_cache_size: int = ...,
) -> Mapper: ...
def synonym(
    name,
    map_column: Incomplete | None = ...,
    descriptor: Incomplete | None = ...,
    comparator_factory: Incomplete | None = ...,
    doc: Incomplete | None = ...,
    info: Incomplete | None = ...,
) -> SynonymProperty: ...
def clear_mappers() -> None: ...

joinedload: Any
contains_eager: Any
defer: Any
undefer: Any
undefer_group: Any
with_expression: Any
load_only: Any
lazyload: Any
subqueryload: Any
selectinload: Any
immediateload: Any
noload: Any
raiseload: Any
defaultload: Any
selectin_polymorphic: Any

def eagerload(*args, **kwargs): ...
def contains_alias(alias) -> AliasOption: ...
