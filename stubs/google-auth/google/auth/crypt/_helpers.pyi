import abc
from typing import Any

_DEFAULT_TIMEOUT: int = 120  # in seconds

class _BaseAuthorizedSession(metaclass=abc.ABCMeta):

    credentials: Any

    def __init__(self, credentials: Any) -> None: ...
    @abc.abstractmethod
    def request(
        self,
        method: str,
        url: str,
        data: Any = None,
        headers: Any = None,
        max_allowed_time: Any = None,
        timeout: int = ...,
        **kwargs: Any,
    ) -> Any: ...
    @abc.abstractmethod
    def close(self) -> None: ...
