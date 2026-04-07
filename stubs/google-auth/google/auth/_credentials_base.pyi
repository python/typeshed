import abc
from _typeshed import Incomplete
from collections.abc import Coroutine
from typing import Any

from google.auth.transport import Request as _TransportRequest

class _BaseCredentials(metaclass=abc.ABCMeta):
    token: Incomplete

    def __init__(self) -> None: ...
    @abc.abstractmethod
    def refresh(self, request: _TransportRequest) -> None | Coroutine[Any, Any, None]: ...
