from _typeshed import Incomplete
from typing import Any

from auth0.exceptions import RateLimitError as RateLimitError
from auth0.types import RequestData as RequestData

from .rest import (
    EmptyResponse as EmptyResponse,
    JsonResponse as JsonResponse,
    PlainResponse as PlainResponse,
    Response as Response,
    RestClient as RestClient,
)

class AsyncRestClient(RestClient):
    timeout: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def set_session(self, session) -> None: ...
    async def get(
        self, url: str, params: dict[str, Incomplete] | None = None, headers: dict[str, str] | None = None
    ) -> Incomplete: ...
    async def post(self, url: str, data: RequestData | None = None, headers: dict[str, str] | None = None) -> Incomplete: ...
    async def file_post(self, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
    async def patch(self, url: str, data: RequestData | None = None) -> Incomplete: ...
    async def put(self, url: str, data: RequestData | None = None) -> Incomplete: ...
    async def delete(
        self, url: str, params: dict[str, Incomplete] | None = None, data: RequestData | None = None
    ) -> Incomplete: ...

class RequestsResponse:
    status_code: Incomplete
    headers: Incomplete
    text: Incomplete
    def __init__(self, response, text: str) -> None: ...
