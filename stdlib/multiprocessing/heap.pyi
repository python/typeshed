from _typeshed import Incomplete
from collections.abc import Callable
from mmap import mmap
from collections import defaultdict
import sys
import tempfile
import threading
from typing import TypeAlias

_Block: TypeAlias = tuple[Arena, int, int]

__all__ = ["BufferWrapper"]

if sys.platform == "win32":
    class Arena:
        _rand: tempfile._RandomNameSequence
        _state: tuple[int, str]
        buffer: mmap
        name: str
        size: int

        def __init__(self, size: int) -> None: ...
        def __getstate__(self) -> tuple[int, str]: ...
        def __setstate__(self, state: tuple[int, str]) -> None: ...

else:
    class Arena:
        _dir_candidates: list[str]
        size: int
        fd: int
        buffer: mmap
        def __init__(self, size: int, fd: int = ...) -> None: ...
        def _choose_dir(self, size: int) -> str: ...

    def reduce_arena(a: Arena) -> tuple[Callable[[int, Incomplete], Arena], tuple[int, Incomplete]]: ...
    def rebuild_arena(size: int, dupfd: Incomplete) -> Arena: ...

class Heap:
    _alignment: int
    _DISCARD_FREE_SPACE_LARGER_THAN: int
    _DOUBLE_ARENA_SIZE_UNTIL: int
    _lastpid: int
    _lock: threading.Lock
    _size: int
    _lengths: list[int]
    _len_to_seq: dict[int, tuple[Arena, int, int]]
    _start_to_block: dict[tuple[Arena, int], _Block]
    _stop_to_block: dict[tuple[Arena, int], _Block]
    _allocated_blocks: defaultdict[tuple[Arena, int], _Block]
    _arenas: list[Arena]
    _n_mallocs: int
    _n_frees: int

    def __init__(self, size: int = ...) -> None: ...
    @staticmethod
    def _roundup(n: int, alignment: int) -> int: ...
    def _new_arena(self, size: int) -> _Block: ...
    def _discard_arena(self, arena: Arena) -> None: ...
    def _malloc(self, size: int) -> _Block: ...
    def _add_free_block(self, block: _Block) -> None: ...
    def _absorb(self, block: _Block) -> tuple[int, int]: ...
    def _remove_allocated_block(self, block: _Block) -> None: ...
    def _free_pending_blocks(self) -> None: ...
    def free(self, block: _Block) -> None: ...
    def malloc(self, size: int) -> _Block: ...

class BufferWrapper:
    _heap = Heap
    _state: tuple[_Block, int]

    def __init__(self, size: int) -> None: ...
    def create_memoryview(self) -> memoryview: ...
