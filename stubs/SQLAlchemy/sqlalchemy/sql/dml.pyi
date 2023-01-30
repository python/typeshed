from _typeshed import Incomplete, Self
from collections.abc import Iterable
from typing import Any, NoReturn

from ..orm.query import Query
from ..schema import Table
from ..sql.coercions import _CoercibleElement
from ..sql.schema import Column
from ..sql.visitors import Traversible
from . import roles
from .base import CompileState, DialectKWArgs, Executable, HasCompileState
from .elements import ClauseElement, ColumnElement
from .selectable import FromClause, HasCTE, HasPrefixes, ReturnsRows, Selectable, TableClause

class DMLState(CompileState):
    isupdate: bool
    isdelete: bool
    isinsert: bool
    def __init__(self, statement, compiler, **kw) -> None: ...
    @property
    def dml_table(self): ...

class InsertDMLState(DMLState):
    isinsert: bool
    include_table_with_column_exprs: bool
    statement: Any
    def __init__(self, statement, compiler, **kw) -> None: ...

class UpdateDMLState(DMLState):
    isupdate: bool
    include_table_with_column_exprs: bool
    statement: Any
    is_multitable: Any
    def __init__(self, statement, compiler, **kw) -> None: ...

class DeleteDMLState(DMLState):
    isdelete: bool
    statement: Any
    def __init__(self, statement, compiler, **kw) -> None: ...

class UpdateBase(roles.DMLRole, HasCTE, HasCompileState, DialectKWArgs, HasPrefixes, ReturnsRows, Executable, ClauseElement):
    __visit_name__: str
    named_with_column: bool
    is_dml: bool
    def params(self, *arg, **kw) -> NoReturn: ...
    def with_dialect_options(self: Self, **opt) -> Self: ...
    bind: Any
    def returning(self: Self, *cols: ColumnElement[Incomplete] | Table) -> Self: ...
    @property
    def exported_columns(self): ...
    def with_hint(self: Self, text: str, selectable: _CoercibleElement | None = ..., dialect_name: str = ...) -> Self: ...

class ValuesBase(UpdateBase):
    __visit_name__: str
    select: Selectable | None
    table: Table
    def __init__(self, table: TableClause, values, prefixes) -> None: ...
    def values(self: Self, *args, **kwargs) -> Self: ...
    def return_defaults(self: Self, *cols) -> Self: ...

class Insert(ValuesBase):
    __visit_name__: str
    select: Selectable | None
    include_insert_from_select_defaults: bool
    is_insert: bool
    def __init__(
        self,
        table: TableClause,
        values: Incomplete | None = ...,
        inline: bool = ...,
        bind: Incomplete | None = ...,
        prefixes: Incomplete | None = ...,
        returning: Incomplete | None = ...,
        return_defaults: bool = ...,
        **dialect_kw,
    ) -> None: ...
    def inline(self: Self) -> Self: ...
    def from_select(
        self: Self, names: Iterable[str | Column], select: FromClause | Query[Incomplete], include_defaults: bool = ...
    ) -> Self: ...

class DMLWhereBase:
    def where(self: Self, *whereclause: bool | str | Traversible | None) -> Self: ...
    def filter(self: Self, *criteria) -> Self: ...
    def filter_by(self: Self, **kwargs) -> Self: ...
    @property
    def whereclause(self): ...

class Update(DMLWhereBase, ValuesBase):
    __visit_name__: str
    select: None
    is_update: bool
    def __init__(
        self,
        table: TableClause,
        whereclause: bool | str | Traversible | None = ...,
        values: Incomplete | None = ...,
        inline: bool = ...,
        bind: Incomplete | None = ...,
        prefixes: Incomplete | None = ...,
        returning: Incomplete | None = ...,
        return_defaults: bool = ...,
        preserve_parameter_order: bool = ...,
        **dialect_kw,
    ) -> None: ...
    def ordered_values(self: Self, *args) -> Self: ...
    def inline(self: Self) -> Self: ...

class Delete(DMLWhereBase, UpdateBase):
    __visit_name__: str
    is_delete: bool
    def __init__(
        self,
        table: TableClause,
        whereclause: bool | str | Traversible | None = ...,
        bind: Incomplete | None = ...,
        returning: Incomplete | None = ...,
        prefixes: Incomplete | None = ...,
        **dialect_kw,
    ) -> None: ...
