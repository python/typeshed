import socket
import sys
import types
from _typeshed import ReadableBuffer, Self
from collections.abc import Iterable
from typing import Any
from typing_extensions import SupportsIndex, TypeAlias

__all__ = ["Client", "Listener", "Pipe", "wait"]

# https://docs.python.org/3/library/multiprocessing.html#address-formats
_Address: TypeAlias = str | tuple[str, int]

class _ConnectionBase:
    def __init__(self, handle: SupportsIndex, readable: bool = True, writable: bool = True) -> None: ...
    @property
    def closed(self) -> bool: ...  # undocumented
    @property
    def readable(self) -> bool: ...  # undocumented
    @property
    def writable(self) -> bool: ...  # undocumented
    def fileno(self) -> int: ...
    def close(self) -> None: ...
    def send_bytes(self, buf: ReadableBuffer, offset: int = 0, size: int | None = None) -> None: ...
    def send(self, obj: Any) -> None: ...
    def recv_bytes(self, maxlength: int | None = None) -> bytes: ...
    def recv_bytes_into(self, buf: Any, offset: int = 0) -> int: ...
    def recv(self) -> Any: ...
    def poll(self, timeout: float | None = 0.0) -> bool: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: types.TracebackType | None
    ) -> None: ...

class Connection(_ConnectionBase): ...

if sys.platform == "win32":
    class PipeConnection(_ConnectionBase): ...

class Listener:
    def __init__(
        self, address: _Address | None = None, family: str | None = None, backlog: int = 1, authkey: bytes | None = None
    ) -> None: ...
    def accept(self) -> Connection: ...
    def close(self) -> None: ...
    @property
    def address(self) -> _Address: ...
    @property
    def last_accepted(self) -> _Address | None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: types.TracebackType | None
    ) -> None: ...

def deliver_challenge(connection: Connection, authkey: bytes) -> None: ...
def answer_challenge(connection: Connection, authkey: bytes) -> None: ...
def wait(
    object_list: Iterable[Connection | socket.socket | int], timeout: float | None = None
) -> list[Connection | socket.socket | int]: ...
def Client(address: _Address, family: str | None = None, authkey: bytes | None = None) -> Connection: ...

# N.B. Keep this in sync with multiprocessing.context.BaseContext.Pipe.
# _ConnectionBase is the common base class of Connection and PipeConnection
# and can be used in cross-platform code.
if sys.platform != "win32":
    def Pipe(duplex: bool = True) -> tuple[Connection, Connection]: ...

else:
    def Pipe(duplex: bool = True) -> tuple[PipeConnection, PipeConnection]: ...
