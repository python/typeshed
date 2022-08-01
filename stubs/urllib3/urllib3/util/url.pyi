from typing import Any

from .. import exceptions

LocationParseError = exceptions.LocationParseError

url_attrs: list[str]

class Url:
    slots: Any
    def __new__(
        cls,
        scheme: str | None = ...,
        auth: str | None = ...,
        host: str | None = ...,
        port: str | None = ...,
        path: str | None = ...,
        query: str | None = ...,
        fragment: str | None = ...,
    ): ...
    @property
    def hostname(self) -> str | None: ...
    @property
    def request_uri(self) -> str: ...
    @property
    def netloc(self) -> str | None: ...
    @property
    def url(self) -> str: ...

def split_first(s, delims): ...
def parse_url(url: str) -> Url: ...
def get_host(url): ...
