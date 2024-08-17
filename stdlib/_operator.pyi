import sys
from _typeshed import SupportsGetItem
from collections.abc import Callable, Container, Iterable, MutableMapping, MutableSequence, Sequence
from typing import Any, AnyStr, Generic, Protocol, SupportsAbs, SupportsIndex, TypeVar, final, overload
from typing_extensions import ParamSpec, TypeAlias, TypeVarTuple, Unpack, TypeIs

_R = TypeVar("_R")
_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_K = TypeVar("_K")
_V = TypeVar("_V")
_P = ParamSpec("_P")
_Ts = TypeVarTuple("_Ts")

# The following protocols return "Any" instead of bool, since the comparison
# operators can be overloaded to return an arbitrary object. For example,
# the numpy.array comparison dunders return another numpy.array.

class _SupportsDunderLT(Protocol):
    def __lt__(self, other: Any, /) -> Any: ...

class _SupportsDunderGT(Protocol):
    def __gt__(self, other: Any, /) -> Any: ...

class _SupportsDunderLE(Protocol):
    def __le__(self, other: Any, /) -> Any: ...

class _SupportsDunderGE(Protocol):
    def __ge__(self, other: Any, /) -> Any: ...

_SupportsComparison: TypeAlias = _SupportsDunderLE | _SupportsDunderGE | _SupportsDunderGT | _SupportsDunderLT

class _SupportsInversion(Protocol[_T_co]):
    def __invert__(self) -> _T_co: ...

class _SupportsNeg(Protocol[_T_co]):
    def __neg__(self) -> _T_co: ...

class _SupportsPos(Protocol[_T_co]):
    def __pos__(self) -> _T_co: ...

# All four comparison functions must have the same signature, or we get false-positive errors
def lt(a: _SupportsComparison, b: _SupportsComparison, /) -> Any: ...
def le(a: _SupportsComparison, b: _SupportsComparison, /) -> Any: ...
def eq(a: object, b: object, /) -> Any: ...
def ne(a: object, b: object, /) -> Any: ...
def ge(a: _SupportsComparison, b: _SupportsComparison, /) -> Any: ...
def gt(a: _SupportsComparison, b: _SupportsComparison, /) -> Any: ...
def not_(a: object, /) -> bool: ...
def truth(a: object, /) -> bool: ...
def is_(a: object, b: object, /) -> bool: ...
def is_not(a: object, b: object, /) -> bool: ...
def abs(a: SupportsAbs[_T], /) -> _T: ...
def add(a: Any, b: Any, /) -> Any: ...
def and_(a: Any, b: Any, /) -> Any: ...
def floordiv(a: Any, b: Any, /) -> Any: ...
def index(a: SupportsIndex, /) -> int: ...
def inv(a: _SupportsInversion[_T_co], /) -> _T_co: ...
def invert(a: _SupportsInversion[_T_co], /) -> _T_co: ...
def lshift(a: Any, b: Any, /) -> Any: ...
def mod(a: Any, b: Any, /) -> Any: ...
def mul(a: Any, b: Any, /) -> Any: ...
def matmul(a: Any, b: Any, /) -> Any: ...
def neg(a: _SupportsNeg[_T_co], /) -> _T_co: ...
def or_(a: Any, b: Any, /) -> Any: ...
def pos(a: _SupportsPos[_T_co], /) -> _T_co: ...
def pow(a: Any, b: Any, /) -> Any: ...
def rshift(a: Any, b: Any, /) -> Any: ...
def sub(a: Any, b: Any, /) -> Any: ...
def truediv(a: Any, b: Any, /) -> Any: ...
def xor(a: Any, b: Any, /) -> Any: ...
def concat(a: Sequence[_T], b: Sequence[_T], /) -> Sequence[_T]: ...
def contains(a: Container[object], b: object, /) -> bool: ...
def countOf(a: Iterable[object], b: object, /) -> int: ...
@overload
def delitem(a: MutableSequence[Any], b: SupportsIndex, /) -> None: ...
@overload
def delitem(a: MutableSequence[Any], b: slice, /) -> None: ...
@overload
def delitem(a: MutableMapping[_K, Any], b: _K, /) -> None: ...
@overload
def getitem(a: Sequence[_T], b: slice, /) -> Sequence[_T]: ...
@overload
def getitem(a: SupportsGetItem[_K, _V], b: _K, /) -> _V: ...
def indexOf(a: Iterable[_T], b: _T, /) -> int: ...
@overload
def setitem(a: MutableSequence[_T], b: SupportsIndex, c: _T, /) -> None: ...
@overload
def setitem(a: MutableSequence[_T], b: slice, c: Sequence[_T], /) -> None: ...
@overload
def setitem(a: MutableMapping[_K, _V], b: _K, c: _V, /) -> None: ...
def length_hint(obj: object, default: int = 0, /) -> int: ...
@final
class attrgetter(Generic[_T_co]):
    @overload
    def __new__(cls, attr: str, /) -> attrgetter[Any]: ...
    @overload
    def __new__(cls, attr: str, attr2: str, /) -> attrgetter[tuple[Any, Any]]: ...
    @overload
    def __new__(cls, attr: str, attr2: str, attr3: str, /) -> attrgetter[tuple[Any, Any, Any]]: ...
    @overload
    def __new__(cls, attr: str, attr2: str, attr3: str, attr4: str, /) -> attrgetter[tuple[Any, Any, Any, Any]]: ...
    @overload
    def __new__(cls, attr: str, /, *attrs: str) -> attrgetter[tuple[Any, ...]]: ...
    def __call__(self, obj: Any, /) -> _T_co: ...

@final
class itemgetter(Generic[_T_co]):
    @overload
    def __new__(cls, item: _T, /) -> itemgetter[_T]: ...
    @overload
    def __new__(cls, item1: _T1, item2: _T2, /, *items: Unpack[_Ts]) -> itemgetter[tuple[_T1, _T2, Unpack[_Ts]]]: ...
    # __key: _KT_contra in SupportsGetItem seems to be causing variance issues, ie:
    # TypeVar "_KT_contra@SupportsGetItem" is contravariant
    #   "tuple[int, int]" is incompatible with protocol "SupportsIndex"
    # preventing [_T_co, ...] instead of [Any, ...]
    #
    # A suspected mypy issue prevents using [..., _T] instead of [..., Any] here.
    # https://github.com/python/mypy/issues/14032
    def __call__(self, obj: SupportsGetItem[Any, Any]) -> Any: ...

@final
class methodcaller:
    def __init__(self, name: str, /, *args: Any, **kwargs: Any) -> None: ...
    def __call__(self, obj: Any) -> Any: ...

def iadd(a: Any, b: Any, /) -> Any: ...
def iand(a: Any, b: Any, /) -> Any: ...
def iconcat(a: Any, b: Any, /) -> Any: ...
def ifloordiv(a: Any, b: Any, /) -> Any: ...
def ilshift(a: Any, b: Any, /) -> Any: ...
def imod(a: Any, b: Any, /) -> Any: ...
def imul(a: Any, b: Any, /) -> Any: ...
def imatmul(a: Any, b: Any, /) -> Any: ...
def ior(a: Any, b: Any, /) -> Any: ...
def ipow(a: Any, b: Any, /) -> Any: ...
def irshift(a: Any, b: Any, /) -> Any: ...
def isub(a: Any, b: Any, /) -> Any: ...
def itruediv(a: Any, b: Any, /) -> Any: ...
def ixor(a: Any, b: Any, /) -> Any: ...

if sys.version_info >= (3, 11):
    def call(obj: Callable[_P, _R], /, *args: _P.args, **kwargs: _P.kwargs) -> _R: ...

def _compare_digest(a: AnyStr, b: AnyStr, /) -> bool: ...

if sys.version_info >= (3, 14):
    def is_none(a: Any | None, /) -> TypeIs[None]: ...
    def is_not_none(a: _T | None, /) -> TypeIs[_T]: ...
