import sys
from _typeshed import ReadableBuffer, SupportsRead, SupportsWrite
from collections.abc import Iterable

# pytype crashes if array inherits from collections.abc.MutableSequence instead of typing.MutableSequence
from typing import Any, Generic, MutableSequence, TypeVar, overload  # noqa: Y022
from typing_extensions import Literal, Self, SupportsIndex, TypeAlias

if sys.version_info >= (3, 12):
    from types import GenericAlias

_IntTypeCode: TypeAlias = Literal["b", "B", "h", "H", "i", "I", "l", "L", "q", "Q"]
_FloatTypeCode: TypeAlias = Literal["f", "d"]
_UnicodeTypeCode: TypeAlias = Literal["u"]
_TypeCode: TypeAlias = _IntTypeCode | _FloatTypeCode | _UnicodeTypeCode

_T = TypeVar("_T", int, float, str)

typecodes: str

class array(MutableSequence[_T], Generic[_T]):
    @property
    def typecode(self) -> _TypeCode: ...
    @property
    def itemsize(self) -> int: ...
    @overload
    def __init__(self: array[int], __typecode: _IntTypeCode, __initializer: bytes | bytearray | Iterable[int] = ...) -> None: ...
    @overload
    def __init__(
        self: array[float], __typecode: _FloatTypeCode, __initializer: bytes | bytearray | Iterable[float] = ...
    ) -> None: ...
    @overload
    def __init__(
        self: array[str], __typecode: _UnicodeTypeCode, __initializer: bytes | bytearray | Iterable[str] = ...
    ) -> None: ...
    @overload
    def __init__(self, __typecode: str, __initializer: Iterable[_T]) -> None: ...
    @overload
    def __init__(self, __typecode: str, __initializer: bytes | bytearray = ...) -> None: ...
    def append(self, __v: _T) -> None: ...
    def buffer_info(self) -> tuple[int, int]: ...
    def byteswap(self) -> None: ...
    def count(self, __v: _T) -> int: ...
    def extend(self, __bb: Iterable[_T]) -> None: ...
    def frombytes(self, __buffer: ReadableBuffer) -> None: ...
    def fromfile(self, __f: SupportsRead[bytes], __n: int) -> None: ...
    def fromlist(self, __list: list[_T]) -> None: ...
    def fromunicode(self, __ustr: str) -> None: ...
    if sys.version_info >= (3, 10):
        def index(self, __v: _T, __start: int = 0, __stop: int = sys.maxsize) -> int: ...
    else:
        def index(self, __v: _T) -> int: ...  # type: ignore[override]

    def insert(self, __i: int, __v: _T) -> None: ...
    def pop(self, __i: int = -1) -> _T: ...
    def remove(self, __v: _T) -> None: ...
    def tobytes(self) -> bytes: ...
    def tofile(self, __f: SupportsWrite[bytes]) -> None: ...
    def tolist(self) -> list[_T]: ...
    def tounicode(self) -> str: ...
    if sys.version_info < (3, 9):
        def fromstring(self, __buffer: str | ReadableBuffer) -> None: ...
        def tostring(self) -> bytes: ...

    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, __key: SupportsIndex) -> _T: ...
    @overload
    def __getitem__(self, __key: slice) -> array[_T]: ...
    @overload  # type: ignore[override]
    def __setitem__(self, __key: SupportsIndex, __value: _T) -> None: ...
    @overload
    def __setitem__(self, __key: slice, __value: array[_T]) -> None: ...
    def __delitem__(self, __key: SupportsIndex | slice) -> None: ...
    def __add__(self, __value: array[_T]) -> array[_T]: ...
    def __eq__(self, __value: object) -> bool: ...
    def __ge__(self, __value: array[_T]) -> bool: ...
    def __gt__(self, __value: array[_T]) -> bool: ...
    def __iadd__(self, __value: array[_T]) -> Self: ...  # type: ignore[override]
    def __imul__(self, __value: int) -> Self: ...
    def __le__(self, __value: array[_T]) -> bool: ...
    def __lt__(self, __value: array[_T]) -> bool: ...
    def __mul__(self, __value: int) -> array[_T]: ...
    def __rmul__(self, __value: int) -> array[_T]: ...
    def __copy__(self) -> array[_T]: ...
    def __deepcopy__(self, __unused: Any) -> array[_T]: ...
    def __buffer__(self, __flags: int) -> memoryview: ...
    def __release_buffer__(self, __buffer: memoryview) -> None: ...
    if sys.version_info >= (3, 12):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...

ArrayType = array
