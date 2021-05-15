import sys
from typing import (
    Any,
    Container,
    Generic,
    Mapping,
    MutableMapping,
    MutableSequence,
    Sequence,
    SupportsAbs,
    Tuple,
    TypeVar,
    overload,
)

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_K = TypeVar("_K")
_V = TypeVar("_V")

def lt(__a: Any, __b: Any) -> Any: ...
def le(__a: Any, __b: Any) -> Any: ...
def eq(__a: Any, __b: Any) -> Any: ...
def ne(__a: Any, __b: Any) -> Any: ...
def ge(__a: Any, __b: Any) -> Any: ...
def gt(__a: Any, __b: Any) -> Any: ...
def __lt__(a: Any, b: Any) -> Any: ...
def __le__(a: Any, b: Any) -> Any: ...
def __eq__(a: Any, b: Any) -> Any: ...
def __ne__(a: Any, b: Any) -> Any: ...
def __ge__(a: Any, b: Any) -> Any: ...
def __gt__(a: Any, b: Any) -> Any: ...
def not_(__a: Any) -> bool: ...
def __not__(a: Any) -> bool: ...
def truth(__a: Any) -> bool: ...
def is_(__a: Any, __b: Any) -> bool: ...
def is_not(__a: Any, __b: Any) -> bool: ...
def abs(__a: SupportsAbs[_T]) -> _T: ...
def __abs__(a: SupportsAbs[_T]) -> _T: ...
def add(__a: Any, __b: Any) -> Any: ...
def __add__(a: Any, b: Any) -> Any: ...
def and_(__a: Any, __b: Any) -> Any: ...
def __and__(a: Any, b: Any) -> Any: ...

def floordiv(__a: Any, __b: Any) -> Any: ...
def __floordiv__(a: Any, b: Any) -> Any: ...
def index(__a: Any) -> int: ...
def __index__(a: Any) -> int: ...
def inv(__a: Any) -> Any: ...
def invert(__a: Any) -> Any: ...
def __inv__(a: Any) -> Any: ...
def __invert__(a: Any) -> Any: ...
def lshift(__a: Any, __b: Any) -> Any: ...
def __lshift__(a: Any, b: Any) -> Any: ...
def mod(__a: Any, __b: Any) -> Any: ...
def __mod__(a: Any, b: Any) -> Any: ...
def mul(__a: Any, __b: Any) -> Any: ...
def __mul__(a: Any, b: Any) -> Any: ...

def matmul(__a: Any, __b: Any) -> Any: ...
def __matmul__(a: Any, b: Any) -> Any: ...

def neg(__a: Any) -> Any: ...
def __neg__(a: Any) -> Any: ...
def or_(__a: Any, __b: Any) -> Any: ...
def __or__(a: Any, b: Any) -> Any: ...
def pos(__a: Any) -> Any: ...
def __pos__(a: Any) -> Any: ...
def pow(__a: Any, __b: Any) -> Any: ...
def __pow__(a: Any, b: Any) -> Any: ...
def rshift(__a: Any, __b: Any) -> Any: ...
def __rshift__(a: Any, b: Any) -> Any: ...
def sub(__a: Any, __b: Any) -> Any: ...
def __sub__(a: Any, b: Any) -> Any: ...
def truediv(__a: Any, __b: Any) -> Any: ...
def __truediv__(a: Any, b: Any) -> Any: ...
def xor(__a: Any, __b: Any) -> Any: ...
def __xor__(a: Any, b: Any) -> Any: ...
def concat(__a: Sequence[_T], __b: Sequence[_T]) -> Sequence[_T]: ...
def __concat__(a: Sequence[_T], b: Sequence[_T]) -> Sequence[_T]: ...
def contains(__a: Container[Any], __b: Any) -> bool: ...
def __contains__(a: Container[Any], b: Any) -> bool: ...
def countOf(__a: Container[Any], __b: Any) -> int: ...
@overload
def delitem(__a: MutableSequence[Any], __b: int) -> None: ...
@overload
def delitem(__a: MutableSequence[Any], __b: slice) -> None: ...
@overload
def delitem(__a: MutableMapping[_K, Any], __b: _K) -> None: ...
@overload
def __delitem__(a: MutableSequence[Any], b: int) -> None: ...
@overload
def __delitem__(a: MutableSequence[Any], b: slice) -> None: ...
@overload
def __delitem__(a: MutableMapping[_K, Any], b: _K) -> None: ...

@overload
def getitem(__a: Sequence[_T], __b: int) -> _T: ...
@overload
def getitem(__a: Sequence[_T], __b: slice) -> Sequence[_T]: ...
@overload
def getitem(__a: Mapping[_K, _V], __b: _K) -> _V: ...
@overload
def __getitem__(a: Sequence[_T], b: int) -> _T: ...
@overload
def __getitem__(a: Sequence[_T], b: slice) -> Sequence[_T]: ...
@overload
def __getitem__(a: Mapping[_K, _V], b: _K) -> _V: ...

def indexOf(__a: Sequence[_T], __b: _T) -> int: ...

@overload
def setitem(__a: MutableSequence[_T], __b: int, __c: _T) -> None: ...
@overload
def setitem(__a: MutableSequence[_T], __b: slice, __c: Sequence[_T]) -> None: ...
@overload
def setitem(__a: MutableMapping[_K, _V], __b: _K, __c: _V) -> None: ...
@overload
def __setitem__(a: MutableSequence[_T], b: int, c: _T) -> None: ...
@overload
def __setitem__(a: MutableSequence[_T], b: slice, c: Sequence[_T]) -> None: ...
@overload
def __setitem__(a: MutableMapping[_K, _V], b: _K, c: _V) -> None: ...

def length_hint(__obj: Any, __default: int = ...) -> int: ...

class attrgetter(Generic[_T_co]):
    @overload
    def __new__(cls, attr: str) -> attrgetter[Any]: ...
    @overload
    def __new__(cls, attr: str, __attr2: str) -> attrgetter[Tuple[Any, Any]]: ...
    @overload
    def __new__(cls, attr: str, __attr2: str, __attr3: str) -> attrgetter[Tuple[Any, Any, Any]]: ...
    @overload
    def __new__(cls, attr: str, __attr2: str, __attr3: str, __attr4: str) -> attrgetter[Tuple[Any, Any, Any, Any]]: ...
    @overload
    def __new__(cls, attr: str, *attrs: str) -> attrgetter[Tuple[Any, ...]]: ...
    def __call__(self, obj: Any) -> _T_co: ...

class itemgetter(Generic[_T_co]):
    @overload
    def __new__(cls, item: Any) -> itemgetter[Any]: ...
    @overload
    def __new__(cls, item: Any, __item2: Any) -> itemgetter[Tuple[Any, Any]]: ...
    @overload
    def __new__(cls, item: Any, __item2: Any, __item3: Any) -> itemgetter[Tuple[Any, Any, Any]]: ...
    @overload
    def __new__(cls, item: Any, __item2: Any, __item3: Any, __item4: Any) -> itemgetter[Tuple[Any, Any, Any, Any]]: ...
    @overload
    def __new__(cls, item: Any, *items: Any) -> itemgetter[Tuple[Any, ...]]: ...
    def __call__(self, obj: Any) -> _T_co: ...

class methodcaller:
    def __init__(self, __name: str, *args: Any, **kwargs: Any) -> None: ...
    def __call__(self, obj: Any) -> Any: ...

def iadd(__a: Any, __b: Any) -> Any: ...
def __iadd__(a: Any, b: Any) -> Any: ...
def iand(__a: Any, __b: Any) -> Any: ...
def __iand__(a: Any, b: Any) -> Any: ...
def iconcat(__a: Any, __b: Any) -> Any: ...
def __iconcat__(a: Any, b: Any) -> Any: ...

def ifloordiv(__a: Any, __b: Any) -> Any: ...
def __ifloordiv__(a: Any, b: Any) -> Any: ...
def ilshift(__a: Any, __b: Any) -> Any: ...
def __ilshift__(a: Any, b: Any) -> Any: ...
def imod(__a: Any, __b: Any) -> Any: ...
def __imod__(a: Any, b: Any) -> Any: ...
def imul(__a: Any, __b: Any) -> Any: ...
def __imul__(a: Any, b: Any) -> Any: ...

def imatmul(__a: Any, __b: Any) -> Any: ...
def __imatmul__(a: Any, b: Any) -> Any: ...

def ior(__a: Any, __b: Any) -> Any: ...
def __ior__(a: Any, b: Any) -> Any: ...
def ipow(__a: Any, __b: Any) -> Any: ...
def __ipow__(a: Any, b: Any) -> Any: ...

def irshift(__a: Any, __b: Any) -> Any: ...
def __irshift__(a: Any, b: Any) -> Any: ...
def isub(__a: Any, __b: Any) -> Any: ...
def __isub__(a: Any, b: Any) -> Any: ...
def itruediv(__a: Any, __b: Any) -> Any: ...
def __itruediv__(a: Any, b: Any) -> Any: ...
def ixor(__a: Any, __b: Any) -> Any: ...
def __ixor__(a: Any, b: Any) -> Any: ...

