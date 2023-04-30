import sys
from _typeshed import ReadableBuffer, WriteableBuffer
from abc import abstractmethod
from collections.abc import Iterable, Iterator, Mapping
from ctypes import CDLL, _CArgObject, _PointerLike
from typing import Any, Generic, TypeVar, overload
from typing_extensions import Self, TypeAlias

if sys.version_info >= (3, 9):
    from types import GenericAlias

_T = TypeVar("_T")
_CT = TypeVar("_CT", bound=_CData)

FUNCFLAG_CDECL: int
FUNCFLAG_PYTHONAPI: int
FUNCFLAG_USE_ERRNO: int
FUNCFLAG_USE_LASTERROR: int
RTLD_GLOBAL: int
RTLD_LOCAL: int

if sys.version_info >= (3, 11):
    CTYPES_MAX_ARGCOUNT: int

if sys.platform == "win32":
    # Description, Source, HelpFile, HelpContext, scode
    _COMError_Details: TypeAlias = tuple[str | None, str | None, str | None, int | None, int | None]

    class COMError(Exception):
        hresult: int
        text: str | None
        details: _COMError_Details

        def __init__(self, hresult: int, text: str | None, details: _COMError_Details) -> None: ...

    def CopyComPointer(src: _PointerLike, dst: _PointerLike | _CArgObject) -> int: ...

    FUNCFLAG_HRESULT: int
    FUNCFLAG_STDCALL: int

class _CDataMeta(type):
    # By default mypy complains about the following two methods, because strictly speaking cls
    # might not be a Type[_CT]. However this can never actually happen, because the only class that
    # uses _CDataMeta as its metaclass is _CData. So it's safe to ignore the errors here.
    def __mul__(cls: type[_CT], other: int) -> type[Array[_CT]]: ...  # type: ignore[misc]  # pyright: ignore[reportGeneralTypeIssues]
    def __rmul__(cls: type[_CT], other: int) -> type[Array[_CT]]: ...  # type: ignore[misc]  # pyright: ignore[reportGeneralTypeIssues]

class _CData(metaclass=_CDataMeta):
    _b_base_: int
    _b_needsfree_: bool
    _objects: Mapping[Any, int] | None
    @classmethod
    def from_buffer(cls, source: WriteableBuffer, offset: int = ...) -> Self: ...
    @classmethod
    def from_buffer_copy(cls, source: ReadableBuffer, offset: int = ...) -> Self: ...
    @classmethod
    def from_address(cls, address: int) -> Self: ...
    @classmethod
    def from_param(cls, obj: Any) -> Self | _CArgObject: ...
    @classmethod
    def in_dll(cls, library: CDLL, name: str) -> Self: ...

class _SimpleCData(Generic[_T], _CData):
    value: _T
    # The TypeVar can be unsolved here,
    # but we can't use overloads without creating many, many mypy false-positive errors
    def __init__(self, value: _T = ...) -> None: ...  # pyright: ignore[reportInvalidTypeVarUse]

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
    # Note: only available if _CT == c_char
    @property
    def raw(self) -> bytes: ...
    @raw.setter
    def raw(self, value: ReadableBuffer) -> None: ...
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
    def __getitem__(self, __key: int) -> Any: ...
    @overload
    def __getitem__(self, __key: slice) -> list[Any]: ...
    @overload
    def __setitem__(self, __key: int, __value: Any) -> None: ...
    @overload
    def __setitem__(self, __key: slice, __value: Iterable[Any]) -> None: ...
    def __iter__(self) -> Iterator[Any]: ...
    # Can't inherit from Sized because the metaclass conflict between
    # Sized and _CData prevents using _CDataMeta.
    def __len__(self) -> int: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...
