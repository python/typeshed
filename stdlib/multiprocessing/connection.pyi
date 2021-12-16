import socket
import sys
import types
from _typeshed import Self
from typing import Any, Iterable, Tuple, Type, 

if sys.version_info >= (3, 8):
    from typing import SupportsIndex

# https://docs.python.org/3/library/multiprocessing.html#address-formats
_Address = str | Tuple[str, int]

class _ConnectionBase:
    if sys.version_info >= (3, 8):
        def __init__(self, handle: SupportsIndex, readable: bool = ..., writable: bool = ...) -> None: ...
    else:
        def __init__(self, handle: int, readable: bool = ..., writable: bool = ...) -> None: ...
    @property
    def closed(self) -> bool: ...  # undocumented
    @property
    def readable(self) -> bool: ...  # undocumented
    @property
    def writable(self) -> bool: ...  # undocumented
    def fileno(self) -> int: ...
    def close(self) -> None: ...
    def send_bytes(self, buf: bytes, offset: int = ..., size: int | None = ...) -> None: ...
    def send(self, obj: Any) -> None: ...
    def recv_bytes(self, maxlength: int | None = ...) -> bytes: ...
    def recv_bytes_into(self, buf: Any, offset: int = ...) -> int: ...
    def recv(self) -> Any: ...
    def poll(self, timeout: float | None = ...) -> bool: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, exc_type: Type[BaseException] | None, exc_value: BaseException | None, exc_tb: types.TracebackType | None
    ) -> None: ...

class Connection(_ConnectionBase): ...

if sys.platform == "win32":
    class PipeConnection(_ConnectionBase): ...

class Listener:
    def __init__(
        self, address: _Address | None = ..., family: str | None = ..., backlog: int = ..., authkey: bytes | None = ...
    ) -> None: ...
    def accept(self) -> Connection: ...
    def close(self) -> None: ...
    @property
    def address(self) -> _Address: ...
    @property
    def last_accepted(self) -> _Address | None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, exc_type: Type[BaseException] | None, exc_value: BaseException | None, exc_tb: types.TracebackType | None
    ) -> None: ...

def deliver_challenge(connection: Connection, authkey: bytes) -> None: ...
def answer_challenge(connection: Connection, authkey: bytes) -> None: ...
def wait(
    object_list: Iterable[Connection | socket.socket | int], timeout: float | None = ...
) -> list[Connection | socket.socket | int]: ...
def Client(address: _Address, family: str | None = ..., authkey: bytes | None = ...) -> Connection: ...
def Pipe(duplex: bool = ...) -> tuple[Connection, Connection]: ...
