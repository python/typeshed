import http.client
import urllib.request
from _typeshed import Incomplete, SupportsKeysAndGetItem
from typing import Any, TypeVar
from typing_extensions import override

import socks

_K = TypeVar("_K")
_V = TypeVar("_V")

def merge_dict(a: dict[_K, _V], b: SupportsKeysAndGetItem[_K, _V]) -> dict[_K, _V]: ...  # undocumented
def is_ip(s: str) -> bool: ...  # undocumented

socks4_no_rdns: set[str]  # undocumented

class SocksiPyConnection(http.client.HTTPConnection):  # undocumented
    proxyargs: tuple[int, str, int | None, bool, str | None, str | None]
    sock: socks.socksocket
    def __init__(
        self,
        proxytype: int,
        proxyaddr: str,
        proxyport: int | None = None,
        rdns: bool = True,
        username: str | None = None,
        password: str | None = None,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    @override
    def connect(self) -> None: ...

class SocksiPyConnectionS(http.client.HTTPSConnection):  # undocumented
    proxyargs: tuple[int, str, int | None, bool, str | None, str | None]
    sock: socks.socksocket
    def __init__(
        self,
        proxytype: int,
        proxyaddr: str,
        proxyport: int | None = None,
        rdns: bool = True,
        username: str | None = None,
        password: str | None = None,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    @override
    def connect(self) -> None: ...

class SocksiPyHandler(urllib.request.HTTPHandler, urllib.request.HTTPSHandler):
    args: tuple[Incomplete, ...]  # undocumented
    kw: dict[str, Incomplete]  # undocumented
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @override
    def http_open(self, req: urllib.request.Request) -> http.client.HTTPResponse: ...  # undocumented
    @override
    def https_open(self, req: urllib.request.Request) -> http.client.HTTPResponse: ...  # undocumented
