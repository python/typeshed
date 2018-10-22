import sys
from typing import (Optional, Sequence, Union, Generic, overload,
                    Iterable, Iterator, Sized, ContextManager, AnyStr)

ACCESS_DEFAULT = ...  # type: int
ACCESS_READ = ...  # type: int
ACCESS_WRITE = ...  # type: int
ACCESS_COPY = ...  # type: int

ALLOCATIONGRANULARITY = ...  # type: int

if sys.platform != 'win32':
    MAP_ANON = ...  # type: int
    MAP_ANONYMOUS = ...  # type: int
    MAP_DENYWRITE = ...  # type: int
    MAP_EXECUTABLE = ...  # type: int
    MAP_PRIVATE = ...  # type: int
    MAP_SHARED = ...  # type: int
    PROT_EXEC = ...  # type: int
    PROT_READ = ...  # type: int
    PROT_WRITE = ...  # type: int

    PAGESIZE = ...  # type: int

class _mmap(Generic[AnyStr]):
    if sys.platform == 'win32':
        def __init__(self, fileno: int, length: int,
                     tagname: Optional[str] = ..., access: int = ...,
                     offset: int = ...) -> None: ...
    else:
        def __init__(self,
                     fileno: int, length: int, flags: int = ...,
                     prot: int = ..., access: int = ...,
                     offset: int = ...) -> None: ...
    def close(self) -> None: ...
    def find(self, sub: AnyStr,
             start: int = ..., end: int = ...) -> int: ...
    def flush(self, offset: int = ..., size: int = ...) -> int: ...
    def move(self, dest: int, src: int, count: int) -> None: ...
    def read(self, n: int = ...) -> AnyStr: ...
    def read_byte(self) -> AnyStr: ...
    def readline(self) -> AnyStr: ...
    def resize(self, newsize: int) -> None: ...
    def seek(self, pos: int, whence: int = ...) -> None: ...
    def size(self) -> int: ...
    def tell(self) -> int: ...
    def write(self, bytes: AnyStr) -> None: ...
    def write_byte(self, byte: AnyStr) -> None: ...
    def __len__(self) -> int: ...

if sys.version_info >= (3,):
    class mmap(_mmap, ContextManager[mmap], Iterable[bytes], Sized):
        closed = ...  # type: bool
        def rfind(self, sub: bytes, start: int = ..., stop: int = ...) -> int: ...
        @overload
        def __getitem__(self, index: int) -> int: ...
        @overload
        def __getitem__(self, index: slice) -> bytes: ...
        def __delitem__(self, index: Union[int, slice]) -> None: ...
        @overload
        def __setitem__(self, index: int, object: int) -> None: ...
        @overload
        def __setitem__(self, index: slice, object: bytes) -> None: ...
        # Doesn't actually exist, but the object is actually iterable because it has __getitem__ and
        # __len__, so we claim that there is also an __iter__ to help type checkers.
        def __iter__(self) -> Iterator[bytes]: ...
else:
    class mmap(_mmap, Sequence[bytes]):
        def rfind(self, string: bytes, start: int = ..., stop: int = ...) -> int: ...
        def __getitem__(self, index: Union[int, slice]) -> bytes: ...
        def __getslice__(self, i: Optional[int], j: Optional[int]) -> bytes: ...
        def __delitem__(self, index: Union[int, slice]) -> None: ...
        def __setitem__(self, index: Union[int, slice], object: bytes) -> None: ...
