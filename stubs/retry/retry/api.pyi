from _typeshed import FloatInt, IdentityFunction
from collections.abc import Callable, Sequence
from logging import Logger
from typing import Any, TypeVar

_R = TypeVar("_R")

logging_logger: Logger

def retry_call(
    f: Callable[..., _R],
    fargs: Sequence[Any] | None = None,
    fkwargs: dict[str, Any] | None = None,
    exceptions: type[Exception] | tuple[type[Exception], ...] = ...,
    tries: int = -1,
    delay: FloatInt = 0,
    max_delay: FloatInt | None = None,
    backoff: FloatInt = 1,
    jitter: tuple[FloatInt, FloatInt] | FloatInt = 0,
    logger: Logger | None = ...,
) -> _R: ...
def retry(
    exceptions: type[Exception] | tuple[type[Exception], ...] = ...,
    tries: int = -1,
    delay: FloatInt = 0,
    max_delay: FloatInt | None = None,
    backoff: FloatInt = 1,
    jitter: tuple[FloatInt, FloatInt] | FloatInt = 0,
    logger: Logger | None = ...,
) -> IdentityFunction: ...
