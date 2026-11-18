from typing import Protocol, type_check_only

# The HTTP client object accepted by MSAL is duck-typed: it can be a requests.Session,
# an instance of a subclass of HttpClient, or any object with compatible post() and get() methods.
@type_check_only
class _HttpClientLike(Protocol):  # noqa: Y046
    def post(self, url: str, /, *, params=..., data=..., headers=...): ...
    def get(self, url: str, /, *, params=..., headers=...): ...

class HttpClient:
    def post(self, url: str, params=None, data=None, headers=None, **kwargs) -> Response: ...
    def get(self, url: str, params=None, headers=None, **kwargs) -> Response: ...

class Response:
    status_code: int
    text: str
    headers: dict[str, str]
    def raise_for_status(self) -> None: ...
