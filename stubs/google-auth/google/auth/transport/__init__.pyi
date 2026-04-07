import abc
from collections.abc import Mapping, Sequence
from typing import Any

DEFAULT_RETRYABLE_STATUS_CODES: Sequence[int]
DEFAULT_REFRESH_STATUS_CODES: Sequence[int]
DEFAULT_MAX_REFRESH_ATTEMPTS: int

class Response(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def status(self) -> int: ...
    @property
    @abc.abstractmethod
    def headers(self) -> Mapping[str, str]: ...
    @property
    @abc.abstractmethod
    def data(self) -> bytes: ...

class Request(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __call__(
        self,
        url: str,
        method: str = "GET",
        body: bytes | None = None,
        headers: Mapping[str, str] | None = None,
        timeout: float | None = None,
        **kwargs: Any,
    ) -> Response: ...
