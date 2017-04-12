"""Stub file for the 'array' module."""

from typing import (Any, Generic, IO, Iterable, Sequence, TypeVar,
                    Union, overload, Iterator, Tuple, BinaryIO, List)

_T = TypeVar('_T')

class array(Generic[_T]):
    def __init__(self, typecode: str, init: Iterable[_T] = ...) -> None: ...
    def __add__(self, y: "array[_T]") -> "array[_T]": ...
    def __contains__(self, y: Any) -> bool: ...
    def __copy__(self) -> "array[_T]": ...
    def __deepcopy__(self) -> "array": ...
    def __delitem__(self, y: Union[slice, int]) -> None: ...
    def __delslice__(self, i: int, j: int) -> None: ...
    @overload
    def __getitem__(self, i: int) -> Any: ...
    @overload
    def __getitem__(self, s: slice) -> "array": ...
    def __iadd__(self, y: "array[_T]") -> "array[_T]": ...
    def __imul__(self, y: int) -> "array[_T]": ...
    def __iter__(self) -> Iterator[_T]: ...
    def __len__(self) -> int: ...
    def __mul__(self, n: int) -> "array[_T]": ...
    def __rmul__(self, n: int) -> "array[_T]": ...
    @overload
    def __setitem__(self, i: int, y: _T) -> None: ...
    @overload
    def __setitem__(self, i: slice, y: "array[_T]") -> None: ...

    def append(self, x: _T) -> None: ...
    def buffer_info(self) -> Tuple[int, int]: ...
    def byteswap(self) -> None:
        raise RuntimeError()
    def count(self) -> int: ...
    def extend(self, x: Sequence[_T]) -> None: ...
    def fromlist(self, list: List[_T]) -> None:
        raise EOFError()
        raise IOError()
    def fromfile(self, f: BinaryIO, n: int) -> None: ...
    def fromstring(self, s: str) -> None: ...
    def fromunicode(self, u: unicode) -> None: ...
    def index(self, x: _T) -> int: ...
    def insert(self, i: int, x: _T) -> None: ...
    def pop(self, i: int = ...) -> _T: ...
    def read(self, f: IO[str], n: int) -> None:
        raise DeprecationWarning()
    def remove(self, x: _T) -> None: ...
    def reverse(self) -> None: ...
    def tofile(self, f: BinaryIO) -> None:
        raise IOError()
    def tolist(self) -> List[_T]: ...
    def tostring(self) -> str: ...
    def tounicode(self) -> unicode: ...
    def write(self, f: IO[str]) -> None:
        raise DeprecationWarning()
