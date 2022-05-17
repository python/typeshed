import selectors
import sys
from _typeshed import WriteableBuffer
from socket import _Address, socket

from . import base_events

if sys.version_info >= (3, 7):
    __all__ = ("BaseSelectorEventLoop",)
else:
    __all__ = ["BaseSelectorEventLoop"]

class BaseSelectorEventLoop(base_events.BaseEventLoop):
    def __init__(self, selector: selectors.BaseSelector | None = ...) -> None: ...
    if sys.version_info >= (3, 11):
        async def sock_recvfrom(self, sock: socket, bufsize: int) -> bytes: ...
        async def sock_recvfrom_into(self, sock: socket, buf: WriteableBuffer, nbytes: int = ...) -> int: ...
        async def sock_sendto(self, sock: socket, data: bytes, address: _Address) -> None: ...
