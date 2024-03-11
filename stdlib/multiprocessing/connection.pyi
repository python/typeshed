import socket
import sys
from _typeshed import Incomplete, ReadableBuffer
from collections.abc import Iterable
from types import TracebackType
from typing import Any, Generic, SupportsIndex, TypeVar
from typing_extensions import Self, TypeAlias

__all__ = ["Client", "Listener", "Pipe", "wait"]

# https://docs.python.org/3/library/multiprocessing.html#address-formats
_Address: TypeAlias = str | tuple[str, int]

_SendT = TypeVar("_SendT", contravariant=True)
_RecvT = TypeVar("_RecvT", covariant=True)

class _ConnectionBase(Generic[_SendT, _RecvT]):
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
    def send(self, obj: _SendT) -> None: ...
    def recv_bytes(self, maxlength: int | None = None) -> bytes: ...
    def recv_bytes_into(self, buf: Any, offset: int = 0) -> int: ...
    def recv(self) -> _RecvT: ...
    def poll(self, timeout: float | None = 0.0) -> bool: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def __del__(self) -> None: ...

class Connection(_ConnectionBase[_SendT, _RecvT]): ...

if sys.platform == "win32":
    class PipeConnection(_ConnectionBase[_SendT, _RecvT]): ...

class Listener:
    def __init__(
        self, address: _Address | None = None, family: str | None = None, backlog: int = 1, authkey: bytes | None = None
    ) -> None: ...
    def accept(self) -> Connection[Incomplete, Incomplete]: ...
    def close(self) -> None: ...
    @property
    def address(self) -> _Address: ...
    @property
    def last_accepted(self) -> _Address | None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...

# Any: send and recv methods unused
if sys.version_info >= (3, 12):
    def deliver_challenge(connection: Connection[Any, Any], authkey: bytes, digest_name: str = "sha256") -> None: ...

else:
    def deliver_challenge(connection: Connection[Any, Any], authkey: bytes) -> None: ...

def answer_challenge(connection: Connection[Any, Any], authkey: bytes) -> None: ...
def wait(
    object_list: Iterable[Connection[_SendT, _RecvT] | socket.socket | int], timeout: float | None = None
) -> list[Connection[_SendT, _RecvT] | socket.socket | int]: ...
def Client(address: _Address, family: str | None = None, authkey: bytes | None = None) -> Connection[Any, Any]: ...

# N.B. Keep this in sync with multiprocessing.context.BaseContext.Pipe.
# _ConnectionBase is the common base class of Connection and PipeConnection
# and can be used in cross-platform code.
#
# The two connections should have the same generic types but inverted (Connection[_T1, _T2], Connection[_T2, _T1]).
# However, TypeVars scoped entirely within a return annotation is unspecified in the spec.
if sys.platform != "win32":
    def Pipe(duplex: bool = True) -> tuple[Connection[Any, Any], Connection[Any, Any]]: ...

else:
    def Pipe(duplex: bool = True) -> tuple[PipeConnection[Any, Any], PipeConnection[Any, Any]]: ...
