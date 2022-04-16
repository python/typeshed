import sys
from _typeshed import ReadableBuffer, Self, WriteableBuffer
from abc import abstractmethod
from typing import Any, Callable, ClassVar, Generic, Iterable, Iterator, Mapping, Sequence, TypeVar, Union as _UnionT, overload
from typing_extensions import TypeAlias

if sys.version_info >= (3, 9):
    from types import GenericAlias

_T = TypeVar("_T")
_DLLT = TypeVar("_DLLT", bound=CDLL)
_CT = TypeVar("_CT", bound=_CData)

RTLD_GLOBAL: int
RTLD_LOCAL: int
DEFAULT_MODE: int

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
            handle: int | None = ...,
            use_errno: bool = ...,
            use_last_error: bool = ...,
            winmode: int | None = ...,
        ) -> None: ...
    else:
        def __init__(
            self, name: str | None, mode: int = ..., handle: int | None = ..., use_errno: bool = ..., use_last_error: bool = ...
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

class _CDataMeta(type):
    # By default mypy complains about the following two methods, because strictly speaking cls
    # might not be a Type[_CT]. However this can never actually happen, because the only class that
    # uses _CDataMeta as its metaclass is _CData. So it's safe to ignore the errors here.
    def __mul__(cls: type[_CT], other: int) -> type[Array[_CT]]: ...  # type: ignore[misc]
    def __rmul__(cls: type[_CT], other: int) -> type[Array[_CT]]: ...  # type: ignore[misc]

class _CData(metaclass=_CDataMeta):
    _b_base: int
    _b_needsfree_: bool
    _objects: Mapping[Any, int] | None
    @classmethod
    def from_buffer(cls: type[Self], source: WriteableBuffer, offset: int = ...) -> Self: ...
    @classmethod
    def from_buffer_copy(cls: type[Self], source: ReadableBuffer, offset: int = ...) -> Self: ...
    @classmethod
    def from_address(cls: type[Self], address: int) -> Self: ...
    @classmethod
    def from_param(cls: type[Self], obj: Any) -> Self | _CArgObject: ...
    @classmethod
    def in_dll(cls: type[Self], library: CDLL, name: str) -> Self: ...

class _CanCastTo(_CData): ...
class _PointerLike(_CanCastTo): ...

_ECT: TypeAlias = Callable[[type[_CData] | None, _FuncPointer, tuple[_CData, ...]], _CData]
_PF: TypeAlias = _UnionT[tuple[int], tuple[int, str], tuple[int, str, Any]]

class _FuncPointer(_PointerLike, _CData):
    restype: type[_CData] | Callable[[int], Any] | None
    argtypes: Sequence[type[_CData]]
    errcheck: _ECT
    @overload
    def __init__(self, address: int) -> None: ...
    @overload
    def __init__(self, callable: Callable[..., Any]) -> None: ...
    @overload
    def __init__(self, func_spec: tuple[str | int, CDLL], paramflags: tuple[_PF, ...] = ...) -> None: ...
    @overload
    def __init__(self, vtlb_index: int, name: str, paramflags: tuple[_PF, ...] = ..., iid: pointer[c_int] = ...) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...

class _NamedFuncPointer(_FuncPointer):
    __name__: str

class ArgumentError(Exception): ...

def CFUNCTYPE(
    restype: type[_CData] | None, *argtypes: type[_CData], use_errno: bool = ..., use_last_error: bool = ...
) -> type[_FuncPointer]: ...

if sys.platform == "win32":
    def WINFUNCTYPE(
        restype: type[_CData] | None, *argtypes: type[_CData], use_errno: bool = ..., use_last_error: bool = ...
    ) -> type[_FuncPointer]: ...

def PYFUNCTYPE(restype: type[_CData] | None, *argtypes: type[_CData]) -> type[_FuncPointer]: ...

class _CArgObject: ...

# Any type that can be implicitly converted to c_void_p when passed as a C function argument.
# (bytes is not included here, see below.)
_CVoidPLike: TypeAlias = _PointerLike | Array[Any] | _CArgObject | int
# Same as above, but including types known to be read-only (i. e. bytes).
# This distinction is not strictly necessary (ctypes doesn't differentiate between const
# and non-const pointers), but it catches errors like memmove(b'foo', buf, 4)
# when memmove(buf, b'foo', 4) was intended.
_CVoidConstPLike: TypeAlias = _CVoidPLike | bytes

def addressof(obj: _CData) -> int: ...
def alignment(obj_or_type: _CData | type[_CData]) -> int: ...
def byref(obj: _CData, offset: int = ...) -> _CArgObject: ...

_CastT = TypeVar("_CastT", bound=_CanCastTo)

def cast(obj: _CData | _CArgObject | int, typ: type[_CastT]) -> _CastT: ...
def create_string_buffer(init: int | bytes, size: int | None = ...) -> Array[c_char]: ...

c_buffer = create_string_buffer

def create_unicode_buffer(init: int | str, size: int | None = ...) -> Array[c_wchar]: ...

if sys.platform == "win32":
    def DllCanUnloadNow() -> int: ...
    def DllGetClassObject(rclsid: Any, riid: Any, ppv: Any) -> int: ...  # TODO not documented
    def FormatError(code: int = ...) -> str: ...
    def GetLastError() -> int: ...

def get_errno() -> int: ...

if sys.platform == "win32":
    def get_last_error() -> int: ...

def memmove(dst: _CVoidPLike, src: _CVoidConstPLike, count: int) -> int: ...
def memset(dst: _CVoidPLike, c: int, count: int) -> int: ...
def POINTER(type: type[_CT]) -> type[pointer[_CT]]: ...

# The real ctypes.pointer is a function, not a class. The stub version of pointer behaves like
# ctypes._Pointer in that it is the base class for all pointer types. Unlike the real _Pointer,
# it can be instantiated directly (to mimic the behavior of the real pointer function).
class pointer(Generic[_CT], _PointerLike, _CData):
    _type_: type[_CT]
    contents: _CT
    def __init__(self, arg: _CT = ...) -> None: ...
    @overload
    def __getitem__(self, __i: int) -> _CT: ...
    @overload
    def __getitem__(self, __s: slice) -> list[_CT]: ...
    @overload
    def __setitem__(self, __i: int, __o: _CT) -> None: ...
    @overload
    def __setitem__(self, __s: slice, __o: Iterable[_CT]) -> None: ...

def resize(obj: _CData, size: int) -> None: ...
def set_errno(value: int) -> int: ...

if sys.platform == "win32":
    def set_last_error(value: int) -> int: ...

def sizeof(obj_or_type: _CData | type[_CData]) -> int: ...
def string_at(address: _CVoidConstPLike, size: int = ...) -> bytes: ...

if sys.platform == "win32":
    def WinError(code: int | None = ..., descr: str | None = ...) -> OSError: ...

def wstring_at(address: _CVoidConstPLike, size: int = ...) -> str: ...

class _SimpleCData(Generic[_T], _CData):
    value: _T
    def __init__(self, value: _T = ...) -> None: ...

class c_byte(_SimpleCData[int]): ...

class c_char(_SimpleCData[bytes]):
    def __init__(self, value: int | bytes = ...) -> None: ...

class c_char_p(_PointerLike, _SimpleCData[bytes | None]):
    def __init__(self, value: int | bytes | None = ...) -> None: ...

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
class c_void_p(_PointerLike, _SimpleCData[int | None]): ...
class c_wchar(_SimpleCData[str]): ...

class c_wchar_p(_PointerLike, _SimpleCData[str | None]):
    def __init__(self, value: int | str | None = ...) -> None: ...

class c_bool(_SimpleCData[bool]):
    def __init__(self, value: bool = ...) -> None: ...

if sys.platform == "win32":
    class HRESULT(_SimpleCData[int]): ...  # TODO undocumented

class py_object(_CanCastTo, _SimpleCData[_T]): ...

class _CField:
    offset: int
    size: int

class _StructUnionMeta(_CDataMeta):
    _fields_: Sequence[tuple[str, type[_CData]] | tuple[str, type[_CData], int]]
    _pack_: int
    _anonymous_: Sequence[str]
    def __getattr__(self, name: str) -> _CField: ...

class _StructUnionBase(_CData, metaclass=_StructUnionMeta):
    def __init__(self, *args: Any, **kw: Any) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...

class Union(_StructUnionBase): ...
class Structure(_StructUnionBase): ...
class BigEndianStructure(Structure): ...
class LittleEndianStructure(Structure): ...

class Array(Generic[_CT], _CData):
    @property
    @abstractmethod
    def _length_(self) -> int: ...
    @_length_.setter
    def _length_(self, value: int) -> None: ...
    @property
    @abstractmethod
    def _type_(self) -> type[_CT]: ...
    @_type_.setter
    def _type_(self, value: type[_CT]) -> None: ...
    raw: bytes  # Note: only available if _CT == c_char
    value: Any  # Note: bytes if _CT == c_char, str if _CT == c_wchar, unavailable otherwise
    # TODO These methods cannot be annotated correctly at the moment.
    # All of these "Any"s stand for the array's element type, but it's not possible to use _CT
    # here, because of a special feature of ctypes.
    # By default, when accessing an element of an Array[_CT], the returned object has type _CT.
    # However, when _CT is a "simple type" like c_int, ctypes automatically "unboxes" the object
    # and converts it to the corresponding Python primitive. For example, when accessing an element
    # of an Array[c_int], a Python int object is returned, not a c_int.
    # This behavior does *not* apply to subclasses of "simple types".
    # If MyInt is a subclass of c_int, then accessing an element of an Array[MyInt] returns
    # a MyInt, not an int.
    # This special behavior is not easy to model in a stub, so for now all places where
    # the array element type would belong are annotated with Any instead.
    def __init__(self, *args: Any) -> None: ...
    @overload
    def __getitem__(self, __i: int) -> Any: ...
    @overload
    def __getitem__(self, __s: slice) -> list[Any]: ...
    @overload
    def __setitem__(self, __i: int, __o: Any) -> None: ...
    @overload
    def __setitem__(self, __s: slice, __o: Iterable[Any]) -> None: ...
    def __iter__(self) -> Iterator[Any]: ...
    # Can't inherit from Sized because the metaclass conflict between
    # Sized and _CData prevents using _CDataMeta.
    def __len__(self) -> int: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...
