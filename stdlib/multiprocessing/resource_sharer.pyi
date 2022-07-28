import sys
from socket import socket
from typing import Union
from typing_extensions import TypeAlias

__all__ = ["stop"]

# https://docs.python.org/3/library/multiprocessing.html#address-formats
_Address: TypeAlias = Union[str, tuple[str, int]]

if sys.platform == "win32":
    __all__ += ["DupSocket"]

    class DupSocket:
        def __init__(self, sock: socket) -> None: ...
        def detach(self) -> socket: ...

else:
    __all__ += ["DupFd"]

    class DupFd:
        def __init__(self, fd: int) -> None: ...
        def detach(self) -> int: ...

def stop(timeout: float | None = ...) -> None: ...
