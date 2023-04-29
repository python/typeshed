from _typeshed import Incomplete, Unused
from collections.abc import Callable, Iterable
from typing import Any, TypeVar
from typing_extensions import Literal

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

_OB = TypeVar("_OB", str, Column, Callable[[], Incomplete])

def create_session(bind: Incomplete | None = None, **kwargs): ...
def with_loader_criteria(
    entity_or_base,
    where_criteria,
    loader_only: Unused = False,
    include_aliases: bool = False,
    propagate_to_loaders: bool = True,
    track_closure_variables: bool = True,
) -> LoaderCriteriaOption: ...
def relationship(
    argument: _OB,
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
    local_table: Incomplete | None = None,
    properties: Incomplete | None = None,
    primary_key: Incomplete | None = None,
    non_primary: bool = False,
    inherits: Incomplete | None = None,
    inherit_condition: Incomplete | None = None,
    inherit_foreign_keys: Incomplete | None = None,
    always_refresh: bool = False,
    version_id_col: Incomplete | None = None,
    version_id_generator: Callable[[int], int] | Literal[False] | None = None,
    polymorphic_on: Incomplete | None = None,
    _polymorphic_map: Incomplete | None = None,
    polymorphic_identity: Incomplete | None = None,
    concrete: bool = False,
    with_polymorphic: Incomplete | None = None,  # noqa: F811  # False positive
    polymorphic_load: Incomplete | None = None,
    allow_partial_pks: bool = True,
    batch: bool = True,
    column_prefix: Incomplete | None = None,
    include_properties: Incomplete | None = None,
    exclude_properties: Incomplete | None = None,
    passive_updates: bool = True,
    passive_deletes: bool = False,
    confirm_deleted_rows: bool = True,
    eager_defaults: bool = False,
    legacy_is_orphan: bool = False,
    _compiled_cache_size: int = 100,
) -> Mapper: ...
def synonym(
    name,
    map_column: Incomplete | None = None,
    descriptor: Incomplete | None = None,
    comparator_factory: Incomplete | None = None,
    doc: Incomplete | None = None,
    info: Incomplete | None = None,
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
