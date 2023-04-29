from _typeshed import Incomplete, Unused
from collections.abc import Callable, Iterator, Mapping, Sequence as ABCSequence
from threading import local
from typing import Any, NoReturn, overload
from typing_extensions import Self

from ..engine import Connection, Engine
from ..engine.interfaces import Connectable
from ..engine.url import URL
from ..sql import functions
from ..sql.coercions import _CoercibleElement
from ..sql.compiler import DDLCompiler
from ..sql.type_api import TypeEngine
from ..util import FacadeDict, immutabledict, memoized_property
from ..util.langhelpers import _symbol, symbol
from . import visitors
from .base import ColumnCollection, DialectKWArgs, Executable, SchemaEventTarget
from .elements import ClauseElement, ColumnClause, quoted_name
from .selectable import TableClause

RETAIN_SCHEMA: Any
BLANK_SCHEMA: Any
NULL_UNSPECIFIED: Any

class SchemaItem(SchemaEventTarget, visitors.Traversible):
    __visit_name__: str
    create_drop_stringify_dialect: str
    @memoized_property
    def info(self) -> Mapping[str, Incomplete]: ...

class Table(DialectKWArgs, SchemaItem, TableClause):
    __visit_name__: str
    constraints: set[Constraint]
    indexes: set[Index]
    def __new__(cls, *args, **kw): ...
    def __init__(self, *args: Unused, **kw: Unused) -> None: ...
    @property
    def foreign_key_constraints(self) -> set[ForeignKeyConstraint]: ...
    @property
    def key(self) -> str: ...
    @property
    def bind(self) -> Engine | Connection | None: ...
    def add_is_dependent_on(self, table: Table) -> None: ...
    def append_column(self, column: ColumnClause, replace_existing: bool = False) -> None: ...  # type: ignore[override]
    def append_constraint(self, constraint: Constraint) -> None: ...
    def exists(self, bind: Engine | Connection | None = None): ...
    def create(self, bind: Connectable | None = None, checkfirst: bool = False) -> None: ...
    def drop(self, bind: Connectable | None = None, checkfirst: bool = False) -> None: ...
    def to_metadata(
        self,
        metadata: MetaData,
        schema: str | _symbol | symbol = ...,
        referred_schema_fn: Callable[[Table, str, ForeignKeyConstraint, str], str] | None = None,
        name: str | None = None,
    ) -> Table: ...
    tometadata = to_metadata

class Column(DialectKWArgs, SchemaItem, ColumnClause):
    __visit_name__: str
    inherit_cache: bool
    key: str | quoted_name
    primary_key: bool
    nullable: bool
    default: Incomplete | None
    server_default: Incomplete | None
    server_onupdate: FetchedValue | str | ClauseElement | None
    index: int | None
    unique: bool | None
    system: bool
    doc: str | None
    onupdate: ColumnDefault | Sequence | Incomplete | None
    autoincrement: bool | str
    constraints: set[Constraint]
    foreign_keys: set[ForeignKey]  # type: ignore[assignment]  # supertype is list
    comment: str | None
    computed: Incomplete | None
    identity: Incomplete | None
    @memoized_property
    def info(self) -> Mapping[str, Any]: ...
    # FIXME: Only specifying TraversibleType in __init__ to work around a mypy bug!
    # example from pandas.tests.io.tests_sql:
    # ```python
    # date_type = TEXT if dialect == "sqlite" else DateTime
    # bool_type = Integer if dialect == "sqlite" else Boolean
    # Column("DateCol", date_type)
    # ```
    # mypy thinks date_type is TraversibleType instead of Union[type[TEXT], type[DateTime]]
    #
    # If quote in kwargs, then name must not be None
    @overload
    def __init__(
        self,
        name: str,
        type_: TypeEngine | type[TypeEngine] | None | visitors.TraversibleType,
        *args,
        quote: bool | None,
        key: str = ...,
        primary_key: bool = False,
        nullable: bool | _symbol | symbol = ...,
        default=None,
        server_default=None,
        server_onupdate: FetchedValue | str | ClauseElement | None = None,
        index: int | None = None,
        unique: bool | None = None,
        system: bool = False,
        doc: str | None = None,
        onupdate: ColumnDefault | Sequence | Incomplete | None = None,
        autoincrement: bool | str = "auto",
        comment: str | None = None,
        _proxies=...,
        info: Mapping[str, Any] = ...,
        **kwargs,
    ) -> None: ...
    @overload
    def __init__(
        self,
        name: str | None,
        type_: TypeEngine | type[TypeEngine] | None | visitors.TraversibleType,
        *args,
        key: str = ...,
        primary_key: bool = False,
        nullable: bool | _symbol | symbol = ...,
        default=None,
        server_default=None,
        server_onupdate: FetchedValue | str | ClauseElement | None = None,
        index: int | None = None,
        unique: bool | None = None,
        system: bool = False,
        doc: str | None = None,
        onupdate: ColumnDefault | Sequence | Incomplete | None = None,
        autoincrement: bool | str = "auto",
        comment: str | None = None,
        _proxies=...,
        info: Mapping[str, Any] = ...,
        **kwargs,
    ) -> None: ...
    # Name arg is optional
    @overload
    def __init__(
        self,
        type_: TypeEngine | type[TypeEngine] | None | visitors.TraversibleType,
        *args,
        key: str = ...,
        primary_key: bool = False,
        nullable: bool | _symbol | symbol = ...,
        default=None,
        server_default=None,
        server_onupdate: FetchedValue | str | ClauseElement | None = None,
        index: int | None = None,
        unique: bool | None = None,
        system: bool = False,
        doc: str | None = None,
        onupdate: ColumnDefault | Sequence | Incomplete | None = None,
        autoincrement: bool | str = "auto",
        comment: str | None = None,
        _proxies=...,
        info: Mapping[str, Any] = ...,
        **kwargs,
    ) -> None: ...
    def references(self, column: Column) -> bool: ...
    def append_foreign_key(self, fk: ForeignKey) -> None: ...
    def copy(self, **kw) -> Self: ...

class ForeignKey(DialectKWArgs, SchemaItem):
    __visit_name__: str
    constraint: ForeignKeyConstraint | None
    parent: Incomplete | None
    use_alter: bool
    name: str | None
    onupdate: str | None
    ondelete: str | None
    deferrable: bool | None
    initially: str | None
    link_to_name: bool
    match: str | None
    @memoized_property
    def info(self) -> Mapping[str, Incomplete]: ...
    def __init__(
        self,
        column: Column | str,
        _constraint: ForeignKeyConstraint | None = None,
        use_alter: bool = False,
        name: str | None = None,
        onupdate: str | None = None,
        ondelete: str | None = None,
        deferrable: bool | None = None,
        initially: str | None = None,
        link_to_name: bool = False,
        match: str | None = None,
        info: Mapping[str, Incomplete] | None = None,
        _unresolvable: bool = False,
        **dialect_kw,
    ) -> None: ...
    def copy(self, schema: str | _symbol | symbol | None = None, **kw: Unused) -> ForeignKey: ...
    @property
    def target_fullname(self) -> str: ...
    def references(self, table: Table) -> bool: ...
    def get_referent(self, table: Table) -> Column: ...
    @memoized_property
    def column(self) -> Column: ...

class DefaultGenerator(Executable, SchemaItem):
    __visit_name__: str
    is_sequence: bool
    is_server_default: bool
    column: Any
    for_update: Any
    def __init__(self, for_update: bool = False) -> None: ...
    def execute(self, bind: Incomplete | None = None): ...  # type: ignore[override]
    @property
    def bind(self): ...

class ColumnDefault(DefaultGenerator):
    arg: Any
    def __init__(self, arg, **kwargs) -> None: ...
    @memoized_property
    def is_callable(self) -> bool: ...
    @memoized_property
    def is_clause_element(self) -> bool: ...
    @memoized_property
    def is_scalar(self) -> bool: ...

class IdentityOptions:
    start: Any
    increment: Any
    minvalue: Any
    maxvalue: Any
    nominvalue: Any
    nomaxvalue: Any
    cycle: Any
    cache: Any
    order: Any
    def __init__(
        self,
        start: Incomplete | None = None,
        increment: Incomplete | None = None,
        minvalue: Incomplete | None = None,
        maxvalue: Incomplete | None = None,
        nominvalue: Incomplete | None = None,
        nomaxvalue: Incomplete | None = None,
        cycle: Incomplete | None = None,
        cache: Incomplete | None = None,
        order: Incomplete | None = None,
    ) -> None: ...

class Sequence(IdentityOptions, DefaultGenerator):
    __visit_name__: str
    is_sequence: bool
    name: quoted_name
    optional: bool
    schema: str | quoted_name
    metadata: MetaData | None
    data_type: TypeEngine | None
    def __init__(
        self,
        name: str,
        start: int | None = None,
        increment: int | None = None,
        minvalue: int | None = None,
        maxvalue: int | None = None,
        nominvalue: int | None = None,
        nomaxvalue: int | None = None,
        cycle: bool | None = None,
        schema: str | _symbol | symbol | None = None,
        cache: Incomplete | None = None,
        order: Incomplete | None = None,
        data_type: TypeEngine | type[TypeEngine] | None = None,
        optional: bool = False,
        quote: bool | None = None,
        metadata: MetaData | None = None,
        quote_schema: bool | None = None,
        for_update: bool = False,
    ) -> None: ...
    @memoized_property
    def is_callable(self) -> bool: ...
    @memoized_property
    def is_clause_element(self) -> bool: ...
    def next_value(self) -> functions.next_value: ...
    @property
    def bind(self) -> Engine | Connection | None: ...
    def create(self, bind: Engine | Connection | None = None, checkfirst: bool = True) -> None: ...
    def drop(self, bind: Engine | Connection | None = None, checkfirst: bool = True) -> None: ...

class FetchedValue(SchemaEventTarget):
    is_server_default: bool
    reflected: bool
    has_argument: bool
    is_clause_element: bool
    for_update: bool
    def __init__(self, for_update: bool = False) -> None: ...

class DefaultClause(FetchedValue):
    has_argument: bool
    arg: Any
    reflected: bool
    def __init__(self, arg: str | ClauseElement, for_update: bool = False, _reflected: bool = False) -> None: ...

class Constraint(DialectKWArgs, SchemaItem):
    __visit_name__: str
    name: str | None
    deferrable: bool | None
    initially: str | None
    @memoized_property
    def info(self) -> Mapping[str, Incomplete] | None: ...  # type: ignore[override]  # @memoized_property causes override issue
    def __init__(
        self,
        name: str | None = None,
        deferrable: bool | None = None,
        initially: str | None = None,
        _create_rule: Callable[[DDLCompiler], bool] | None = None,
        info: Mapping[str, Incomplete] | None = None,
        _type_bound: bool = False,
        **dialect_kw,
    ) -> None: ...
    @property
    def table(self) -> Table: ...
    # Deprecated
    def copy(self, **kw: Unused) -> NoReturn: ...

class ColumnCollectionMixin:
    columns: ColumnCollection
    def __init__(self, *columns: str | Column, **kw) -> None: ...

class ColumnCollectionConstraint(ColumnCollectionMixin, Constraint):
    def __init__(self, *columns: str | Column, **kw) -> None: ...
    def __contains__(self, x) -> bool: ...
    def copy(self, target_table: Incomplete | None = None, **kw: Unused) -> Self: ...  # type: ignore[override]
    def contains_column(self, col: Column) -> bool: ...
    def __iter__(self) -> Iterator[Column]: ...
    def __len__(self) -> int: ...

class CheckConstraint(ColumnCollectionConstraint):
    __visit_name__: str
    sqltext: Any
    def __init__(
        self,
        sqltext: _CoercibleElement,
        name: str | None = None,
        deferrable: bool | None = None,
        initially: str | None = None,
        table: Table | None = None,
        info: Mapping[str, Incomplete] | None = None,
        _create_rule: Callable[[DDLCompiler], bool] | None = None,
        _autoattach: bool = True,
        _type_bound: bool = False,
        **kw,
    ) -> None: ...
    @property
    def is_column_level(self) -> bool: ...
    def copy(self, target_table: Table | None = None, **kw: Unused) -> CheckConstraint: ...  # type: ignore[override]

class ForeignKeyConstraint(ColumnCollectionConstraint):
    __visit_name__: str
    onupdate: str | None
    ondelete: str | None
    link_to_name: bool
    use_alter: bool
    match: str | None
    elements: list[ForeignKey]
    def __init__(
        self,
        columns: ABCSequence[str],
        refcolumns: ABCSequence[str | Column],
        name: str | None = None,
        onupdate: str | None = None,
        ondelete: str | None = None,
        deferrable: bool | None = None,
        initially: str | None = None,
        use_alter: bool = False,
        link_to_name: bool = False,
        match: str | None = None,
        table: Table | None = None,
        info: Mapping[str, Incomplete] | None = None,
        **dialect_kw,
    ) -> None: ...
    columns: Any
    @property
    def referred_table(self) -> Table: ...
    @property
    def column_keys(self) -> list[str]: ...
    def copy(self, schema: str | None = None, target_table: Table | None = None, **kw: Unused) -> ForeignKeyConstraint: ...  # type: ignore[override]

class PrimaryKeyConstraint(ColumnCollectionConstraint):
    __visit_name__: str
    def __init__(self, *columns, **kw) -> None: ...
    @property
    def columns_autoinc_first(self) -> list[Column]: ...

class UniqueConstraint(ColumnCollectionConstraint):
    __visit_name__: str

class Index(DialectKWArgs, ColumnCollectionMixin, SchemaItem):
    __visit_name__: str
    table: Table | None
    name: quoted_name
    unique: bool
    @memoized_property
    def info(self) -> Mapping[str, Incomplete] | None: ...  # type: ignore[override]  # @memoized_property causes override issue
    expressions: list[Incomplete]
    def __init__(
        self,
        name: str,
        *expressions,
        quote: bool | None = None,
        unique: bool = False,
        _column_flag: bool = False,
        info: Mapping[str, Incomplete] | None = ...,
        _table=...,
        **kw,
    ) -> None: ...
    @property
    def bind(self) -> Engine | Connection | None: ...
    def create(self, bind: Engine | Connection | None = None, checkfirst: bool = False) -> Self: ...
    def drop(self, bind: Engine | Connection | None = None, checkfirst: bool = False) -> None: ...

DEFAULT_NAMING_CONVENTION: immutabledict[str, str]

class MetaData(SchemaItem):
    __visit_name__: str
    tables: FacadeDict
    schema: quoted_name
    naming_convention: Mapping[str, str]
    @memoized_property
    def info(self) -> Mapping[str, Incomplete] | None: ...  # type: ignore[override]  # @memoized_property causes override issue
    def __init__(
        self,
        bind: Engine | Connection | str | URL | None = None,
        schema: str | None = None,
        quote_schema: Incomplete | None = None,
        naming_convention: Mapping[str, str] | None = None,
        info: Mapping[str, Incomplete] | None = None,
    ) -> None: ...
    def __contains__(self, table_or_key: str | Table) -> bool: ...
    def is_bound(self) -> bool: ...
    bind: Engine | Connection | str | URL | None
    def clear(self) -> None: ...
    def remove(self, table: Table) -> None: ...
    @property
    def sorted_tables(self) -> list[Table]: ...
    def reflect(
        self,
        bind: Connectable | None = None,
        schema: str | None = None,
        views: bool = False,
        only: ABCSequence[str] | Callable[[str, MetaData], bool] | None = None,
        extend_existing: bool = False,
        autoload_replace: bool = True,
        resolve_fks: bool = True,
        **dialect_kwargs,
    ) -> None: ...
    def create_all(
        self, bind: Connectable | None = None, tables: ABCSequence[Table] | None = None, checkfirst: bool = True
    ) -> None: ...
    def drop_all(
        self, bind: Connectable | None = None, tables: ABCSequence[Table] | None = None, checkfirst: bool = True
    ) -> None: ...

class ThreadLocalMetaData(MetaData):
    __visit_name__: str
    context: local
    def __init__(self) -> None: ...
    @property
    def bind(self) -> Engine | Connection | str | URL | None: ...  # type: ignore[override]  # Assigned property
    def is_bound(self) -> bool: ...
    def dispose(self) -> None: ...

class Computed(FetchedValue, SchemaItem):
    __visit_name__: str
    sqltext: Any
    persisted: Any
    column: Any
    def __init__(self, sqltext, persisted: Incomplete | None = None) -> None: ...
    def copy(self, target_table: Incomplete | None = None, **kw: Unused) -> Computed: ...

class Identity(IdentityOptions, FetchedValue, SchemaItem):
    __visit_name__: str
    always: Any
    on_null: Any
    column: Any
    def __init__(
        self,
        always: bool = False,
        on_null: Incomplete | None = None,
        start: Incomplete | None = None,
        increment: Incomplete | None = None,
        minvalue: Incomplete | None = None,
        maxvalue: Incomplete | None = None,
        nominvalue: Incomplete | None = None,
        nomaxvalue: Incomplete | None = None,
        cycle: Incomplete | None = None,
        cache: Incomplete | None = None,
        order: Incomplete | None = None,
    ) -> None: ...
    def copy(self, **kw: Unused) -> Identity: ...
