import sys
from _typeshed import SupportsTrunc
from typing import Iterable, SupportsFloat, Union, overload
from typing_extensions import SupportsIndex

if sys.version_info >= (3, 8):
    _SupportsFloatOrIndex = Union[SupportsFloat, SupportsIndex]
else:
    _SupportsFloatOrIndex = SupportsFloat

e: float
pi: float
inf: float
nan: float
tau: float

def acos(__x: _SupportsFloatOrIndex) -> float: ...
def acosh(__x: _SupportsFloatOrIndex) -> float: ...
def asin(__x: _SupportsFloatOrIndex) -> float: ...
def asinh(__x: _SupportsFloatOrIndex) -> float: ...
def atan(__x: _SupportsFloatOrIndex) -> float: ...
def atan2(__y: _SupportsFloatOrIndex, __x: _SupportsFloatOrIndex) -> float: ...
def atanh(__x: _SupportsFloatOrIndex) -> float: ...

if sys.version_info >= (3, 11):
    def cbrt(__x: _SupportsFloatOrIndex) -> float: ...

def ceil(__x: _SupportsFloatOrIndex) -> int: ...

if sys.version_info >= (3, 8):
    def comb(__n: SupportsIndex, __k: SupportsIndex) -> int: ...

def copysign(__x: _SupportsFloatOrIndex, __y: _SupportsFloatOrIndex) -> float: ...
def cos(__x: _SupportsFloatOrIndex) -> float: ...
def cosh(__x: _SupportsFloatOrIndex) -> float: ...
def degrees(__x: _SupportsFloatOrIndex) -> float: ...

if sys.version_info >= (3, 8):
    def dist(__p: Iterable[_SupportsFloatOrIndex], __q: Iterable[_SupportsFloatOrIndex]) -> float: ...

def erf(__x: _SupportsFloatOrIndex) -> float: ...
def erfc(__x: _SupportsFloatOrIndex) -> float: ...
def exp(__x: _SupportsFloatOrIndex) -> float: ...

if sys.version_info >= (3, 11):
    def exp2(__x: _SupportsFloatOrIndex) -> float: ...

def expm1(__x: _SupportsFloatOrIndex) -> float: ...
def fabs(__x: _SupportsFloatOrIndex) -> float: ...

if sys.version_info >= (3, 8):
    def factorial(__x: SupportsIndex) -> int: ...

else:
    def factorial(__x: int) -> int: ...

def floor(__x: _SupportsFloatOrIndex) -> int: ...
def fmod(__x: _SupportsFloatOrIndex, __y: _SupportsFloatOrIndex) -> float: ...
def frexp(__x: _SupportsFloatOrIndex) -> tuple[float, int]: ...
def fsum(__seq: Iterable[_SupportsFloatOrIndex]) -> float: ...
def gamma(__x: _SupportsFloatOrIndex) -> float: ...

if sys.version_info >= (3, 9):
    def gcd(*integers: SupportsIndex) -> int: ...

else:
    def gcd(__x: SupportsIndex, __y: SupportsIndex) -> int: ...

if sys.version_info >= (3, 8):
    def hypot(*coordinates: _SupportsFloatOrIndex) -> float: ...

else:
    def hypot(__x: _SupportsFloatOrIndex, __y: _SupportsFloatOrIndex) -> float: ...

def isclose(
    a: _SupportsFloatOrIndex,
    b: _SupportsFloatOrIndex,
    *,
    rel_tol: _SupportsFloatOrIndex = ...,
    abs_tol: _SupportsFloatOrIndex = ...,
) -> bool: ...
def isinf(__x: _SupportsFloatOrIndex) -> bool: ...
def isfinite(__x: _SupportsFloatOrIndex) -> bool: ...
def isnan(__x: _SupportsFloatOrIndex) -> bool: ...

if sys.version_info >= (3, 8):
    def isqrt(__n: SupportsIndex) -> int: ...

if sys.version_info >= (3, 9):
    def lcm(*integers: SupportsIndex) -> int: ...

def ldexp(__x: _SupportsFloatOrIndex, __i: int) -> float: ...
def lgamma(__x: _SupportsFloatOrIndex) -> float: ...
def log(x: _SupportsFloatOrIndex, base: _SupportsFloatOrIndex = ...) -> float: ...
def log10(__x: _SupportsFloatOrIndex) -> float: ...
def log1p(__x: _SupportsFloatOrIndex) -> float: ...
def log2(__x: _SupportsFloatOrIndex) -> float: ...
def modf(__x: _SupportsFloatOrIndex) -> tuple[float, float]: ...

if sys.version_info >= (3, 9):
    def nextafter(__x: _SupportsFloatOrIndex, __y: _SupportsFloatOrIndex) -> float: ...

if sys.version_info >= (3, 8):
    def perm(__n: SupportsIndex, __k: SupportsIndex | None = ...) -> int: ...

def pow(__x: _SupportsFloatOrIndex, __y: _SupportsFloatOrIndex) -> float: ...

if sys.version_info >= (3, 8):
    @overload
    def prod(__iterable: Iterable[SupportsIndex], *, start: SupportsIndex = ...) -> int: ...  # type: ignore[misc]
    @overload
    def prod(__iterable: Iterable[_SupportsFloatOrIndex], *, start: _SupportsFloatOrIndex = ...) -> float: ...

def radians(__x: _SupportsFloatOrIndex) -> float: ...

if sys.version_info >= (3, 7):
    def remainder(__x: _SupportsFloatOrIndex, __y: _SupportsFloatOrIndex) -> float: ...

def sin(__x: _SupportsFloatOrIndex) -> float: ...
def sinh(__x: _SupportsFloatOrIndex) -> float: ...
def sqrt(__x: _SupportsFloatOrIndex) -> float: ...
def tan(__x: _SupportsFloatOrIndex) -> float: ...
def tanh(__x: _SupportsFloatOrIndex) -> float: ...
def trunc(__x: SupportsTrunc) -> int: ...

if sys.version_info >= (3, 9):
    def ulp(__x: _SupportsFloatOrIndex) -> float: ...
