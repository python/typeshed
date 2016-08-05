# Stubs for decimal (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, SupportsAbs, SupportsFloat, SupportsInt

ROUND_DOWN = ...  # type: Any
ROUND_HALF_UP = ...  # type: Any
ROUND_HALF_EVEN = ...  # type: Any
ROUND_CEILING = ...  # type: Any
ROUND_FLOOR = ...  # type: Any
ROUND_UP = ...  # type: Any
ROUND_HALF_DOWN = ...  # type: Any
ROUND_05UP = ...  # type: Any

class DecimalException(ArithmeticError):
    def handle(self, context, *args): ...

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

def setcontext(context): ...
def getcontext(): ...
def localcontext(ctx=None): ...

class Decimal(SupportsAbs[Decimal], SupportsFloat, SupportsInt):
    def __new__(cls, value=..., context=None): ...
    @classmethod
    def from_float(cls, f): ...
    def __nonzero__(self): ...
    def __eq__(self, other, context=None): ...
    def __ne__(self, other, context=None): ...
    def __lt__(self, other, context=None): ...
    def __le__(self, other, context=None): ...
    def __gt__(self, other, context=None): ...
    def __ge__(self, other, context=None): ...
    def compare(self, other, context=None): ...
    def __hash__(self): ...
    def as_tuple(self): ...
    def to_eng_string(self, context=None): ...
    def __neg__(self, context=None): ...
    def __pos__(self, context=None): ...
    def __abs__(self, round=True, context=None): ...
    def __add__(self, other, context=None): ...
    def __radd__(self, other, context=None): ...
    def __sub__(self, other, context=None): ...
    def __rsub__(self, other, context=None): ...
    def __mul__(self, other, context=None): ...
    def __rmul__(self, other, context=None): ...
    def __truediv__(self, other, context=None): ...
    def __rtruediv__(self, other, context=None): ...
    def __div__(self, other, context=None): ...
    def __rdiv__(self, other, context=None): ...
    def __divmod__(self, other, context=None): ...
    def __rdivmod__(self, other, context=None): ...
    def __mod__(self, other, context=None): ...
    def __rmod__(self, other, context=None): ...
    def remainder_near(self, other, context=None): ...
    def __floordiv__(self, other, context=None): ...
    def __rfloordiv__(self, other, context=None): ...
    def __float__(self): ...
    def __int__(self): ...
    def __trunc__(self): ...
    real = ...  # type: property
    imag = ...  # type: property
    def conjugate(self): ...
    def __complex__(self): ...
    def __long__(self): ...
    def fma(self, other, third, context=None): ...
    def __pow__(self, other, modulo=None, context=None): ...
    def __rpow__(self, other, context=None): ...
    def normalize(self, context=None): ...
    def quantize(self, exp, rounding=None, context=None, watchexp=True): ...
    def same_quantum(self, other): ...
    def to_integral_exact(self, rounding=None, context=None): ...
    def to_integral_value(self, rounding=None, context=None): ...
    def to_integral(self, rounding=None, context=None): ...
    def sqrt(self, context=None): ...
    def max(self, other, context=None): ...
    def min(self, other, context=None): ...
    def adjusted(self): ...
    def canonical(self, context=None): ...
    def compare_signal(self, other, context=None): ...
    def compare_total(self, other): ...
    def compare_total_mag(self, other): ...
    def copy_abs(self): ...
    def copy_negate(self): ...
    def copy_sign(self, other): ...
    def exp(self, context=None): ...
    def is_canonical(self): ...
    def is_finite(self): ...
    def is_infinite(self): ...
    def is_nan(self): ...
    def is_normal(self, context=None): ...
    def is_qnan(self): ...
    def is_signed(self): ...
    def is_snan(self): ...
    def is_subnormal(self, context=None): ...
    def is_zero(self): ...
    def ln(self, context=None): ...
    def log10(self, context=None): ...
    def logb(self, context=None): ...
    def logical_and(self, other, context=None): ...
    def logical_invert(self, context=None): ...
    def logical_or(self, other, context=None): ...
    def logical_xor(self, other, context=None): ...
    def max_mag(self, other, context=None): ...
    def min_mag(self, other, context=None): ...
    def next_minus(self, context=None): ...
    def next_plus(self, context=None): ...
    def next_toward(self, other, context=None): ...
    def number_class(self, context=None): ...
    def radix(self): ...
    def rotate(self, other, context=None): ...
    def scaleb(self, other, context=None): ...
    def shift(self, other, context=None): ...
    def __reduce__(self): ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...
    def __format__(self, specifier, context=None, _localeconv=None): ...

class _ContextManager:
    new_context = ...  # type: Any
    def __init__(self, new_context): ...
    saved_context = ...  # type: Any
    def __enter__(self): ...
    def __exit__(self, t, v, tb): ...

class Context:
    prec = ...  # type: Any
    rounding = ...  # type: Any
    Emin = ...  # type: Any
    Emax = ...  # type: Any
    capitals = ...  # type: Any
    traps = ...  # type: Any
    flags = ...  # type: Any
    def __init__(self, prec=None, rounding=None, traps=None, flags=None, Emin=None, Emax=None, capitals=None, _clamp=0, _ignored_flags=None): ...
    def clear_flags(self): ...
    def copy(self): ...
    __copy__ = ...  # type: Any
    __hash__ = ...  # type: Any
    def Etiny(self): ...
    def Etop(self): ...
    def create_decimal(self, num=...): ...
    def create_decimal_from_float(self, f): ...
    def abs(self, a): ...
    def add(self, a, b): ...
    def canonical(self, a): ...
    def compare(self, a, b): ...
    def compare_signal(self, a, b): ...
    def compare_total(self, a, b): ...
    def compare_total_mag(self, a, b): ...
    def copy_abs(self, a): ...
    def copy_decimal(self, a): ...
    def copy_negate(self, a): ...
    def copy_sign(self, a, b): ...
    def divide(self, a, b): ...
    def divide_int(self, a, b): ...
    def divmod(self, a, b): ...
    def exp(self, a): ...
    def fma(self, a, b, c): ...
    def is_canonical(self, a): ...
    def is_finite(self, a): ...
    def is_infinite(self, a): ...
    def is_nan(self, a): ...
    def is_normal(self, a): ...
    def is_qnan(self, a): ...
    def is_signed(self, a): ...
    def is_snan(self, a): ...
    def is_subnormal(self, a): ...
    def is_zero(self, a): ...
    def ln(self, a): ...
    def log10(self, a): ...
    def logb(self, a): ...
    def logical_and(self, a, b): ...
    def logical_invert(self, a): ...
    def logical_or(self, a, b): ...
    def logical_xor(self, a, b): ...
    def max(self, a, b): ...
    def max_mag(self, a, b): ...
    def min(self, a, b): ...
    def min_mag(self, a, b): ...
    def minus(self, a): ...
    def multiply(self, a, b): ...
    def next_minus(self, a): ...
    def next_plus(self, a): ...
    def next_toward(self, a, b): ...
    def normalize(self, a): ...
    def number_class(self, a): ...
    def plus(self, a): ...
    def power(self, a, b, modulo=None): ...
    def quantize(self, a, b): ...
    def radix(self): ...
    def remainder(self, a, b): ...
    def remainder_near(self, a, b): ...
    def rotate(self, a, b): ...
    def same_quantum(self, a, b): ...
    def scaleb(self, a, b): ...
    def shift(self, a, b): ...
    def sqrt(self, a): ...
    def subtract(self, a, b): ...
    def to_eng_string(self, a): ...
    def to_sci_string(self, a): ...
    def to_integral_exact(self, a): ...
    def to_integral_value(self, a): ...
    def to_integral(self, a): ...

DefaultContext = ...  # type: Any
BasicContext = ...  # type: Any
ExtendedContext = ...  # type: Any
