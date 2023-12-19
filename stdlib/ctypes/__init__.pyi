import sys
from _ctypes import (
    POINTER as POINTER,
    RTLD_GLOBAL as RTLD_GLOBAL,
    RTLD_LOCAL as RTLD_LOCAL,
    Array as Array,
    CFuncPtr as _CFuncPtr,
    Structure as Structure,
    Union as Union,
    _CanCastTo as _CanCastTo,
    _CArgObject as _CArgObject,
    _CData as _CData,
    _CDataMeta as _CDataMeta,
    _CField as _CField,
    _Pointer as _Pointer,
    _PointerLike as _PointerLike,
    _SimpleCData as _SimpleCData,
    _StructUnionBase as _StructUnionBase,
    _StructUnionMeta as _StructUnionMeta,
    addressof as addressof,
    alignment as alignment,
    byref as byref,
    get_errno as get_errno,
    pointer as pointer,
    resize as resize,
    set_errno as set_errno,
    sizeof as sizeof,
)
from ctypes._endian import BigEndianStructure as BigEndianStructure, LittleEndianStructure as LittleEndianStructure
from typing import Any, ClassVar, Generic, TypeVar
from typing_extensions import TypeAlias

if sys.platform == "win32":
    from _ctypes import FormatError as FormatError, get_last_error as get_last_error, set_last_error as set_last_error

if sys.version_info >= (3, 11):
    from ctypes._endian import BigEndianUnion as BigEndianUnion, LittleEndianUnion as LittleEndianUnion

if sys.version_info >= (3, 9):
    from types import GenericAlias

_T = TypeVar("_T")
_DLLT = TypeVar("_DLLT", bound=CDLL)

DEFAULT_MODE: int

class ArgumentError(Exception): ...

class CDLL:
    _func_flags_: ClassVar[int]
    _func_restype_: ClassVar[_CData]
    _name: str
    _handle: int
    _FuncPtr: type[_FuncPointer]
    if sys.version_info >= (3, 8):
        def __init__(
            self,
            name: str | None,
            mode: int = ...,
            handle: int | None = None,
            use_errno: bool = False,
            use_last_error: bool = False,
            winmode: int | None = None,
        ) -> None: ...
    else:
        def __init__(
            self,
            name: str | None,
            mode: int = ...,
            handle: int | None = None,
            use_errno: bool = False,
            use_last_error: bool = False,
        ) -> None: ...

    def __getattr__(self, name: str) -> _NamedFuncPointer: ...
    def __getitem__(self, name_or_ordinal: str) -> _NamedFuncPointer: ...

if sys.platform == "win32":
    class OleDLL(CDLL): ...
    class WinDLL(CDLL): ...

class PyDLL(CDLL): ...

class LibraryLoader(Generic[_DLLT]):
    def __init__(self, dlltype: type[_DLLT]) -> None: ...
    def __getattr__(self, name: str) -> _DLLT: ...
    def __getitem__(self, name: str) -> _DLLT: ...
    def LoadLibrary(self, name: str) -> _DLLT: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...

cdll: LibraryLoader[CDLL]
if sys.platform == "win32":
    windll: LibraryLoader[WinDLL]
    oledll: LibraryLoader[OleDLL]
pydll: LibraryLoader[PyDLL]
pythonapi: PyDLL

class _FuncPointer(_CFuncPtr): ...

class _NamedFuncPointer(_FuncPointer):
    __name__: str

def CFUNCTYPE(
    restype: type[_CData] | None, *argtypes: type[_CData], use_errno: bool = ..., use_last_error: bool = ...
) -> type[_FuncPointer]: ...

if sys.platform == "win32":
    def WINFUNCTYPE(
        restype: type[_CData] | None, *argtypes: type[_CData], use_errno: bool = ..., use_last_error: bool = ...
    ) -> type[_FuncPointer]: ...

def PYFUNCTYPE(restype: type[_CData] | None, *argtypes: type[_CData]) -> type[_FuncPointer]: ...

# Any type that can be implicitly converted to c_void_p when passed as a C function argument.
# (bytes is not included here, see below.)
_CVoidPLike: TypeAlias = _PointerLike | Array[Any] | _CArgObject | int
# Same as above, but including types known to be read-only (i. e. bytes).
# This distinction is not strictly necessary (ctypes doesn't differentiate between const
# and non-const pointers), but it catches errors like memmove(b'foo', buf, 4)
# when memmove(buf, b'foo', 4) was intended.
_CVoidConstPLike: TypeAlias = _CVoidPLike | bytes

_CastT = TypeVar("_CastT", bound=_CanCastTo)

def cast(obj: _CData | _CArgObject | int, typ: type[_CastT]) -> _CastT: ...
def create_string_buffer(init: int | bytes, size: int | None = None) -> Array[c_char]: ...

c_buffer = create_string_buffer

def create_unicode_buffer(init: int | str, size: int | None = None) -> Array[c_wchar]: ...

if sys.platform == "win32":
    def DllCanUnloadNow() -> int: ...
    def DllGetClassObject(rclsid: Any, riid: Any, ppv: Any) -> int: ...  # TODO not documented
    def GetLastError() -> int: ...

def memmove(dst: _CVoidPLike, src: _CVoidConstPLike, count: int) -> int: ...
def memset(dst: _CVoidPLike, c: int, count: int) -> int: ...
def string_at(address: _CVoidConstPLike, size: int = -1) -> bytes: ...

if sys.platform == "win32":
    def WinError(code: int | None = None, descr: str | None = None) -> OSError: ...

def wstring_at(address: _CVoidConstPLike, size: int = -1) -> str: ...

class c_byte(_SimpleCData[int]): ...

class c_char(_SimpleCData[bytes]):
    def __init__(self, value: int | bytes | bytearray = ...) -> None: ...

class c_char_p(_PointerLike, _SimpleCData[bytes | None]):
    def __init__(self, value: int | bytes | None = ...) -> None: ...

class c_double(_SimpleCData[float]): ...
class c_longdouble(_SimpleCData[float]): ...  # can be an alias for c_double
class c_float(_SimpleCData[float]): ...
class c_int(_SimpleCData[int]): ...  # can be an alias for c_long
class c_long(_SimpleCData[int]): ...
class c_longlong(_SimpleCData[int]): ...  # can be an alias for c_long
class c_short(_SimpleCData[int]): ...
class c_size_t(_SimpleCData[int]): ...  # alias for c_uint, c_ulong, or c_ulonglong
class c_ssize_t(_SimpleCData[int]): ...  # alias for c_int, c_long, or c_longlong
class c_ubyte(_SimpleCData[int]): ...
class c_uint(_SimpleCData[int]): ...  # can be an alias for c_ulong
class c_ulong(_SimpleCData[int]): ...
class c_ulonglong(_SimpleCData[int]): ...  # can be an alias for c_ulong
class c_ushort(_SimpleCData[int]): ...
class c_void_p(_PointerLike, _SimpleCData[int | None]): ...
class c_wchar(_SimpleCData[str]): ...

c_int8 = c_byte

# these are actually dymanic aliases for c_short, c_int, c_long, or c_longlong
class c_int16(_SimpleCData[int]): ...
class c_int32(_SimpleCData[int]): ...
class c_int64(_SimpleCData[int]): ...

c_uint8 = c_ubyte

# these are actually dymanic aliases for c_ushort, c_uint, c_ulong, or c_ulonglong
class c_uint16(_SimpleCData[int]): ...
class c_uint32(_SimpleCData[int]): ...
class c_uint64(_SimpleCData[int]): ...

class c_wchar_p(_PointerLike, _SimpleCData[str | None]):
    def __init__(self, value: int | str | None = ...) -> None: ...

class c_bool(_SimpleCData[bool]):
    def __init__(self, value: bool = ...) -> None: ...

if sys.platform == "win32":
    class HRESULT(_SimpleCData[int]): ...  # TODO undocumented

if sys.version_info >= (3, 12):
    c_time_t: type[c_int32 | c_int64]  # alias for one or the other at runtime

class py_object(_CanCastTo, _SimpleCData[_T]): ...
