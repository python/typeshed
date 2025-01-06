import numbers
from _decimal import (
    HAVE_CONTEXTVAR as HAVE_CONTEXTVAR,
    HAVE_THREADS as HAVE_THREADS,
    MAX_EMAX as MAX_EMAX,
    MAX_PREC as MAX_PREC,
    MIN_EMIN as MIN_EMIN,
    MIN_ETINY as MIN_ETINY,
    ROUND_05UP as ROUND_05UP,
    ROUND_CEILING as ROUND_CEILING,
    ROUND_DOWN as ROUND_DOWN,
    ROUND_FLOOR as ROUND_FLOOR,
    ROUND_HALF_DOWN as ROUND_HALF_DOWN,
    ROUND_HALF_EVEN as ROUND_HALF_EVEN,
    ROUND_HALF_UP as ROUND_HALF_UP,
    ROUND_UP as ROUND_UP,
    BasicContext as BasicContext,
    DefaultContext as DefaultContext,
    ExtendedContext as ExtendedContext,
    __libmpdec_version__ as __libmpdec_version__,
    __version__ as __version__,
    getcontext as getcontext,
    localcontext as localcontext,
    setcontext as setcontext,
)
from collections.abc import Container, Sequence
from types import TracebackType
from typing import Any, ClassVar, Literal, NamedTuple, final, overload, type_check_only
from typing_extensions import Self, TypeAlias

_Decimal: TypeAlias = Decimal | int
_DecimalNew: TypeAlias = Decimal | float | str | tuple[int, Sequence[int], int]
_ComparableNum: TypeAlias = Decimal | float | numbers.Rational
_TrapType: TypeAlias = type[DecimalException]

# At runtime, these classes are implemented in C as part of "_decimal".
# However, they consider themselves to live in "decimal", so we'll put them here.

# This type isn't exposed at runtime. It calls itself decimal.ContextManager
@final
@type_check_only
class _ContextManager:
    def __init__(self, new_context: Context) -> None: ...
    def __enter__(self) -> Context: ...
    def __exit__(self, t: type[BaseException] | None, v: BaseException | None, tb: TracebackType | None) -> None: ...

class DecimalTuple(NamedTuple):
    sign: int
    digits: tuple[int, ...]
    exponent: int | Literal["n", "N", "F"]

class DecimalException(ArithmeticError): ...
class Clamped(DecimalException): ...
class InvalidOperation(DecimalException): ...
class ConversionSyntax(InvalidOperation): ...
class DivisionByZero(DecimalException, ZeroDivisionError): ...
class DivisionImpossible(InvalidOperation): ...
class DivisionUndefined(InvalidOperation, ZeroDivisionError): ...
class Inexact(DecimalException): ...
class InvalidContext(InvalidOperation): ...
class Rounded(DecimalException): ...
class Subnormal(DecimalException): ...
class Overflow(Inexact, Rounded): ...
class Underflow(Inexact, Rounded, Subnormal): ...
class FloatOperation(DecimalException, TypeError): ...

class Decimal:
    def __new__(cls, value: _DecimalNew = ..., context: Context | None = ...) -> Self: ...
    @classmethod
    def from_float(cls, f: float, /) -> Self: ...
    def __bool__(self) -> bool: ...
    def compare(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def __hash__(self) -> int: ...
    def as_tuple(self) -> DecimalTuple: ...
    def as_integer_ratio(self) -> tuple[int, int]: ...
    def to_eng_string(self, context: Context | None = None) -> str: ...
    def __abs__(self) -> Decimal: ...
    def __add__(self, value: _Decimal, /) -> Decimal: ...
    def __divmod__(self, value: _Decimal, /) -> tuple[Decimal, Decimal]: ...
    def __eq__(self, value: object, /) -> bool: ...
    def __floordiv__(self, value: _Decimal, /) -> Decimal: ...
    def __ge__(self, value: _ComparableNum, /) -> bool: ...
    def __gt__(self, value: _ComparableNum, /) -> bool: ...
    def __le__(self, value: _ComparableNum, /) -> bool: ...
    def __lt__(self, value: _ComparableNum, /) -> bool: ...
    def __mod__(self, value: _Decimal, /) -> Decimal: ...
    def __mul__(self, value: _Decimal, /) -> Decimal: ...
    def __neg__(self) -> Decimal: ...
    def __pos__(self) -> Decimal: ...
    def __pow__(self, value: _Decimal, mod: _Decimal | None = None, /) -> Decimal: ...
    def __radd__(self, value: _Decimal, /) -> Decimal: ...
    def __rdivmod__(self, value: _Decimal, /) -> tuple[Decimal, Decimal]: ...
    def __rfloordiv__(self, value: _Decimal, /) -> Decimal: ...
    def __rmod__(self, value: _Decimal, /) -> Decimal: ...
    def __rmul__(self, value: _Decimal, /) -> Decimal: ...
    def __rsub__(self, value: _Decimal, /) -> Decimal: ...
    def __rtruediv__(self, value: _Decimal, /) -> Decimal: ...
    def __sub__(self, value: _Decimal, /) -> Decimal: ...
    def __truediv__(self, value: _Decimal, /) -> Decimal: ...
    def remainder_near(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def __float__(self) -> float: ...
    def __int__(self) -> int: ...
    def __trunc__(self) -> int: ...
    @property
    def real(self) -> Decimal: ...
    @property
    def imag(self) -> Decimal: ...
    def conjugate(self) -> Decimal: ...
    def __complex__(self) -> complex: ...
    @overload
    def __round__(self) -> int: ...
    @overload
    def __round__(self, ndigits: int, /) -> Decimal: ...
    def __floor__(self) -> int: ...
    def __ceil__(self) -> int: ...
    def fma(self, other: _Decimal, third: _Decimal, context: Context | None = None) -> Decimal: ...
    def __rpow__(self, value: _Decimal, mod: Context | None = None, /) -> Decimal: ...
    def normalize(self, context: Context | None = None) -> Decimal: ...
    def quantize(self, exp: _Decimal, rounding: str | None = None, context: Context | None = None) -> Decimal: ...
    def same_quantum(self, other: _Decimal, context: Context | None = None) -> bool: ...
    def to_integral_exact(self, rounding: str | None = None, context: Context | None = None) -> Decimal: ...
    def to_integral_value(self, rounding: str | None = None, context: Context | None = None) -> Decimal: ...
    def to_integral(self, rounding: str | None = None, context: Context | None = None) -> Decimal: ...
    def sqrt(self, context: Context | None = None) -> Decimal: ...
    def max(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def min(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def adjusted(self) -> int: ...
    def canonical(self) -> Decimal: ...
    def compare_signal(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def compare_total(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def compare_total_mag(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def copy_abs(self) -> Decimal: ...
    def copy_negate(self) -> Decimal: ...
    def copy_sign(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def exp(self, context: Context | None = None) -> Decimal: ...
    def is_canonical(self) -> bool: ...
    def is_finite(self) -> bool: ...
    def is_infinite(self) -> bool: ...
    def is_nan(self) -> bool: ...
    def is_normal(self, context: Context | None = None) -> bool: ...
    def is_qnan(self) -> bool: ...
    def is_signed(self) -> bool: ...
    def is_snan(self) -> bool: ...
    def is_subnormal(self, context: Context | None = None) -> bool: ...
    def is_zero(self) -> bool: ...
    def ln(self, context: Context | None = None) -> Decimal: ...
    def log10(self, context: Context | None = None) -> Decimal: ...
    def logb(self, context: Context | None = None) -> Decimal: ...
    def logical_and(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def logical_invert(self, context: Context | None = None) -> Decimal: ...
    def logical_or(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def logical_xor(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def max_mag(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def min_mag(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def next_minus(self, context: Context | None = None) -> Decimal: ...
    def next_plus(self, context: Context | None = None) -> Decimal: ...
    def next_toward(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def number_class(self, context: Context | None = None) -> str: ...
    def radix(self) -> Decimal: ...
    def rotate(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def scaleb(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def shift(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def __reduce__(self) -> tuple[type[Self], tuple[str]]: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, memo: Any, /) -> Self: ...
    def __format__(self, specifier: str, context: Context | None = ..., /) -> str: ...

class Context:
    # TODO: Context doesn't allow you to delete *any* attributes from instances of the class at runtime,
    # even settable attributes like `prec` and `rounding`,
    # but that's inexpressable in the stub.
    # Type checkers either ignore it or misinterpret it
    # if you add a `def __delattr__(self, name: str, /) -> NoReturn` method to the stub
    prec: int
    rounding: str
    Emin: int
    Emax: int
    capitals: int
    clamp: int
    traps: dict[_TrapType, bool]
    flags: dict[_TrapType, bool]
    def __init__(
        self,
        prec: int | None = ...,
        rounding: str | None = ...,
        Emin: int | None = ...,
        Emax: int | None = ...,
        capitals: int | None = ...,
        clamp: int | None = ...,
        flags: None | dict[_TrapType, bool] | Container[_TrapType] = ...,
        traps: None | dict[_TrapType, bool] | Container[_TrapType] = ...,
    ) -> None: ...
    def __reduce__(self) -> tuple[type[Self], tuple[Any, ...]]: ...
    def clear_flags(self) -> None: ...
    def clear_traps(self) -> None: ...
    def copy(self) -> Context: ...
    def __copy__(self) -> Context: ...
    # see https://github.com/python/cpython/issues/94107
    __hash__: ClassVar[None]  # type: ignore[assignment]
    def Etiny(self) -> int: ...
    def Etop(self) -> int: ...
    def create_decimal(self, num: _DecimalNew = "0", /) -> Decimal: ...
    def create_decimal_from_float(self, f: float, /) -> Decimal: ...
    def abs(self, x: _Decimal, /) -> Decimal: ...
    def add(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def canonical(self, x: Decimal, /) -> Decimal: ...
    def compare(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def compare_signal(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def compare_total(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def compare_total_mag(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def copy_abs(self, x: _Decimal, /) -> Decimal: ...
    def copy_decimal(self, x: _Decimal, /) -> Decimal: ...
    def copy_negate(self, x: _Decimal, /) -> Decimal: ...
    def copy_sign(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def divide(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def divide_int(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def divmod(self, x: _Decimal, y: _Decimal, /) -> tuple[Decimal, Decimal]: ...
    def exp(self, x: _Decimal, /) -> Decimal: ...
    def fma(self, x: _Decimal, y: _Decimal, z: _Decimal, /) -> Decimal: ...
    def is_canonical(self, x: _Decimal, /) -> bool: ...
    def is_finite(self, x: _Decimal, /) -> bool: ...
    def is_infinite(self, x: _Decimal, /) -> bool: ...
    def is_nan(self, x: _Decimal, /) -> bool: ...
    def is_normal(self, x: _Decimal, /) -> bool: ...
    def is_qnan(self, x: _Decimal, /) -> bool: ...
    def is_signed(self, x: _Decimal, /) -> bool: ...
    def is_snan(self, x: _Decimal, /) -> bool: ...
    def is_subnormal(self, x: _Decimal, /) -> bool: ...
    def is_zero(self, x: _Decimal, /) -> bool: ...
    def ln(self, x: _Decimal, /) -> Decimal: ...
    def log10(self, x: _Decimal, /) -> Decimal: ...
    def logb(self, x: _Decimal, /) -> Decimal: ...
    def logical_and(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def logical_invert(self, x: _Decimal, /) -> Decimal: ...
    def logical_or(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def logical_xor(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def max(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def max_mag(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def min(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def min_mag(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def minus(self, x: _Decimal, /) -> Decimal: ...
    def multiply(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def next_minus(self, x: _Decimal, /) -> Decimal: ...
    def next_plus(self, x: _Decimal, /) -> Decimal: ...
    def next_toward(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def normalize(self, x: _Decimal, /) -> Decimal: ...
    def number_class(self, x: _Decimal, /) -> str: ...
    def plus(self, x: _Decimal, /) -> Decimal: ...
    def power(self, a: _Decimal, b: _Decimal, modulo: _Decimal | None = None) -> Decimal: ...
    def quantize(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def radix(self) -> Decimal: ...
    def remainder(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def remainder_near(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def rotate(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def same_quantum(self, x: _Decimal, y: _Decimal, /) -> bool: ...
    def scaleb(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def shift(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def sqrt(self, x: _Decimal, /) -> Decimal: ...
    def subtract(self, x: _Decimal, y: _Decimal, /) -> Decimal: ...
    def to_eng_string(self, x: _Decimal, /) -> str: ...
    def to_sci_string(self, x: _Decimal, /) -> str: ...
    def to_integral_exact(self, x: _Decimal, /) -> Decimal: ...
    def to_integral_value(self, x: _Decimal, /) -> Decimal: ...
    def to_integral(self, x: _Decimal, /) -> Decimal: ...
