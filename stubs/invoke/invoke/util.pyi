import threading
from types import TracebackType
from typing import Any, Callable, ContextManager,  NamedTuple, Type
from logging import Logger

LOG_FORMAT: str

def enable_logging() -> None: ...

log: Logger

def task_name_sort_key(name: str) -> tuple[list[str], str]: ...
def cd(where: str) -> ContextManager[None]: ...
def has_fileno(stream) -> bool: ...
def isatty(stream) -> bool: ...
def encode_output(string: str, encoding: str) -> str: ...
def helpline(obj: Callable[..., Any]) -> str | None: ...

class ExceptionHandlingThread(threading.Thread):
    def exception(self) -> ExceptionWrapper | None: ...
    @property
    def is_dead(self) -> bool: ...

class ExceptionWrapper(NamedTuple):
    kwargs: Any
    type: Type[BaseException]
    value: BaseException
    traceback: TracebackType
