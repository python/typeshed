import threading
from _typeshed import Self, StrOrBytesPath
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

_logger: Logger | None = None
_log_to_stderr = False

def sub_debug(msg: object, *args: object) -> None: ...
def debug(msg: object, *args: object) -> None: ...
def info(msg: object, *args: object) -> None: ...
def sub_warning(msg: object, *args: object) -> None: ...
def get_logger() -> Logger: ...
def log_to_stderr(level: int | None = ...) -> Logger: ...
def _platform_supports_abstract_sockets() -> bool: ...
def is_abstract_socket_namespace(address: str | bytes | None) -> bool: ...

abstract_sockets_supported: bool

def _remove_temp_dir(rmtree: Callable[[StrOrBytesPath], None], tempdir: StrOrBytesPath) -> None: ...
def get_temp_dir() -> str: ...

_afterfork_registry: WeakValueDictionary[tuple[int, int, Callable[[Any], Any]], object]
_afterfork_counter: count[int]

def _run_after_forkers() -> None: ...
def register_after_fork(obj: object, func: Callable[[Any], Any]) -> None: ...

_finalizer_registry: dict[tuple[int | None, int], Finalize]
_finalizer_counter: count[int]

class Finalize(object):
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
        kwargs: dict[Any, Any] = ...,
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
    def __repr__(self) -> str: ...

def _run_finalizers(minpriority: Finalize = ...) -> None: ...
def is_exiting() -> bool: ...

_exiting = False

def _exit_function(
    info: Callable[[object, object], None] = ...,
    debug: Callable[[object, object], None] = ...,
    _run_finalizers: Callable[[Finalize], None] = ...,
    active_children: Callable[[], list[process.BaseProcess]] = ...,
    current_process: Callable[[], process.BaseProcess] = ...,
) -> None: ...

class ForkAwareThreadLock(object):
    _lock: threading.Lock
    acquire: Callable[[bool, float], bool]
    release: Callable[[], None]
    def __init__(self) -> None: ...
    def _at_fork_reinit(self) -> None: ...
    def __enter__(self) -> bool: ...
    def __exit__(self, *args) -> None: ...

class ForkAwareLocal(threading.local):
    def __init__(self) -> None: ...
    def __reduce__(self: Self) -> tuple[type[Self], tuple[()]]: ...

MAXFD: int

def close_all_fds_except(fds: Iterable[int]) -> None: ...
def _close_stdin() -> None: ...
def _flush_std_streams() -> None: ...
def spawnv_passfds(path: bytes, args: Sequence[str], passfds: Sequence[int]) -> int: ...
def close_fds(*fds: Iterable[int]) -> None: ...
def _cleanup_tests() -> None: ...
