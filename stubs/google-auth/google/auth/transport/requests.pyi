import types
from _typeshed import SupportsItems, SupportsRead
from collections.abc import Callable, Iterable, Mapping, MutableMapping, Sequence
from typing import Any
from typing_extensions import Self

import requests
import requests.adapters
from google.auth import transport
from requests import Response, Response as _RequestsResponse
from requests.auth import AuthBase
from requests.sessions import PreparedRequest, RequestsCookieJar

class _Response(transport.Response):
    def __init__(self, response: _RequestsResponse) -> None: ...
    @property
    def status(self) -> int: ...
    @property
    def headers(self) -> Mapping[str, str]: ...
    @property
    def data(self) -> bytes: ...

class TimeoutGuard:
    remaining_timeout: Any

    def __init__(self, timeout: Any, timeout_error_type: type[Exception] = requests.exceptions.Timeout) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None
    ) -> None: ...

class Request(transport.Request):
    session: requests.Session | None

    def __init__(self, session: requests.Session | None = None) -> None: ...
    def __del__(self) -> None: ...
    def __call__(
        self,
        url: str,
        method: str = "GET",
        body: bytes | None = None,
        headers: Mapping[str, str] | None = None,
        timeout: float | None = None,
        **kwargs: Any,
    ) -> _Response: ...

class _MutualTlsAdapter(requests.adapters.HTTPAdapter):
    def __init__(self, cert: bytes, key: bytes) -> None: ...
    def init_poolmanager(self, *args: Any, **kwargs: Any) -> None: ...
    def proxy_manager_for(self, *args: Any, **kwargs: Any) -> Any: ...

class _MutualTlsOffloadAdapter(requests.adapters.HTTPAdapter):
    signer: Any

    def __init__(self, enterprise_cert_file_path: str) -> None: ...
    def init_poolmanager(self, *args: Any, **kwargs: Any) -> None: ...
    def proxy_manager_for(self, *args: Any, **kwargs: Any) -> Any: ...

class AuthorizedSession(requests.Session):
    credentials: Any

    def __init__(
        self,
        credentials: Any,
        refresh_status_codes: Sequence[int] = ...,
        max_refresh_attempts: int = ...,
        refresh_timeout: float | None = None,
        auth_request: Request | None = None,
        default_host: str | None = None,
    ) -> None: ...
    def configure_mtls_channel(self, client_cert_callback: Any | None = None) -> None: ...
    def request(
        self,
        method: str | bytes,
        url: str | bytes,
        params: (
            SupportsItems[str | bytes | float, str | bytes | float | Iterable[str | bytes | float] | None]
            | tuple[str | bytes | float, str | bytes | float | Iterable[str | bytes | float] | None]
            | Iterable[tuple[str | bytes | float, str | bytes | float | Iterable[str | bytes | float] | None]]
            | str
            | bytes
            | None
        ) = ...,
        data: (
            Iterable[bytes]
            | str
            | bytes
            | SupportsRead[str | bytes]
            | list[tuple[Any, Any]]
            | tuple[tuple[Any, Any], ...]
            | Mapping[Any, Any]
            | None
        ) = ...,
        headers: Mapping[str, str | bytes | None] | None = ...,
        cookies: RequestsCookieJar | MutableMapping[str, str] | None = ...,
        files: (
            Mapping[
                str,
                SupportsRead[str | bytes]
                | str
                | bytes
                | tuple[str | None, SupportsRead[str | bytes] | str | bytes]
                | tuple[str | None, SupportsRead[str | bytes] | str | bytes, str]
                | tuple[str | None, SupportsRead[str | bytes] | str | bytes, str, Mapping[str, str]],
            ]
            | Iterable[
                tuple[
                    str,
                    SupportsRead[str | bytes]
                    | str
                    | bytes
                    | tuple[str | None, SupportsRead[str | bytes] | str | bytes]
                    | tuple[str | None, SupportsRead[str | bytes] | str | bytes, str]
                    | tuple[str | None, SupportsRead[str | bytes] | str | bytes, str, Mapping[str, str]],
                ]
            ]
            | None
        ) = ...,
        auth: tuple[str, str] | AuthBase | Callable[[PreparedRequest], PreparedRequest] | None = ...,
        timeout: float | tuple[float | None, float | None] | None = ...,
        allow_redirects: bool = ...,
        proxies: MutableMapping[str, str] | None = ...,
        hooks: Mapping[str, Iterable[Callable[[Response], Any]] | Callable[[Response], Any]] | None = ...,
        stream: bool | None = ...,
        verify: bool | str | None = ...,
        cert: str | tuple[str, str] | None = ...,
        json: Any | None = ...,
    ) -> Response: ...
    @property
    def is_mtls(self) -> bool: ...
