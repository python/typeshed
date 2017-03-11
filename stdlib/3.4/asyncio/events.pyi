import sys
from typing import Any, Awaitable, Callable, Dict, Generator, List, Optional, Tuple, TypeVar, Union, overload
from abc import ABCMeta, abstractmethod
from asyncio.futures import Future
from asyncio.coroutines import coroutine
from asyncio.protocols import BaseProtocol
from asyncio.tasks import Task
from asyncio.transports import BaseTransport

__all__ = ...  # type: str

_T = TypeVar('_T')
_Context = Dict[str, Any]
_ExceptionHandler = Callable[[AbstractEventLoop, _Context], Any]

PIPE = ...  # type: Any  # from subprocess.PIPE

AF_UNSPEC = 0     # from socket
AI_PASSIVE = 0

class Handle:
    _cancelled = False
    _args = ...  # type: List[Any]
    def __init__(self, callback: Callable[..., Any], args: List[Any],
        loop: AbstractEventLoop) -> None: ...
    def __repr__(self) -> str: ...
    def cancel(self) -> None: ...
    def _run(self) -> None: ...

class AbstractServer:
    def close(self) -> None: ...
    @coroutine
    def wait_closed(self) -> Generator[Any, Any, None]: ...

class AbstractEventLoop(metaclass=ABCMeta):
    @abstractmethod
    def run_forever(self) -> None: ...

    # Can't use a union, see mypy issue  # 1873.
    @overload
    @abstractmethod
    def run_until_complete(self, future: Generator[Any, Any, _T]) -> _T: ...
    @overload
    @abstractmethod
    def run_until_complete(self, future: Awaitable[_T]) -> _T: ...

    @abstractmethod
    def stop(self) -> None: ...
    @abstractmethod
    def is_running(self) -> bool: ...
    @abstractmethod
    def is_closed(self) -> bool: ...
    @abstractmethod
    def close(self) -> None: ...
    if sys.version_info >= (3, 6):
        @abstractmethod
        @coroutine
        def shutdown_asyncgens(self) -> Generator[Any, Any, None]: ...
    # Methods scheduling callbacks.  All these return Handles.
    @abstractmethod
    def call_soon(self, callback: Callable[..., Any], *args: Any) -> Handle: ...
    @abstractmethod
    def call_later(self, delay: Union[int, float], callback: Callable[..., Any], *args: Any) -> Handle: ...
    @abstractmethod
    def call_at(self, when: float, callback: Callable[..., Any], *args: Any) -> Handle: ...
    @abstractmethod
    def time(self) -> float: ...
    # Future methods
    if sys.version_info >= (3, 5):
        @abstractmethod
        def create_future(self) -> Future[Any]: ...
    # Tasks methods
    @abstractmethod
    def create_task(self, coro: Union[Future[_T], Generator[Any, None, _T]]) -> Task[_T]: ...
    @abstractmethod
    def set_task_factory(self, factory: Optional[Callable[[AbstractEventLoop, Generator[Any, None, _T]], Future[_T]]]) -> None: ...
    @abstractmethod
    def get_task_factory(self) -> Optional[Callable[[AbstractEventLoop, Generator[Any, None, _T]], Future[_T]]]: ...
    # Methods for interacting with threads
    @abstractmethod
    def call_soon_threadsafe(self, callback: Callable[..., Any], *args: Any) -> Handle: ...
    @abstractmethod
    @coroutine
    def run_in_executor(self, executor: Any,
        callback: Callable[..., Any], *args: Any) -> Generator[None, None, Any]: ...
    @abstractmethod
    def set_default_executor(self, executor: Any) -> None: ...
    # Network I/O methods returning Futures.
    @abstractmethod
    @coroutine
    def getaddrinfo(self, host: str, port: int, *,
        family: int = ..., type: int = ..., proto: int = ..., flags: int = ...) -> Generator[None, None, List[Tuple[int, int, int, str, tuple]]]: ...
    @abstractmethod
    @coroutine
    def getnameinfo(self, sockaddr: tuple, flags: int = ...) -> Generator[None, None, Tuple[str, int]]: ...
    @abstractmethod
    @coroutine
    def create_connection(self, protocol_factory: Any, host: str = ..., port: int = ..., *,
                          ssl: Any = ..., family: int = ..., proto: int = ..., flags: int = ..., sock: Any = ...,
                          local_addr: str = ..., server_hostname: str = ...) -> Generator[None, None, tuple]: ...
    @abstractmethod
    @coroutine
    def create_server(self, protocol_factory: Any, host: str = ..., port: int = ..., *,
                      family: int = ..., flags: int = ...,
                      sock: Any = ..., backlog: int = ..., ssl: Any = ..., reuse_address: Any = ...) -> Generator[None, None, Any]: ...
    @abstractmethod
    @coroutine
    def create_unix_connection(self, protocol_factory: Any, path: str, *,
                               ssl: Any = ..., sock: Any = ...,
                               server_hostname: str = ...) -> Generator[None, None, tuple]: ...
    @abstractmethod
    @coroutine
    def create_unix_server(self, protocol_factory: Any, path: str, *,
                           sock: Any = ..., backlog: int = ..., ssl: Any = ...) -> Generator[None, None, Any]: ...
    @abstractmethod
    @coroutine
    def create_datagram_endpoint(self, protocol_factory: Any,
                                 local_addr: str = ..., remote_addr: str = ..., *,
                                 family: int = ..., proto: int = ..., flags: int = ...) -> Generator[None, None, tuple]: ...
    @abstractmethod
    @coroutine
    def connect_accepted_socket(self, protocol_factory: Any, sock: Any, *, ssl: Any = ...) -> Generator[None, None, Tuple[BaseTransport, BaseProtocol]]: ...
    # Pipes and subprocesses.
    @abstractmethod
    @coroutine
    def connect_read_pipe(self, protocol_factory: Any, pipe: Any) -> Generator[None, None, tuple]: ...
    @abstractmethod
    @coroutine
    def connect_write_pipe(self, protocol_factory: Any, pipe: Any) -> Generator[None, None, tuple]: ...
    @abstractmethod
    @coroutine
    def subprocess_shell(self, protocol_factory: Any, cmd: Union[bytes, str], *, stdin: Any = ...,
                         stdout: Any = ..., stderr: Any = ...,
                         **kwargs: Any) -> Generator[None, None, tuple]: ...
    @abstractmethod
    @coroutine
    def subprocess_exec(self, protocol_factory: Any, *args: List[Any], stdin: Any = ...,
                        stdout: Any = ..., stderr: Any = ...,
                        **kwargs: Any) -> Generator[None, None, tuple]: ...
    @abstractmethod
    def add_reader(self, fd: int, callback: Callable[..., Any], *args: List[Any]) -> None: ...
    @abstractmethod
    def remove_reader(self, fd: int) -> None: ...
    @abstractmethod
    def add_writer(self, fd: int, callback: Callable[..., Any], *args: List[Any]) -> None: ...
    @abstractmethod
    def remove_writer(self, fd: int) -> None: ...
    # Completion based I/O methods returning Futures.
    @abstractmethod
    @coroutine
    def sock_recv(self, sock: Any, nbytes: int) -> Generator[None, None, Any]: ...  # TODO
    @abstractmethod
    @coroutine
    def sock_sendall(self, sock: Any, data: bytes) -> Generator[None, None, None]: ...  # TODO
    @abstractmethod
    @coroutine
    def sock_connect(self, sock: Any, address: str) -> Generator[None, None, Any]: ...  # TODO
    @abstractmethod
    @coroutine
    def sock_accept(self, sock: Any) -> Generator[None, None, Any]: ...
    # Signal handling.
    @abstractmethod
    def add_signal_handler(self, sig: int, callback: Callable[..., Any], *args: List[Any]) -> None: ...
    @abstractmethod
    def remove_signal_handler(self, sig: int) -> None: ...
    # Error handlers.
    @abstractmethod
    def set_exception_handler(self, handler: _ExceptionHandler) -> None: ...
    @abstractmethod
    def get_exception_handler(self) -> _ExceptionHandler: ...
    @abstractmethod
    def default_exception_handler(self, context: _Context) -> None: ...
    @abstractmethod
    def call_exception_handler(self, context: _Context) -> None: ...
    # Debug flag management.
    @abstractmethod
    def get_debug(self) -> bool: ...
    @abstractmethod
    def set_debug(self, enabled: bool) -> None: ...

class AbstractEventLoopPolicy(metaclass=ABCMeta):
    @abstractmethod
    def get_event_loop(self) -> AbstractEventLoop: ...
    @abstractmethod
    def set_event_loop(self, loop: AbstractEventLoop): ...
    @abstractmethod
    def new_event_loop(self) -> AbstractEventLoop: ...
    # Child processes handling (Unix only).
    @abstractmethod
    def get_child_watcher(self) -> Any: ...  # TODO: unix_events.AbstractChildWatcher
    @abstractmethod
    def set_child_watcher(self, watcher: Any) -> None: ...  # TODO: unix_events.AbstractChildWatcher

class BaseDefaultEventLoopPolicy(AbstractEventLoopPolicy):
    def __init__(self) -> None: ...
    def get_event_loop(self) -> AbstractEventLoop: ...
    def set_event_loop(self, loop: AbstractEventLoop): ...
    def new_event_loop(self) -> AbstractEventLoop: ...

def get_event_loop_policy() -> AbstractEventLoopPolicy: ...
def set_event_loop_policy(policy: AbstractEventLoopPolicy) -> None: ...

def get_event_loop() -> AbstractEventLoop: ...
def set_event_loop(loop: AbstractEventLoop) -> None: ...
def new_event_loop() -> AbstractEventLoop: ...

def get_child_watcher() -> Any: ...  # TODO: unix_events.AbstractChildWatcher
def set_child_watcher(watcher: Any) -> None: ...  # TODO: unix_events.AbstractChildWatcher
