from _typeshed import Incomplete, SupportsItems, SupportsRead
from collections.abc import Callable, Iterable, Iterator, Sequence
from datetime import timedelta
from typing import IO, Any, NoReturn, Protocol
from typing_extensions import Literal, TypeAlias, TypedDict

from webob.byterange import ContentRange
from webob.cachecontrol import _ResponseCacheControl
from webob.descriptors import _authorization, _DateProperty, _ListProperty, _SimpleProperty
from webob.headers import ResponseHeaders
from webob.request import Request

class _ResponseCacheExpires(Protocol):
    def __call__(
        self,
        seconds: int | timedelta = 0,
        *,
        public: bool = ...,
        private: Literal[True] | str = ...,
        no_cache: Literal[True] | str = ...,
        no_store: bool = ...,
        no_transform: bool = ...,
        must_revalidate: bool = ...,
        proxy_revalidate: bool = ...,
        max_age: int = ...,
        s_maxage: int = ...,
        s_max_age: int = ...,
        stale_while_revalidate: int = ...,
        stale_if_error: int = ...,
    ) -> None: ...

class _ResponseCacheControlDict(TypedDict, total=False):
    public: bool
    private: Literal[True] | str
    no_cache: Literal[True] | str
    no_store: bool
    no_transform: bool
    must_revalidate: bool
    proxy_revalidate: bool
    max_age: int
    s_maxage: int
    s_max_age: int
    stale_while_revalidate: int
    stale_if_error: int

_HTTPHeader: TypeAlias = tuple[str, str]
_StartResponse: TypeAlias = Callable[[str, list[_HTTPHeader]], None]
_WSGIApplication: TypeAlias = Callable[[dict[str, Any], _StartResponse], Iterator[bytes]]
_ContentRangeParams: TypeAlias = (
    ContentRange
    | list[int | None]
    | tuple[int, int]
    | tuple[None, None]
    | tuple[int, int, int | None]
    | tuple[None, None, int | None]
    | str
    | bytes
    | None
)

class Response:
    default_content_type: str
    default_charset: str
    unicode_errors: str
    default_conditional_response: bool
    default_body_encoding: str
    request: Request | None
    environ: dict[str, Any] | None
    status: str
    conditional_response: bool

    def __init__(
        self,
        body: bytes | str | None = ...,
        status: str | None = ...,
        headerlist: list[_HTTPHeader] | None = ...,
        app_iter: Iterator[bytes] | None = ...,
        content_type: str | None = ...,
        conditional_response: Incomplete | None = ...,
        charset: str = ...,
        **kw,
    ) -> None: ...
    @classmethod
    def from_file(cls, fp: IO[str]) -> Response: ...
    def copy(self) -> Response: ...
    status_code: int
    status_int: int
    @property
    def headerlist(self) -> list[_HTTPHeader]: ...
    @headerlist.setter
    def headerlist(self, value: Iterable[tuple[str, str]] | SupportsItems[str, str]) -> None: ...
    @headerlist.deleter
    def headerlist(self) -> None: ...
    @property
    def headers(self) -> ResponseHeaders: ...
    @headers.setter
    def headers(self, value: SupportsItems[str, str] | Iterable[tuple[str, str]]) -> None: ...
    body: bytes
    json: Any
    json_body: Any
    @property
    def has_body(self) -> bool: ...
    text: str
    unicode_body: str  # deprecated
    ubody: str  # deprecated
    @property
    def body_file(self) -> ResponseBodyFile: ...
    @body_file.setter
    def body_file(self, __value: SupportsRead[bytes]) -> None: ...
    @body_file.deleter
    def body_file(self) -> None: ...
    content_length: int | None
    def write(self, text) -> None: ...
    app_iter: Iterator[bytes]
    allow: _ListProperty[str | bytes]
    vary: _ListProperty[str | bytes]
    content_encoding: _SimpleProperty[str | bytes]
    content_language: _ListProperty[str | bytes]
    content_location: _SimpleProperty[str | bytes]
    content_md5: _SimpleProperty[str | bytes]
    content_disposition: _SimpleProperty[str | bytes]
    accept_ranges: _SimpleProperty[str | bytes]
    @property
    def content_range(self) -> ContentRange: ...
    @content_range.setter
    def content_range(self, value: _ContentRangeParams) -> None: ...
    @content_range.deleter
    def content_range(self) -> None: ...
    date: _DateProperty[str | bytes]
    expires: _DateProperty[str | bytes]
    last_modified: _DateProperty[str | bytes]
    @property
    def etag(self) -> str | None: ...
    @etag.setter
    def etag(self, value: tuple[str, bool] | str | None) -> None: ...
    @etag.deleter
    def etag(self) -> None: ...
    @property
    def etag_strong(self) -> str | None: ...
    location: _SimpleProperty[str | bytes]
    pragma: _SimpleProperty[str | bytes]
    age: int | None
    retry_after: _DateProperty[str | bytes]
    server: _SimpleProperty[str | bytes]
    @property
    def www_authenticate(self) -> _authorization | None: ...
    @www_authenticate.setter
    def www_authenticate(self, value: tuple[str, str | dict[str, str]] | list[Any] | str | bytes | None): ...
    @www_authenticate.deleter
    def www_authenticate(self) -> None: ...
    charset: str | None
    content_type: str | None
    @property
    def content_type_params(self) -> dict[str, str]: ...
    @content_type_params.setter
    def content_type_params(self, value: SupportsItems[str, str] | None) -> None: ...
    @content_type_params.deleter
    def content_type_params(self) -> None: ...
    def set_cookie(
        self,
        name: str,
        value: str | None = ...,
        max_age: int | timedelta | None = ...,
        path: str = ...,
        domain: str | None = ...,
        secure: bool = ...,
        httponly: bool = ...,
        comment: str | None = ...,
        overwrite: bool = ...,
        samesite: Literal["strict", "lax", "none"] | None = ...,
    ) -> None: ...
    def delete_cookie(self, name: str, path: str = ..., domain: str | None = ...) -> None: ...
    def unset_cookie(self, name: str, strict: bool = ...) -> None: ...
    def merge_cookies(self, resp: Response | _WSGIApplication) -> None: ...
    @property
    def cache_control(self) -> _ResponseCacheControl: ...
    @cache_control.setter
    def cache_control(self, value: _ResponseCacheControl | _ResponseCacheControlDict | str | bytes | None) -> None: ...
    @property
    def cache_expires(self) -> _ResponseCacheExpires: ...
    @cache_expires.setter
    def cache_expires(self, value: timedelta | int | bool | None) -> None: ...
    def encode_content(self, encoding: Literal["gzip", "identity"] = ..., lazy: bool = ...) -> None: ...
    def decode_content(self) -> None: ...
    def md5_etag(self, body: bytes | None = ..., set_content_md5: bool = ...) -> None: ...
    def __call__(self, environ: dict[str, Any], start_response: _StartResponse) -> Iterator[bytes]: ...
    def conditional_response_app(self, environ: dict[str, Any], start_response: _StartResponse) -> Iterator[bytes]: ...
    def app_iter_range(self, start: int, stop: int | None) -> AppIterRange: ...

class ResponseBodyFile:
    mode: Literal["wb"] = "wb"
    closed: Literal[False] = False
    response: Response
    def __init__(self, response: Response): ...
    @property
    def encoding(self) -> str | None: ...
    def write(self, text: str | bytes) -> int: ...
    def writelines(self, seq: Sequence[str | bytes]) -> int: ...
    def close(self) -> NoReturn: ...
    def flush(self) -> None: ...
    def tell(self) -> int: ...

class AppIterRange:
    app_iter: Iterator[bytes]
    start: int
    stop: int | None
    def __init__(self, app_iter: Iterator[bytes], start: int, stop: int | None) -> None: ...
    def __iter__(self) -> Iterator[bytes]: ...
    def next(self) -> bytes: ...
    __next__ = next
    def close(self) -> None: ...

class EmptyResponse:
    def __init__(self, app_iter: Iterator[bytes] | None = ...) -> None: ...
    def __iter__(self) -> Iterator[bytes]: ...
    def __len__(self) -> int: ...
    def next(self) -> NoReturn: ...
    __next__ = next
