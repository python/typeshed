import selectors
from socket import socket, _Address
import ssl
import sys
from typing import Any, Awaitable, Callable, Dict, Generator, List, Optional, Sequence, Tuple, TypeVar, Union, overload
from asyncio.futures import Future
from asyncio.coroutines import coroutine
from asyncio.events import AbstractEventLoop, AbstractServer, Handle, TimerHandle
from asyncio.protocols import BaseProtocol
from asyncio.tasks import Task
from asyncio.transports import BaseTransport

_T = TypeVar('_T')
_Context = Dict[str, Any]
_ExceptionHandler = Callable[[AbstractEventLoop, _Context], Any]
_ProtocolFactory = Callable[[], BaseProtocol]
_SSLContext = Union[bool, None, ssl.SSLContext]
_TransProtPair = Tuple[BaseTransport, BaseProtocol]

class Server(AbstractServer): ...

class BaseEventLoop(AbstractEventLoop):
    def run_forever(self) -> None: ...

    # Can't use a union, see mypy issue  # 1873.
    @overload
    def run_until_complete(self, future: Generator[Any, None, _T]) -> _T: ...
    @overload
    def run_until_complete(self, future: Awaitable[_T]) -> _T: ...

    def stop(self) -> None: ...
    def is_running(self) -> bool: ...
    def is_closed(self) -> bool: ...
    def close(self) -> None: ...
    if sys.version_info >= (3, 6):
        @coroutine
        def shutdown_asyncgens(self) -> Generator[Any, None, None]: ...
    # Methods scheduling callbacks.  All these return Handles.
    def call_soon(self, callback: Callable[..., Any], *args: Any) -> Handle: ...
    def call_later(self, delay: float, callback: Callable[..., Any], *args: Any) -> TimerHandle: ...
    def call_at(self, when: float, callback: Callable[..., Any], *args: Any) -> TimerHandle: ...
    def time(self) -> float: ...
    # Future methods
    if sys.version_info >= (3, 5):
        def create_future(self) -> Future[Any]: ...
    # Tasks methods
    def create_task(self, coro: Union[Awaitable[_T], Generator[Any, None, _T]]) -> Task[_T]: ...
    def set_task_factory(self, factory: Optional[Callable[[AbstractEventLoop, Generator[Any, None, _T]], Future[_T]]]) -> None: ...
    def get_task_factory(self) -> Optional[Callable[[AbstractEventLoop, Generator[Any, None, _T]], Future[_T]]]: ...
    # Methods for interacting with threads
    def call_soon_threadsafe(self, callback: Callable[..., Any], *args: Any) -> Handle: ...
    @coroutine
    def run_in_executor(self, executor: Any,
                        func: Callable[..., _T], *args: Any) -> Generator[Any, None, _T]: ...
    def set_default_executor(self, executor: Any) -> None: ...
    # Network I/O methods returning Futures.
    @coroutine
    # TODO the "Tuple[Any, ...]" should be "Union[Tuple[str, int], Tuple[str, int, int, int]]" but that triggers
    # https://github.com/python/mypy/issues/2509
    def getaddrinfo(self, host: Optional[str], port: Union[str, int, None], *,
                    family: int = ..., type: int = ..., proto: int = ...,
                    flags: int = ...) -> Generator[Any, None, List[Tuple[int, int, int, str, Tuple[Any, ...]]]]: ...
    @coroutine
    def getnameinfo(self, sockaddr: tuple, flags: int = ...) -> Generator[Any, None, Tuple[str, int]]: ...
    @overload
    @coroutine
    def create_connection(self, protocol_factory: _ProtocolFactory, host: str = ..., port: int = ..., *,
                          ssl: _SSLContext = ..., family: int = ..., proto: int = ..., flags: int = ..., sock: None = ...,
                          local_addr: Optional[str] = ..., server_hostname: Optional[str] = ...) -> Generator[Any, None, _TransProtPair]: ...
    @overload
    @coroutine
    def create_connection(self, protocol_factory: _ProtocolFactory, host: None = ..., port: None = ..., *,
                          ssl: _SSLContext = ..., family: int = ..., proto: int = ..., flags: int = ..., sock: socket,
                          local_addr: None = ..., server_hostname: Optional[str] = ...) -> Generator[Any, None, _TransProtPair]: ...
    @overload
    @coroutine
    def create_server(self, protocol_factory: _ProtocolFactory, host: Optional[Union[str, Sequence[str]]] = ..., port: int = ..., *,
                      family: int = ..., flags: int = ...,
                      sock: None = ..., backlog: int = ..., ssl: _SSLContext = ...,
                      reuse_address: Optional[bool] = ...,
                      reuse_port: Optional[bool] = ...) -> Generator[Any, None, Server]: ...
    @overload
    @coroutine
    def create_server(self, protocol_factory: _ProtocolFactory, host: None = ..., port: None = ..., *,
                      family: int = ..., flags: int = ...,
                      sock: socket, backlog: int = ..., ssl: _SSLContext = ...,
                      reuse_address: Optional[bool] = ...,
                      reuse_port: Optional[bool] = ...) -> Generator[Any, None, Server]: ...
    @coroutine
    def create_unix_connection(self, protocol_factory: _ProtocolFactory, path: str, *,
                               ssl: _SSLContext = ..., sock: Optional[socket] = ...,
                               server_hostname: str = ...) -> Generator[Any, None, _TransProtPair]: ...
    @coroutine
    def create_datagram_endpoint(self, protocol_factory: _ProtocolFactory,
                                 local_addr: Optional[Tuple[str, int]] = ..., remote_addr: Optional[Tuple[str, int]] = ..., *,
                                 family: int = ..., proto: int = ..., flags: int = ...,
                                 reuse_address: Optional[bool] = ..., reuse_port: Optional[bool] = ...,
                                 allow_broadcast: Optional[bool] = ...,
                                 sock: Optional[socket] = ...) -> Generator[Any, None, _TransProtPair]: ...
    @coroutine
    def connect_accepted_socket(self, protocol_factory: _ProtocolFactory, sock: socket, *, ssl: _SSLContext = ...) -> Generator[Any, None, _TransProtPair]: ...
    # Pipes and subprocesses.
    @coroutine
    def connect_read_pipe(self, protocol_factory: _ProtocolFactory, pipe: Any) -> Generator[Any, None, _TransProtPair]: ...
    @coroutine
    def connect_write_pipe(self, protocol_factory: _ProtocolFactory, pipe: Any) -> Generator[Any, None, _TransProtPair]: ...
    @coroutine
    def subprocess_shell(self, protocol_factory: _ProtocolFactory, cmd: Union[bytes, str], *, stdin: Any = ...,
                         stdout: Any = ..., stderr: Any = ...,
                         **kwargs: Any) -> Generator[Any, None, _TransProtPair]: ...
    @coroutine
    def subprocess_exec(self, protocol_factory: _ProtocolFactory, *args: Any, stdin: Any = ...,
                        stdout: Any = ..., stderr: Any = ...,
                        **kwargs: Any) -> Generator[Any, None, _TransProtPair]: ...
    def add_reader(self, fd: selectors._FileObject, callback: Callable[..., Any], *args: Any) -> None: ...
    def remove_reader(self, fd: selectors._FileObject) -> None: ...
    def add_writer(self, fd: selectors._FileObject, callback: Callable[..., Any], *args: Any) -> None: ...
    def remove_writer(self, fd: selectors._FileObject) -> None: ...
    # Completion based I/O methods returning Futures.
    @coroutine
    def sock_recv(self, sock: socket, nbytes: int) -> Generator[Any, None, bytes]: ...
    @coroutine
    def sock_sendall(self, sock: socket, data: bytes) -> Generator[Any, None, None]: ...
    @coroutine
    def sock_connect(self, sock: socket, address: _Address) -> Generator[Any, None, None]: ...
    @coroutine
    def sock_accept(self, sock: socket) -> Generator[Any, None, Tuple[socket, Any]]: ...
    # Signal handling.
    def add_signal_handler(self, sig: int, callback: Callable[..., Any], *args: Any) -> None: ...
    def remove_signal_handler(self, sig: int) -> None: ...
    # Error handlers.
    def set_exception_handler(self, handler: Optional[_ExceptionHandler]) -> None: ...
    if sys.version_info >= (3, 5):
        def get_exception_handler(self) -> Optional[_ExceptionHandler]: ...
    def default_exception_handler(self, context: _Context) -> None: ...
    def call_exception_handler(self, context: _Context) -> None: ...
    # Debug flag management.
    def get_debug(self) -> bool: ...
    def set_debug(self, enabled: bool) -> None: ...
