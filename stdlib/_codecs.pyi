import codecs
import sys
from typing import Any, Callable, Dict, Tuple

# This type is not exposed; it is defined in unicodeobject.c
class _EncodingMap:
    def size(self) -> int: ...

_MapT = Dict[int, int] | _EncodingMap
_Handler = Callable[[Exception], Tuple[str, int]]

def register(__search_function: Callable[[str], Any]) -> None: ...
def register_error(__errors: str, __handler: _Handler) -> None: ...
def lookup(__encoding: str) -> codecs.CodecInfo: ...
def lookup_error(__name: str) -> _Handler: ...
def decode(obj: Any, encoding: str = ..., errors: str | None = ...) -> Any: ...
def encode(obj: Any, encoding: str = ..., errors: str | None = ...) -> Any: ...
def charmap_build(__map: str) -> _MapT: ...
def ascii_decode(__data: bytes, __errors: str | None = ...) -> tuple[str, int]: ...
def ascii_encode(__str: str, __errors: str | None = ...) -> tuple[bytes, int]: ...
def charmap_decode(__data: bytes, __errors: str | None = ..., __mapping: _MapT | None = ...) -> tuple[str, int]: ...
def charmap_encode(__str: str, __errors: str | None = ..., __mapping: _MapT | None = ...) -> tuple[bytes, int]: ...
def escape_decode(__data: str | bytes, __errors: str | None = ...) -> tuple[str, int]: ...
def escape_encode(__data: bytes, __errors: str | None = ...) -> tuple[bytes, int]: ...
def latin_1_decode(__data: bytes, __errors: str | None = ...) -> tuple[str, int]: ...
def latin_1_encode(__str: str, __errors: str | None = ...) -> tuple[bytes, int]: ...

if sys.version_info >= (3, 9):
    def raw_unicode_escape_decode(__data: str | bytes, __errors: str | None = ..., __final: bool = ...) -> tuple[str, int]: ...

else:
    def raw_unicode_escape_decode(__data: str | bytes, __errors: str | None = ...) -> tuple[str, int]: ...

def raw_unicode_escape_encode(__str: str, __errors: str | None = ...) -> tuple[bytes, int]: ...
def readbuffer_encode(__data: str | bytes, __errors: str | None = ...) -> tuple[bytes, int]: ...

if sys.version_info >= (3, 9):
    def unicode_escape_decode(__data: str | bytes, __errors: str | None = ..., __final: bool = ...) -> tuple[str, int]: ...

else:
    def unicode_escape_decode(__data: str | bytes, __errors: str | None = ...) -> tuple[str, int]: ...

def unicode_escape_encode(__str: str, __errors: str | None = ...) -> tuple[bytes, int]: ...

if sys.version_info < (3, 8):
    def unicode_internal_decode(__obj: str | bytes, __errors: str | None = ...) -> tuple[str, int]: ...
    def unicode_internal_encode(__obj: str | bytes, __errors: str | None = ...) -> tuple[bytes, int]: ...

def utf_16_be_decode(__data: bytes, __errors: str | None = ..., __final: int = ...) -> tuple[str, int]: ...
def utf_16_be_encode(__str: str, __errors: str | None = ...) -> tuple[bytes, int]: ...
def utf_16_decode(__data: bytes, __errors: str | None = ..., __final: int = ...) -> tuple[str, int]: ...
def utf_16_encode(__str: str, __errors: str | None = ..., __byteorder: int = ...) -> tuple[bytes, int]: ...
def utf_16_ex_decode(
    __data: bytes, __errors: str | None = ..., __byteorder: int = ..., __final: int = ...
) -> tuple[str, int, int]: ...
def utf_16_le_decode(__data: bytes, __errors: str | None = ..., __final: int = ...) -> tuple[str, int]: ...
def utf_16_le_encode(__str: str, __errors: str | None = ...) -> tuple[bytes, int]: ...
def utf_32_be_decode(__data: bytes, __errors: str | None = ..., __final: int = ...) -> tuple[str, int]: ...
def utf_32_be_encode(__str: str, __errors: str | None = ...) -> tuple[bytes, int]: ...
def utf_32_decode(__data: bytes, __errors: str | None = ..., __final: int = ...) -> tuple[str, int]: ...
def utf_32_encode(__str: str, __errors: str | None = ..., __byteorder: int = ...) -> tuple[bytes, int]: ...
def utf_32_ex_decode(
    __data: bytes, __errors: str | None = ..., __byteorder: int = ..., __final: int = ...
) -> tuple[str, int, int]: ...
def utf_32_le_decode(__data: bytes, __errors: str | None = ..., __final: int = ...) -> tuple[str, int]: ...
def utf_32_le_encode(__str: str, __errors: str | None = ...) -> tuple[bytes, int]: ...
def utf_7_decode(__data: bytes, __errors: str | None = ..., __final: int = ...) -> tuple[str, int]: ...
def utf_7_encode(__str: str, __errors: str | None = ...) -> tuple[bytes, int]: ...
def utf_8_decode(__data: bytes, __errors: str | None = ..., __final: int = ...) -> tuple[str, int]: ...
def utf_8_encode(__str: str, __errors: str | None = ...) -> tuple[bytes, int]: ...

if sys.platform == "win32":
    def mbcs_decode(__data: bytes, __errors: str | None = ..., __final: int = ...) -> tuple[str, int]: ...
    def mbcs_encode(__str: str, __errors: str | None = ...) -> tuple[bytes, int]: ...
    def code_page_decode(__codepage: int, __data: bytes, __errors: str | None = ..., __final: int = ...) -> tuple[str, int]: ...
    def code_page_encode(__code_page: int, __str: str, __errors: str | None = ...) -> tuple[bytes, int]: ...
    def oem_decode(__data: bytes, __errors: str | None = ..., __final: int = ...) -> tuple[str, int]: ...
    def oem_encode(__str: str, __errors: str | None = ...) -> tuple[bytes, int]: ...
