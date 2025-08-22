import logging
import socket
import types
from _typeshed import Incomplete, ReadableBuffer
from collections.abc import Callable, Iterable, Mapping
from typing import Final, TypeVar
from typing_extensions import ParamSpec, TypeAlias

__version__: Final[str]

log: logging.Logger  # undocumented

_ProxyType: TypeAlias = int

PROXY_TYPE_SOCKS4: Final[_ProxyType]
SOCKS4: Final[_ProxyType]
PROXY_TYPE_SOCKS5: Final[_ProxyType]
SOCKS5: Final[_ProxyType]
PROXY_TYPE_HTTP: Final[_ProxyType]
HTTP: Final[_ProxyType]

PROXY_TYPES: Final[dict[str, _ProxyType]]
PRINTABLE_PROXY_TYPES: Final[dict[_ProxyType, str]]

_T = TypeVar("_T")
_P = ParamSpec("_P")

def set_self_blocking(function: Callable[_P, _T]) -> Callable[_P, _T]: ...  # undocumented

class ProxyError(IOError):
    msg: str
    socket_err: socket.error
    def __init__(self, msg: str, socket_err: socket.error | None = None) -> None: ...

class GeneralProxyError(ProxyError): ...
class ProxyConnectionError(ProxyError): ...
class SOCKS5AuthError(ProxyError): ...
class SOCKS5Error(ProxyError): ...
class SOCKS4Error(ProxyError): ...
class HTTPError(ProxyError): ...

SOCKS4_ERRORS: Final[Mapping[int, str]]
SOCKS5_ERRORS: Final[Mapping[int, str]]
DEFAULT_PORTS: Final[Mapping[_ProxyType, int]]

_DefaultProxy: TypeAlias = tuple[_ProxyType | None, str | None, int | None, bool, bytes | None, bytes | None]

def set_default_proxy(
    proxy_type: _ProxyType | None = None,
    addr: str | None = None,
    port: int | None = None,
    rdns: bool = True,
    username: str | None = None,
    password: str | None = None,
) -> None: ...
def setdefaultproxy(*args: Incomplete, **kwargs: Incomplete) -> None: ...
def get_default_proxy() -> _DefaultProxy | None: ...

getdefaultproxy = get_default_proxy

def wrap_module(module: types.ModuleType) -> None: ...

wrapmodule = wrap_module

_Endpoint: TypeAlias = tuple[str, int]

def create_connection(
    dest_pair: _Endpoint,
    timeout: int | None = None,
    source_address: _Endpoint | None = None,
    proxy_type: _ProxyType | None = None,
    proxy_addr: str | None = None,
    proxy_port: int | None = None,
    proxy_rdns: bool = True,
    proxy_username: str | None = None,
    proxy_password: str | None = None,
    socket_options: (
        Iterable[tuple[int, int, int | ReadableBuffer] | tuple[int, int, None, int]] | None
    ) = None,  # values passing to `socket.setsockopt` method
) -> socksocket: ...

class _BaseSocket(socket.socket):  # undocumented
    def __init__(self, *pos: Incomplete, **kw: Incomplete) -> None: ...

method: object  # undocumented
name: object  # undocumented

class socksocket(_BaseSocket):
    default_proxy: _DefaultProxy | None  # undocumented
    proxy: _DefaultProxy  # undocumented
    proxy_sockname: _Endpoint | None  # undocumented
    proxy_peername: _Endpoint | None  # undocumented
    def __init__(
        self,
        family: socket.AddressFamily = ...,
        type: socket.SocketKind = ...,
        proto: int = 0,
        *args: Incomplete,
        **kwargs: Incomplete,
    ) -> None: ...
    def settimeout(self, timeout: float | None) -> None: ...
    def gettimeout(self) -> float | None: ...
    def setblocking(self, v: bool) -> None: ...
    def set_proxy(
        self,
        proxy_type: _ProxyType | None = None,
        addr: str | None = None,
        port: int | None = None,
        rdns: bool = True,
        username: str | None = None,
        password: str | None = None,
    ) -> None: ...
    def setproxy(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def bind(self, *pos: Incomplete, **kw: Incomplete) -> None: ...
    def sendto(self, bytes: ReadableBuffer, *args: Incomplete, **kwargs: Incomplete) -> int: ...
    def send(self, bytes: ReadableBuffer, flags: int = 0, **kwargs: Incomplete) -> int: ...
    def recvfrom(self, bufsize: int, flags: int = 0) -> tuple[bytes, _Endpoint]: ...
    def recv(self, *pos: Incomplete, **kw: Incomplete) -> bytes: ...
    def close(self) -> None: ...
    def get_proxy_sockname(self) -> _Endpoint | None: ...
    getproxysockname = get_proxy_sockname
    def get_proxy_peername(self) -> _Endpoint | None: ...
    getproxypeername = get_proxy_peername
    def get_peername(self) -> _Endpoint | None: ...
    getpeername = get_peername
    @set_self_blocking
    def connect(self, dest_pair: _Endpoint, catch_errors: bool | None = None) -> None: ...  # type: ignore[override]
    @set_self_blocking
    def connect_ex(self, dest_pair: _Endpoint) -> int: ...  # type: ignore[override]
