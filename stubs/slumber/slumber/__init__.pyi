from typing import Any
from typing_extensions import Self

from requests import Response, Session
from requests.sessions import _Auth, _Data, _Files

from .serialize import Serializer

__all__ = ["Resource", "API"]

class ResourceAttributesMixin:
    # Exists at runtime:
    def __getattr__(self, item: str) -> Any: ...

class Resource(ResourceAttributesMixin):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __call__(self, id: str | None = None, format: str | None = None, url_override: str | None = None) -> Self: ...
    def as_raw(self) -> Self: ...
    def get(self, **kwargs: Any) -> Response: ...
    def options(self, **kwargs: Any) -> Response: ...
    def head(self, **kwargs: Any) -> Response: ...
    def post(self, data: _Data | None = None, files: _Files | None = None, **kwargs: Any) -> Response: ...
    def patch(self, data: _Data | None = None, files: _Files | None = None, **kwargs: Any) -> Response: ...
    def put(self, data: _Data | None = None, files: _Files | None = None, **kwargs: Any) -> Response: ...
    def delete(self, **kwargs: Any) -> Response: ...
    def url(self) -> str: ...

class API(ResourceAttributesMixin):
    resource_class: type[Resource]
    def __init__(
        self,
        base_url: str | None = None,
        auth: _Auth | None = None,
        format: str | None = None,
        append_slash: bool = True,
        session: Session | None = None,
        serializer: Serializer | None = None,
        raw: bool = ...,
    ) -> None: ...
