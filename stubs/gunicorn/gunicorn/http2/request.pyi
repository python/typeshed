from typing import Literal
from typing_extensions import Self

from gunicorn._types import _AddressType
from gunicorn.asgi.parser import _ProxyProtocolInfo, _ProxyProtocolInfoUnknown
from gunicorn.config import Config
from gunicorn.http.message import HeaderPolicy
from gunicorn.http2.stream import HTTP2Stream

class HTTP2Body:
    def __init__(self, source: HTTP2Stream | bytes | bytearray) -> None: ...
    def read(self, size: int | None = None) -> bytes: ...
    def readline(self, size: int | None = None) -> bytes: ...
    def readlines(self, hint: int | None = None) -> list[bytes]: ...
    def close(self) -> None: ...
    def __iter__(self) -> Self: ...
    def __next__(self) -> bytes: ...

class HTTP2Request(HeaderPolicy):
    stream: HTTP2Stream
    cfg: Config
    peer_addr: _AddressType
    remote_addr: _AddressType
    version: tuple[int, int]
    method: str
    scheme: Literal["https", "http"]
    uri: str
    path: str
    query: str
    fragment: str
    headers: list[tuple[str, str]]
    body: HTTP2Body
    must_close: bool
    req_number: int
    proxy_protocol_info: _ProxyProtocolInfo | _ProxyProtocolInfoUnknown | None
    priority_weight: int
    priority_depends_on: int

    def __init__(self, stream: HTTP2Stream, cfg: Config, peer_addr: _AddressType) -> None: ...
    @property
    def trailers(self) -> list[tuple[str, str]]: ...
    def force_close(self) -> None: ...
    def should_close(self) -> bool: ...
    def get_header(self, name: str) -> str | None: ...
    @property
    def content_length(self) -> int | None: ...
    @property
    def content_type(self) -> str | None: ...

__all__ = ["HTTP2Request", "HTTP2Body"]
