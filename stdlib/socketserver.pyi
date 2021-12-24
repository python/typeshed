import sys
import types
from _typeshed import Self
from collections.abc import Callable
from socket import socket as _socket
from typing import Any, BinaryIO, ClassVar, Type, TypeVar, Union

_T = TypeVar("_T")
_RequestType = Union[_socket, tuple[bytes, _socket]]
_AddressType = Union[tuple[str, int], str]

class BaseServer:
    address_family: int
    RequestHandlerClass: Callable[..., BaseRequestHandler]
    server_address: tuple[str, int]
    socket: _socket
    allow_reuse_address: bool
    request_queue_size: int
    socket_type: int
    timeout: float | None
    def __init__(self, server_address: Any, RequestHandlerClass: Callable[..., BaseRequestHandler]) -> None: ...
    def fileno(self) -> int: ...
    def handle_request(self) -> None: ...
    def serve_forever(self, poll_interval: float = ...) -> None: ...
    def shutdown(self) -> None: ...
    def server_close(self) -> None: ...
    def finish_request(self, request: _RequestType, client_address: _AddressType) -> None: ...
    def get_request(self) -> tuple[Any, Any]: ...
    def handle_error(self, request: _RequestType, client_address: _AddressType) -> None: ...
    def handle_timeout(self) -> None: ...
    def process_request(self, request: _RequestType, client_address: _AddressType) -> None: ...
    def server_activate(self) -> None: ...
    def server_bind(self) -> None: ...
    def verify_request(self, request: _RequestType, client_address: _AddressType) -> bool: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None
    ) -> None: ...
    def service_actions(self) -> None: ...
    def shutdown_request(self, request: _RequestType) -> None: ...  # undocumented
    def close_request(self, request: _RequestType) -> None: ...  # undocumented

class TCPServer(BaseServer):
    def __init__(
        self,
        server_address: tuple[str, int],
        RequestHandlerClass: Callable[..., BaseRequestHandler],
        bind_and_activate: bool = ...,
    ) -> None: ...
    def get_request(self) -> tuple[_socket, Any]: ...
    def finish_request(self, request: _RequestType, client_address: _AddressType) -> None: ...
    def handle_error(self, request: _RequestType, client_address: _AddressType) -> None: ...
    def process_request(self, request: _RequestType, client_address: _AddressType) -> None: ...
    def verify_request(self, request: _RequestType, client_address: _AddressType) -> bool: ...
    def shutdown_request(self, request: _RequestType) -> None: ...  # undocumented
    def close_request(self, request: _RequestType) -> None: ...  # undocumented

class UDPServer(BaseServer):
    max_packet_size: ClassVar[int]
    def __init__(
        self,
        server_address: tuple[str, int],
        RequestHandlerClass: Callable[..., BaseRequestHandler],
        bind_and_activate: bool = ...,
    ) -> None: ...
    def get_request(self) -> tuple[tuple[bytes, _socket], Any]: ...
    def finish_request(self, request: _RequestType, client_address: _AddressType) -> None: ...
    def handle_error(self, request: _RequestType, client_address: _AddressType) -> None: ...
    def process_request(self, request: _RequestType, client_address: _AddressType) -> None: ...
    def verify_request(self, request: _RequestType, client_address: _AddressType) -> bool: ...
    def shutdown_request(self, request: _RequestType) -> None: ...  # undocumented
    def close_request(self, request: _RequestType) -> None: ...  # undocumented

if sys.platform != "win32":
    class UnixStreamServer(BaseServer):
        def __init__(
            self,
            server_address: str | bytes,
            RequestHandlerClass: Callable[..., BaseRequestHandler],
            bind_and_activate: bool = ...,
        ) -> None: ...
    class UnixDatagramServer(BaseServer):
        def __init__(
            self,
            server_address: str | bytes,
            RequestHandlerClass: Callable[..., BaseRequestHandler],
            bind_and_activate: bool = ...,
        ) -> None: ...

if sys.platform != "win32":
    class ForkingMixIn:
        timeout: float | None  # undocumented
        active_children: set[int] | None  # undocumented
        max_children: int  # undocumented
        if sys.version_info >= (3, 7):
            block_on_close: bool
        def collect_children(self, *, blocking: bool = ...) -> None: ...  # undocumented
        def handle_timeout(self) -> None: ...  # undocumented
        def service_actions(self) -> None: ...  # undocumented
        def process_request(self, request: _RequestType, client_address: _AddressType) -> None: ...
        def server_close(self) -> None: ...

class ThreadingMixIn:
    daemon_threads: bool
    if sys.version_info >= (3, 7):
        block_on_close: bool
    def process_request_thread(self, request: _RequestType, client_address: _AddressType) -> None: ...  # undocumented
    def process_request(self, request: _RequestType, client_address: _AddressType) -> None: ...
    def server_close(self) -> None: ...

if sys.platform != "win32":
    class ForkingTCPServer(ForkingMixIn, TCPServer): ...
    class ForkingUDPServer(ForkingMixIn, UDPServer): ...

class ThreadingTCPServer(ThreadingMixIn, TCPServer): ...
class ThreadingUDPServer(ThreadingMixIn, UDPServer): ...

if sys.platform != "win32":
    class ThreadingUnixStreamServer(ThreadingMixIn, UnixStreamServer): ...
    class ThreadingUnixDatagramServer(ThreadingMixIn, UnixDatagramServer): ...

class BaseRequestHandler:
    # Those are technically of types, respectively:
    # * _RequestType
    # * _AddressType
    # But there are some concerns that having unions here would cause
    # too much inconvenience to people using it (see
    # https://github.com/python/typeshed/pull/384#issuecomment-234649696)
    request: Any
    client_address: Any
    server: BaseServer
    def __init__(self, request: _RequestType, client_address: _AddressType, server: BaseServer) -> None: ...
    def setup(self) -> None: ...
    def handle(self) -> None: ...
    def finish(self) -> None: ...

class StreamRequestHandler(BaseRequestHandler):
    rbufsize: ClassVar[int]  # undocumented
    wbufsize: ClassVar[int]  # undocumented
    timeout: ClassVar[float | None]  # undocumented
    disable_nagle_algorithm: ClassVar[bool]  # undocumented
    connection: _socket  # undocumented
    rfile: BinaryIO
    wfile: BinaryIO

class DatagramRequestHandler(BaseRequestHandler):
    packet: _socket  # undocumented
    socket: _socket  # undocumented
    rfile: BinaryIO
    wfile: BinaryIO
