from typing import Any, ClassVar, Collection

from .. import exceptions
from ..response import HTTPResponse

ConnectTimeoutError = exceptions.ConnectTimeoutError
MaxRetryError = exceptions.MaxRetryError
ProtocolError = exceptions.ProtocolError
ReadTimeoutError = exceptions.ReadTimeoutError
ResponseError = exceptions.ResponseError

log: Any


class RequestHistory:
    method: str | None
    url: str | None
    error: Exception | None
    status: int | None
    redirect_location: str | None


class Retry:
    DEFAULT_ALLOWED_METHODS: ClassVar[frozenset[str]]
    RETRY_AFTER_STATUS_CODES: ClassVar[frozenset[int]]
    DEFAULT_REMOVE_HEADERS_ON_REDIRECT: ClassVar[frozenset[str]]
    DEFAULT_BACKOFF_MAX: ClassVar[int]

    total: bool | int | None
    connect: int | None
    read: int | None
    redirect: bool | int | None
    status: int | None
    other: int | None
    allowed_methods: Collection[str] | None
    status_forcelist: Collection[int] | None
    backoff_factor: float
    backoff_max: float
    raise_on_redirect: bool
    raise_on_status: bool
    history: tuple[RequestHistory, ...] | None
    respect_retry_after_header: bool
    remove_headers_on_redirect: Collection[str]

    def __init__(
        self,
        total=...,
        connect=...,
        read=...,
        redirect=...,
        status=...,
        other=...,
        allowed_methods=...,
        status_forcelist=...,
        backoff_factor=...,
        backoff_max=...,
        raise_on_redirect=...,
        raise_on_status=...,
        history=...,
        respect_retry_after_header=...,
        remove_headers_on_redirect=...,
    ) -> None: ...
    def new(self, **kw): ...
    @classmethod
    def from_int(cls, retries, redirect=..., default=...) -> "Retry": ...
    def get_backoff_time(self) -> float: ...
    def parse_retry_after(self, retry_after: str) -> float: ...
    def get_retry_after(self, response: HTTPResponse) -> float | None: ...
    def sleep_for_retry(self, response: HTTPResponse) -> bool: ...
    def sleep(self, response: HTTPResponse | None = ...) -> None: ...
    def is_retry(self, method: str, status_code: int, has_retry_after: bool) -> bool: ...
    def is_exhausted(self) -> bool: ...
    def increment(self, method=..., url=..., response=..., error=..., _pool=..., _stacktrace=...) -> "Retry": ...
