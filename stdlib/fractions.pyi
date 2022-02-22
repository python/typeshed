import sys
from _typeshed import Self
from decimal import Decimal
from numbers import Integral, Rational, Real
from typing import Any, Union, overload
from typing_extensions import Literal

_ComparableNum = Union[int, float, Decimal, Real]

if sys.version_info >= (3, 9):
    __all__ = ["Fraction"]
else:
    __all__ = ["Fraction", "gcd"]
    @overload
    def gcd(a: int, b: int) -> int: ...
    @overload
    def gcd(a: Integral, b: int) -> Integral: ...
    @overload
    def gcd(a: int, b: Integral) -> Integral: ...
    @overload
    def gcd(a: Integral, b: Integral) -> Integral: ...

class Fraction(Rational):
    @overload
    def __new__(
        cls: type[Self], numerator: int | Rational = ..., denominator: int | Rational | None = ..., *, _normalize: bool = ...
    ) -> Self: ...
    @overload
    def __new__(cls: type[Self], __value: float | Decimal | str, *, _normalize: bool = ...) -> Self: ...
    @classmethod
    def from_float(cls: type[Self], f: float) -> Self: ...
    @classmethod
    def from_decimal(cls: type[Self], dec: Decimal) -> Self: ...
    def limit_denominator(self, max_denominator: int = ...) -> Fraction: ...
    if sys.version_info >= (3, 8):
        def as_integer_ratio(self) -> tuple[int, int]: ...

    @property
    def numerator(self) -> int: ...
    @property
    def denominator(self) -> int: ...
    @overload
    def __add__(self, other: int | Fraction) -> Fraction: ...
    @overload
    def __add__(self, other: float) -> float: ...
    @overload
    def __add__(self, other: complex) -> complex: ...
    @overload
    def __radd__(self, other: int | Fraction) -> Fraction: ...
    @overload
    def __radd__(self, other: float) -> float: ...
    @overload
    def __radd__(self, other: complex) -> complex: ...
    @overload
    def __sub__(self, other: int | Fraction) -> Fraction: ...
    @overload
    def __sub__(self, other: float) -> float: ...
    @overload
    def __sub__(self, other: complex) -> complex: ...
    @overload
    def __rsub__(self, other: int | Fraction) -> Fraction: ...
    @overload
    def __rsub__(self, other: float) -> float: ...
    @overload
    def __rsub__(self, other: complex) -> complex: ...
    @overload
    def __mul__(self, other: int | Fraction) -> Fraction: ...
    @overload
    def __mul__(self, other: float) -> float: ...
    @overload
    def __mul__(self, other: complex) -> complex: ...
    @overload
    def __rmul__(self, other: int | Fraction) -> Fraction: ...
    @overload
    def __rmul__(self, other: float) -> float: ...
    @overload
    def __rmul__(self, other: complex) -> complex: ...
    @overload
    def __truediv__(self, other: int | Fraction) -> Fraction: ...
    @overload
    def __truediv__(self, other: float) -> float: ...
    @overload
    def __truediv__(self, other: complex) -> complex: ...
    @overload
    def __rtruediv__(self, other: int | Fraction) -> Fraction: ...
    @overload
    def __rtruediv__(self, other: float) -> float: ...
    @overload
    def __rtruediv__(self, other: complex) -> complex: ...
    @overload
    def __floordiv__(self, other: int | Fraction) -> int: ...
    @overload
    def __floordiv__(self, other: float) -> float: ...
    @overload
    def __rfloordiv__(self, other: int | Fraction) -> int: ...
    @overload
    def __rfloordiv__(self, other: float) -> float: ...
    @overload
    def __mod__(self, other: int | Fraction) -> Fraction: ...
    @overload
    def __mod__(self, other: float) -> float: ...
    @overload
    def __rmod__(self, other: int | Fraction) -> Fraction: ...
    @overload
    def __rmod__(self, other: float) -> float: ...
    @overload
    def __divmod__(self, other: int | Fraction) -> tuple[int, Fraction]: ...
    @overload
    def __divmod__(self, other: float) -> tuple[float, Fraction]: ...
    @overload
    def __rdivmod__(self, other: int | Fraction) -> tuple[int, Fraction]: ...
    @overload
    def __rdivmod__(self, other: float) -> tuple[float, Fraction]: ...
    @overload
    def __pow__(self, other: int) -> Fraction: ...
    @overload
    def __pow__(self, other: float | Fraction) -> float: ...
    @overload
    def __pow__(self, other: complex) -> complex: ...
    @overload
    def __rpow__(self, other: int | float | Fraction) -> float: ...
    @overload
    def __rpow__(self, other: complex) -> complex: ...
    def __pos__(self) -> Fraction: ...
    def __neg__(self) -> Fraction: ...
    def __abs__(self) -> Fraction: ...
    def __trunc__(self) -> int: ...
    def __floor__(self) -> int: ...
    def __ceil__(self) -> int: ...
    @overload
    def __round__(self, ndigits: None = ...) -> int: ...
    @overload
    def __round__(self, ndigits: int) -> Fraction: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: _ComparableNum) -> bool: ...
    def __gt__(self, other: _ComparableNum) -> bool: ...
    def __le__(self, other: _ComparableNum) -> bool: ...
    def __ge__(self, other: _ComparableNum) -> bool: ...
    def __bool__(self) -> bool: ...
    def __copy__(self: Self) -> Self: ...
    def __deepcopy__(self: Self, memo: Any) -> Self: ...
    if sys.version_info >= (3, 11):
        def __int__(self) -> int: ...
    # Not actually defined within fractions.py, but provides more useful
    # overrides
    @property
    def real(self) -> Fraction: ...
    @property
    def imag(self) -> Literal[0]: ...
    def conjugate(self) -> Fraction: ...
