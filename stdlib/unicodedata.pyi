import sys
from typing import Any, TypeVar, Union

ucd_3_2_0: UCD
ucnhash_CAPI: Any
unidata_version: str

_T = TypeVar("_T")

def bidirectional(__chr: str) -> str: ...
def category(__chr: str) -> str: ...
def combining(__chr: str) -> int: ...
def decimal(__chr: str, __default: _T = ...) -> Union[int, _T]: ...
def decomposition(__chr: str) -> str: ...
def digit(__chr: str, __default: _T = ...) -> Union[int, _T]: ...
def east_asian_width(__chr: str) -> str: ...

if sys.version_info >= (3, 8):
    def is_normalized(__form: str, __unistr: str) -> bool: ...

def lookup(__name: Union[str, bytes]) -> str: ...
def mirrored(__chr: str) -> int: ...
def name(__chr: str, __default: _T = ...) -> Union[str, _T]: ...
def normalize(__form: str, __unistr: str) -> str: ...
def numeric(__chr: str, __default: _T = ...) -> Union[float, _T]: ...

class UCD(object):
    # The methods below are constructed from the same array in C
    # (unicodedata_functions) and hence identical to the methods above.
    unidata_version: str
    def bidirectional(self, __chr: str) -> str: ...
    def category(self, __chr: str) -> str: ...
    def combining(self, __chr: str) -> int: ...
    def decimal(self, __chr: str, __default: _T = ...) -> Union[int, _T]: ...
    def decomposition(self, __chr: str) -> str: ...
    def digit(self, __chr: str, __default: _T = ...) -> Union[int, _T]: ...
    def east_asian_width(self, __chr: str) -> str: ...
    def lookup(self, __name: Union[str, bytes]) -> str: ...
    def mirrored(self, __chr: str) -> int: ...
    def name(self, __chr: str, __default: _T = ...) -> Union[str, _T]: ...
    def normalize(self, __form: str, __unistr: str) -> str: ...
    def numeric(self, __chr: str, __default: _T = ...) -> Union[float, _T]: ...
