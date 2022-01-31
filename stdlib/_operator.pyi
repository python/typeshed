import sys
from typing import (
    Any,
    AnyStr,
    Callable,
    Container,
    Generic,
    Iterable,
    Mapping,
    MutableMapping,
    MutableSequence,
    Protocol,
    Sequence,
    SupportsAbs,
    TypeVar,
    overload,
)
from typing_extensions import ParamSpec, SupportsIndex, final

_R = TypeVar("_R")
_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_K = TypeVar("_K")
_V = TypeVar("_V")
_P = ParamSpec("_P")

# The following protocols return "Any" instead of bool, since the comparison
# operators can be overloaded to return an arbitrary object. For example,
# the numpy.array comparison dunders return another numpy.array.

class _SupportsDunderLT(Protocol):
    def __lt__(self, __other: Any) -> Any: ...

class _SupportsDunderGT(Protocol):
    def __gt__(self, __other: Any) -> Any: ...

class _SupportsDunderLE(Protocol):
    def __le__(self, __other: Any) -> Any: ...

class _SupportsDunderGE(Protocol):
    def __ge__(self, __other: Any) -> Any: ...

_SupportsAnyComparison = Union[_SupportsDunderLE, _SupportsDunderGE, _SupportsDunderGT, _SupportsDunderLT]

class _SupportsInversion(Protocol[_T_co]):
    def __invert__(self) -> _T_co: ...

class _SupportsNeg(Protocol[_T_co]):
    def __neg__(self) -> _T_co: ...

class _SupportsPos(Protocol[_T_co]):
    def __pos__(self) -> _T_co: ...

# All four comparison functions must have the same signature, or we get false-positive errors
def lt(__a: _SupportsAnyComparison, __b: _SupportsAnyComparison) -> Any: ...
def le(__a: _SupportsAnyComparison, __b: _SupportsAnyComparison) -> Any: ...
def eq(__a: object, __b: object) -> Any: ...
def ne(__a: object, __b: object) -> Any: ...
def ge(__a: _SupportsAnyComparison, __b: _SupportsAnyComparison) -> Any: ...
def gt(__a: _SupportsAnyComparison, __b: _SupportsAnyComparison) -> Any: ...
def not_(__a: object) -> bool: ...
def truth(__a: object) -> bool: ...
def is_(__a: object, __b: object) -> bool: ...
def is_not(__a: object, __b: object) -> bool: ...
def abs(__a: SupportsAbs[_T]) -> _T: ...
def add(__a: Any, __b: Any) -> Any: ...
def and_(__a: Any, __b: Any) -> Any: ...
def floordiv(__a: Any, __b: Any) -> Any: ...
def index(__a: SupportsIndex) -> int: ...
def inv(__a: _SupportsInversion[_T_co]) -> _T_co: ...
def invert(__a: _SupportsInversion[_T_co]) -> _T_co: ...
def lshift(__a: Any, __b: Any) -> Any: ...
def mod(__a: Any, __b: Any) -> Any: ...
def mul(__a: Any, __b: Any) -> Any: ...
def matmul(__a: Any, __b: Any) -> Any: ...
def neg(__a: _SupportsNeg[_T_co]) -> _T_co: ...
def or_(__a: Any, __b: Any) -> Any: ...
def pos(__a: _SupportsPos[_T_co]) -> _T_co: ...
def pow(__a: Any, __b: Any) -> Any: ...
def rshift(__a: Any, __b: Any) -> Any: ...
def sub(__a: Any, __b: Any) -> Any: ...
def truediv(__a: Any, __b: Any) -> Any: ...
def xor(__a: Any, __b: Any) -> Any: ...
def concat(__a: Sequence[_T], __b: Sequence[_T]) -> Sequence[_T]: ...
def contains(__a: Container[object], __b: object) -> bool: ...
def countOf(__a: Iterable[object], __b: object) -> int: ...
@overload
def delitem(__a: MutableSequence[Any], __b: SupportsIndex) -> None: ...
@overload
def delitem(__a: MutableSequence[Any], __b: slice) -> None: ...
@overload
def delitem(__a: MutableMapping[_K, Any], __b: _K) -> None: ...
@overload
def getitem(__a: Sequence[_T], __b: SupportsIndex) -> _T: ...
@overload
def getitem(__a: Sequence[_T], __b: slice) -> Sequence[_T]: ...
@overload
def getitem(__a: Mapping[_K, _V], __b: _K) -> _V: ...
def indexOf(__a: Iterable[_T], __b: _T) -> int: ...
@overload
def setitem(__a: MutableSequence[_T], __b: SupportsIndex, __c: _T) -> None: ...
@overload
def setitem(__a: MutableSequence[_T], __b: slice, __c: Sequence[_T]) -> None: ...
@overload
def setitem(__a: MutableMapping[_K, _V], __b: _K, __c: _V) -> None: ...
def length_hint(__obj: object, __default: int = ...) -> int: ...
@final
class attrgetter(Generic[_T_co]):
    @overload
    def __new__(cls, attr: str) -> attrgetter[Any]: ...
    @overload
    def __new__(cls, attr: str, __attr2: str) -> attrgetter[tuple[Any, Any]]: ...
    @overload
    def __new__(cls, attr: str, __attr2: str, __attr3: str) -> attrgetter[tuple[Any, Any, Any]]: ...
    @overload
    def __new__(cls, attr: str, __attr2: str, __attr3: str, __attr4: str) -> attrgetter[tuple[Any, Any, Any, Any]]: ...
    @overload
    def __new__(cls, attr: str, *attrs: str) -> attrgetter[tuple[Any, ...]]: ...
    def __call__(self, obj: Any) -> _T_co: ...

@final
class itemgetter(Generic[_T_co]):
    @overload
    def __new__(cls, item: Any) -> itemgetter[Any]: ...
    @overload
    def __new__(cls, item: Any, __item2: Any) -> itemgetter[tuple[Any, Any]]: ...
    @overload
    def __new__(cls, item: Any, __item2: Any, __item3: Any) -> itemgetter[tuple[Any, Any, Any]]: ...
    @overload
    def __new__(cls, item: Any, __item2: Any, __item3: Any, __item4: Any) -> itemgetter[tuple[Any, Any, Any, Any]]: ...
    @overload
    def __new__(cls, item: Any, *items: Any) -> itemgetter[tuple[Any, ...]]: ...
    def __call__(self, obj: Any) -> _T_co: ...

@final
class methodcaller:
    def __init__(self, __name: str, *args: Any, **kwargs: Any) -> None: ...
    def __call__(self, obj: Any) -> Any: ...

def iadd(__a: Any, __b: Any) -> Any: ...
def iand(__a: Any, __b: Any) -> Any: ...
def iconcat(__a: Any, __b: Any) -> Any: ...
def ifloordiv(__a: Any, __b: Any) -> Any: ...
def ilshift(__a: Any, __b: Any) -> Any: ...
def imod(__a: Any, __b: Any) -> Any: ...
def imul(__a: Any, __b: Any) -> Any: ...
def imatmul(__a: Any, __b: Any) -> Any: ...
def ior(__a: Any, __b: Any) -> Any: ...
def ipow(__a: Any, __b: Any) -> Any: ...
def irshift(__a: Any, __b: Any) -> Any: ...
def isub(__a: Any, __b: Any) -> Any: ...
def itruediv(__a: Any, __b: Any) -> Any: ...
def ixor(__a: Any, __b: Any) -> Any: ...

if sys.version_info >= (3, 11):
    def call(__obj: Callable[_P, _R], *args: _P.args, **kwargs: _P.kwargs) -> _R: ...

def _compare_digest(__a: AnyStr, __b: AnyStr) -> bool: ...
