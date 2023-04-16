from _typeshed import Incomplete
from collections.abc import Callable, Iterable, Mapping
from typing import Any, Protocol
from typing_extensions import Self

from ..engine import Connection, Engine
from ..engine.cursor import CursorResult
from ..engine.default import DefaultDialect
from ..engine.interfaces import Connectable
from ..sql.compiler import IdentifierPreparer
from . import roles
from .base import Executable, SchemaVisitor
from .elements import ClauseElement, ColumnElement
from .schema import Constraint, ForeignKey, ForeignKeyConstraint, Index, MetaData, SchemaItem, Sequence, Table

class _DDLCallable(Protocol):
    def __call__(
        self,
        ddl: DDLElement,
        target: Table | MetaData | None,
        bind: Connectable,
        tables: list[Incomplete] | None = ...,
        state: Incomplete | None = ...,
        checkfirst: bool = ...,
    ) -> bool: ...

class _DDLCompiles(ClauseElement): ...

class DDLElement(roles.DDLRole, Executable, _DDLCompiles):
    target: SchemaItem | None
    on: None  # Never assigned or used
    dialect: str | tuple[str] | list[str] | set[str] | None
    callable_: _DDLCallable | None
    def execute(self, bind: Engine | Connection | None = ..., target: Incomplete | None = ...) -> CursorResult: ...
    def against(self, target: SchemaItem) -> Self: ...
    state: Any
    def execute_if(
        self,
        dialect: str | tuple[str] | list[str] | set[str] | None = ...,
        callable_: _DDLCallable | None = ...,
        state: Incomplete | None = ...,
    ) -> Self: ...
    def __call__(self, target: Table | MetaData | None, bind: Connectable, **kw): ...
    bind: Connectable | None  # type: ignore[assignment]  # Any Connectable is valid

class DDL(DDLElement):
    __visit_name__: str
    statement: str
    context: Mapping[Incomplete, Incomplete]
    def __init__(
        self, statement: str, context: Mapping[Incomplete, Incomplete] | None = ..., bind: Connectable | None = ...
    ) -> None: ...

class _CreateDropBase(DDLElement):
    element: SchemaItem
    if_exists: Any
    if_not_exists: Any
    def __init__(
        self,
        element: SchemaItem,
        bind: Connectable | None = ...,
        if_exists: bool = ...,
        if_not_exists: bool = ...,
        _legacy_bind: Connectable | None = ...,
    ) -> None: ...
    @property
    def stringify_dialect(self): ...

class CreateSchema(_CreateDropBase):
    __visit_name__: str
    quote: bool | None
    def __init__(self, name, quote: bool | None = ..., **kw) -> None: ...

class DropSchema(_CreateDropBase):
    __visit_name__: str
    quote: bool | None
    cascade: bool
    def __init__(self, name, quote: bool | None = ..., cascade: bool = ..., **kw) -> None: ...

class CreateTable(_CreateDropBase):
    __visit_name__: str
    columns: list[CreateColumn]
    include_foreign_key_constraints: Iterable[ForeignKeyConstraint] | None
    element: Table
    def __init__(
        self,
        element: Table,
        bind: Connectable | None = ...,
        include_foreign_key_constraints: Iterable[ForeignKeyConstraint] | None = ...,
        if_not_exists: bool = ...,
    ) -> None: ...

class _DropView(_CreateDropBase):
    __visit_name__: str

class CreateColumn(_DDLCompiles):
    __visit_name__: str
    element: ColumnElement[Incomplete]
    def __init__(self, element: ColumnElement[Incomplete]) -> None: ...

class DropTable(_CreateDropBase):
    __visit_name__: str
    element: Table
    def __init__(self, element: Table, bind: Incomplete | None = ..., if_exists: bool = ...) -> None: ...

class CreateSequence(_CreateDropBase):
    __visit_name__: str

class DropSequence(_CreateDropBase):
    __visit_name__: str

class CreateIndex(_CreateDropBase):
    __visit_name__: str
    element: Index
    def __init__(self, element: Index, bind: Incomplete | None = ..., if_not_exists: bool = ...) -> None: ...

class DropIndex(_CreateDropBase):
    __visit_name__: str
    element: Index
    def __init__(self, element: Index, bind: Incomplete | None = ..., if_exists: bool = ...) -> None: ...

class AddConstraint(_CreateDropBase):
    __visit_name__: str
    element: Constraint
    def __init__(self, element: Constraint, *args, **kw) -> None: ...

class DropConstraint(_CreateDropBase):
    __visit_name__: str
    cascade: bool
    element: Constraint
    def __init__(self, element: Constraint, cascade: bool = ..., **kw) -> None: ...

class SetTableComment(_CreateDropBase):
    __visit_name__: str

class DropTableComment(_CreateDropBase):
    __visit_name__: str

class SetColumnComment(_CreateDropBase):
    __visit_name__: str

class DropColumnComment(_CreateDropBase):
    __visit_name__: str

class DDLBase(SchemaVisitor):
    connection: Connection
    def __init__(self, connection: Connection) -> None: ...

class SchemaGenerator(DDLBase):
    checkfirst: bool
    tables: Iterable[Table] | None
    preparer: IdentifierPreparer
    dialect: DefaultDialect
    memo: dict[Incomplete, Incomplete]
    def __init__(
        self,
        dialect: DefaultDialect,
        connection: Connection,
        checkfirst: bool = ...,
        tables: Iterable[Table] | None = ...,
        **kwargs,
    ) -> None: ...
    def visit_metadata(self, metadata: MetaData) -> None: ...
    def visit_table(
        self,
        table: Table,
        create_ok: bool = ...,
        include_foreign_key_constraints: Incomplete | None = ...,
        _is_metadata_operation: bool = ...,
    ) -> None: ...
    def visit_foreign_key_constraint(self, constraint: ForeignKeyConstraint) -> None: ...
    def visit_sequence(self, sequence: Sequence, create_ok: bool = ...) -> None: ...
    def visit_index(self, index: Index, create_ok: bool = ...) -> None: ...

class SchemaDropper(DDLBase):
    checkfirst: bool
    tables: Iterable[Table] | None
    preparer: IdentifierPreparer
    dialect: DefaultDialect
    memo: dict[Incomplete, Incomplete]
    def __init__(
        self,
        dialect: DefaultDialect,
        connection: Connection,
        checkfirst: bool = ...,
        tables: Iterable[Table] | None = ...,
        **kwargs,
    ) -> None: ...
    def visit_metadata(self, metadata: MetaData): ...
    def visit_index(self, index: Index, drop_ok: bool = ...) -> None: ...
    def visit_table(
        self, table: Table, drop_ok: bool = ..., _is_metadata_operation: bool = ..., _ignore_sequences=...
    ) -> None: ...
    def visit_foreign_key_constraint(self, constraint: ForeignKeyConstraint) -> None: ...
    def visit_sequence(self, sequence: Sequence, drop_ok: bool = ...) -> None: ...

def sort_tables(
    tables: Iterable[Table],
    skip_fn: Callable[[ForeignKey], bool] | None = ...,
    extra_dependencies: Iterable[tuple[Table, Table]] | None = ...,
): ...
def sort_tables_and_constraints(
    tables: Iterable[Table],
    filter_fn: Callable[[ForeignKeyConstraint], bool | None] | None = ...,
    extra_dependencies: Iterable[tuple[Table, Table]] | None = ...,
    _warn_for_cycles: bool = ...,
) -> list[tuple[Table | None, set[ForeignKeyConstraint] | list[ForeignKeyConstraint]]]: ...
