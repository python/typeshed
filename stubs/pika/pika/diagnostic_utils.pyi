from collections.abc import Callable
from logging import Logger
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])  # exists at runtime

def create_log_exception_decorator(logger: Logger) -> Callable[[F], F]: ...
