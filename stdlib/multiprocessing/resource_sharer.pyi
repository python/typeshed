import socket
import sys
import threading
from _typeshed import Incomplete
from collections.abc import Callable
from typing import Union
from typing_extensions import TypeAlias

from .connection import Connection, Listener

__all__ = ["stop"]

# https://docs.python.org/3/library/multiprocessing.html#address-formats
_Address: TypeAlias = Union[str, tuple[str, int]]

if sys.platform == "win32":
    __all__ += ["DupSocket"]

    class DupSocket:
        _id: tuple[_Address, int]

        def __init__(self, sock: socket.socket) -> None: ...
        def detach(self) -> bytes: ...

else:
    __all__ += ["DupFd"]

    class DupFd:
        _id: tuple[_Address, int]

        def __init__(self, fd: int) -> None: ...
        def detach(self) -> None: ...

class _ResourceSharer:
    _key: int
    _cache: dict[int, tuple[Incomplete, Incomplete]]
    _lock: threading.Lock
    _listener: Listener | None
    _address: _Address | None
    _thread: threading.Thread | None
    def __init__(self) -> None: ...
    def register(self, send: Callable[[Connection, int], None], close: Callable[[], None]) -> tuple[_Address, int]: ...
    @staticmethod
    def get_connection(ident: tuple[_Address, int]) -> Connection: ...
    def stop(self, timeout: float | None = ...) -> None: ...
    def _afterfork(self) -> None: ...
    def _start(self) -> None: ...
    def _serve(self) -> None: ...

_resource_sharer: _ResourceSharer
stop = _resource_sharer.stop
