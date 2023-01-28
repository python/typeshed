from _typeshed import Incomplete, Self, SupportsGetItem
from collections.abc import Callable, Sequence
from typing import NoReturn, TypeVar, overload

from ...sql import expression, sqltypes
from ...sql.elements import BinaryExpression, Grouping
from ...sql.type_api import TypeEngine
from ...util.langhelpers import memoized_property

_T = TypeVar("_T")
_K = TypeVar("_K")
_V = TypeVar("_V")

def Any(other, arrexpr, operator=...): ...
def All(other, arrexpr, operator=...): ...

class array(expression.ClauseList, expression.ColumnElement[Incomplete]):
    __visit_name__: str
    stringify_dialect: str
    inherit_cache: bool
    @memoized_property
    def type(self) -> ARRAY: ...  # type: ignore[override]  # Is always assigned ARRAY
    def __init__(self, clauses, **kw) -> None: ...
    @overload  # type: ignore[override]  # Actual return type
    def self_group(  # type: ignore[misc]  # Actual return type
        self: Self,
        against: Callable[[Incomplete], Incomplete]
        | Callable[[Sequence[_V], slice], Sequence[_V]]
        | Callable[[SupportsGetItem[_K, _V], _K], _V],
    ) -> Grouping | Self: ...
    @overload
    def self_group(self: Self, against: object = ...) -> Self: ...

CONTAINS: Incomplete
CONTAINED_BY: Incomplete
OVERLAP: Incomplete

class ARRAY(sqltypes.ARRAY):
    class Comparator(sqltypes.ARRAY.Comparator[_T]):
        def contains(self, other: str, **kwargs) -> BinaryExpression: ...
        def contained_by(self, other) -> BinaryExpression: ...
        def overlap(self, other) -> BinaryExpression: ...
    comparator_factory: Callable[[Incomplete], Comparator[Incomplete]]
    item_type: TypeEngine
    as_tuple: bool
    dimensions: Incomplete
    zero_indexes: bool
    @overload
    def __init__(
        self,
        item_type: ARRAY,  # (Not[Array])
        as_tuple: bool = ...,
        dimensions: Incomplete | None = ...,
        zero_indexes: bool = ...,
    ) -> NoReturn: ...
    @overload
    def __init__(
        self,
        item_type: TypeEngine | type[TypeEngine],
        as_tuple: bool = ...,
        dimensions: Incomplete | None = ...,
        zero_indexes: bool = ...,
    ) -> None: ...
    @property
    def hashable(self): ...
    @property
    def python_type(self): ...
    def compare_values(self, x, y): ...
    def bind_expression(self, bindvalue): ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...
