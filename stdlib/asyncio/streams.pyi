import ssl
import sys
from _typeshed import StrPath
from collections.abc import AsyncIterator, Awaitable, Callable, Iterable, Sequence
from typing import Any
from typing_extensions import Self, SupportsIndex, TypeAlias

from . import events, protocols, transports
from .base_events import Server

if sys.platform == "win32":
    if sys.version_info >= (3, 8):
        __all__ = ("StreamReader", "StreamWriter", "StreamReaderProtocol", "open_connection", "start_server")
    else:
        __all__ = (
            "StreamReader",
            "StreamWriter",
            "StreamReaderProtocol",
            "open_connection",
            "start_server",
            "IncompleteReadError",
            "LimitOverrunError",
        )
else:
    if sys.version_info >= (3, 8):
        __all__ = (
            "StreamReader",
            "StreamWriter",
            "StreamReaderProtocol",
            "open_connection",
            "start_server",
            "open_unix_connection",
            "start_unix_server",
        )
    else:
        __all__ = (
            "StreamReader",
            "StreamWriter",
            "StreamReaderProtocol",
            "open_connection",
            "start_server",
            "IncompleteReadError",
            "LimitOverrunError",
            "open_unix_connection",
            "start_unix_server",
        )

_ClientConnectedCallback: TypeAlias = Callable[[StreamReader, StreamWriter], Awaitable[None] | None]

if sys.version_info < (3, 8):
    class IncompleteReadError(EOFError):
        expected: int | None
        partial: bytes
        def __init__(self, partial: bytes, expected: int | None) -> None: ...

    class LimitOverrunError(Exception):
        consumed: int
        def __init__(self, message: str, consumed: int) -> None: ...

if sys.version_info >= (3, 10):
    async def open_connection(
        host: str | None = None,
        port: int | str | None = None,
        *,
        limit: int = 65536,
        ssl_handshake_timeout: float | None = ...,
        **kwds: Any,
    ) -> tuple[StreamReader, StreamWriter]: ...
    async def start_server(
        client_connected_cb: _ClientConnectedCallback,
        host: str | Sequence[str] | None = None,
        port: int | str | None = None,
        *,
        limit: int = 65536,
        ssl_handshake_timeout: float | None = ...,
        **kwds: Any,
    ) -> Server: ...

else:
    async def open_connection(
        host: str | None = None,
        port: int | str | None = None,
        *,
        loop: events.AbstractEventLoop | None = None,
        limit: int = 65536,
        ssl_handshake_timeout: float | None = ...,
        **kwds: Any,
    ) -> tuple[StreamReader, StreamWriter]: ...
    async def start_server(
        client_connected_cb: _ClientConnectedCallback,
        host: str | None = None,
        port: int | str | None = None,
        *,
        loop: events.AbstractEventLoop | None = None,
        limit: int = 65536,
        ssl_handshake_timeout: float | None = ...,
        **kwds: Any,
    ) -> Server: ...

if sys.platform != "win32":
    if sys.version_info >= (3, 10):
        async def open_unix_connection(
            path: StrPath | None = None, *, limit: int = 65536, **kwds: Any
        ) -> tuple[StreamReader, StreamWriter]: ...
        async def start_unix_server(
            client_connected_cb: _ClientConnectedCallback, path: StrPath | None = None, *, limit: int = 65536, **kwds: Any
        ) -> Server: ...
    else:
        async def open_unix_connection(
            path: StrPath | None = None, *, loop: events.AbstractEventLoop | None = None, limit: int = 65536, **kwds: Any
        ) -> tuple[StreamReader, StreamWriter]: ...
        async def start_unix_server(
            client_connected_cb: _ClientConnectedCallback,
            path: StrPath | None = None,
            *,
            loop: events.AbstractEventLoop | None = None,
            limit: int = 65536,
            **kwds: Any,
        ) -> Server: ...

class FlowControlMixin(protocols.Protocol):
    def __init__(self, loop: events.AbstractEventLoop | None = None) -> None: ...

class StreamReaderProtocol(FlowControlMixin, protocols.Protocol):
    def __init__(
        self,
        stream_reader: StreamReader,
        client_connected_cb: _ClientConnectedCallback | None = None,
        loop: events.AbstractEventLoop | None = None,
    ) -> None: ...
    def __del__(self) -> None: ...

class StreamWriter:
    def __init__(
        self,
        transport: transports.WriteTransport,
        protocol: protocols.BaseProtocol,
        reader: StreamReader | None,
        loop: events.AbstractEventLoop,
    ) -> None: ...
    @property
    def transport(self) -> transports.WriteTransport: ...
    def write(self, data: bytes | bytearray | memoryview) -> None: ...
    def writelines(self, data: Iterable[bytes | bytearray | memoryview]) -> None: ...
    def write_eof(self) -> None: ...
    def can_write_eof(self) -> bool: ...
    def close(self) -> None: ...
    def is_closing(self) -> bool: ...
    async def wait_closed(self) -> None: ...
    def get_extra_info(self, name: str, default: Any = None) -> Any: ...
    async def drain(self) -> None: ...
    if sys.version_info >= (3, 12):
        async def start_tls(
            self,
            sslcontext: ssl.SSLContext,
            *,
            server_hostname: str | None = None,
            ssl_handshake_timeout: float | None = None,
            ssl_shutdown_timeout: float | None = None,
        ) -> None: ...
    elif sys.version_info >= (3, 11):
        async def start_tls(
            self, sslcontext: ssl.SSLContext, *, server_hostname: str | None = None, ssl_handshake_timeout: float | None = None
        ) -> None: ...
    def __del__(self) -> None: ...

class StreamReader(AsyncIterator[bytes]):
    def __init__(self, limit: int = 65536, loop: events.AbstractEventLoop | None = None) -> None: ...
    def exception(self) -> Exception: ...
    def set_exception(self, exc: Exception) -> None: ...
    def set_transport(self, transport: transports.BaseTransport) -> None: ...
    def feed_eof(self) -> None: ...
    def at_eof(self) -> bool: ...
    def feed_data(self, data: Iterable[SupportsIndex]) -> None: ...
    async def readline(self) -> bytes: ...
    # Can be any buffer that supports len(); consider changing to a Protocol if PEP 688 is accepted
    async def readuntil(self, separator: bytes | bytearray | memoryview = b"\n") -> bytes: ...
    async def read(self, n: int = -1) -> bytes: ...
    async def readexactly(self, n: int) -> bytes: ...
    def __aiter__(self) -> Self: ...
    async def __anext__(self) -> bytes: ...
