from typing import Any, ClassVar

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

    total: Any
    connect: Any
    read: Any
    redirect: Any
    status: Any
    other: Any
    allowed_methods: Any
    status_forcelist: Any
    backoff_factor: Any
    raise_on_redirect: Any
    raise_on_status: Any
    history: Any
    respect_retry_after_header: Any
    remove_headers_on_redirect: Any
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
    def parse_retry_after(self, retry_after: str): ...
    def get_retry_after(self, response: HTTPResponse): ...
    def sleep_for_retry(self, response: HTTPResponse | None = ...): ...
    def sleep(self, response: HTTPResponse | None = ...): ...
    def is_retry(self, method: str, status_code: int, has_retry_after: bool = ...): ...
    def is_exhausted(self): ...
    def increment(self, method=..., url=..., response=..., error=..., _pool=..., _stacktrace=...): ...
