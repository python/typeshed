import socket
from _typeshed import ReadableBuffer, SliceableBuffer

DEFAULT_TIMEOUT: int
DEFAULT_MAXSIZE: int

class BufferedSocket:
    sock: socket.socket
    rbuf: bytes
    sbuf: list[SliceableBuffer]
    maxsize: int
    timeout: int
    def __init__(self, sock: socket.socket, timeout: int = ..., maxsize: int = ..., recvsize: int = ...) -> None: ...
    def settimeout(self, timeout: float) -> None: ...
    def gettimeout(self) -> float: ...
    def setblocking(self, blocking: bool) -> None: ...
    def setmaxsize(self, maxsize) -> None: ...
    def getrecvbuffer(self) -> bytes: ...
    def getsendbuffer(self) -> bytes: ...
    def recv(self, size: int, flags: int = ..., timeout: float = ...) -> bytes: ...
    def peek(self, size: int, timeout: float = ...) -> bytes: ...
    def recv_close(self, timeout: float = ..., maxsize: int = ...) -> bytes: ...
    def recv_until(
        self, delimiter: ReadableBuffer, timeout: float = ..., maxsize: int = ..., with_delimiter: bool = ...
    ) -> bytes: ...
    def recv_size(self, size: int, timeout: float = ...) -> bytes: ...
    def send(self, data: SliceableBuffer, flags: int = ..., timeout: float = ...) -> str: ...
    def sendall(self, data: SliceableBuffer, flags: int = ..., timeout: float = ...) -> str: ...
    def flush(self) -> None: ...
    def buffer(self, data: SliceableBuffer) -> None: ...
    def getsockname(self) -> str: ...
    def getpeername(self) -> str: ...
    def getsockopt(self, level: int, optname: int, buflen: int | None = ...) -> bytes | int: ...
    def setsockopt(self, level: int, optname: int, value: int | ReadableBuffer | None) -> bytes | int: ...
    @property
    def type(self) -> int: ...
    @property
    def family(self) -> int: ...
    @property
    def proto(self) -> int: ...
    def fileno(self) -> int: ...
    rbuf_unconsumed: bytes
    def close(self) -> None: ...
    def shutdown(self, how: int) -> None: ...

class Error(socket.error): ...
class ConnectionClosed(Error): ...

class MessageTooLong(Error):
    def __init__(self, bytes_read: int | None = ..., delimiter: str | None = ...) -> None: ...

class Timeout(socket.timeout, Error):
    def __init__(self, timeout: float, extra: str = ...) -> None: ...

class NetstringSocket:
    bsock: BufferedSocket
    timeout: float
    maxsize: int
    def __init__(self, sock: socket.socket, timeout: float = ..., maxsize: int = ...) -> None: ...
    def fileno(self) -> int: ...
    def settimeout(self, timeout: float) -> None: ...
    def setmaxsize(self, maxsize: int) -> None: ...
    def read_ns(self, timeout: float = ..., maxsize: int = ...): ...
    def write_ns(self, payload: bytes) -> None: ...

class NetstringProtocolError(Error): ...

class NetstringInvalidSize(NetstringProtocolError):
    def __init__(self, msg: str) -> None: ...

class NetstringMessageTooLong(NetstringProtocolError):
    def __init__(self, size: int, maxsize: int) -> None: ...
