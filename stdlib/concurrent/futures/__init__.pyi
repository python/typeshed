import sys

from ._base import (
    ALL_COMPLETED as ALL_COMPLETED,
    FIRST_COMPLETED as FIRST_COMPLETED,
    FIRST_EXCEPTION as FIRST_EXCEPTION,
    BrokenExecutor as BrokenExecutor,
    CancelledError as CancelledError,
    Executor as Executor,
    Future as Future,
    InvalidStateError as InvalidStateError,
    TimeoutError as TimeoutError,
    as_completed as as_completed,
    wait as wait,
)
from .process import ProcessPoolExecutor as ProcessPoolExecutor
from .thread import ThreadPoolExecutor as ThreadPoolExecutor

if sys.version_info >= (3, 13):
    __all__ = (
        "ALL_COMPLETED",
        "FIRST_COMPLETED",
        "FIRST_EXCEPTION",
        "BrokenExecutor",
        "CancelledError",
        "Executor",
        "Future",
        "InvalidStateError",
        "ProcessPoolExecutor",
        "ThreadPoolExecutor",
        "TimeoutError",
        "as_completed",
        "wait",
    )
else:
    __all__ = (
        "ALL_COMPLETED",
        "FIRST_COMPLETED",
        "FIRST_EXCEPTION",
        "BrokenExecutor",
        "CancelledError",
        "Executor",
        "Future",
        "ProcessPoolExecutor",
        "ThreadPoolExecutor",
        "TimeoutError",
        "as_completed",
        "wait",
    )

def __dir__() -> tuple[str, ...]: ...
