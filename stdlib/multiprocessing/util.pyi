import threading
from _typeshed import StrOrBytesPath
from collections.abc import Callable, Iterable, Sequence
from itertools import count
from logging import Logger
from typing import Any
from weakref import WeakValueDictionary

from . import process

__all__ = [
    "sub_debug",
    "debug",
    "info",
    "sub_warning",
    "get_logger",
    "log_to_stderr",
    "get_temp_dir",
    "register_after_fork",
    "is_exiting",
    "Finalize",
    "ForkAwareThreadLock",
    "ForkAwareLocal",
    "close_all_fds_except",
    "SUBDEBUG",
    "SUBWARNING",
]

NOTSET: int
SUBDEBUG: int
DEBUG: int
INFO: int
SUBWARNING: int

LOGGER_NAME: str
DEFAULT_LOGGING_FORMAT: str

def sub_debug(msg: object, *args: object) -> None: ...
def debug(msg: object, *args: object) -> None: ...
def info(msg: object, *args: object) -> None: ...
def sub_warning(msg: object, *args: object) -> None: ...
def get_logger() -> Logger: ...
def log_to_stderr(level: int | None = ...) -> Logger: ...
def is_abstract_socket_namespace(address: str | bytes | None) -> bool: ...

abstract_sockets_supported: bool

def get_temp_dir() -> str: ...

_afterfork_registry: WeakValueDictionary[tuple[int, int, Callable[[Any], Any]], object]
_afterfork_counter: count[int]

def _run_after_forkers() -> None: ...
def register_after_fork(obj: object, func: Callable[[Any], Any]) -> None: ...

_finalizer_registry: dict[tuple[int | None, int], Finalize] = ...
_finalizer_counter: count[int] = ...

class Finalize:
    _args: Any
    _kwargs: dict[Any, Any]
    _callback: Callable[[Any], Any]
    _key: tuple[int | None, int]
    _pid: int

    def __init__(
        self,
        obj: object | None,
        callback: Callable[[Any], Any],
        args: Any = ...,
        kwargs: dict[Any, Any] | None = ...,
        exitpriority: int | None = ...,
    ) -> None: ...
    def __call__(
        self,
        wr: Any = ...,
        # Need to bind these locally because the globals can have
        # been cleared at shutdown
        _finalizer_registry: dict[Any, Any] = ...,
        sub_debug=...,
        getpid: Callable[[], int] = ...,
    ) -> Any: ...
    def cancel(self) -> None: ...
    def still_active(self) -> bool: ...

def _run_finalizers(minpriority: Finalize | None = ...) -> None: ...
def is_exiting() -> bool: ...
def _exit_function(
    info: Callable[[object, object], None] = ...,
    debug: Callable[[object, object], None] = ...,
    _run_finalizers: Callable[[Finalize | None], None] = ...,
    active_children: Callable[[], list[process.BaseProcess]] = ...,
    current_process: Callable[[], process.BaseProcess] = ...,
) -> None: ...

class ForkAwareThreadLock:
    acquire: Callable[[bool, float], bool]
    release: Callable[[], None]
    def __init__(self) -> None: ...
    def __enter__(self) -> bool: ...
    def __exit__(self, *args: object) -> None: ...

class ForkAwareLocal(threading.local):
    def __init__(self) -> None: ...

MAXFD: int

def close_all_fds_except(fds: Iterable[int]) -> None: ...
def spawnv_passfds(path: bytes, args: Sequence[str], passfds: Sequence[int]) -> int: ...
