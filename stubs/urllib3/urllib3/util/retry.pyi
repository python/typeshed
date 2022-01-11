from typing import Any, ClassVar, Collection, Optional, Union

from .. import exceptions
from ..response import HTTPResponse

ConnectTimeoutError = exceptions.ConnectTimeoutError
MaxRetryError = exceptions.MaxRetryError
ProtocolError = exceptions.ProtocolError
ReadTimeoutError = exceptions.ReadTimeoutError
ResponseError = exceptions.ResponseError

log: Any


class RequestHistory:
    method: Optional[str]
    url: Optional[str]
    error: Optional[Exception]
    status: Optional[int]
    redirect_location: Optional[str]


class Retry:
    DEFAULT_ALLOWED_METHODS: ClassVar[frozenset[str]]
    RETRY_AFTER_STATUS_CODES: ClassVar[frozenset[int]]
    DEFAULT_REMOVE_HEADERS_ON_REDIRECT: ClassVar[frozenset[str]]
    DEFAULT_BACKOFF_MAX: ClassVar[int]

    total: Optional[Union[bool, int]]
    connect: Optional[int]
    read: Optional[int]
    redirect: Optional[Union[bool, int]]
    status: Optional[int]
    other: Optional[int]
    allowed_methods: Optional[Collection[str]]
    status_forcelist: Optional[Collection[int]]
    backoff_factor: float
    backoff_max: float
    raise_on_redirect: bool
    raise_on_status: bool
    history: Optional[tuple[RequestHistory, ...]]
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
    def get_retry_after(self, response: HTTPResponse) -> Optional[float]: ...
    def sleep_for_retry(self, response: HTTPResponse) -> bool: ...
    def sleep(self, response: HTTPResponse | None = ...) -> None: ...
    def is_retry(self, method: str, status_code: int, has_retry_after: bool) -> bool: ...
    def is_exhausted(self) -> bool: ...
    def increment(self, method=..., url=..., response=..., error=..., _pool=..., _stacktrace=...) -> "Retry": ...
