# Stubs for numbers

from typing import (
    Any, Optional,
    SupportsAbs, SupportsComplex, SupportsFloat, SupportsInt, SupportsRound,
)
from abc import abstractmethod
import sys


class Number: ...

class Complex(Number, SupportsComplex, SupportsAbs[float]):
    @property
    @abstractmethod
    def real(self) -> Complex: ...
    @property
    @abstractmethod
    def imag(self) -> Complex: ...
    @abstractmethod
    def __add__(self, other: Complex) -> Complex: ...
    def __neg__(self) -> Complex: ...
    @abstractmethod
    def __mul__(self, other: Complex) -> Complex: ...
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
    def __divmod__(self, other: Real) -> Real: ...
    @abstractmethod
    def __floordiv__(self, other: Real) -> Real: ...
    @abstractmethod
    def __mod__(self, other: Real) -> Real: ...
    @abstractmethod
    def __lt__(self, other: Real) -> bool: ...
    @abstractmethod
    def __le__(self, other: Real) -> bool: ...
    @abstractmethod
    def __gt__(self, other: Real) -> bool: ...
    @abstractmethod
    def __ge__(self, other: Real) -> bool: ...
    def __complex__(self) -> Complex: ...  # type: ignore
    @property
    def real(self) -> Real: ...
    @property
    def imag(self) -> Real: ...
    def conjugate(self) -> Real: ...

    @abstractmethod
    def __add__(self, other: Real) -> Real: ...  # type: ignore
    def __neg__(self) -> Real: ...  # type: ignore
    @abstractmethod
    def __mul__(self, other: Real) -> Real: ...  # type: ignore
    if sys.version_info >= (3,):
        @abstractmethod
        def __truediv__(self, other: Real) -> Real: ...  # type: ignore
    else:
        @abstractmethod
        def __div__(self, other: Real) -> Real: ...  # type: ignore

class Rational(Real):
    @property
    @abstractmethod
    def numerator(self) -> int: ...
    @property
    @abstractmethod
    def denominator(self) -> int: ...
    def __float__(self) -> float: ...

    @abstractmethod
    def __divmod__(self, other: Rational) -> Rational: ...  # type: ignore
    @abstractmethod
    def __floordiv__(self, other: Rational) -> Rational: ...  # type: ignore
    @abstractmethod
    def __mod__(self, other: Rational) -> Rational: ...  # type: ignore
    @abstractmethod
    def __lt__(self, other: Rational, float) -> bool: ...  # type: ignore
    @abstractmethod
    def __le__(self, other: Rational) -> bool: ...  # type: ignore
    @abstractmethod
    def __gt__(self, other: Rational) -> bool: ...  # type: ignore
    @abstractmethod
    def __ge__(self, other: Rational) -> bool: ...  # type: ignore
    def __complex__(self) -> Complex: ...  # type: ignore
    @property
    def real(self) -> Rational: ...  # type: ignore
    @property
    def imag(self) -> Rational: ...  # type: ignore
    def conjugate(self) -> Rational: ...  # type: ignore

    @abstractmethod
    def __add__(self, other: Rational) -> Rational: ...  # type: ignore
    def __neg__(self) -> Rational: ...
    @abstractmethod
    def __mul__(self, other: Rational) -> Rational: ...  # type: ignore
    if sys.version_info >= (3,):
        @abstractmethod
        def __truediv__(self, other: Rational) -> Rational: ...  # type: ignore
    else:
        @abstractmethod
        def __div__(self, other: Rational) -> Rational: ...  # type: ignore

class Integral(Rational, SupportsInt, SupportsAbs[int]):
    @property
    def numerator(self) -> int: ...  # type: ignore
    @property
    def denominator(self) -> int: ...  # type: ignore
    @abstractmethod
    def __pow__(self, exponent: float,  # type: ignore
                modulus: Optional[int] = ...) -> Integral: ...
    @abstractmethod
    def __lshift__(self, other: Integral) -> Integral: ...  # type: ignore
    @abstractmethod
    def __rshift__(self, other: Integral) -> Integral: ...  # type: ignore
    @abstractmethod
    def __and__(self, other: Integral) -> Integral: ...  # type: ignore
    @abstractmethod
    def __xor__(self, other: Integral) -> Integral: ...  # type: ignore
    @abstractmethod
    def __or__(self, other: Integral) -> Integral: ...  # type: ignore
    @abstractmethod
    def __invert__(self) -> Integral: ...  # type: ignore

    @abstractmethod
    def __divmod__(self, other: Integral) -> Integral: ...  # type: ignore
    @abstractmethod
    def __floordiv__(self, other: Integral) -> Integral: ...  # type: ignore
    @abstractmethod
    def __mod__(self, other: Integral) -> Integral: ...  # type: ignore
    @abstractmethod
    def __lt__(self, other: Integral) -> bool: ...  # type: ignore
    @abstractmethod
    def __le__(self, other: Integral) -> bool: ...  # type: ignore
    @abstractmethod
    def __gt__(self, other: Integral) -> bool: ...  # type: ignore
    @abstractmethod
    def __ge__(self, other: Integral) -> bool: ...  # type: ignore
    def __complex__(self) -> Complex: ...  # type: ignore
    @property
    def real(self) -> Integral: ...  # type: ignore
    @property
    def imag(self) -> Integral: ...  # type: ignore
    def conjugate(self) -> Integral: ...  # type: ignore

    @abstractmethod
    def __add__(self, other: Integral) -> Integral: ...  # type: ignore
    def __neg__(self) -> Integral: ...  # type: ignore
    @abstractmethod
    def __mul__(self, other: Integral) -> Integral: ...  # type: ignore
    if sys.version_info >= (3,):
        @abstractmethod
        def __truediv__(self, other: Integral) -> Integral: ...  # type: ignore
    else:
        @abstractmethod
        def __div__(self, other: Integral) -> Integral: ...  # type: ignore
