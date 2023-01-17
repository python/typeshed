from _typeshed import Incomplete
import socket
from typing import Any

PROXY_TYPE_SOCKS4: int
PROXY_TYPE_SOCKS5: int
PROXY_TYPE_HTTP: int
PROXY_TYPE_HTTP_NO_TUNNEL: int

class ProxyError(Exception): ...
class GeneralProxyError(ProxyError): ...
class Socks5AuthError(ProxyError): ...
class Socks5Error(ProxyError): ...
class Socks4Error(ProxyError): ...
class HTTPError(ProxyError): ...

def setdefaultproxy(
    proxytype: Incomplete | None = ...,
    addr: Incomplete | None = ...,
    port: Incomplete | None = ...,
    rdns: bool = ...,
    username: Incomplete | None = ...,
    password: Incomplete | None = ...,
) -> None: ...
def wrapmodule(module) -> None: ...

class socksocket(socket.socket):
    def __init__(self, family=..., type=..., proto: int = ..., _sock: Incomplete | None = ...) -> None: ...
    def sendall(self, content, *args): ...
    def setproxy(
        self,
        proxytype: Incomplete | None = ...,
        addr: Incomplete | None = ...,
        port: Incomplete | None = ...,
        rdns: bool = ...,
        username: Incomplete | None = ...,
        password: Incomplete | None = ...,
        headers: Incomplete | None = ...,
    ) -> None: ...
    def getproxysockname(self): ...
    def getproxypeername(self): ...
    def getpeername(self): ...
    def connect(self, destpair) -> None: ...