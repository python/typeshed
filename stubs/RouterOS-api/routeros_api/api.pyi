import ssl
from collections.abc import Mapping
from typing import TypeVar, overload

from routeros_api.api_socket import DummySocket, SocketWrapper
from routeros_api.api_structure import _Field
from routeros_api.communication_exception_parsers import ExceptionHandler
from routeros_api.resource import RouterOsBinaryResource, RouterOsResource, _Communicator

_In = TypeVar("_In")
_Out = TypeVar("_Out")

def connect(
    host: str,
    username: str | bytes = "admin",
    password: str | bytes = "",
    port: int | None = None,
    plaintext_login: bool = False,
    use_ssl: bool = False,
    ssl_verify: bool = True,
    ssl_verify_hostname: bool = True,
    ssl_context: ssl.SSLContext | None = None,
) -> RouterOsApi: ...

class RouterOsApiPool:
    socket_timeout: float | None
    host: str
    username: str | bytes
    password: str | bytes
    port: int
    plaintext_login: bool
    use_ssl: bool
    ssl_verify: bool
    ssl_verify_hostname: bool
    ssl_context: ssl.SSLContext | None
    connected: bool
    # A DummySocket while not connected.
    socket: DummySocket | SocketWrapper
    communication_exception_parser: ExceptionHandler
    # Set by get_api, absent before its first call.
    api: RouterOsApi
    def __init__(
        self,
        host: str,
        username: str | bytes = "admin",
        password: str | bytes = "",
        port: int | None = None,
        plaintext_login: bool = False,
        use_ssl: bool = False,
        ssl_verify: bool = True,
        ssl_verify_hostname: bool = True,
        ssl_context: ssl.SSLContext | None = None,
    ) -> None: ...
    def get_api(self) -> RouterOsApi: ...
    def disconnect(self) -> None: ...
    def set_timeout(self, socket_timeout: float | None) -> None: ...

class RouterOsApi:
    communicator: _Communicator
    def __init__(self, communicator: _Communicator) -> None: ...
    def login(self, login: str | bytes, password: str | bytes, plaintext_login: bool) -> None: ...

    # None selects the default structure, every field text.
    @overload
    def get_resource(self, path: str, structure: None = None) -> RouterOsResource[str, str]: ...
    @overload
    def get_resource(self, path: str, structure: Mapping[str, _Field[_In, _Out]]) -> RouterOsResource[_In, _Out]: ...

    def get_binary_resource(self, path: str) -> RouterOsBinaryResource: ...

# Disconnects the pool on a connection or fatal error.
class CloseConnectionExceptionHandler:
    pool: RouterOsApiPool
    def __init__(self, pool: RouterOsApiPool) -> None: ...
    def handle(self, exception: BaseException) -> None: ...
