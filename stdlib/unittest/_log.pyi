import logging
from types import TracebackType
from typing import Generic, NamedTuple, TypeVar
from unittest.case import TestCase

_L = TypeVar("_L", None, _LoggingWatcher)

class _LoggingWatcher(NamedTuple):
    records: list[logging.LogRecord]
    output: list[str]

class _AssertLogsContext(Generic[_L]):
    LOGGING_FORMAT: str
    records: list[logging.LogRecord]
    output: list[str]
    if sys.version_info >= (3, 10):
        def __init__(self, test_case: TestCase, logger_name: str, level: int, no_logs: bool) -> None: ...
    else:
        def __init__(self, test_case: TestCase, logger_name: str, level: int) -> None: ...
    def __enter__(self) -> _L: ...
    def __exit__(
        self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> bool | None: ...
