from _operator import _SupportsComparison
from _typeshed import Incomplete, SupportsGetItem, Unused
from collections.abc import Callable, Container, Iterable, Mapping
from typing import Any, Generic, NoReturn, TypeVar, overload
from typing_extensions import ParamSpec, Self

from .. import util
from ..engine.interfaces import Dialect
from ..sql.coercions import _CoercibleElement
from ..sql.elements import BinaryExpression, BindParameter, BooleanClauseList, CollectionAggregate, ColumnElement, UnaryExpression
from ..sql.sqltypes import Boolean, Indexable, Integer, MatchType, NullType, String, TableValueType
from . import operators
from .base import SchemaEventTarget
from .visitors import Traversible, TraversibleType

_T = TypeVar("_T")
_P = ParamSpec("_P")

BOOLEANTYPE: Boolean
INTEGERTYPE: Integer
NULLTYPE: NullType
STRINGTYPE: String
MATCHTYPE: MatchType
INDEXABLE: type[Indexable]
TABLEVALUE: TableValueType

class TypeEngine(Traversible):
    class Comparator(operators.ColumnOperators[_T], Generic[_T]):
        default_comparator: Any
        def __clause_element__(self): ...
        expr: Any
        type: Incomplete
        def __init__(self, expr) -> None: ...
        def __reduce__(self): ...
        # Uses sql.default_comparator.operator_lookup[op.__name__][0] instead of calling the op parameter directly
        def operate(self, op: operators._AnyOperator, *other, **kwargs): ...
        def reverse_operate(self, op: operators._AnyOperator, other, **kwargs): ...
        # ALL of the methods below use self.operate in ColumnOperators.
        # This means we must redefine ALL of those methods to match the overriden self.operate.
        # TODO: Parameters have not been validated. For now they're the same as supertype
        def __invert__(self) -> UnaryExpression: ...
        def __and__(self, other: _CoercibleElement) -> BooleanClauseList | ColumnElement[Incomplete]: ...
        def __or__(self, other: _CoercibleElement) -> BooleanClauseList | ColumnElement[Incomplete]: ...
        def is_distinct_from(self, other) -> BinaryExpression: ...
        def is_not_distinct_from(self, other) -> BinaryExpression: ...
        def concat(self, other: _T | operators.ColumnOperators[_T] | None) -> BinaryExpression: ...
        def like(self, other: _T, escape: str | None = ...) -> BinaryExpression: ...
        def ilike(self, other: _T, escape: str | None = ...) -> BinaryExpression: ...
        def in_(self, other: Container[_T] | Iterable[_T]) -> BinaryExpression: ...
        def not_in(self, other: Container[_T] | Iterable[_T]) -> BinaryExpression: ...
        def not_like(self, other: _T, escape: str | None = ...) -> BinaryExpression: ...
        def not_ilike(self, other: _T, escape: str | None = ...) -> BinaryExpression: ...
        def is_(self, other: _T) -> BinaryExpression: ...
        def is_not(self, other: _T) -> BinaryExpression: ...
        def startswith(self, other: str, **kwargs) -> BinaryExpression: ...
        def endswith(self, other: str, **kwargs) -> BinaryExpression: ...
        def contains(self, other: str, **kwargs) -> BinaryExpression: ...
        def match(self, other: str, **kwargs) -> BinaryExpression: ...
        def regexp_match(self, pattern, flags: Incomplete | None = ...) -> BinaryExpression: ...
        def regexp_replace(self, pattern, replacement, flags: Incomplete | None = ...) -> BinaryExpression: ...
        def collate(self, collation) -> BinaryExpression: ...
        def between(self, cleft, cright, symmetric: bool = ...) -> BinaryExpression: ...
        def desc(self) -> UnaryExpression: ...
        def asc(self) -> UnaryExpression: ...
        def nulls_first(self) -> UnaryExpression: ...
        def nulls_last(self) -> UnaryExpression: ...
        def distinct(self) -> UnaryExpression: ...
        def any_(self) -> CollectionAggregate: ...
        def all_(self) -> CollectionAggregate: ...
        isnot_distinct_from = is_not_distinct_from
        isnot = is_not
        notin_ = not_in
        notlike = not_like
        notilike = not_ilike
        nullsfirst = nulls_first
        nullslast = nulls_last
        def __eq__(self, other: object) -> BinaryExpression: ...  # type: ignore[override]
        def __ne__(self, other: object) -> BinaryExpression: ...  # type: ignore[override]
        def __ge__(self, other: _SupportsComparison) -> BinaryExpression: ...
        def __gt__(self, other: _SupportsComparison) -> BinaryExpression: ...
        def __le__(self, other: _SupportsComparison) -> BinaryExpression: ...
        def __lt__(self, other: _SupportsComparison) -> BinaryExpression: ...
        def __contains__(self, other: Unused) -> NoReturn: ...
        def __lshift__(self, other: Unused) -> NoReturn | BinaryExpression: ...
        def __rshift__(self, other: Unused) -> NoReturn | BinaryExpression: ...
        def __add__(self, other) -> BinaryExpression: ...
        def __radd__(self, other) -> BinaryExpression: ...
        def __mod__(self, other) -> BinaryExpression: ...
        def __rmod__(self, other) -> BinaryExpression: ...
        def __mul__(self, other) -> BinaryExpression: ...
        def __rmul__(self, other) -> BinaryExpression: ...
        def __sub__(self, other) -> BinaryExpression: ...
        def __rsub__(self, other) -> BinaryExpression: ...
        def __div__(self, other) -> BinaryExpression: ...
        def __rdiv__(self, other) -> BinaryExpression: ...
        def __truediv__(self, other) -> BinaryExpression: ...
        def __rtruediv__(self, other) -> BinaryExpression: ...
        def __neg__(self) -> UnaryExpression: ...
        def __getitem__(self, index: SupportsGetItem[Any, _T]) -> BinaryExpression: ...  # no __b means Any key type is viable
    hashable: bool
    comparator_factory: Callable[[Incomplete], Comparator[Incomplete]]
    sort_key_function: Any
    should_evaluate_none: bool
    def evaluates_none(self) -> Self: ...
    def copy(self, **kw: Unused) -> Self: ...
    def compare_against_backend(self, dialect: Dialect, conn_type): ...
    def copy_value(self, value: _T) -> _T: ...
    def literal_processor(self, dialect: Dialect) -> Callable[..., Incomplete] | None: ...
    def bind_processor(self, dialect: Dialect) -> Callable[..., Incomplete] | None: ...
    def result_processor(self, dialect: Dialect, coltype) -> Callable[..., Incomplete] | None: ...
    def column_expression(self, colexpr: str | ColumnElement[_T]) -> ColumnElement[_T] | None: ...
    def bind_expression(self, bindvalue: BindParameter[Incomplete]) -> Incomplete | None: ...
    def compare_values(self, x: object, y: object) -> bool: ...
    def get_dbapi_type(self, dbapi) -> Incomplete | None: ...
    @property
    def python_type(self) -> type: ...
    def with_variant(self, type_: type[TypeEngine] | TypeEngine, dialect_name: str) -> Variant: ...
    def as_generic(self, allow_nulltype: bool = ...): ...
    def dialect_impl(self, dialect: Dialect): ...
    def adapt(self, cls: type[_T], **kw) -> _T: ...
    def coerce_compared_value(self, op: Unused, value) -> TypeEngine | Self: ...
    def compile(self, dialect: Dialect | None = ...): ...

class VisitableCheckKWArg(util.EnsureKWArgType, TraversibleType): ...

class ExternalType:
    cache_ok: Any

class UserDefinedType(ExternalType, TypeEngine, metaclass=VisitableCheckKWArg):
    __visit_name__: str
    ensure_kwarg: str
    def coerce_compared_value(self, op: Unused, value: Unused) -> Self: ...

class Emulated:
    def adapt_to_emulated(self, impltype: type[Incomplete], **kw): ...
    def adapt(self, impltype: type[Incomplete], **kw): ...

class NativeForEmulated:
    @classmethod
    def adapt_native_to_emulated(cls, impl, **kw): ...
    @classmethod
    def adapt_emulated_to_native(cls, impl: Unused, **kw) -> Self: ...

class TypeDecorator(ExternalType, SchemaEventTarget, TypeEngine):
    __visit_name__: str
    impl: Any
    def __init__(self, *args, **kwargs) -> None: ...
    coerce_to_is_types: tuple[type[Incomplete], ...]

    class Comparator(TypeEngine.Comparator[_T]):
        def operate(self, op: Callable[_P, _T], *other: _P.args, **kwargs: _P.kwargs) -> _T: ...  # type: ignore[override]  # _T doesn't match
        def reverse_operate(self, op: Callable[..., _T], other, **kwargs) -> _T: ...  # type: ignore[override]  # _T doesn't match

    @property
    def comparator_factory(self) -> type[TypeDecorator.Comparator[Incomplete]]: ...  # type: ignore[override]  # supertype is attribute
    def type_engine(self, dialect: Dialect) -> TypeEngine: ...
    def load_dialect_impl(self, dialect: Dialect) -> TypeEngine: ...
    def __getattr__(self, key: str): ...
    def process_literal_param(self, value, dialect: Dialect) -> str | None: ...
    def process_bind_param(self, value, dialect: Dialect) -> str | None: ...
    def process_result_value(self, value, dialect: Dialect) -> Incomplete | None: ...
    def literal_processor(self, dialect: Dialect) -> Callable[[Incomplete | None], str | None]: ...
    def bind_processor(self, dialect: Dialect) -> Callable[[Incomplete | None], str | None]: ...
    def result_processor(self, dialect: Dialect, coltype) -> Callable[[Incomplete | None], Incomplete | None]: ...
    def bind_expression(self, bindparam): ...
    def column_expression(self, column): ...
    def coerce_compared_value(self, op: Unused, value: Unused) -> Self | TypeEngine: ...
    def copy(self, **kw: Unused) -> Self: ...
    def get_dbapi_type(self, dbapi): ...
    def compare_values(self, x, y) -> bool: ...
    @property
    def sort_key_function(self): ...

class Variant(TypeDecorator):
    cache_ok: bool
    impl: Any
    mapping: Mapping[str, TypeEngine]
    def __init__(self, base: TypeEngine, mapping: Mapping[str, TypeEngine]) -> None: ...
    def coerce_compared_value(self, operator, value) -> Self | TypeEngine: ...
    def load_dialect_impl(self, dialect: Dialect) -> TypeEngine: ...
    def with_variant(  # type: ignore[override]  # supertype ensures type[TypeEngine] is instanciated
        self, type_: TypeEngine, dialect_name: str
    ) -> Variant: ...
    @property
    def comparator_factory(self) -> type: ...  # type: ignore[override]  # supertype is attribute

@overload
def to_instance(typeobj: None, *arg: Unused, **kw: Unused) -> None: ...
@overload
def to_instance(typeobj: Callable[_P, _T], *arg: _P.args, **kw: _P.kwargs) -> _T: ...
@overload
def to_instance(typeobj: _T, *arg: Unused, **kw: Unused) -> _T: ...
def adapt_type(typeobj, colspecs: Mapping[type[Incomplete], Incomplete]): ...
