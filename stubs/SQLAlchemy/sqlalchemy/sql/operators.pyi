from _typeshed import Incomplete
from collections.abc import Container, Iterable
from operator import truediv
from typing import Any, Generic, TypeVar

_T = TypeVar("_T")

div = truediv

class Operators:
    def __and__(self, other): ...
    def __or__(self, other): ...
    def __invert__(self): ...
    def op(self, opstring, precedence: int = ..., is_comparison: bool = ..., return_type: Incomplete | None = ...): ...
    def bool_op(self, opstring, precedence: int = ...): ...
    def operate(self, op, *other, **kwargs): ...
    def reverse_operate(self, op, other, **kwargs): ...

class custom_op:
    __name__: str
    opstring: Any
    precedence: Any
    is_comparison: Any
    natural_self_precedent: Any
    eager_grouping: Any
    return_type: Any
    def __init__(
        self,
        opstring,
        precedence: int = ...,
        is_comparison: bool = ...,
        return_type: Incomplete | None = ...,
        natural_self_precedent: bool = ...,
        eager_grouping: bool = ...,
    ) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self) -> int: ...
    def __call__(self, left, right, **kw): ...

class ColumnOperators(Operators, Generic[_T]):
    timetuple: Any
    def __lt__(self, other: _T | ColumnOperators[_T] | None) -> ColumnOperators[_T]: ...
    def __le__(self, other: _T | ColumnOperators[_T] | None) -> ColumnOperators[_T]: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: _T | ColumnOperators[_T] | None) -> ColumnOperators[_T]: ...  # type: ignore[override]
    def __ne__(self, other: _T | ColumnOperators[_T] | None) -> ColumnOperators[_T]: ...  # type: ignore[override]
    def is_distinct_from(self, other) -> ColumnOperators[_T]: ...
    def is_not_distinct_from(self, other) -> ColumnOperators[_T]: ...
    def isnot_distinct_from(self, other) -> ColumnOperators[_T]: ...
    def __gt__(self, other: _T | ColumnOperators[_T] | None) -> ColumnOperators[_T]: ...
    def __ge__(self, other: _T | ColumnOperators[_T] | None) -> ColumnOperators[_T]: ...
    def __neg__(self) -> ColumnOperators[_T]: ...
    def __contains__(self, other) -> ColumnOperators[_T]: ...
    def __getitem__(self, index: int) -> ColumnOperators[_T]: ...
    def __lshift__(self, other) -> ColumnOperators[_T]: ...
    def __rshift__(self, other) -> ColumnOperators[_T]: ...
    def concat(self, other: _T | ColumnOperators[_T] | None) -> ColumnOperators[_T]: ...
    def like(self, other: _T, escape: str | None = ...) -> ColumnOperators[_T]: ...
    def ilike(self, other: _T, escape: str | None = ...) -> ColumnOperators[_T]: ...
    def in_(self, other: Container[_T] | Iterable[_T]) -> ColumnOperators[_T]: ...
    def not_in(self, other: Container[_T] | Iterable[_T]) -> ColumnOperators[_T]: ...
    def notin_(self, other: Container[_T] | Iterable[_T]) -> ColumnOperators[_T]: ...
    def not_like(self, other: _T, escape: str | None = ...) -> ColumnOperators[_T]: ...
    def notlike(self, other: _T, escape: str | None = ...) -> ColumnOperators[_T]: ...
    def not_ilike(self, other: _T, escape: str | None = ...) -> ColumnOperators[_T]: ...
    def notilike(self, other: _T, escape: str | None = ...) -> ColumnOperators[_T]: ...
    def is_(self, other: _T) -> ColumnOperators[_T]: ...
    def is_not(self, other: _T) -> ColumnOperators[_T]: ...
    def isnot(self, other: _T) -> ColumnOperators[_T]: ...
    def startswith(self, other: str, **kwargs) -> ColumnOperators[_T]: ...
    def endswith(self, other: str, **kwargs) -> ColumnOperators[_T]: ...
    def contains(self, other: str, **kwargs) -> ColumnOperators[_T]: ...
    def match(self, other: str, **kwargs) -> ColumnOperators[_T]: ...
    def regexp_match(self, pattern, flags: Incomplete | None = ...) -> ColumnOperators[_T]: ...
    def regexp_replace(self, pattern, replacement, flags: Incomplete | None = ...) -> ColumnOperators[_T]: ...
    def desc(self) -> ColumnOperators[_T]: ...
    def asc(self) -> ColumnOperators[_T]: ...
    def nulls_first(self) -> ColumnOperators[_T]: ...
    def nullsfirst(self) -> ColumnOperators[_T]: ...
    def nulls_last(self) -> ColumnOperators[_T]: ...
    def nullslast(self) -> ColumnOperators[_T]: ...
    def collate(self, collation) -> ColumnOperators[_T]: ...
    def __radd__(self, other) -> ColumnOperators[_T]: ...
    def __rsub__(self, other) -> ColumnOperators[_T]: ...
    def __rmul__(self, other) -> ColumnOperators[_T]: ...
    def __rdiv__(self, other) -> ColumnOperators[_T]: ...
    def __rmod__(self, other) -> ColumnOperators[_T]: ...
    def between(self, cleft, cright, symmetric: bool = ...) -> ColumnOperators[_T]: ...
    def distinct(self) -> ColumnOperators[_T]: ...
    def any_(self) -> ColumnOperators[_T]: ...
    def all_(self) -> ColumnOperators[_T]: ...
    def __add__(self, other) -> ColumnOperators[_T]: ...
    def __sub__(self, other) -> ColumnOperators[_T]: ...
    def __mul__(self, other) -> ColumnOperators[_T]: ...
    def __div__(self, other) -> ColumnOperators[_T]: ...
    def __mod__(self, other) -> ColumnOperators[_T]: ...
    def __truediv__(self, other) -> ColumnOperators[_T]: ...
    def __rtruediv__(self, other) -> ColumnOperators[_T]: ...

def commutative_op(fn): ...
def comparison_op(fn): ...
def from_() -> None: ...
def function_as_comparison_op() -> None: ...
def as_() -> None: ...
def exists() -> None: ...
def is_true(a) -> None: ...

istrue = is_true

def is_false(a) -> None: ...

isfalse = is_false

def is_distinct_from(a, b): ...
def is_not_distinct_from(a, b): ...

isnot_distinct_from = is_not_distinct_from

def is_(a, b): ...
def is_not(a, b): ...

isnot = is_not

def collate(a, b): ...
def op(a, opstring, b): ...
def like_op(a, b, escape: Incomplete | None = ...): ...
def not_like_op(a, b, escape: Incomplete | None = ...): ...

notlike_op = not_like_op

def ilike_op(a, b, escape: Incomplete | None = ...): ...
def not_ilike_op(a, b, escape: Incomplete | None = ...): ...

notilike_op = not_ilike_op

def between_op(a, b, c, symmetric: bool = ...): ...
def not_between_op(a, b, c, symmetric: bool = ...): ...

notbetween_op = not_between_op

def in_op(a, b): ...
def not_in_op(a, b): ...

notin_op = not_in_op

def distinct_op(a): ...
def any_op(a): ...
def all_op(a): ...
def startswith_op(a, b, escape: Incomplete | None = ..., autoescape: bool = ...): ...
def not_startswith_op(a, b, escape: Incomplete | None = ..., autoescape: bool = ...): ...

notstartswith_op = not_startswith_op

def endswith_op(a, b, escape: Incomplete | None = ..., autoescape: bool = ...): ...
def not_endswith_op(a, b, escape: Incomplete | None = ..., autoescape: bool = ...): ...

notendswith_op = not_endswith_op

def contains_op(a, b, escape: Incomplete | None = ..., autoescape: bool = ...): ...
def not_contains_op(a, b, escape: Incomplete | None = ..., autoescape: bool = ...): ...

notcontains_op = not_contains_op

def match_op(a, b, **kw): ...
def regexp_match_op(a, b, flags: Incomplete | None = ...): ...
def not_regexp_match_op(a, b, flags: Incomplete | None = ...): ...
def regexp_replace_op(a, b, replacement, flags: Incomplete | None = ...): ...
def not_match_op(a, b, **kw): ...

notmatch_op = not_match_op

def comma_op(a, b) -> None: ...
def filter_op(a, b) -> None: ...
def concat_op(a, b): ...
def desc_op(a): ...
def asc_op(a): ...
def nulls_first_op(a): ...

nullsfirst_op = nulls_first_op

def nulls_last_op(a): ...

nullslast_op = nulls_last_op

def json_getitem_op(a, b) -> None: ...
def json_path_getitem_op(a, b) -> None: ...
def is_comparison(op) -> bool: ...
def is_commutative(op) -> bool: ...
def is_ordering_modifier(op) -> bool: ...
def is_natural_self_precedent(op) -> bool: ...
def is_boolean(op) -> bool: ...
def mirror(op): ...
def is_associative(op) -> bool: ...
def is_precedent(operator, against) -> bool: ...