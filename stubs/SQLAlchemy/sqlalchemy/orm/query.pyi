from _typeshed import Incomplete
from collections.abc import Iterator
from typing import Any, Generic, TypeVar
from typing_extensions import Literal, Self, TypeAlias

from ..orm.session import Session
from ..sql.annotation import SupportsCloneAnnotations
from ..sql.base import Executable
from ..sql.elements import Label
from ..sql.selectable import CTE, GroupedElement, HasHints, HasPrefixes, HasSuffixes, SelectBase, Subquery, _SelectFromElements
from . import interfaces
from .context import QueryContext as QueryContext
from .util import aliased as aliased

__all__ = ["Query", "QueryContext", "aliased"]

_T = TypeVar("_T")
_SynchronizeSessionArgument: TypeAlias = Literal[False, "evaluate", "fetch"]

class Query(_SelectFromElements, SupportsCloneAnnotations, HasPrefixes, HasSuffixes, HasHints, Executable, Generic[_T]):
    logger: Any
    load_options: Any
    session: Session | None
    dispatch: Incomplete
    def __init__(self, entities, session: Session | None = None) -> None: ...
    @property
    def statement(self): ...
    def subquery(self, name: str | None = None, with_labels: bool = False, reduce_columns: bool = False) -> Subquery: ...
    def cte(self, name: str | None = None, recursive: bool = False, nesting: bool = False) -> CTE: ...
    def label(self, name: str) -> Label: ...
    def as_scalar(self): ...
    def scalar_subquery(self): ...
    @property
    def selectable(self): ...
    def __clause_element__(self): ...
    def only_return_tuples(self, value) -> Self: ...
    @property
    def is_single_entity(self) -> bool: ...
    def enable_eagerloads(self, value: bool) -> Self: ...
    def with_labels(self) -> Self: ...
    apply_labels: Any
    @property
    def get_label_style(self): ...
    def set_label_style(self, style) -> Self: ...
    def enable_assertions(self, value: bool) -> Self: ...
    @property
    def whereclause(self): ...
    def with_polymorphic(
        self, cls_or_mappers, selectable: Incomplete | None = None, polymorphic_on: Incomplete | None = None
    ) -> Self: ...
    def yield_per(self, count: int) -> Self: ...
    def get(self, ident) -> _T | None: ...
    @property
    def lazy_loaded_from(self): ...
    def correlate(self, *fromclauses) -> Self: ...
    def autoflush(self, setting: bool) -> Self: ...
    def populate_existing(self) -> Self: ...
    def with_parent(self, instance, property: Incomplete | None = None, from_entity: Incomplete | None = None): ...
    def add_entity(self, entity, alias: Incomplete | None = None) -> Self: ...
    def with_session(self, session: Session | None) -> Self: ...
    def from_self(self, *entities): ...
    def values(self, *columns): ...
    def value(self, column): ...
    def with_entities(self, *entities) -> Self: ...
    def add_columns(self, *column) -> Self: ...
    def add_column(self, column): ...
    def options(self, *args) -> Self: ...
    def with_transformation(self, fn): ...
    def get_execution_options(self): ...
    def execution_options(self, **kwargs) -> Self: ...
    def with_for_update(
        self,
        read: bool = False,
        nowait: bool = False,
        of: Incomplete | None = None,
        skip_locked: bool = False,
        key_share: bool = False,
    ) -> Self: ...
    def params(self, *args, **kwargs) -> Self: ...
    def where(self, *criterion): ...
    def filter(self, *criterion) -> Self: ...
    def filter_by(self, **kwargs) -> Self: ...
    def order_by(self, *clauses) -> Self: ...
    def group_by(self, *clauses) -> Self: ...
    def having(self, criterion) -> Self: ...
    def union(self, *q): ...
    def union_all(self, *q): ...
    def intersect(self, *q): ...
    def intersect_all(self, *q): ...
    def except_(self, *q): ...
    def except_all(self, *q): ...
    def join(self, target, *props, **kwargs) -> Self: ...
    def outerjoin(self, target, *props, **kwargs) -> Self: ...
    def reset_joinpoint(self) -> Self: ...
    def select_from(self, *from_obj) -> Self: ...
    def select_entity_from(self, from_obj) -> Self: ...
    def __getitem__(self, item): ...
    def slice(self, start: int | None, stop: int | None) -> Self: ...
    def limit(self, limit: int | None) -> Self: ...
    def offset(self, offset: int | None) -> Self: ...
    def distinct(self, *expr) -> Self: ...
    def all(self) -> list[_T]: ...
    def from_statement(self, statement) -> Self: ...
    def first(self) -> _T | None: ...
    def one_or_none(self) -> _T | None: ...
    def one(self) -> _T: ...
    def scalar(self) -> Any: ...  # type: ignore[override]
    def __iter__(self) -> Iterator[_T]: ...
    @property
    def column_descriptions(self): ...
    def instances(self, result_proxy, context: Incomplete | None = None): ...
    def merge_result(self, iterator, load: bool = True): ...
    def exists(self): ...
    def count(self) -> int: ...
    def delete(self, synchronize_session: _SynchronizeSessionArgument = "evaluate") -> int: ...
    def update(
        self, values, synchronize_session: _SynchronizeSessionArgument = "evaluate", update_args: Incomplete | None = None
    ): ...

class FromStatement(GroupedElement, SelectBase, Executable):
    __visit_name__: str
    element: Any
    def __init__(self, entities, element) -> None: ...
    def get_label_style(self): ...
    def set_label_style(self, label_style): ...
    def get_children(self, **kw) -> None: ...  # type: ignore[override]

class AliasOption(interfaces.LoaderOption):
    def __init__(self, alias) -> None: ...
    inherit_cache: bool
    def process_compile_state(self, compile_state) -> None: ...

class BulkUD:
    query: Any
    mapper: Any
    def __init__(self, query) -> None: ...
    @property
    def session(self): ...

class BulkUpdate(BulkUD):
    values: Any
    update_kwargs: Any
    def __init__(self, query, values, update_kwargs) -> None: ...

class BulkDelete(BulkUD): ...
