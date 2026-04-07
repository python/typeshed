from collections.abc import AsyncGenerator, Callable, Mapping
from contextlib import asynccontextmanager
from typing import Any

from google.auth.aio import transport
from google.auth.aio.credentials import Credentials

class ClientTimeout: ...

AIOHTTP_INSTALLED: bool

@asynccontextmanager
def timeout_guard(timeout: float) -> AsyncGenerator[Any]: ...

class AsyncAuthorizedSession:
    def __init__(self, credentials: Credentials, auth_request: transport.Request | None = None) -> None: ...
    async def configure_mtls_channel(self, client_cert_callback: Callable[[], tuple[bytes, bytes]] | None = None) -> None: ...
    async def request(
        self,
        method: str,
        url: str,
        data: bytes | None = None,
        headers: Mapping[str, str] | None = None,
        max_allowed_time: float = ...,
        timeout: float | ClientTimeout = ...,
        total_attempts: int | None = ...,
        **kwargs: Any,
    ) -> transport.Response: ...
    async def get(
        self,
        url: str,
        data: bytes | None = None,
        headers: Mapping[str, str] | None = None,
        max_allowed_time: float = ...,
        timeout: float | ClientTimeout = ...,
        total_attempts: int | None = ...,
        **kwargs: Any,
    ) -> transport.Response: ...
    async def post(
        self,
        url: str,
        data: bytes | None = None,
        headers: Mapping[str, str] | None = None,
        max_allowed_time: float = ...,
        timeout: float | ClientTimeout = ...,
        total_attempts: int | None = ...,
        **kwargs: Any,
    ) -> transport.Response: ...
    async def put(
        self,
        url: str,
        data: bytes | None = None,
        headers: Mapping[str, str] | None = None,
        max_allowed_time: float = ...,
        timeout: float | ClientTimeout = ...,
        total_attempts: int | None = ...,
        **kwargs: Any,
    ) -> transport.Response: ...
    async def patch(
        self,
        url: str,
        data: bytes | None = None,
        headers: Mapping[str, str] | None = None,
        max_allowed_time: float = ...,
        timeout: float | ClientTimeout = ...,
        total_attempts: int | None = ...,
        **kwargs: Any,
    ) -> transport.Response: ...
    async def delete(
        self,
        url: str,
        data: bytes | None = None,
        headers: Mapping[str, str] | None = None,
        max_allowed_time: float = ...,
        timeout: float | ClientTimeout = ...,
        total_attempts: int | None = ...,
        **kwargs: Any,
    ) -> transport.Response: ...
    @property
    def is_mtls(self) -> bool: ...
    async def close(self) -> None: ...
