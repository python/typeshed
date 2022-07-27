from _typeshed import Incomplete
from collections.abc import Callable
from mmap import mmap
from typing_extensions import TypeAlias
import sys

_Block: TypeAlias = tuple[Arena, int, int]

__all__ = ["BufferWrapper"]

if sys.platform == "win32":
    class Arena:
        buffer: mmap
        name: str
        size: int

        def __init__(self, size: int) -> None: ...
        def __getstate__(self) -> tuple[int, str]: ...
        def __setstate__(self, state: tuple[int, str]) -> None: ...

else:
    class Arena:
        size: int
        fd: int
        buffer: mmap
        def __init__(self, size: int, fd: int = ...) -> None: ...

    def reduce_arena(a: Arena) -> tuple[Callable[[int, Incomplete], Arena], tuple[int, Incomplete]]: ...
    def rebuild_arena(size: int, dupfd: Incomplete) -> Arena: ...

class Heap:
    def __init__(self, size: int = ...) -> None: ...
    def free(self, block: _Block) -> None: ...
    def malloc(self, size: int) -> _Block: ...

class BufferWrapper:
    def __init__(self, size: int) -> None: ...
    def create_memoryview(self) -> memoryview: ...
