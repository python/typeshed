"""
This module contains provisional support for SOCKS proxies from within
urllib3. This module supports SOCKS4, SOCKS4A (an extension of SOCKS4), and
SOCKS5. To enable its functionality, either install PySocks or install this
module with the ``socks`` extra.

The SOCKS implementation supports the full range of urllib3 features. It also
supports the following SOCKS features:

- SOCKS4A (``proxy_url='socks4a://...``)
- SOCKS4 (``proxy_url='socks4://...``)
- SOCKS5 with remote DNS (``proxy_url='socks5h://...``)
- SOCKS5 with local DNS (``proxy_url='socks5://...``)
- Usernames and passwords for the SOCKS proxy

.. note::
   It is recommended to use ``socks5h://`` or ``socks4a://`` schemes in
   your ``proxy_url`` to ensure that DNS resolution is done from the remote
   server instead of client-side when connecting to a domain name.

SOCKS4 supports IPv4 and domain names with the SOCKS4A extension. SOCKS5
supports IPv4, IPv6, and domain names.

When connecting to a SOCKS4 proxy the ``username`` portion of the ``proxy_url``
will be sent as the ``userid`` section of the SOCKS request:

.. code-block:: python

    proxy_url="socks4a://<userid>@proxy-host"

When connecting to a SOCKS5 proxy the ``username`` and ``password`` portion
of the ``proxy_url`` will be sent as the username/password to authenticate
with the proxy:

.. code-block:: python

    proxy_url="socks5h://<username>:<password>@proxy-host"

"""

from typing import Any, ClassVar, Mapping, Optional

from ..connection import HTTPConnection, HTTPSConnection
from ..connectionpool import HTTPConnectionPool, HTTPSConnectionPool
from ..poolmanager import PoolManager

from typing_extensions import TypedDict

class _SockOptions(TypedDict):
    socks_version: int
    proxy_host: Optional[str]
    proxy_port: Optional[str]
    username: Optional[str]
    password: Optional[str]
    rdns: bool

class SOCKSConnection(HTTPConnection):
    def __init__(self, _socks_options: _SockOptions, *args: Any, **kwargs: Any) -> None: ...
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
        **connection_pool_kw: Any,
    ) -> None: ...
