# Stubs for ctypes

from typing import (
    Any, Callable, ClassVar, Iterable, List, Mapping, Optional, Sequence, Sized, Tuple, Type,
    Generic, TypeVar, overload,
)
from typing import Union as _UnionT
import sys

_T = TypeVar('_T')
if sys.platform == 'win32':
    _DLLT = TypeVar('_DLLT', CDLL, OleDLL, WinDLL, PyDLL)
else:
    _DLLT = TypeVar('_DLLT', CDLL, PyDLL)
_CT = TypeVar('_CT', bound=_CData)


RTLD_GLOBAL: int = ...
RTLD_LOCAL: int = ...
DEFAULT_MODE: int = ...


class _DLL:
    def __init__(self, name: str, mode: int = ..., handle: Optional[int] = ...,
                 use_errno: bool = ..., use_last_error: bool = ...) -> None: ...
    def __getattr__(self, name: str) -> _FuncPtr: ...
    def __getitem__(self, name: str) -> _FuncPtr: ...
class CDLL(_DLL): ...
if sys.platform == 'win32':
    class OleDLL(_DLL): ...
    class WinDLL(_DLL): ...
class PyDLL(_DLL):
    _handle: int = ...
    _name: str = ...
    def __init__(self, name: str, mode: int = ...,
                 handle: Optional[int] = ...) -> None: ...

class LibraryLoader(Generic[_DLLT]):
    def __init__(self, dlltype: Type[_DLLT]) -> None: ...
    def LoadLibrary(self, name: str) -> _DLLT: ...

cdll: LibraryLoader[CDLL] = ...
if sys.platform == 'win32':
    windll: LibraryLoader[WinDLL] = ...
    oledll: LibraryLoader[OleDLL] = ...
pydll: LibraryLoader[PyDLL] = ...
pythonapi: PyDLL = ...

class _CDataMeta(type):
    # TODO The return type is not accurate. The method definition *should* look like this:
    # def __mul__(cls: Type[_CT], other: int) -> Type[Array[_CT]]: ...
    # but that is not valid, because technically a _CDataMeta might not be a Type[_CT].
    # This can never actually happen, because all _CDataMeta instances are _CData subclasses, but a typechecker doesn't know that.
    def __mul__(cls: _CDataMeta, other: int) -> Type[Array[_CT]]: ...
    def __rmul__(cls: _CDataMeta, other: int) -> Type[Array[_CT]]: ...
class _CData(metaclass=_CDataMeta):
    _b_base: int = ...
    _b_needsfree_: bool = ...
    _objects: Optional[Mapping[Any, int]] = ...
    @classmethod
    def from_buffer(cls: Type[_CT], source: bytearray, offset: int = ...) -> _CT: ...
    @classmethod
    def from_buffer_copy(cls: Type[_CT], source: bytearray, offset: int = ...) -> _CT: ...
    @classmethod
    def from_address(cls: Type[_CT], address: int) -> _CT: ...
    @classmethod
    def from_param(cls: Type[_CT], obj: Any) -> _UnionT[_CT, _cparam]: ...
    @classmethod
    def in_dll(cls: Type[_CT], library: _DLL, name: str) -> _CT: ...

class _PointerLike(_CData): pass

_ECT = Callable[[Optional[Type[_CData]],
                 _FuncPtr,
                 Tuple[_CData, ...]],
                _CData]
class _FuncPtr(_PointerLike, _CData):
    restype: _UnionT[Type[_CData], Callable[[int], None], None] = ...
    argtypes: Tuple[Type[_CData], ...] = ...
    errcheck: _ECT = ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...

class ArgumentError(Exception): ...


def CFUNCTYPE(restype: Type[_CData],
              *argtypes: Type[_CData],
              use_errno: bool = ...,
              use_last_error: bool = ...) -> Type[_FuncProto]: ...
if sys.platform == 'win32':
    def WINFUNCTYPE(restype: Type[_CData],
                    *argtypes: Type[_CData],
                    use_errno: bool = ...,
                    use_last_error: bool = ...) -> Type[_FuncProto]: ...
def PYFUNCTYPE(restype: Type[_CData],
               *argtypes: Type[_CData]) -> Type[_FuncProto]: ...

_PF = _UnionT[
    Tuple[int],
    Tuple[int, str],
    Tuple[int, str, Any]
]

class _FuncProto(_FuncPtr):
    @overload
    def __init__(self, address: int) -> None: ...
    @overload
    def __init__(self, callable: Callable[..., Any]) -> None: ...
    @overload
    def __init__(self, func_spec: Tuple[_UnionT[str, int], _DLL],
                 paramflags: Tuple[_PF, ...] = ...) -> None: ...
    @overload
    def __init__(self, vtlb_index: int, name: str,
                 paramflags: Tuple[_PF, ...] = ...,
                 iid: _Pointer[c_int] = ...) -> None: ...

class _cparam: ...

def addressof(obj: _CData) -> int: ...
def alignment(obj_or_type: _UnionT[_CData, Type[_CData]]) -> int: ...
def byref(obj: _CData, offset: int = ...) -> _cparam: ...
_PT = TypeVar('_PT', bound=_PointerLike)
def cast(obj: _CData, type: Type[_PT]) -> _PT: ...
def create_string_buffer(init_or_size: _UnionT[int, bytes],
                         size: Optional[int] = ...) -> Array[c_char]: ...
c_buffer = create_string_buffer
def create_unicode_buffer(init_or_size: _UnionT[int, str],
                          size: Optional[int] = ...) -> Array[c_wchar]: ...
if sys.platform == 'win32':
    def DllCanUnloadNow() -> int: ...
    def DllGetClassObject(rclsid: Any, riid: Any, ppv: Any) -> int: ...  # TODO not documented
    def FormatError(code: int) -> str: ...
    def GetLastError() -> int: ...
def get_errno() -> int: ...
if sys.platform == 'win32':
    def get_last_error() -> int: ...
def memmove(dst: _UnionT[int, _CData],
            src: _UnionT[int, _CData],
            count: int) -> None: ...
def memset(dst: _UnionT[int, _CData],
           c: int, count: int) -> None: ...
def POINTER(type: Type[_CT]) -> Type[_Pointer[_CT]]: ...
def pointer(obj: _CT) -> _Pointer[_CT]: ...
def resize(obj: _CData, size: int) -> None: ...
if sys.version_info < (3,):
    def set_conversion_mode(encoding: str, errors: str) -> Tuple[str, str]: ...
def set_errno(value: int) -> int: ...
if sys.platform == 'win32':
    def set_last_error(value: int) -> int: ...
def sizeof(obj_or_type: _UnionT[_CData, Type[_CData]]) -> int: ...
def string_at(address: int, size: int = ...) -> bytes: ...
if sys.platform == 'win32':
    def WinError(code: Optional[int] = ...,
                 desc: Optional[str] = ...) -> OSError: ...
def wstring_at(address: int, size: int = ...) -> str: ...

class _SimpleCData(Generic[_T], _CData):
    value: _T = ...
    def __init__(self, value: _T = ...) -> None: ...

class c_byte(_SimpleCData[int]): ...

class c_char(_SimpleCData[bytes]): ...
class c_char_p(_PointerLike, _SimpleCData[Optional[bytes]]):
    def __init__(self, value: _UnionT[int, bytes] = ...) -> None: ...

class c_double(_SimpleCData[float]): ...
class c_longdouble(_SimpleCData[float]): ...
class c_float(_SimpleCData[float]): ...

class c_int(_SimpleCData[int]): ...
class c_int8(_SimpleCData[int]): ...
class c_int16(_SimpleCData[int]): ...
class c_int32(_SimpleCData[int]): ...
class c_int64(_SimpleCData[int]): ...

class c_long(_SimpleCData[int]): ...
class c_longlong(_SimpleCData[int]): ...

class c_short(_SimpleCData[int]): ...

class c_size_t(_SimpleCData[int]): ...
class c_ssize_t(_SimpleCData[int]): ...

class c_ubyte(_SimpleCData[int]): ...

class c_uint(_SimpleCData[int]): ...
class c_uint8(_SimpleCData[int]): ...
class c_uint16(_SimpleCData[int]): ...
class c_uint32(_SimpleCData[int]): ...
class c_uint64(_SimpleCData[int]): ...

class c_ulong(_SimpleCData[int]): ...
class c_ulonglong(_SimpleCData[int]): ...

class c_ushort(_SimpleCData[int]): ...

class c_void_p(_PointerLike, _SimpleCData[Optional[int]]): ...

class c_wchar(_SimpleCData[str]): ...
class c_wchar_p(_PointerLike, _SimpleCData[Optional[str]]):
    def __init__(self, value: _UnionT[int, str] = ...) -> None: ...

class c_bool(_SimpleCData[bool]):
    def __init__(self, value: bool) -> None: ...

if sys.platform == 'win32':
    class HRESULT(_SimpleCData[Any]): ...  # TODO undocumented

class py_object(Generic[_T], _SimpleCData[_T]): ...

class _CField:
    offset: int = ...
    size: int = ...
class _StructUnionMeta(_CDataMeta):
    _fields_: Sequence[_UnionT[Tuple[str, Type[_CData]], Tuple[str, Type[_CData], int]]] = ...
    _pack_: int = ...
    _anonymous_: Sequence[str] = ...
    def __getattr__(self, name: str) -> _CField: ...
class _StructUnionBase(_CData, metaclass=_StructUnionMeta):
    def __init__(self, *args: Any, **kw: Any) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...

class Union(_StructUnionBase): pass
class Structure(_StructUnionBase): pass
class BigEndianStructure(Structure): pass
class LittleEndianStructure(Structure): pass

class Array(Generic[_T], Sized, _CData):
    _length_: ClassVar[int] = ...
    _type_: ClassVar[Type[_T]] = ...
    raw: bytes = ...  # TODO only available with _T == c_char
    value: bytes = ...  # TODO only available with _T == c_char
    def __init__(self, *args: _T) -> None: ...
    @overload
    def __getitem__(self, i: int) -> _T: ...
    @overload
    def __getitem__(self, s: slice) -> List[_T]: ...
    @overload
    def __setitem__(self, i: int, o: _T) -> None: ...
    @overload
    def __setitem__(self, s: slice, o: Iterable[_T]) -> None: ...
    def __iter__(self) -> Iterable[_T]: ...


class _Pointer(Generic[_T], _PointerLike, _CData):
    _type_: ClassVar[Type[_T]] = ...
    contents: _T = ...
    def __init__(self, arg: _T = ...) -> None: ...
    @overload
    def __getitem__(self, i: int) -> _T: ...
    @overload
    def __getitem__(self, s: slice) -> List[_T]: ...
    @overload
    def __setitem__(self, i: int, o: _T) -> None: ...
    @overload
    def __setitem__(self, s: slice, o: Iterable[_T]) -> None: ...
