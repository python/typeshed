import sys
from _typeshed import ReadOnlyBuffer
from typing import Any, Literal, TypeVar, final, overload
from typing_extensions import TypeAlias

ucd_3_2_0: UCD
unidata_version: str

if sys.version_info < (3, 10):
    ucnhash_CAPI: Any

_T = TypeVar("_T")

def bidirectional(__chr: str) -> str: ...
def category(__chr: str) -> str: ...
def combining(__chr: str) -> int: ...
@overload
def decimal(__chr: str) -> int: ...
@overload
def decimal(__chr: str, __default: _T) -> int | _T: ...
def decomposition(__chr: str) -> str: ...
@overload
def digit(__chr: str) -> int: ...
@overload
def digit(__chr: str, __default: _T) -> int | _T: ...

_EastAsianWidth: TypeAlias = Literal["F", "H", "W", "Na", "A", "N"]

def east_asian_width(__chr: str) -> _EastAsianWidth: ...
def is_normalized(__form: str, __unistr: str) -> bool: ...
def lookup(__name: str | ReadOnlyBuffer) -> str: ...
def mirrored(__chr: str) -> int: ...
@overload
def name(__chr: str) -> str: ...
@overload
def name(__chr: str, __default: _T) -> str | _T: ...
def normalize(__form: str, __unistr: str) -> str: ...
@overload
def numeric(__chr: str) -> float: ...
@overload
def numeric(__chr: str, __default: _T) -> float | _T: ...
@final
class UCD:
    # The methods below are constructed from the same array in C
    # (unicodedata_functions) and hence identical to the functions above.
    unidata_version: str
    def bidirectional(self, __chr: str) -> str: ...
    def category(self, __chr: str) -> str: ...
    def combining(self, __chr: str) -> int: ...
    @overload
    def decimal(self, __chr: str) -> int: ...
    @overload
    def decimal(self, __chr: str, __default: _T) -> int | _T: ...
    def decomposition(self, __chr: str) -> str: ...
    @overload
    def digit(self, __chr: str) -> int: ...
    @overload
    def digit(self, __chr: str, __default: _T) -> int | _T: ...
    def east_asian_width(self, __chr: str) -> _EastAsianWidth: ...
    def is_normalized(self, __form: str, __unistr: str) -> bool: ...
    def lookup(self, __name: str | ReadOnlyBuffer) -> str: ...
    def mirrored(self, __chr: str) -> int: ...
    @overload
    def name(self, __chr: str) -> str: ...
    @overload
    def name(self, __chr: str, __default: _T) -> str | _T: ...
    def normalize(self, __form: str, __unistr: str) -> str: ...
    @overload
    def numeric(self, __chr: str) -> float: ...
    @overload
    def numeric(self, __chr: str, __default: _T) -> float | _T: ...
