# Stubs for numbers (Python 3.5)
# See https://docs.python.org/2.7/library/numbers.html
# and https://docs.python.org/3/library/numbers.html
#
# Note: these stubs are incomplete. The more complex type
# signatures are currently omitted.

import sys
from abc import ABCMeta, abstractmethod
from typing import Any, Optional, SupportsFloat, Type, TypeVar

_T = TypeVar("_T")

class Number(metaclass=ABCMeta):
    @abstractmethod
    def __hash__(self) -> int: ...

class Complex(Number):
    @abstractmethod
    def __complex__(self) -> complex: ...
    if sys.version_info >= (3, 0):
        def __bool__(self) -> bool: ...
    else:
        def __nonzero__(self) -> bool: ...
    @property
    @abstractmethod
    def real(self: _T) -> _T: ...
    @property
    @abstractmethod
    def imag(self: _T) -> _T: ...
    @abstractmethod
    def __add__(self: _T, other: Any) -> _T: ...
    @abstractmethod
    def __radd__(self: _T, other: Any) -> _T: ...
    @abstractmethod
    def __neg__(self: _T) -> _T: ...
    @abstractmethod
    def __pos__(self: _T) -> _T: ...
    def __sub__(self: _T, other: Any) -> _T: ...
    def __rsub__(self: _T, other: Any) -> _T: ...
    @abstractmethod
    def __mul__(self: _T, other: Any) -> _T: ...
    @abstractmethod
    def __rmul__(self: _T, other: Any) -> _T: ...
    if sys.version_info < (3, 0):
        @abstractmethod
        def __div__(self, other): ...
        @abstractmethod
        def __rdiv__(self, other): ...
    @abstractmethod
    def __truediv__(self: _T, other: Any) -> _T: ...
    @abstractmethod
    def __rtruediv__(self: _T, other: Any) -> _T: ...
    @abstractmethod
    def __pow__(self: _T, exponent: Any) -> _T: ...
    @abstractmethod
    def __rpow__(self: _T, base: Any) -> _T: ...
    def __abs__(self: _T) -> _T: ...
    def conjugate(self: _T) -> _T: ...
    def __eq__(self, other: Any) -> bool: ...
    if sys.version_info < (3, 0):
        def __ne__(self, other: Any) -> bool: ...

class Real(Complex, SupportsFloat):
    @abstractmethod
    def __float__(self) -> float: ...
    @abstractmethod
    def __trunc__(self) -> int: ...
    if sys.version_info >= (3, 0):
        @abstractmethod
        def __floor__(self) -> int: ...
        @abstractmethod
        def __ceil__(self) -> int: ...
        @abstractmethod
        def __round__(self: _T, ndigits: Optional[int] = ...) -> _T: ...
    def __divmod__(self: _T, other: Any) -> _T: ...
    def __rdivmod__(self: _T, other: Any) -> _T: ...
    @abstractmethod
    def __floordiv__(self, other: Any) -> int: ...
    @abstractmethod
    def __rfloordiv__(self, other: Any) -> int: ...
    @abstractmethod
    def __mod__(self: _T, other: Any) -> _T: ...
    @abstractmethod
    def __rmod__(self: _T, other: Any) -> _T: ...
    @abstractmethod
    def __lt__(self, other: Any) -> bool: ...
    @abstractmethod
    def __le__(self, other: Any) -> bool: ...
    def __complex__(self) -> complex: ...
    @property
    def real(self: _T) -> _T: ...
    @property
    def imag(self: _T) -> _T: ...
    def conjugate(self: _T) -> _T: ...

class Rational(Real):
    @property
    @abstractmethod
    def numerator(self) -> int: ...
    @property
    @abstractmethod
    def denominator(self) -> int: ...
    def __float__(self) -> float: ...

class Integral(Rational):
    if sys.version_info >= (3, 0):
        @abstractmethod
        def __int__(self) -> int: ...
    else:
        @abstractmethod
        def __long__(self) -> long: ...
    def __index__(self) -> int: ...
    @abstractmethod
    def __pow__(self: _T, exponent: Any, modulus: Optional[Any] = ...) -> _T: ...
    @abstractmethod
    def __lshift__(self: _T, other: Any) -> _T: ...
    @abstractmethod
    def __rlshift__(self: _T, other: Any) -> _T: ...
    @abstractmethod
    def __rshift__(self: _T, other: Any) -> _T: ...
    @abstractmethod
    def __rrshift__(self: _T, other: Any) -> _T: ...
    @abstractmethod
    def __and__(self: _T, other: Any) -> _T: ...
    @abstractmethod
    def __rand__(self: _T, other: Any) -> _T: ...
    @abstractmethod
    def __xor__(self: _T, other: Any) -> _T: ...
    @abstractmethod
    def __rxor__(self: _T, other: Any) -> _T: ...
    @abstractmethod
    def __or__(self: _T, other: Any) -> _T: ...
    @abstractmethod
    def __ror__(self: _T, other: Any) -> _T: ...
    @abstractmethod
    def __invert__(self: _T) -> _T: ...
    def __float__(self) -> float: ...
    @property
    def numerator(self) -> int: ...
    @property
    def denominator(self) -> int: ...

