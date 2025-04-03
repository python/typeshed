import sys
from _typeshed import ReadableBuffer, SupportsRead, SupportsWrite
from collections.abc import Iterable, MutableSequence
from typing import Any, ClassVar, Literal, SupportsIndex, TypeVar, overload
from typing_extensions import Self, TypeAlias
from types import GenericAlias

_IntTypeCode: TypeAlias = Literal["b", "B", "h", "H", "i", "I", "l", "L", "q", "Q"]
_FloatTypeCode: TypeAlias = Literal["f", "d"]
_UnicodeTypeCode: TypeAlias = Literal["u"]
_TypeCode: TypeAlias = _IntTypeCode | _FloatTypeCode | _UnicodeTypeCode

_T = TypeVar("_T", int, float, str)

typecodes: str

class array(MutableSequence[_T]):
    @property
    def typecode(self) -> _TypeCode: ...
    @property
    def itemsize(self) -> int: ...
    @overload
    def __new__(
        cls: type[array[int]], typecode: _IntTypeCode, initializer: bytes | bytearray | Iterable[int] = ..., /
    ) -> array[int]: ...
    @overload
    def __new__(
        cls: type[array[float]], typecode: _FloatTypeCode, initializer: bytes | bytearray | Iterable[float] = ..., /
    ) -> array[float]: ...
    @overload
    def __new__(
        cls: type[array[str]], typecode: _UnicodeTypeCode, initializer: bytes | bytearray | Iterable[str] = ..., /
    ) -> array[str]: ...
    @overload
    def __new__(cls, typecode: str, initializer: Iterable[_T], /) -> Self: ...
    @overload
    def __new__(cls, typecode: str, initializer: bytes | bytearray = ..., /) -> Self: ...
    def append(self, v: _T, /) -> None: ...
    def buffer_info(self) -> tuple[int, int]: ...
    def byteswap(self) -> None: ...
    def count(self, v: _T, /) -> int: ...
    def extend(self, bb: Iterable[_T], /) -> None: ...
    def frombytes(self, buffer: ReadableBuffer, /) -> None: ...
    def fromfile(self, f: SupportsRead[bytes], n: int, /) -> None: ...
    def fromlist(self, list: list[_T], /) -> None: ...
    def fromunicode(self, ustr: str, /) -> None: ...
    if sys.version_info >= (3, 10):
        def index(self, v: _T, start: int = 0, stop: int = sys.maxsize, /) -> int: ...
    else:
        def index(self, v: _T, /) -> int: ...  # type: ignore[override]

    def insert(self, i: int, v: _T, /) -> None: ...
    def pop(self, i: int = -1, /) -> _T: ...
    def remove(self, v: _T, /) -> None: ...
    def tobytes(self) -> bytes: ...
    def tofile(self, f: SupportsWrite[bytes], /) -> None: ...
    def tolist(self) -> list[_T]: ...
    def tounicode(self) -> str: ...

    __hash__: ClassVar[None]  # type: ignore[assignment]
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, key: SupportsIndex, /) -> _T: ...
    @overload
    def __getitem__(self, key: slice, /) -> array[_T]: ...
    @overload  # type: ignore[override]
    def __setitem__(self, key: SupportsIndex, value: _T, /) -> None: ...
    @overload
    def __setitem__(self, key: slice, value: array[_T], /) -> None: ...
    def __delitem__(self, key: SupportsIndex | slice, /) -> None: ...
    def __add__(self, value: array[_T], /) -> array[_T]: ...
    def __eq__(self, value: object, /) -> bool: ...
    def __ge__(self, value: array[_T], /) -> bool: ...
    def __gt__(self, value: array[_T], /) -> bool: ...
    def __iadd__(self, value: array[_T], /) -> Self: ...  # type: ignore[override]
    def __imul__(self, value: int, /) -> Self: ...
    def __le__(self, value: array[_T], /) -> bool: ...
    def __lt__(self, value: array[_T], /) -> bool: ...
    def __mul__(self, value: int, /) -> array[_T]: ...
    def __rmul__(self, value: int, /) -> array[_T]: ...
    def __copy__(self) -> array[_T]: ...
    def __deepcopy__(self, unused: Any, /) -> array[_T]: ...
    def __buffer__(self, flags: int, /) -> memoryview: ...
    def __release_buffer__(self, buffer: memoryview, /) -> None: ...
    if sys.version_info >= (3, 12):
        def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...

ArrayType = array
