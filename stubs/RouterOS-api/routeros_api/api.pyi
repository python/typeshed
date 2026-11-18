import ssl
from collections.abc import Mapping
from typing import Any, TypeVar, overload

from routeros_api.api_socket import DummySocket, SocketWrapper
from routeros_api.api_structure import _Field
from routeros_api.communication_exception_parsers import ExceptionHandler
from routeros_api.resource import RouterOsBinaryResource, RouterOsResource, _Communicator

_In = TypeVar("_In")
_Out = TypeVar("_Out")

def connect(  # undocumented
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
    socket_timeout: float | None  # undocumented
    host: str  # undocumented
    username: str | bytes  # undocumented
    password: str | bytes  # undocumented
    port: int  # undocumented
    plaintext_login: bool  # undocumented
    use_ssl: bool  # undocumented
    ssl_verify: bool  # undocumented
    ssl_verify_hostname: bool  # undocumented
    ssl_context: ssl.SSLContext | None  # undocumented
    connected: bool  # undocumented
    # A DummySocket while not connected.
    socket: DummySocket | SocketWrapper  # undocumented
    communication_exception_parser: ExceptionHandler  # undocumented
    # Set by get_api, absent before its first call.
    api: RouterOsApi  # undocumented
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
    def set_timeout(self, socket_timeout: float | None) -> None: ...  # undocumented

class RouterOsApi:
    communicator: _Communicator  # undocumented
    def __init__(self, communicator: _Communicator) -> None: ...
    def login(self, login: str | bytes, password: str | bytes, plaintext_login: bool) -> None: ...  # undocumented

    # None selects the default structure, every field text.
    @overload
    def get_resource(self, path: str, structure: None = None) -> RouterOsResource[str, str]: ...
    @overload
    def get_resource(self, path: str, structure: Mapping[str, _Field[_In, _Out]]) -> RouterOsResource[_In, _Out]: ...
    # A structure whose fields encode and decode different types: each key's type can't be expressed,
    # so the resource's arguments and values go unchecked.
    @overload
    def get_resource(
        self, path: str, structure: Mapping[str, _Field[Any, Any]]  # Any: the type each key's field encodes and decodes
    ) -> RouterOsResource[Any, Any]: ...  # Any: the type of each key's value

    def get_binary_resource(self, path: str) -> RouterOsBinaryResource: ...

# Disconnects the pool on a connection or fatal error.
class CloseConnectionExceptionHandler:  # undocumented
    pool: RouterOsApiPool
    def __init__(self, pool: RouterOsApiPool) -> None: ...
    def handle(self, exception: BaseException) -> None: ...
