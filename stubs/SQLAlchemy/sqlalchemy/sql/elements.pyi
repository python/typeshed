from _typeshed import Incomplete, ReadableBuffer, SupportsGetItem, SupportsTrunc, Unused
from builtins import type as _type
from collections.abc import Callable, Iterable, Iterator, Sequence
from typing import Any, Generic, NoReturn, SupportsInt, TypeVar, overload
from typing_extensions import Literal, ParamSpec, Self, SupportsIndex

from .. import util
from ..engine import Connection, Engine
from ..sql.coercions import _CoercibleElement
from ..sql.functions import FunctionElement
from ..sql.schema import ForeignKey
from ..sql.selectable import Subquery, TableClause, TextualSelect
from ..sql.type_api import TypeEngine
from ..util import HasMemoized, memoized_property
from ..util.langhelpers import _symbol, symbol
from . import roles
from .annotation import Annotated, SupportsWrappingAnnotations
from .base import Executable, Immutable, SingletonConstant
from .operators import _AnyOperator
from .sqltypes import Boolean, Integer, NullType, TupleType
from .traversals import HasCopyInternals, MemoizedHasCacheKey
from .visitors import Traversible

_T = TypeVar("_T")
_K = TypeVar("_K")
_V = TypeVar("_V")
_P = ParamSpec("_P")

def collate(expression, collation): ...
def between(expr, lower_bound, upper_bound, symmetric: bool = False): ...
def literal(value, type_: Incomplete | None = None): ...
def outparam(key, type_: Incomplete | None = None): ...
def not_(clause): ...

class ClauseElement(roles.SQLRole, SupportsWrappingAnnotations, MemoizedHasCacheKey, HasCopyInternals, Traversible):
    __visit_name__: str
    supports_execution: bool
    stringify_dialect: str
    bind: Any
    description: Any
    is_clause_element: bool
    is_selectable: bool
    @property
    def entity_namespace(self) -> None: ...
    def unique_params(self, *optionaldict, **kwargs): ...
    def params(self, *optionaldict, **kwargs): ...
    def compare(self, other: ClauseElement, **kw) -> bool: ...
    # This method is meant to be overriden
    def self_group(self, against: _AnyOperator | None = None) -> Self | Grouping: ...
    def compile(self, bind: Incomplete | None = None, dialect: Incomplete | None = None, **kw): ...
    def __invert__(self): ...
    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...

class ColumnElement(
    roles.ColumnArgumentOrKeyRole,
    roles.StatementOptionRole,
    roles.WhereHavingRole,
    roles.BinaryElementRole,
    roles.OrderByRole,
    roles.ColumnsClauseRole,
    roles.LimitOffsetRole,
    roles.DMLColumnRole,
    roles.DDLConstraintColumnRole,
    roles.DDLExpressionRole,
    # The actual supertype is operators.ColumnOperators[_T], not TypeEngine.Comparator[_T],
    # but this will give us all redefined operation methods from self.comparator.
    TypeEngine.Comparator[_T],
    ClauseElement,
    Generic[_T],
):
    __visit_name__: str
    primary_key: bool
    foreign_keys: list[ForeignKey]
    key: str | None
    # self_group Any: Same as operator.and_/or_
    @overload
    def self_group(  # type: ignore[misc]  # Actual return type
        self, against: Callable[[Any, Any], Any] | _symbol | symbol
    ) -> AsBoolean | Self: ...
    @overload
    def self_group(self, against: Callable[[Incomplete], Incomplete]) -> Grouping: ...  # type: ignore[misc]  # Actual return type
    @overload
    def self_group(self, against: object = None) -> Self: ...
    @memoized_property
    def type(self) -> TypeEngine | None: ...
    @HasMemoized.memoized_attribute
    def comparator(self) -> TypeEngine.Comparator[_T]: ...
    def __getattr__(self, key: str): ...
    @property
    def expression(self) -> Self: ...
    @memoized_property
    def base_columns(self) -> set[ColumnElement[_T]]: ...
    @memoized_property
    def proxy_set(self) -> set[ColumnElement[_T]]: ...
    def shares_lineage(self, othercolumn: ColumnElement[_T]) -> bool: ...
    def cast(self, type_: TypeEngine | _type[TypeEngine] | None) -> Cast: ...
    def label(self, name: str) -> Label: ...
    @property
    def anon_label(self) -> Callable[[], _anonymous_label]: ...
    @property
    def anon_key_label(self) -> Callable[[], _anonymous_label]: ...

class WrapsColumnExpression:
    @property
    def wrapped_column_expression(self) -> None: ...

class BindParameter(roles.InElementRole, ColumnElement[_T], Generic[_T]):
    __visit_name__: str
    inherit_cache: bool
    key: quoted_name | _anonymous_label | str
    unique: bool
    value: _T | None
    callable: Callable[[], _T] | None
    isoutparam: bool
    required: bool
    expanding: bool
    expand_op: Incomplete | None
    literal_execute: Any
    @memoized_property
    def type(self) -> TypeEngine | None: ...
    # If the parameter quote is not None. The parameter key is strigified.
    @overload
    def __init__(
        self,
        key: str,
        value: _T | _symbol | symbol | None = None,
        type_: TypeEngine | _type[TypeEngine] | None = None,
        unique: bool = False,
        required: bool | _symbol | symbol = ...,
        quote: None = None,
        callable_: Callable[[], _T] | None = None,
        expanding: bool = False,
        isoutparam: bool = False,
        literal_execute: bool = False,
        _compared_to_operator: Incomplete | None = None,
        _compared_to_type: Incomplete | None = None,
        _is_crud: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self,
        key: object,
        *,
        value: _T | _symbol | symbol | None = None,
        type_: TypeEngine | _type[TypeEngine] | None = None,
        unique: bool = False,
        required: bool | _symbol | symbol = ...,
        quote: bool,
        callable_: Callable[[], _T] | None = None,
        expanding: bool = False,
        isoutparam: bool = False,
        literal_execute: bool = False,
        _compared_to_operator: Incomplete | None = None,
        _compared_to_type: Incomplete | None = None,
        _is_crud: bool = False,
    ) -> None: ...
    @property
    def effective_value(self) -> _T: ...
    def render_literal_execute(self): ...

class TypeClause(ClauseElement):
    __visit_name__: str
    type: TypeEngine
    def __init__(self, type_: TypeEngine) -> None: ...

class TextClause(
    roles.DDLConstraintColumnRole,
    roles.DDLExpressionRole,
    roles.StatementOptionRole,
    roles.WhereHavingRole,
    roles.OrderByRole,
    roles.FromClauseRole,
    roles.SelectStatementRole,
    roles.BinaryElementRole,
    roles.InElementRole,
    Executable,
    ClauseElement,
):
    __visit_name__: str
    def __and__(self, other): ...
    key: Any
    text: str
    def __init__(self, text: str, bind: Engine | Connection | None = None) -> None: ...
    def bindparams(self, *binds: BindParameter[Incomplete], **names_to_values) -> Self: ...
    def columns(self, *cols: ColumnClause, **types: TypeEngine | _type[TypeEngine] | None) -> TextualSelect: ...
    @property
    def type(self) -> NullType: ...
    @property
    def comparator(self): ...
    @overload
    def self_group(  # type: ignore[misc]  # Actual return type
        self, against: Callable[[Incomplete, Incomplete], Incomplete]
    ) -> Grouping | Self: ...
    @overload
    def self_group(self, against: object = None) -> Self: ...
    # SelectStatementRole.subquery is an abstractmethod. But TextClause isn't abstract.
    def subquery(self) -> NoReturn | Subquery: ...

class Null(SingletonConstant, roles.ConstExprRole, ColumnElement[None]):
    __visit_name__: str
    @memoized_property
    def type(self) -> NullType: ...  # type: ignore[override]  # Unsure why

class False_(SingletonConstant, roles.ConstExprRole, ColumnElement[Literal[False]]):
    __visit_name__: str
    @memoized_property
    def type(self) -> Boolean: ...  # type: ignore[override]  # Unsure why

class True_(SingletonConstant, roles.ConstExprRole, ColumnElement[Literal[True]]):
    __visit_name__: str
    @memoized_property
    def type(self) -> Boolean: ...  # type: ignore[override]  # Unsure why

class ClauseList(roles.InElementRole, roles.OrderByRole, roles.ColumnsClauseRole, roles.DMLColumnRole, ClauseElement):
    __visit_name__: str
    operator: Callable[[Incomplete, Incomplete], Incomplete]
    group: bool
    group_contents: Any
    clauses: list[ClauseElement]
    @overload
    def __init__(
        self,
        *clauses: Iterable[_CoercibleElement] | _CoercibleElement,
        operator: Callable[[Incomplete, Incomplete], Incomplete] = ...,
        group: bool = ...,
        group_contents: bool = ...,
        _flatten_sub_clauses: Literal[True],
        _literal_as_text_role=...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *clauses: _CoercibleElement,
        operator: Callable[[Incomplete, Incomplete], Incomplete] = ...,
        group: bool = ...,
        group_contents: bool = ...,
        _flatten_sub_clauses: Literal[False] = False,
        _literal_as_text_role=...,
    ) -> None: ...
    def __iter__(self) -> Iterator[ClauseElement]: ...
    def __len__(self) -> int: ...
    def append(self, clause: ClauseElement) -> None: ...
    def self_group(self, against: _AnyOperator | None = None) -> Grouping | Self: ...

class BooleanClauseList(ClauseList, ColumnElement[Any]):
    __visit_name__: str
    inherit_cache: bool
    def __init__(self, *arg, **kw) -> None: ...
    @overload
    @classmethod
    def and_(cls) -> Self: ...
    @overload
    @classmethod
    def and_(cls, __clause: _CoercibleElement) -> ClauseElement: ...
    @overload
    @classmethod
    def and_(cls, __clause1: _CoercibleElement, __clause2: _CoercibleElement, *clauses: _CoercibleElement) -> Self: ...
    @overload
    @classmethod
    def or_(cls) -> Self: ...
    @overload
    @classmethod
    def or_(cls, __clause: _CoercibleElement) -> ClauseElement: ...
    @overload
    @classmethod
    def or_(cls, __clause1: _CoercibleElement, __clause2: _CoercibleElement, *clauses: _CoercibleElement) -> Self: ...
    def self_group(  # type: ignore[override]  # supertype has overloads
        self, against: _AnyOperator | None = None
    ) -> Grouping | Self: ...

and_ = BooleanClauseList.and_
or_ = BooleanClauseList.or_

class Tuple(ClauseList, ColumnElement[Any]):
    __visit_name__: str
    @memoized_property
    def type(self) -> TupleType: ...  # type: ignore[override]  # Is always assigned TupleType
    def __init__(self, *clauses: ColumnElement[Incomplete], **kw) -> None: ...
    def self_group(self, against: Unused = None) -> Self: ...  # type: ignore[override]  # supertype has overloads

class Case(ColumnElement[Any]):
    __visit_name__: str
    value: Incomplete | None
    @memoized_property
    def type(self) -> Incomplete | None: ...
    whens: Any
    else_: Incomplete | None
    def __init__(
        self, *whens: tuple[ClauseElement, Incomplete], value: Incomplete | None = None, else_: Incomplete | None = None
    ) -> None: ...

def literal_column(text, type_: TypeEngine | _type[TypeEngine] | None = None) -> ColumnClause: ...  # ColumnClause[TypeEngine[_T]]

class Cast(WrapsColumnExpression, ColumnElement[Any]):
    __visit_name__: str
    @memoized_property
    def type(self) -> TypeEngine | None: ...
    clause: ClauseElement
    typeclause: Any
    def __init__(self, expression, type_: TypeEngine | _type[TypeEngine] | None) -> None: ...
    @property
    def wrapped_column_expression(self): ...

class TypeCoerce(WrapsColumnExpression, ColumnElement[Any]):
    __visit_name__: str
    @memoized_property
    def type(self) -> TypeEngine | None: ...
    clause: Any
    def __init__(self, expression: str | ColumnElement[Incomplete], type_: TypeEngine | _type[TypeEngine] | None) -> None: ...
    @HasMemoized.memoized_attribute
    def typed_expression(self): ...
    @property
    def wrapped_column_expression(self): ...
    def self_group(  # type: ignore[override]  # supertype has overloads
        self, against: _AnyOperator | None = None
    ) -> TypeCoerce | Self: ...

class Extract(ColumnElement[Any]):
    __visit_name__: str
    @memoized_property
    def type(self) -> Integer: ...  # type: ignore[override]  # @memoized_property causes override issue
    field: Any
    expr: ClauseElement
    def __init__(self, field, expr: ClauseElement, **kwargs: Unused) -> None: ...

class _label_reference(ColumnElement[Any]):
    __visit_name__: str
    element: Any
    def __init__(self, element) -> None: ...

class _textual_label_reference(ColumnElement[Any]):
    __visit_name__: str
    element: Any
    def __init__(self, element) -> None: ...

class UnaryExpression(ColumnElement[Any]):
    __visit_name__: str
    operator: (Callable[[Any, Any], Any] | Callable[[Incomplete], Incomplete] | None)
    modifier: Any
    element: Any
    @memoized_property
    def type(self) -> TypeEngine | None: ...
    wraps_column_expression: bool
    def __init__(
        self,
        element,
        operator: Callable[[Any, Any], Any] | Callable[[Incomplete], Incomplete] | None = None,
        modifier: Incomplete | None = None,
        type_: TypeEngine | _type[TypeEngine] | None = None,
        wraps_column_expression: bool = False,
    ) -> None: ...
    def self_group(  # type: ignore[override]  # supertype has overloads
        self, against: _AnyOperator | None = None
    ) -> Grouping | Self: ...

class CollectionAggregate(UnaryExpression):
    inherit_cache: bool
    def operate(self, op: Callable[_P, _T], *other: _P.args, **kwargs: _P.kwargs) -> _T: ...  # type: ignore[override]  # _T doesn't match
    # comparison operators should never call reverse_operate
    def reverse_operate(self, op: object, other: Unused, **kwargs: Unused) -> NoReturn: ...

class AsBoolean(WrapsColumnExpression, UnaryExpression):
    inherit_cache: bool
    element: ColumnElement[Incomplete]
    @memoized_property
    def type(self) -> Boolean: ...  # type: ignore[override]  # @memoized_property causes override issue
    operator: Callable[[Any, Any], Any] | Callable[[Incomplete], Incomplete] | None
    negate: Callable[[Any, Any], Any] | Callable[[Incomplete], Incomplete] | None
    modifier: Any
    wraps_column_expression: bool
    def __init__(
        self,
        element: ColumnElement[Incomplete],
        operator: Callable[[Any, Any], Any] | Callable[[Incomplete], Incomplete] | None,
        negate: Callable[[Any, Any], Any] | Callable[[Incomplete], Incomplete] | None,
    ) -> None: ...
    @property
    def wrapped_column_expression(self) -> ColumnElement[Incomplete]: ...  # type: ignore[override]
    def self_group(self, against: Unused = None) -> Self: ...  # type: ignore[override]  # supertype has overloads

class BinaryExpression(ColumnElement[Any]):
    __visit_name__: str
    left: ClauseElement | Grouping
    right: ClauseElement | Grouping
    operator: Callable[[object, object], Any]  # Same as operator.eq/ne
    @memoized_property
    def type(self) -> TypeEngine | None: ...
    negate: Callable[[object, object], Any] | None  # Same as operator.eq/ne
    modifiers: Any
    def __init__(
        self,
        left: ClauseElement,
        right: ClauseElement,
        operator: Callable[[object, object], Any],
        type_: TypeEngine | _type[TypeEngine] | None = None,
        negate: Callable[[object, object], Any] | None = None,
        modifiers: Incomplete | None = None,
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...
    @property
    def is_comparison(self) -> bool: ...
    @overload  # type: ignore[override]  # Actual return type
    def self_group(self, against: _AnyOperator) -> Grouping | Self: ...  # type: ignore[misc]  # supertype has more overloads
    @overload
    def self_group(self, against: object = None) -> Grouping: ...

class Slice(ColumnElement[Any]):
    __visit_name__: str
    start: Any
    stop: Any
    step: Any
    @memoized_property
    def type(self) -> NullType: ...  # type: ignore[override]  # @memoized_property causes override issue
    def __init__(self, start, stop, step, _name: Incomplete | None = None) -> None: ...
    # Argument `against` must be operator.getitem
    def self_group(  # type: ignore[override]
        self, against: Callable[[Sequence[_T], slice], Sequence[_T]] | Callable[[SupportsGetItem[_K, _V], _K], _V] = ...
    ) -> Self: ...

class IndexExpression(BinaryExpression):
    inherit_cache: bool

class GroupedElement(ClauseElement):
    __visit_name__: str
    def self_group(self, against: Unused = None) -> Self: ...

class Grouping(GroupedElement, ColumnElement[Any]):  # type: ignore[misc]  # Supertypes' self_group differs
    element: ClauseElement
    @memoized_property
    def type(self) -> TypeEngine | None: ...
    def __init__(self, element: ClauseElement) -> None: ...
    def __getattr__(self, attr: str): ...

RANGE_UNBOUNDED: Any
RANGE_CURRENT: Any

class Over(ColumnElement[Any]):
    __visit_name__: str
    order_by: ClauseList | None
    partition_by: ClauseList | None
    element: FunctionElement | WithinGroup
    range_: tuple[_symbol, _symbol] | None
    rows: tuple[_symbol, _symbol] | None
    def __init__(
        self,
        element: FunctionElement | WithinGroup,
        partition_by: _CoercibleElement | None = None,
        order_by: _CoercibleElement | None = None,
        range_: tuple[
            str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc | None,
            str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc | None,
        ]
        | None = None,
        rows: tuple[
            str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc | None,
            str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc | None,
        ]
        | None = None,
    ) -> None: ...
    def __reduce__(self): ...
    @memoized_property
    def type(self) -> Incomplete: ...

class WithinGroup(ColumnElement[Any]):
    __visit_name__: str
    order_by: ClauseList | None
    element: FunctionElement
    def __init__(self, element: FunctionElement, *order_by: _CoercibleElement) -> None: ...
    def __reduce__(self): ...
    def over(
        self,
        partition_by: _CoercibleElement | None = None,
        order_by: _CoercibleElement | None = None,
        range_: tuple[
            str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc | None,
            str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc | None,
        ]
        | None = None,
        rows: tuple[
            str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc | None,
            str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc | None,
        ]
        | None = None,
    ): ...
    @memoized_property
    def type(self) -> Incomplete: ...

class FunctionFilter(ColumnElement[Any]):
    __visit_name__: str
    criterion: Any
    func: FunctionElement
    def __init__(self, func: FunctionFilter, *criterion) -> None: ...
    def filter(self, *criterion) -> FunctionFilter: ...
    def over(
        self,
        partition_by: _CoercibleElement | None = None,
        order_by: _CoercibleElement | None = None,
        range_: tuple[
            str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc | None,
            str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc | None,
        ]
        | None = None,
        rows: tuple[
            str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc | None,
            str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc | None,
        ]
        | None = None,
    ): ...
    @overload  # type: ignore[override]  # Actual return type
    def self_group(self, against: _AnyOperator) -> Grouping | Self: ...  # type: ignore[misc]  # Actual return type
    @overload
    def self_group(self, against: object = None) -> Grouping: ...
    @memoized_property
    def type(self) -> Incomplete: ...

class Label(roles.LabeledColumnExprRole, ColumnElement[Any]):
    __visit_name__: str
    name: str | _anonymous_label
    key: str | _anonymous_label
    def __init__(
        self, name: str, element: ColumnElement[Incomplete], type_: TypeEngine | _type[TypeEngine] | None = None
    ) -> None: ...
    def __reduce__(self): ...
    @memoized_property
    def type(self) -> TypeEngine | None: ...
    @HasMemoized.memoized_attribute
    def element(self) -> ColumnElement[Incomplete]: ...
    @property
    def primary_key(self) -> bool: ...  # type: ignore[override]  # property overrides attribute
    @property
    def foreign_keys(self) -> list[ForeignKey]: ...  # type: ignore[override]  # property overrides attribute

class NamedColumn(ColumnElement[Any]):
    is_literal: bool
    table: Any
    @memoized_property
    def description(self) -> str: ...

class ColumnClause(roles.DDLReferredColumnRole, roles.LabeledColumnExprRole, roles.StrAsPlainColumnRole, Immutable, NamedColumn):
    table: Any
    is_literal: bool
    __visit_name__: str
    onupdate: Any
    default: Any
    server_default: Any
    server_onupdate: Any
    key: str
    name: str
    @memoized_property
    def type(self) -> TypeEngine | None: ...
    def __init__(
        self,
        text,
        type_: TypeEngine | _type[TypeEngine] | None = None,
        is_literal: bool = False,
        _selectable: Incomplete | None = None,
    ) -> None: ...
    def get_children(self, column_tables: bool = False, **kw): ...  # type: ignore[override]  # Different parameter name
    @property
    def entity_namespace(self): ...

class TableValuedColumn(NamedColumn):
    __visit_name__: str
    scalar_alias: Any
    key: str
    name: str
    @memoized_property
    def type(self) -> TypeEngine | None: ...
    def __init__(self, scalar_alias, type_: TypeEngine | None) -> None: ...

class CollationClause(ColumnElement[Any]):
    __visit_name__: str
    collation: Any
    def __init__(self, collation) -> None: ...

class _IdentifiedClause(Executable, ClauseElement):
    __visit_name__: str
    ident: Any
    def __init__(self, ident) -> None: ...

class SavepointClause(_IdentifiedClause):
    __visit_name__: str
    inherit_cache: bool

class RollbackToSavepointClause(_IdentifiedClause):
    __visit_name__: str
    inherit_cache: bool

class ReleaseSavepointClause(_IdentifiedClause):
    __visit_name__: str
    inherit_cache: bool

class quoted_name(util.MemoizedSlots, util.text_type):
    quote: bool | None
    @overload
    def __new__(cls, value: None, quote: Unused) -> None: ...  # type: ignore[misc]
    @overload
    def __new__(cls, value: object, quote: bool | None) -> Self: ...
    def __reduce__(self): ...

class AnnotatedColumnElement(Annotated):  # pyright: ignore[reportMissingTypeArgument]  # pytype issue
    def __init__(self, element: ColumnElement[Incomplete], values) -> None: ...
    @memoized_property
    def name(self) -> str: ...
    @memoized_property
    def table(self) -> TableClause: ...
    @memoized_property
    def key(self) -> str: ...
    @memoized_property
    def info(self): ...

class _truncated_label(quoted_name):
    @overload
    def __new__(cls, value: None, quote: Unused = None) -> None: ...  # type: ignore[misc]
    @overload
    def __new__(cls, value: object, quote: bool | None = None) -> Self: ...
    def __reduce__(self): ...
    def apply_map(self, map_: Unused) -> Self: ...

class conv(_truncated_label): ...

class _anonymous_label(_truncated_label):
    @classmethod
    def safe_construct(cls, seed, body, enclosing_label: Incomplete | None = None, sanitize_key: bool = False): ...
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def apply_map(self, map_): ...
