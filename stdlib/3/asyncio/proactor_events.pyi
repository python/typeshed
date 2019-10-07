
from typing import Any, Mapping, Optional, Generator
from . import base_events, transports, events, streams, futures
from asyncio import coroutine
from socket import socket
import sys

class _ProactorBasePipeTransport(transports._FlowControlMixin, transports.BaseTransport):

    def __init__(self, loop: events.AbstractEventLoop, sock: socket, protocol: streams.StreamReaderProtocol, waiter: futures.Future[Any] = ..., extra: Mapping[Any, Any] = ..., server: events.AbstractServer = ...) -> None: ...
    def __repr__(self) -> str: ...
    def __del__(self) -> None: ...
    def get_write_buffer_size(self) -> int: ...

class _ProactorReadPipeTransport(_ProactorBasePipeTransport, transports.ReadTransport):

    def __init__(self, loop: events.AbstractEventLoop, sock: socket, protocol: streams.StreamReaderProtocol, waiter: futures.Future[Any] = ..., extra: Mapping[Any, Any] = ..., server: events.AbstractServer = ...) -> None: ...

class _ProactorBaseWritePipeTransport(_ProactorBasePipeTransport, transports.WriteTransport):

    def __init__(self, loop: events.AbstractEventLoop, sock: socket, protocol: streams.StreamReaderProtocol, waiter: futures.Future[Any] = ..., extra: Mapping[Any, Any] = ..., server: events.AbstractServer = ...) -> None: ...

class _ProactorWritePipeTransport(_ProactorBaseWritePipeTransport):

    def __init__(self, loop: events.AbstractEventLoop, sock: socket, protocol: streams.StreamReaderProtocol, waiter: futures.Future[Any] = ..., extra: Mapping[Any, Any] = ..., server: events.AbstractServer = ...) -> None: ...

class _ProactorDuplexPipeTransport(_ProactorReadPipeTransport, _ProactorBaseWritePipeTransport, transports.Transport):
    pass

class BaseProactorEventLoop(base_events.BaseEventLoop):

    def __init__(self, proactor: Any) -> None: ...
    # The methods below don't actually exist directly, ProactorEventLoops do not implement them. However, they are
    # needed to satisfy mypy
    if sys.version_info >= (3, 7):
        async def create_unix_connection(self, protocol_factory: events._ProtocolFactory, path: str, *, ssl: events._SSLContext = ...,
                                         sock: Optional[socket] = ..., server_hostname: str = ...,
                                         ssl_handshake_timeout: Optional[float] = ...) -> events._TransProtPair: ...
        async def create_unix_server(self, protocol_factory: events._ProtocolFactory, path: str, *, sock: Optional[socket] = ...,
                                     backlog: int = ..., ssl: events._SSLContext = ..., ssl_handshake_timeout: Optional[float] = ...,
                                     start_serving: bool = ...) -> events.AbstractServer: ...
    else:
        @coroutine
        def create_unix_connection(self, protocol_factory: events._ProtocolFactory, path: str, *,
                                   ssl: events._SSLContext = ..., sock: Optional[socket] = ...,
                                   server_hostname: str = ...) -> Generator[Any, None, events._TransProtPair]: ...
        @coroutine
        def create_unix_server(self, protocol_factory: events._ProtocolFactory, path: str, *,
                               sock: Optional[socket] = ..., backlog: int = ..., ssl: events._SSLContext = ...) -> Generator[Any, None, events.AbstractServer]: ...
