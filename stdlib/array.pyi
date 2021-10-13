import sys
from typing import Any, BinaryIO, Generic, Iterable, MutableSequence, Tuple, TypeVar, Union, overload
from typing_extensions import Literal

_IntTypeCode = Literal["b", "B", "h", "H", "i", "I", "l", "L", "q", "Q"]
_FloatTypeCode = Literal["f", "d"]
_UnicodeTypeCode = Literal["u"]
_TypeCode = Union[_IntTypeCode, _FloatTypeCode, _UnicodeTypeCode]

_T = TypeVar("_T", int, float, str)

typecodes: str

class array(MutableSequence[_T], Generic[_T]):
    typecode: _TypeCode
    itemsize: int
    @overload
    def __init__(self: array[int], typecode: _IntTypeCode, __initializer: bytes | Iterable[_T] = ...) -> None: ...
    @overload
    def __init__(self: array[float], typecode: _FloatTypeCode, __initializer: bytes | Iterable[_T] = ...) -> None: ...
    @overload
    def __init__(self: array[str], typecode: _UnicodeTypeCode, __initializer: bytes | Iterable[_T] = ...) -> None: ...
    @overload
    def __init__(self, typecode: str, __initializer: bytes | Iterable[_T] = ...) -> None: ...
    def append(self, __v: _T) -> None: ...
    def buffer_info(self) -> tuple[int, int]: ...
    def byteswap(self) -> None: ...
    def count(self, __v: Any) -> int: ...
    def extend(self, __bb: Iterable[_T]) -> None: ...
    def frombytes(self, __buffer: bytes) -> None: ...
    def fromfile(self, __f: BinaryIO, __n: int) -> None: ...
    def fromlist(self, __list: list[_T]) -> None: ...
    def fromunicode(self, __ustr: str) -> None: ...
    if sys.version_info >= (3, 10):
        def index(self, __v: _T, __start: int = ..., __stop: int = ...) -> int: ...
    else:
        def index(self, __v: _T) -> int: ...  # type: ignore  # Overrides Sequence
    def insert(self, __i: int, __v: _T) -> None: ...
    def pop(self, __i: int = ...) -> _T: ...
    def remove(self, __v: Any) -> None: ...
    def reverse(self) -> None: ...
    def tobytes(self) -> bytes: ...
    def tofile(self, __f: BinaryIO) -> None: ...
    def tolist(self) -> list[_T]: ...
    def tounicode(self) -> str: ...
    if sys.version_info < (3, 9):
        def fromstring(self, __buffer: bytes) -> None: ...
        def tostring(self) -> bytes: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, i: int) -> _T: ...
    @overload
    def __getitem__(self, s: slice) -> array[_T]: ...
    @overload  # type: ignore  # Overrides MutableSequence
    def __setitem__(self, i: int, o: _T) -> None: ...
    @overload
    def __setitem__(self, s: slice, o: array[_T]) -> None: ...
    def __delitem__(self, i: int | slice) -> None: ...
    def __add__(self, x: array[_T]) -> array[_T]: ...
    def __ge__(self, other: array[_T]) -> bool: ...
    def __gt__(self, other: array[_T]) -> bool: ...
    def __iadd__(self, x: array[_T]) -> array[_T]: ...  # type: ignore  # Overrides MutableSequence
    def __imul__(self, n: int) -> array[_T]: ...
    def __le__(self, other: array[_T]) -> bool: ...
    def __lt__(self, other: array[_T]) -> bool: ...
    def __mul__(self, n: int) -> array[_T]: ...
    def __rmul__(self, n: int) -> array[_T]: ...

ArrayType = array
