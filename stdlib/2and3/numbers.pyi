# Stubs for numbers

from typing import (
    Any, Optional, Union,
    SupportsAbs, SupportsComplex, SupportsFloat, SupportsInt, SupportsRound,
)
from abc import abstractmethod
import sys


class Number: ...

class Complex(Number, SupportsComplex, SupportsAbs):
    @property
    @abstractmethod
    def real(self) -> Complex: ...
    @property
    @abstractmethod
    def imag(self) -> Complex: ...
    @abstractmethod
    def __add__(self, other: Union[Number, complex]) -> Complex: ...
    def __neg__(self) -> Complex: ...
    @abstractmethod
    def __mul__(self, other: Union[Number, complex]) -> Complex: ...
    if sys.version_info >= (3,):
        @abstractmethod
        def __truediv__(self, other: Complex) -> Complex: ...
    else:
        @abstractmethod
        def __div__(self, other: Complex) -> Complex: ...
    @abstractmethod
    def conjugate(self) -> Complex: ...

class Real(Complex, SupportsFloat, SupportsRound):
    @abstractmethod
    def __trunc__(self) -> int: ...
    @abstractmethod
    def __floor__(self) -> int: ...
    @abstractmethod
    def __ceil__(self) -> int: ...
    @abstractmethod
    def __divmod__(self, other: Union[Real, float]) -> Real: ...
    @abstractmethod
    def __floordiv__(self, other: Union[Real, float]) -> Real: ...
    @abstractmethod
    def __mod__(self, other: Union[Real, float]) -> Real: ...
    @abstractmethod
    def __lt__(self, other: Union[Real, float]) -> bool: ...
    @abstractmethod
    def __le__(self, other: Union[Real, float]) -> bool: ...
    @abstractmethod
    def __gt__(self, other: Union[Real, float]) -> bool: ...
    @abstractmethod
    def __ge__(self, other: Union[Real, float]) -> bool: ...
    def __complex__(self) -> Complex: ...  # type: ignore
    @property
    def real(self) -> Real: ...
    @property
    def imag(self) -> Real: ...
    def conjugate(self) -> Real: ...

class Rational(Real):
    @property
    @abstractmethod
    def numerator(self) -> int: ...
    @property
    @abstractmethod
    def denominator(self) -> int: ...
    def __float__(self) -> float: ...

class Integral(Rational, SupportsInt):
    @property
    def numerator(self) -> int: ...
    @property
    def denominator(self) -> int: ...
    @abstractmethod
    def __pow__(self, exponent: float,
                modulus: Optional[int] = ...) -> Integral: ...
    @abstractmethod
    def __lshift__(self, other: Union[int, Integral]) -> Integral: ...
    @abstractmethod
    def __rshift__(self, other: Union[int, Integral]) -> Integral: ...
    @abstractmethod
    def __and__(self, other: Union[int, Integral]) -> Integral: ...
    @abstractmethod
    def __xor__(self, other: Union[int, Integral]) -> Integral: ...
    @abstractmethod
    def __or__(self, other: Union[int, Integral]) -> Integral: ...
    @abstractmethod
    def __invert__(self) -> Integral: ...
