import sys
from collections.abc import Callable
from socket import socket
from typing import Union
from typing_extensions import TypeAlias

from .connection import Connection

__all__ = ["stop"]

# https://docs.python.org/3/library/multiprocessing.html#address-formats
_Address: TypeAlias = Union[str, tuple[str, int]]

if sys.platform == "win32":
    __all__ += ["DupSocket"]

    class DupSocket:
        def __init__(self, sock: socket) -> None: ...
        def detach(self) -> bytes: ...

else:
    __all__ += ["DupFd"]

    class DupFd:
        def __init__(self, fd: int) -> None: ...
        def detach(self) -> None: ...

class _ResourceSharer:
    def __init__(self) -> None: ...
    def register(self, send: Callable[[Connection, int], None], close: Callable[[], None]) -> tuple[_Address, int]: ...
    @staticmethod
    def get_connection(ident: tuple[_Address, int]) -> Connection: ...
    def stop(self, timeout: float | None = ...) -> None: ...

_resource_sharer: _ResourceSharer = ...
stop = _resource_sharer.stop
