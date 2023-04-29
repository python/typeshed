from _typeshed import Incomplete, ReadableBuffer, SupportsTrunc, Unused
from builtins import type as _type
from collections.abc import Iterable
from typing import Any, ClassVar, SupportsInt, overload
from typing_extensions import Self, SupportsIndex

from ..engine import ResultProxy
from ..engine.base import Connection, Engine
from ..sql import sqltypes
from ..sql.coercions import _CoercibleElement
from ..sql.operators import _AnyOperator
from ..sql.schema import Sequence
from ..sql.type_api import TypeEngine
from ..util import HasMemoized
from ..util.langhelpers import memoized_property
from .base import ColumnCollection, Executable, Generative
from .elements import (
    AsBoolean,
    BinaryExpression,
    ClauseList,
    ColumnElement,
    FunctionFilter,
    Grouping,
    NamedColumn,
    WithinGroup,
    _anonymous_label,
    quoted_name,
)
from .selectable import FromClause, Select, TableValuedAlias
from .visitors import TraversibleType

def register_function(identifier, fn, package: str = "_default") -> None: ...

class FunctionElement(Executable, ColumnElement[Any], FromClause, Generative):  # type: ignore[misc]
    packagenames: Incomplete
    clause_expr: Grouping
    def __init__(self, *clauses, **kwargs: Unused) -> None: ...
    def scalar_table_valued(self, name, type_: type[TypeEngine] | TypeEngine | None = None): ...
    def table_valued(self, *expr, **kw): ...
    def column_valued(self, name: str | None = None, joins_implicitly: bool = False): ...
    @property
    def columns(self) -> ColumnCollection: ...  # type: ignore[override]  # Incompatible with supertype
    @property
    def exported_columns(self): ...
    @HasMemoized.memoized_attribute
    def clauses(self) -> ClauseList: ...
    def over(
        self,
        partition_by: _CoercibleElement | None = None,
        order_by: _CoercibleElement | None = None,
        rows: tuple[
            str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc | None,
            str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc | None,
        ]
        | None = None,
        range_: tuple[
            str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc | None,
            str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc | None,
        ]
        | None = None,
    ): ...
    def within_group(self, *order_by: _CoercibleElement): ...
    @overload
    def filter(self) -> Self: ...  # type: ignore[misc]
    @overload
    def filter(self, *criterion) -> FunctionFilter: ...
    def as_comparison(self, left_index, right_index): ...
    def within_group_type(self, within_group: Unused) -> None: ...
    def alias(self, name: str | None = None, joins_implicitly: bool = False) -> TableValuedAlias: ...  # type: ignore[override]
    def select(self) -> Select | None: ...  # type: ignore[override]  # Incompatible with supertype
    def scalar(self): ...
    def execute(self) -> ResultProxy: ...
    def self_group(  # type: ignore[override]  # supertype has overloads
        self, against: _AnyOperator | None = None
    ) -> Self | Grouping | AsBoolean: ...
    @property
    def entity_namespace(self): ...

class FunctionAsBinary(BinaryExpression):
    sql_function: Incomplete
    left_index: Incomplete
    right_index: Incomplete
    operator: Incomplete
    type: Incomplete
    negate: Incomplete
    modifiers: Incomplete
    def __init__(self, fn, left_index, right_index) -> None: ...
    @property
    def left(self): ...
    @left.setter
    def left(self, value) -> None: ...
    @property
    def right(self): ...
    @right.setter
    def right(self, value) -> None: ...

class ScalarFunctionColumn(NamedColumn):
    __visit_name__: str
    is_literal: bool
    table: Incomplete
    fn: Incomplete
    name: Incomplete
    @memoized_property
    def type(self) -> TypeEngine | None: ...
    def __init__(self, fn, name, type_: TypeEngine | _type[TypeEngine] | None = None) -> None: ...

class _FunctionGenerator:
    opts: Incomplete
    def __init__(self, **opts) -> None: ...
    def __getattr__(self, name: str): ...
    def __call__(self, *c, **kwargs) -> Function: ...

func: _FunctionGenerator
modifier: _FunctionGenerator

class Function(FunctionElement):
    __visit_name__: str
    @memoized_property
    def type(self) -> TypeEngine | _type[TypeEngine]: ...  # type: ignore[override]  # @memoized_property causes override issue
    packagenames: Incomplete
    name: quoted_name | _anonymous_label | str
    def __init__(
        self, name: str, *clauses, packagenames: Incomplete | None = None, type_: TypeEngine | _type[TypeEngine] | None, **kw
    ) -> None: ...

class _GenericMeta(TraversibleType):
    name: ClassVar[str]
    identifier: ClassVar[str]
    def __init__(cls, clsname: str, bases, clsdict) -> None: ...

class GenericFunction(Function, metaclass=_GenericMeta):
    name: Incomplete
    identifier: Incomplete
    coerce_arguments: bool
    inherit_cache: bool
    packagenames: Incomplete
    clause_expr: Grouping
    @memoized_property
    def type(self) -> TypeEngine | _type[TypeEngine]: ...  # type: ignore[override]  # @memoized_property causes override issue
    def __init__(
        self,
        *args,
        _parsed_args: Iterable[ColumnElement[Incomplete]] | None = None,
        bind: Engine | Connection | None = ...,
        type_: TypeEngine | _type[TypeEngine] | None = None,
    ) -> None: ...

class next_value(GenericFunction):
    @memoized_property
    def type(self) -> TypeEngine: ...  # type: ignore[override]  # @memoized_property causes override issue
    name: str
    sequence: Sequence
    def __init__(self, seq: Sequence, **kw) -> None: ...
    def compare(self, other, **kw): ...

class AnsiFunction(GenericFunction):
    inherit_cache: bool
    def __init__(self, *args, **kwargs) -> None: ...

class ReturnTypeFromArgs(GenericFunction):
    inherit_cache: bool
    def __init__(self, *args, **kwargs) -> None: ...

class coalesce(ReturnTypeFromArgs):
    inherit_cache: bool

class max(ReturnTypeFromArgs):
    inherit_cache: bool

class min(ReturnTypeFromArgs):
    inherit_cache: bool

class sum(ReturnTypeFromArgs):
    inherit_cache: bool

class now(GenericFunction):
    type: Incomplete
    inherit_cache: bool

class concat(GenericFunction):
    type: Incomplete
    inherit_cache: bool

class char_length(GenericFunction):
    type: Incomplete
    inherit_cache: bool
    def __init__(self, arg, **kwargs) -> None: ...

class random(GenericFunction):
    inherit_cache: bool

class count(GenericFunction):
    type: Incomplete
    inherit_cache: bool
    def __init__(self, expression: Incomplete | None = None, **kwargs) -> None: ...

class current_date(AnsiFunction):
    type: Incomplete
    inherit_cache: bool

class current_time(AnsiFunction):
    type: Incomplete
    inherit_cache: bool

class current_timestamp(AnsiFunction):
    type: Incomplete
    inherit_cache: bool

class current_user(AnsiFunction):
    type: Incomplete
    inherit_cache: bool

class localtime(AnsiFunction):
    type: Incomplete
    inherit_cache: bool

class localtimestamp(AnsiFunction):
    type: Incomplete
    inherit_cache: bool

class session_user(AnsiFunction):
    type: Incomplete
    inherit_cache: bool

class sysdate(AnsiFunction):
    type: Incomplete
    inherit_cache: bool

class user(AnsiFunction):
    type: Incomplete
    inherit_cache: bool

class array_agg(GenericFunction):
    type: _type[sqltypes.ARRAY]  # type: ignore[assignment]  # supertype is @memoized_property
    inherit_cache: bool
    def __init__(
        self,
        *args: ColumnElement[Incomplete],
        bind: Engine | Connection | None = ...,
        type_: TypeEngine | None = None,
        _default_array_type: _type[TypeEngine] = ...,
    ) -> None: ...

class OrderedSetAgg(GenericFunction):
    array_for_multi_clause: bool
    inherit_cache: bool
    def within_group_type(self, within_group: WithinGroup) -> sqltypes.ARRAY | TypeEngine: ...  # type: ignore [override]

class mode(OrderedSetAgg):
    inherit_cache: bool

class percentile_cont(OrderedSetAgg):
    array_for_multi_clause: bool
    inherit_cache: bool

class percentile_disc(OrderedSetAgg):
    array_for_multi_clause: bool
    inherit_cache: bool

class rank(GenericFunction):
    type: Incomplete
    inherit_cache: bool

class dense_rank(GenericFunction):
    type: Incomplete
    inherit_cache: bool

class percent_rank(GenericFunction):
    type: Incomplete
    inherit_cache: bool

class cume_dist(GenericFunction):
    type: Incomplete
    inherit_cache: bool

class cube(GenericFunction):
    inherit_cache: bool

class rollup(GenericFunction):
    inherit_cache: bool

class grouping_sets(GenericFunction):
    inherit_cache: bool
