# Stubs for operator

from typing import (
    Any, Callable, Container, Mapping, MutableSequence, Sequence, SupportsAbs, Tuple,
    TypeVar, overload,
)
import sys


_K = TypeVar('_K')
_T = TypeVar('_T')


def lt(a: Any, b: Any) -> Any: ...
def le(a: Any, b: Any) -> Any: ...
def eq(a: Any, b: Any) -> Any: ...
def ne(a: Any, b: Any) -> Any: ...
def ge(a: Any, b: Any) -> Any: ...
def gt(a: Any, b: Any) -> Any: ...
def __lt__(a: Any, b: Any) -> Any: ...
def __le__(a: Any, b: Any) -> Any: ...
def __eq__(a: Any, b: Any) -> Any: ...
def __ne__(a: Any, b: Any) -> Any: ...
def __ge__(a: Any, b: Any) -> Any: ...
def __gt__(a: Any, b: Any) -> Any: ...

def not_(obj: Any) -> bool: ...
def __not__(obj: Any) -> bool: ...

def truth(x: Any) -> bool: ...
def is_(a: Any, b: Any) -> bool: ...
def is_not(a: Any, b: Any) -> bool: ...

def abs(x: SupportsAbs) -> Any: ...
def __abs__(a: SupportsAbs) -> Any: ...

def add(a: Any, b: Any) -> Any: ...
def __add__(a: Any, b: Any) -> Any: ...

def and_(a: Any, b: Any) -> Any: ...
def __and__(a: Any, b: Any) -> Any: ...

def floordiv(a: Any, b: Any) -> Any: ...
def __floordiv__(a: Any, b: Any) -> Any: ...

def index(x: Any) -> int: ...
def __index__(x: Any) -> int: ...

def inv(x: Any) -> Any: ...
def invert(x: Any) -> Any: ...
def __inv__(x: Any) -> Any: ...
def __invert__(x: Any) -> Any: ...

def lshift(a: Any, b: Any) -> Any: ...
def __lshift__(a: Any, b: Any) -> Any: ...

def mod(a: Any, b: Any) -> Any: ...
def __mod__(a: Any, b: Any) -> Any: ...

def mul(a: Any, b: Any) -> Any: ...
def __mul__(a: Any, b: Any) -> Any: ...

if sys.version_info >= (3,5):
    def matmul(a: Any, b: Any) -> Any: ...
    def __matmul__(a: Any, b: Any) -> Any: ...

def neg(x: Any) -> Any: ...
def __neg__(x: Any) -> Any: ...

def or_(a: Any, b: Any) -> Any: ...
def __or__(a: Any, b: Any) -> Any: ...

def pos(x: Any) -> Any: ...
def __pos__(x: Any) -> Any: ...

def pow(a: Any, b: Any) -> Any: ...
def __pow__(a: Any, b: Any) -> Any: ...

def rshift(a: Any, b: Any) -> Any: ...
def __rshift__(a: Any, b: Any) -> Any: ...

def sub(a: Any, b: Any) -> Any: ...
def __sub__(a: Any, b: Any) -> Any: ...

def truediv(a: Any, b: Any) -> Any: ...
def __truediv__(a: Any, b: Any) -> Any: ...

def xor(a: Any, b: Any) -> Any: ...
def __xor__(a: Any, b: Any) -> Any: ...

def concat(a: Sequence[_T], b: Sequence[_T]) -> Sequence[_T]: ...
def __concat__(a: Sequence[_T], b: Sequence[_T]) -> Sequence[_T]: ...

def contains(a: Container[Any], b: Any) -> bool: ...
def __contains__(a: Container[Any], b: Any) -> bool: ...

def countOf(a: Container[Any], b: Any) -> int: ...

def delitem(a: Container[_T], b: _T) -> None: ...
def __delitem__(a: Any, b: Any) -> None: ...

def getitem(a: Any, b: Any) -> Any: ...
def __getitem__(a: Any, b: Any) -> Any: ...

def indexOf(a: Sequence[_T], b: _T) -> int: ...

def setitem(a: Any, b: Any, c: Any) -> None: ...
def __setitem__(a: Any, b: Any, c: Any) -> None: ...

if sys.version_info >= (3, 4):
    def length_hint(obj: Any, default: int = ...) -> int: ...

@overload
def attrgetter(attr: str) -> Callable[[Any], Any]: ...
@overload
def attrgetter(*attrs: str) -> Callable[[Any], Tuple[Any, ...]]: ...

@overload
def itemgetter(item: int) -> Callable[[Any], Any]: ...
@overload
def itemgetter(*items: int) -> Callable[[Any], Tuple[Any, ...]]: ...

def methodcaller(name: str, *args: Any, **kwargs: Any) -> Callable[..., Any]: ...


def iadd(a: Any, b: Any) -> Any: ...
def __iadd__(a: Any, b: Any) -> Any: ...

def iand(a: Any, b: Any) -> Any: ...
def __iand__(a: Any, b: Any) -> Any: ...

def iconcat(a: Any, b: Any) -> Any: ...
def __iconcat__(a: Any, b: Any) -> Any: ...

def ifloordiv(a: Any, b: Any) -> Any: ...
def __ifloordiv__(a: Any, b: Any) -> Any: ...

def ilshift(a: Any, b: Any) -> Any: ...
def __ilshift__(a: Any, b: Any) -> Any: ...

def imod(a: Any, b: Any) -> Any: ...
def __imod__(a: Any, b: Any) -> Any: ...

def imul(a: Any, b: Any) -> Any: ...
def __imul__(a: Any, b: Any) -> Any: ...

if sys.version_info >= (3,5):
    def imatmul(a: Any, b: Any) -> Any: ...
    def __imatmul__(a: Any, b: Any) -> Any: ...

def ior(a: Any, b: Any) -> Any: ...
def __ior__(a: Any, b: Any) -> Any: ...

def ipow(a: Any, b: Any) -> Any: ...
def __ipow__(a: Any, b: Any) -> Any: ...

def irshift(a: Any, b: Any) -> Any: ...
def __irshift__(a: Any, b: Any) -> Any: ...

def isub(a: Any, b: Any) -> Any: ...
def __isub__(a: Any, b: Any) -> Any: ...

def itruediv(a: Any, b: Any) -> Any: ...
def __itruediv__(a: Any, b: Any) -> Any: ...

def ixor(a: Any, b: Any) -> Any: ...
def __ixor__(a: Any, b: Any) -> Any: ...


#def __delslice__(container: Any, b: int, c: int) -> None: ...
#def __div__(a: Any, b: Any) -> Any: ...
#def __getslice__(container, b: int, c: int) -> Any: ...
#def __idiv__(a: Any, b: Any) -> Any: ...
#def __irepeat__(a: Any, b: int) -> Any: ...
#def __repeat__(a, b: int) -> Any: ...
#def __setslice__(container: Any, b: int, c: int, item: Any) -> None: ...

#def delslice(container: Any, b: int, c: int) -> None: ...
#def div(a: Any, b: Any) -> Any: ...
#def getslice(container: Any, b: int, c: int) -> Any: ...
#def idiv(a: Any, b: Any) -> Any: ...
#def irepeat(a, b: int) -> Any: ...
#def isCallable(x: Any) -> bool: ...
#def isMappingType(x: Any) -> bool: ...
#def isNumberType(x: Any) -> bool: ...
#def isSequenceType(x: Any) -> bool: ...
#def repeat(a, b: int) -> Any: ...
#def sequenceIncludes(seq1: Any, seq2: Any) -> bool: ...
#def setslice(container: Any, b: int, c: int, slice: Any) -> None: ...
