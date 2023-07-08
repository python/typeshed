import ssl
import sys
from _typeshed import FileDescriptorLike, ReadableBuffer, WriteableBuffer
from asyncio import _AwaitableLike, _CoroutineLike
from asyncio.events import AbstractEventLoop, AbstractServer, Handle, TimerHandle, _TaskFactory
from asyncio.futures import Future
from asyncio.protocols import BaseProtocol
from asyncio.tasks import Task
from asyncio.transports import BaseTransport, DatagramTransport, ReadTransport, SubprocessTransport, Transport, WriteTransport
from collections.abc import Callable, Iterable, Sequence
from contextvars import Context
from socket import AddressFamily, SocketKind, _Address, _RetAddress, socket
from typing import IO, Any, TypeVar, overload
from typing_extensions import Literal, TypeAlias

if sys.version_info >= (3, 9):
    __all__ = ("BaseEventLoop", "Server")
else:
    __all__ = ("BaseEventLoop",)

_T = TypeVar("_T")
_ProtocolT = TypeVar("_ProtocolT", bound=BaseProtocol)
_Context: TypeAlias = dict[str, Any]
_ExceptionHandler: TypeAlias = Callable[[AbstractEventLoop, _Context], object]
_ProtocolFactory: TypeAlias = Callable[[], BaseProtocol]
_SSLContext: TypeAlias = bool | None | ssl.SSLContext

class Server(AbstractServer):
    if sys.version_info >= (3, 11):
        def __init__(
            self,
            loop: AbstractEventLoop,
            sockets: Iterable[socket],
            protocol_factory: _ProtocolFactory,
            ssl_context: _SSLContext,
            backlog: int,
            ssl_handshake_timeout: float | None,
            ssl_shutdown_timeout: float | None = None,
        ) -> None: ...
    else:
        def __init__(
            self,
            loop: AbstractEventLoop,
            sockets: Iterable[socket],
            protocol_factory: _ProtocolFactory,
            ssl_context: _SSLContext,
            backlog: int,
            ssl_handshake_timeout: float | None,
        ) -> None: ...

    def get_loop(self) -> AbstractEventLoop: ...
    def is_serving(self) -> bool: ...
    async def start_serving(self) -> None: ...
    async def serve_forever(self) -> None: ...
    if sys.version_info >= (3, 8):
        @property
        def sockets(self) -> tuple[socket, ...]: ...
    else:
        @property
        def sockets(self) -> list[socket]: ...

    def close(self) -> None: ...
    async def wait_closed(self) -> None: ...

class BaseEventLoop(AbstractEventLoop):
    def run_forever(self) -> None: ...
    def run_until_complete(self, future: _AwaitableLike[_T]) -> _T: ...
    def stop(self) -> None: ...
    def is_running(self) -> bool: ...
    def is_closed(self) -> bool: ...
    def close(self) -> None: ...
    async def shutdown_asyncgens(self) -> None: ...
    # Methods scheduling callbacks.  All these return Handles.
    def call_soon(self, callback: Callable[..., object], *args: Any, context: Context | None = None) -> Handle: ...
    def call_later(
        self, delay: float, callback: Callable[..., object], *args: Any, context: Context | None = None
    ) -> TimerHandle: ...
    def call_at(
        self, when: float, callback: Callable[..., object], *args: Any, context: Context | None = None
    ) -> TimerHandle: ...
    def time(self) -> float: ...
    # Future methods
    def create_future(self) -> Future[Any]: ...
    # Tasks methods
    if sys.version_info >= (3, 11):
        def create_task(self, coro: _CoroutineLike[_T], *, name: object = None, context: Context | None = None) -> Task[_T]: ...
    elif sys.version_info >= (3, 8):
        def create_task(self, coro: _CoroutineLike[_T], *, name: object = None) -> Task[_T]: ...
    else:
        def create_task(self, coro: _CoroutineLike[_T]) -> Task[_T]: ...

    def set_task_factory(self, factory: _TaskFactory | None) -> None: ...
    def get_task_factory(self) -> _TaskFactory | None: ...
    # Methods for interacting with threads
    def call_soon_threadsafe(self, callback: Callable[..., object], *args: Any, context: Context | None = None) -> Handle: ...
    def run_in_executor(self, executor: Any, func: Callable[..., _T], *args: Any) -> Future[_T]: ...
    def set_default_executor(self, executor: Any) -> None: ...
    # Network I/O methods returning Futures.
    async def getaddrinfo(
        self,
        host: bytes | str | None,
        port: bytes | str | int | None,
        *,
        family: int = 0,
        type: int = 0,
        proto: int = 0,
        flags: int = 0,
    ) -> list[tuple[AddressFamily, SocketKind, int, str, tuple[str, int] | tuple[str, int, int, int]]]: ...
    async def getnameinfo(self, sockaddr: tuple[str, int] | tuple[str, int, int, int], flags: int = 0) -> tuple[str, str]: ...
    if sys.version_info >= (3, 11):
        @overload
        async def create_connection(
            self,
            protocol_factory: Callable[[], _ProtocolT],
            host: str = ...,
            port: int = ...,
            *,
            ssl: _SSLContext = None,
            family: int = 0,
            proto: int = 0,
            flags: int = 0,
            sock: None = None,
            local_addr: tuple[str, int] | None = None,
            server_hostname: str | None = None,
            ssl_handshake_timeout: float | None = None,
            ssl_shutdown_timeout: float | None = None,
            happy_eyeballs_delay: float | None = None,
            interleave: int | None = None,
        ) -> tuple[Transport, _ProtocolT]: ...
        @overload
        async def create_connection(
            self,
            protocol_factory: Callable[[], _ProtocolT],
            host: None = None,
            port: None = None,
            *,
            ssl: _SSLContext = None,
            family: int = 0,
            proto: int = 0,
            flags: int = 0,
            sock: socket,
            local_addr: None = None,
            server_hostname: str | None = None,
            ssl_handshake_timeout: float | None = None,
            ssl_shutdown_timeout: float | None = None,
            happy_eyeballs_delay: float | None = None,
            interleave: int | None = None,
        ) -> tuple[Transport, _ProtocolT]: ...
    elif sys.version_info >= (3, 8):
        @overload
        async def create_connection(
            self,
            protocol_factory: Callable[[], _ProtocolT],
            host: str = ...,
            port: int = ...,
            *,
            ssl: _SSLContext = None,
            family: int = 0,
            proto: int = 0,
            flags: int = 0,
            sock: None = None,
            local_addr: tuple[str, int] | None = None,
            server_hostname: str | None = None,
            ssl_handshake_timeout: float | None = None,
            happy_eyeballs_delay: float | None = None,
            interleave: int | None = None,
        ) -> tuple[Transport, _ProtocolT]: ...
        @overload
        async def create_connection(
            self,
            protocol_factory: Callable[[], _ProtocolT],
            host: None = None,
            port: None = None,
            *,
            ssl: _SSLContext = None,
            family: int = 0,
            proto: int = 0,
            flags: int = 0,
            sock: socket,
            local_addr: None = None,
            server_hostname: str | None = None,
            ssl_handshake_timeout: float | None = None,
            happy_eyeballs_delay: float | None = None,
            interleave: int | None = None,
        ) -> tuple[Transport, _ProtocolT]: ...
    else:
        @overload
        async def create_connection(
            self,
            protocol_factory: Callable[[], _ProtocolT],
            host: str = ...,
            port: int = ...,
            *,
            ssl: _SSLContext = None,
            family: int = 0,
            proto: int = 0,
            flags: int = 0,
            sock: None = None,
            local_addr: tuple[str, int] | None = None,
            server_hostname: str | None = None,
            ssl_handshake_timeout: float | None = None,
        ) -> tuple[Transport, _ProtocolT]: ...
        @overload
        async def create_connection(
            self,
            protocol_factory: Callable[[], _ProtocolT],
            host: None = None,
            port: None = None,
            *,
            ssl: _SSLContext = None,
            family: int = 0,
            proto: int = 0,
            flags: int = 0,
            sock: socket,
            local_addr: None = None,
            server_hostname: str | None = None,
            ssl_handshake_timeout: float | None = None,
        ) -> tuple[Transport, _ProtocolT]: ...
    if sys.version_info >= (3, 11):
        @overload
        async def create_server(
            self,
            protocol_factory: _ProtocolFactory,
            host: str | Sequence[str] | None = None,
            port: int = ...,
            *,
            family: int = ...,
            flags: int = ...,
            sock: None = None,
            backlog: int = 100,
            ssl: _SSLContext = None,
            reuse_address: bool | None = None,
            reuse_port: bool | None = None,
            ssl_handshake_timeout: float | None = None,
            ssl_shutdown_timeout: float | None = None,
            start_serving: bool = True,
        ) -> Server: ...
        @overload
        async def create_server(
            self,
            protocol_factory: _ProtocolFactory,
            host: None = None,
            port: None = None,
            *,
            family: int = ...,
            flags: int = ...,
            sock: socket = ...,
            backlog: int = 100,
            ssl: _SSLContext = None,
            reuse_address: bool | None = None,
            reuse_port: bool | None = None,
            ssl_handshake_timeout: float | None = None,
            ssl_shutdown_timeout: float | None = None,
            start_serving: bool = True,
        ) -> Server: ...
        async def start_tls(
            self,
            transport: BaseTransport,
            protocol: BaseProtocol,
            sslcontext: ssl.SSLContext,
            *,
            server_side: bool = False,
            server_hostname: str | None = None,
            ssl_handshake_timeout: float | None = None,
            ssl_shutdown_timeout: float | None = None,
        ) -> Transport | None: ...
        async def connect_accepted_socket(
            self,
            protocol_factory: Callable[[], _ProtocolT],
            sock: socket,
            *,
            ssl: _SSLContext = None,
            ssl_handshake_timeout: float | None = None,
            ssl_shutdown_timeout: float | None = None,
        ) -> tuple[Transport, _ProtocolT]: ...
    else:
        @overload
        async def create_server(
            self,
            protocol_factory: _ProtocolFactory,
            host: str | Sequence[str] | None = None,
            port: int = ...,
            *,
            family: int = ...,
            flags: int = ...,
            sock: None = None,
            backlog: int = 100,
            ssl: _SSLContext = None,
            reuse_address: bool | None = None,
            reuse_port: bool | None = None,
            ssl_handshake_timeout: float | None = None,
            start_serving: bool = True,
        ) -> Server: ...
        @overload
        async def create_server(
            self,
            protocol_factory: _ProtocolFactory,
            host: None = None,
            port: None = None,
            *,
            family: int = ...,
            flags: int = ...,
            sock: socket = ...,
            backlog: int = 100,
            ssl: _SSLContext = None,
            reuse_address: bool | None = None,
            reuse_port: bool | None = None,
            ssl_handshake_timeout: float | None = None,
            start_serving: bool = True,
        ) -> Server: ...
        async def start_tls(
            self,
            transport: BaseTransport,
            protocol: BaseProtocol,
            sslcontext: ssl.SSLContext,
            *,
            server_side: bool = False,
            server_hostname: str | None = None,
            ssl_handshake_timeout: float | None = None,
        ) -> Transport | None: ...
        async def connect_accepted_socket(
            self,
            protocol_factory: Callable[[], _ProtocolT],
            sock: socket,
            *,
            ssl: _SSLContext = None,
            ssl_handshake_timeout: float | None = None,
        ) -> tuple[Transport, _ProtocolT]: ...

    async def sock_sendfile(
        self, sock: socket, file: IO[bytes], offset: int = 0, count: int | None = None, *, fallback: bool | None = True
    ) -> int: ...
    async def sendfile(
        self, transport: WriteTransport, file: IO[bytes], offset: int = 0, count: int | None = None, *, fallback: bool = True
    ) -> int: ...
    if sys.version_info >= (3, 11):
        async def create_datagram_endpoint(  # type: ignore[override]
            self,
            protocol_factory: Callable[[], _ProtocolT],
            local_addr: tuple[str, int] | str | None = None,
            remote_addr: tuple[str, int] | str | None = None,
            *,
            family: int = 0,
            proto: int = 0,
            flags: int = 0,
            reuse_port: bool | None = None,
            allow_broadcast: bool | None = None,
            sock: socket | None = None,
        ) -> tuple[DatagramTransport, _ProtocolT]: ...
    else:
        async def create_datagram_endpoint(
            self,
            protocol_factory: Callable[[], _ProtocolT],
            local_addr: tuple[str, int] | str | None = None,
            remote_addr: tuple[str, int] | str | None = None,
            *,
            family: int = 0,
            proto: int = 0,
            flags: int = 0,
            reuse_address: bool | None = ...,
            reuse_port: bool | None = None,
            allow_broadcast: bool | None = None,
            sock: socket | None = None,
        ) -> tuple[DatagramTransport, _ProtocolT]: ...
    # Pipes and subprocesses.
    async def connect_read_pipe(
        self, protocol_factory: Callable[[], _ProtocolT], pipe: Any
    ) -> tuple[ReadTransport, _ProtocolT]: ...
    async def connect_write_pipe(
        self, protocol_factory: Callable[[], _ProtocolT], pipe: Any
    ) -> tuple[WriteTransport, _ProtocolT]: ...
    async def subprocess_shell(
        self,
        protocol_factory: Callable[[], _ProtocolT],
        cmd: bytes | str,
        *,
        stdin: int | IO[Any] | None = -1,
        stdout: int | IO[Any] | None = -1,
        stderr: int | IO[Any] | None = -1,
        universal_newlines: Literal[False] = False,
        shell: Literal[True] = True,
        bufsize: Literal[0] = 0,
        encoding: None = None,
        errors: None = None,
        text: Literal[False, None] = None,
        **kwargs: Any,
    ) -> tuple[SubprocessTransport, _ProtocolT]: ...
    async def subprocess_exec(
        self,
        protocol_factory: Callable[[], _ProtocolT],
        program: Any,
        *args: Any,
        stdin: int | IO[Any] | None = -1,
        stdout: int | IO[Any] | None = -1,
        stderr: int | IO[Any] | None = -1,
        universal_newlines: Literal[False] = False,
        shell: Literal[False] = False,
        bufsize: Literal[0] = 0,
        encoding: None = None,
        errors: None = None,
        **kwargs: Any,
    ) -> tuple[SubprocessTransport, _ProtocolT]: ...
    def add_reader(self, fd: FileDescriptorLike, callback: Callable[..., Any], *args: Any) -> None: ...
    def remove_reader(self, fd: FileDescriptorLike) -> bool: ...
    def add_writer(self, fd: FileDescriptorLike, callback: Callable[..., Any], *args: Any) -> None: ...
    def remove_writer(self, fd: FileDescriptorLike) -> bool: ...
    # The sock_* methods (and probably some others) are not actually implemented on
    # BaseEventLoop, only on subclasses. We list them here for now for convenience.
    async def sock_recv(self, sock: socket, nbytes: int) -> bytes: ...
    async def sock_recv_into(self, sock: socket, buf: WriteableBuffer) -> int: ...
    async def sock_sendall(self, sock: socket, data: ReadableBuffer) -> None: ...
    async def sock_connect(self, sock: socket, address: _Address) -> None: ...
    async def sock_accept(self, sock: socket) -> tuple[socket, _RetAddress]: ...
    if sys.version_info >= (3, 11):
        async def sock_recvfrom(self, sock: socket, bufsize: int) -> tuple[bytes, _RetAddress]: ...
        async def sock_recvfrom_into(self, sock: socket, buf: WriteableBuffer, nbytes: int = 0) -> tuple[int, _RetAddress]: ...
        async def sock_sendto(self, sock: socket, data: ReadableBuffer, address: _Address) -> int: ...
    # Signal handling.
    def add_signal_handler(self, sig: int, callback: Callable[..., Any], *args: Any) -> None: ...
    def remove_signal_handler(self, sig: int) -> bool: ...
    # Error handlers.
    def set_exception_handler(self, handler: _ExceptionHandler | None) -> None: ...
    def get_exception_handler(self) -> _ExceptionHandler | None: ...
    def default_exception_handler(self, context: _Context) -> None: ...
    def call_exception_handler(self, context: _Context) -> None: ...
    # Debug flag management.
    def get_debug(self) -> bool: ...
    def set_debug(self, enabled: bool) -> None: ...
    if sys.version_info >= (3, 9):
        async def shutdown_default_executor(self) -> None: ...
