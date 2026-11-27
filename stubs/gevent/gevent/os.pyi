import os
import sys
from _typeshed import FileDescriptor, ReadableBuffer
from collections.abc import Callable
from typing import Literal

from gevent._types import _ChildWatcher, _Loop

__all__ = ["tp_read", "tp_write"]

if sys.platform != "win32":
    __all__ += [
        "close",
        "fork",
        "fork_and_watch",
        "fork_gevent",
        "forkpty",
        "forkpty_and_watch",
        "forkpty_gevent",
        "make_nonblocking",
        "nb_read",
        "nb_write",
        "posix_spawn",
        "posix_spawnp",
        "waitpid",
    ]

def tp_read(fd: FileDescriptor, n: int) -> bytes: ...
def tp_write(fd: FileDescriptor, buf: ReadableBuffer) -> int: ...

if sys.platform != "win32":
    def close(fd: FileDescriptor) -> None: ...
    def make_nonblocking(fd: FileDescriptor) -> Literal[True] | None: ...
    def nb_read(fd: FileDescriptor, n: int) -> bytes: ...
    def nb_write(fd: FileDescriptor, buf: ReadableBuffer) -> int: ...
    fork = os.fork
    forkpty = os.forkpty
    def fork_gevent() -> int: ...
    def forkpty_gevent() -> tuple[int, int]: ...
    waitpid = os.waitpid
    def fork_and_watch(
        callback: Callable[[_ChildWatcher], object] | None = None,
        loop: _Loop | None = None,
        ref: bool = False,
        fork: Callable[[], int] = ...,
    ) -> int: ...
    def forkpty_and_watch(
        callback: Callable[[_ChildWatcher], object] | None = None,
        loop: _Loop | None = None,
        ref: bool = False,
        forkpty: Callable[[], tuple[int, int]] = ...,
    ) -> tuple[int, int]: ...

    posix_spawn = os.posix_spawn
    posix_spawnp = os.posix_spawnp
