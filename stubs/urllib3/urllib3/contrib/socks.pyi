from collections.abc import Mapping
from typing import Any, ClassVar
from typing_extensions import TypedDict

from ..connection import HTTPConnection, HTTPSConnection
from ..connectionpool import HTTPConnectionPool, HTTPSConnectionPool
from ..poolmanager import PoolManager

class _TYPE_SOCKS_OPTIONS(TypedDict):
    socks_version: int
    proxy_host: str | None
    proxy_port: str | None
    username: str | None
    password: str | None
    rdns: bool

class SOCKSConnection(HTTPConnection):
    def __init__(self, _socks_options: _TYPE_SOCKS_OPTIONS, *args, **kwargs) -> None: ...
    def _new_conn(self) -> Any: ...  # "socks.socksocket":

class SOCKSHTTPSConnection(SOCKSConnection, HTTPSConnection): ...
class SOCKSHTTPConnectionPool(HTTPConnectionPool): ...
class SOCKSHTTPSConnectionPool(HTTPSConnectionPool): ...

class _ConnectionPoolClasses(TypedDict):
    http: type[SOCKSHTTPSConnectionPool]
    https: type[SOCKSHTTPSConnectionPool]

class SOCKSProxyManager(PoolManager):
    pool_classes_by_scheme: ClassVar[_ConnectionPoolClasses]
    proxy_url: str

    def __init__(
        self,
        proxy_url: str,
        username: str | None = ...,
        password: str | None = ...,
        num_pools: int = ...,
        headers: Mapping[str, str] | None = ...,
        **connection_pool_kw,
    ) -> None: ...
