
from typing import Any, Mapping
from . import base_events, transports, events, streams, futures
import socket

class _ProactorBasePipeTransport(transports._FlowControlMixin, transports.BaseTransport):

    def __init__(self, loop: events.AbstractEventLoop, sock: socket.socket, protocol: streams.StreamReaderProtocol, waiter: futures.Future = ..., extra: Mapping[Any, Any] = ..., server: events.AbstractServer = ...) -> None: ...
    def __repr__(self) -> str: ...
    def __del__(self) -> None: ...
    def get_write_buffer_size(self) -> int: ...

class _ProactorReadPipeTransport(_ProactorBasePipeTransport, transports.ReadTransport):

    def __init__(self, loop: events.AbstractEventLoop, sock: socket.socket, protocol: streams.StreamReaderProtocol, waiter: futures.Future = ..., extra: Mapping[Any, Any] = ..., server: events.AbstractServer = ...) -> None: ...

class _ProactorBaseWritePipeTransport(_ProactorBasePipeTransport, transports.WriteTransport):

    def __init__(self, loop: events.AbstractEventLoop, sock: socket.socket, protocol: streams.StreamReaderProtocol, waiter: futures.Future = ..., extra: Mapping[Any, Any] = ..., server: events.AbstractServer = ...) -> None: ...

class _ProactorWritePipeTransport(_ProactorBaseWritePipeTransport):

    def __init__(self, loop: events.AbstractEventLoop, sock: socket.socket, protocol: streams.StreamReaderProtocol, waiter: futures.Future = ..., extra: Mapping[Any, Any] = ..., server: events.AbstractServer = ...) -> None: ...

class _ProactorDuplexPipeTransport(_ProactorReadPipeTransport, _ProactorBaseWritePipeTransport, transports.Transport):
    pass

class BaseProactorEventLoop(base_events.BaseEventLoop):

    def __init__(self, proactor: Any) -> None: ...
