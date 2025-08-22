import http.client
import urllib.request
from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import override

import socks

_T = TypeVar("_T")

def merge_dict(a: Mapping[_T, Any], b: Mapping[_T, Any]) -> dict[_T, Any]: ...  # undocumented
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
    args: Any  # undocumented
    kw: Any  # undocumented
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @override
    def http_open(self, req: urllib.request.Request) -> http.client.HTTPResponse: ...  # undocumented
    @override
    def https_open(self, req: urllib.request.Request) -> http.client.HTTPResponse: ...  # undocumented
