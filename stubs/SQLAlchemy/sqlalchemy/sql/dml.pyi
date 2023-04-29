from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Any, NoReturn
from typing_extensions import Self

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
    @classmethod
    def get_entity_description(cls, statement) -> dict[str, Incomplete]: ...
    @classmethod
    def get_returning_column_descriptions(cls, statement) -> list[dict[str, Incomplete]]: ...

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
    def with_dialect_options(self, **opt) -> Self: ...
    bind: Any
    def returning(self, *cols: ColumnElement[Incomplete] | Table) -> Self: ...
    @property
    def exported_columns(self): ...
    def with_hint(self, text: str, selectable: _CoercibleElement | None = None, dialect_name: str = "*") -> Self: ...
    @property
    def entity_description(self): ...
    @property
    def returning_column_descriptions(self): ...

class ValuesBase(UpdateBase):
    __visit_name__: str
    select: Selectable | None
    table: Table
    def __init__(self, table: TableClause, values, prefixes) -> None: ...
    def values(self, *args, **kwargs) -> Self: ...
    def return_defaults(self, *cols) -> Self: ...

class Insert(ValuesBase):
    __visit_name__: str
    select: Selectable | None
    include_insert_from_select_defaults: bool
    is_insert: bool
    def __init__(
        self,
        table: TableClause,
        values: Incomplete | None = None,
        inline: bool = False,
        bind: Incomplete | None = None,
        prefixes: Incomplete | None = None,
        returning: Incomplete | None = None,
        return_defaults: bool = False,
        **dialect_kw,
    ) -> None: ...
    def inline(self) -> Self: ...
    def from_select(
        self, names: Iterable[str | Column], select: FromClause | Query[Incomplete], include_defaults: bool = True
    ) -> Self: ...

class DMLWhereBase:
    def where(self, *whereclause: bool | str | Traversible | None) -> Self: ...
    def filter(self, *criteria) -> Self: ...
    def filter_by(self, **kwargs) -> Self: ...
    @property
    def whereclause(self): ...

class Update(DMLWhereBase, ValuesBase):
    __visit_name__: str
    select: None
    is_update: bool
    def __init__(
        self,
        table: TableClause,
        whereclause: bool | str | Traversible | None = None,
        values: Incomplete | None = None,
        inline: bool = False,
        bind: Incomplete | None = None,
        prefixes: Incomplete | None = None,
        returning: Incomplete | None = None,
        return_defaults: bool = False,
        preserve_parameter_order: bool = False,
        **dialect_kw,
    ) -> None: ...
    def ordered_values(self, *args) -> Self: ...
    def inline(self) -> Self: ...

class Delete(DMLWhereBase, UpdateBase):
    __visit_name__: str
    is_delete: bool
    def __init__(
        self,
        table: TableClause,
        whereclause: bool | str | Traversible | None = None,
        bind: Incomplete | None = None,
        returning: Incomplete | None = None,
        prefixes: Incomplete | None = None,
        **dialect_kw,
    ) -> None: ...
