import socket
from _typeshed import Incomplete
from collections.abc import Iterable
from logging import Logger
from ssl import SSLSocket, SSLContext
from typing import Any, ClassVar, Literal, SupportsIndex, override

from .config import Config


class BaseSocket:
    def __init__(self, address: str, conf: Config, log: Logger, fd: SupportsIndex | None = None) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def set_options[T: socket.socket](self, sock: T, bound: bool = False) -> T: ...
    def bind(self, sock: socket.socket) -> None: ...
    def close(self) -> None: ...


class TCPSocket(BaseSocket):
    FAMILY: ClassVar[Literal[socket.AddressFamily.AF_INET, socket.AddressFamily.AF_INET6]]

    @override
    def set_options[T: socket.socket](self, sock: T, bound: bool = False) -> T: ...


class TCP6Socket(TCPSocket):
    FAMILY: ClassVar[Literal[socket.AddressFamily.AF_INET6]]


class UnixSocket(BaseSocket):
    FAMILY: ClassVar[Literal[socket.AddressFamily.AF_UNIX]]

    def __init__(self, addr: str, conf: Config, log: Logger, fd: SupportsIndex | None = None) -> None: ...
    @override
    def bind(self, sock: socket.socket) -> None: ...


def create_sockets(conf: Config, log: Logger, fds: Iterable[SupportsIndex] | None = None) -> list[BaseSocket]: ...
def close_sockets(listeners: Iterable[socket.socket], unlink: bool = True) -> None: ...
def ssl_context(conf: Config) -> SSLContext: ...
def ssl_wrap_socket(sock: socket.socket, conf: Config) -> SSLSocket: ...
