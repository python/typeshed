from typing import Any, ClassVar, Iterable

from .. import exceptions
from ..response import HTTPResponse

ConnectTimeoutError = exceptions.ConnectTimeoutError
MaxRetryError = exceptions.MaxRetryError
ProtocolError = exceptions.ProtocolError
ReadTimeoutError = exceptions.ReadTimeoutError
ResponseError = exceptions.ResponseError

log: Any

class Retry:
    DEFAULT_ALLOWED_METHODS: ClassVar[frozenset[str]]
    RETRY_AFTER_STATUS_CODES: ClassVar[frozenset[int]]
    DEFAULT_REMOVE_HEADERS_ON_REDIRECT: ClassVar[frozenset[str]]
    DEFAULT_BACKOFF_MAX: ClassVar[int]

    total: int
    connect: int
    read: int
    redirect: int
    status: int
    other: int
    status_forcelist: Iterable
    allowed_methods: Iterable
    backoff_factor: float
    raise_on_status: bool
    raise_on_redirect: bool
    history: tuple
    respect_retry_after_header: bool
    remove_headers_on_redirect: Iterable
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
        raise_on_redirect=...,
        raise_on_status=...,
        history=...,
        respect_retry_after_header=...,
        remove_headers_on_redirect=...,
        method_whitelist=...,
    ) -> None: ...
    def new(self, **kw): ...
    @classmethod
    def from_int(cls, retries, redirect=..., default=...): ...
    def get_backoff_time(self): ...
    def sleep(self, response: HTTPResponse | None = ...) -> None: ...
    def is_forced_retry(self, method, status_code): ...
    def is_exhausted(self): ...
    def increment(self, method=..., url=..., response=..., error=..., _pool=..., _stacktrace=...): ...
