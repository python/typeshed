from collections.abc import AsyncGenerator, Mapping
from typing import Any, TypeAlias

from google.auth.aio import transport

ClientTimeout: TypeAlias = Any

class Response(transport.Response):
    def __init__(self, response: Any) -> None: ...
    @property
    def status_code(self) -> int: ...
    @property
    def headers(self) -> Mapping[str, str]: ...
    async def content(self, chunk_size: int = 1024) -> AsyncGenerator[bytes]: ...
    async def read(self) -> bytes: ...
    async def close(self) -> None: ...

class Request(transport.Request):
    def __init__(self, session: Any | None = None) -> None: ...
    async def __call__(
        self,
        url: str,
        method: str = "GET",
        body: bytes | None = None,
        headers: Mapping[str, str] | None = None,
        timeout: float | ClientTimeout = ...,
        *args: Any,
        **kwargs: Any,
    ) -> transport.Response: ...
    async def close(self) -> None: ...
