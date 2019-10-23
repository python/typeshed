from os import PathLike
from typing import Optional, Any, Generator
from . import base_events, events
from socket import socket
from asyncio import coroutine
import selectors
import sys

if sys.version_info >= (3, 7):
    _Path = Union[str, PathLike[str]]
else:
    _Path = str

class BaseSelectorEventLoop(base_events.BaseEventLoop):

    def __init__(self, selector: selectors.BaseSelector = ...) -> None: ...
    if sys.version_info >= (3, 7):
        async def create_unix_connection(
            self,
            protocol_factory: events._ProtocolFactory,
            path: _Path,
            *,
            ssl: events._SSLContext = ...,
            sock: Optional[socket] = ...,
            server_hostname: str = ...,
            ssl_handshake_timeout: Optional[float] = ...,
        ) -> events._TransProtPair: ...
        async def create_unix_server(
            self,
            protocol_factory: events._ProtocolFactory,
            path: _Path,
            *,
            sock: Optional[socket] = ...,
            backlog: int = ...,
            ssl: events._SSLContext = ...,
            ssl_handshake_timeout: Optional[float] = ...,
            start_serving: bool = ...,
        ) -> events.AbstractServer: ...
    else:
        @coroutine
        def create_unix_connection(self, protocol_factory: events._ProtocolFactory, path: str, *,
                                   ssl: events._SSLContext = ..., sock: Optional[socket] = ...,
                                   server_hostname: str = ...) -> Generator[Any, None, events._TransProtPair]: ...
        @coroutine
        def create_unix_server(self, protocol_factory: events._ProtocolFactory, path: str, *,
                               sock: Optional[socket] = ..., backlog: int = ..., ssl: events._SSLContext = ...) -> Generator[Any, None, events.AbstractServer]: ...
