# Stubs for multiprocessing

import sys
from logging import Logger
from multiprocessing import connection, pool, spawn, synchronize
from multiprocessing.context import (
    AuthenticationError as AuthenticationError,
    BaseContext,
    BufferTooShort as BufferTooShort,
    ProcessError as ProcessError,
    TimeoutError as TimeoutError,
)
from multiprocessing.managers import SyncManager
from multiprocessing.process import current_process as current_process
from multiprocessing.queues import JoinableQueue as JoinableQueue, Queue as Queue, SimpleQueue as SimpleQueue
from multiprocessing.spawn import freeze_support as freeze_support, set_executable as set_executable
from typing import Any, Callable, ContextManager, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union

# N.B. The functions below are generated at runtime by partially applying
# multiprocessing.context.BaseContext's methods, so the two signatures should
# be identical (modulo self).

# Sychronization primitives
_LockLike = Union[synchronize.Lock, synchronize.RLock]

def Barrier(parties: int, action: Optional[Callable] = ..., timeout: Optional[float] = ...) -> synchronize.Barrier: ...
def BoundedSemaphore(value: int = ...) -> synchronize.BoundedSemaphore: ...
def Condition(lock: Optional[_LockLike] = ...) -> synchronize.Condition: ...
def Event(lock: Optional[_LockLike] = ...) -> synchronize.Event: ...
def Lock() -> synchronize.Lock: ...
def RLock() -> synchronize.RLock: ...
def Semaphore(value: int = ...) -> synchronize.Semaphore: ...
def Pipe(duplex: bool = ...) -> Tuple[connection.Connection, connection.Connection]: ...
def Pool(
    processes: Optional[int] = ...,
    initializer: Optional[Callable[..., Any]] = ...,
    initargs: Iterable[Any] = ...,
    maxtasksperchild: Optional[int] = ...,
) -> pool.Pool: ...

class Process:
    name: str
    daemon: bool
    pid: Optional[int]
    exitcode: Optional[int]
    authkey: bytes
    sentinel: int
    # TODO: set type of group to None
    def __init__(
        self,
        group: Any = ...,
        target: Optional[Callable] = ...,
        name: Optional[str] = ...,
        args: Iterable[Any] = ...,
        kwargs: Mapping[Any, Any] = ...,
        *,
        daemon: Optional[bool] = ...
    ) -> None: ...
    def start(self) -> None: ...
    def run(self) -> None: ...
    def terminate(self) -> None: ...
    if sys.version_info >= (3, 7):
        def kill(self) -> None: ...
        def close(self) -> None: ...
    def is_alive(self) -> bool: ...
    def join(self, timeout: Optional[float] = ...) -> None: ...

class Value:
    value: Any = ...
    def __init__(self, typecode_or_type: str, *args: Any, lock: Union[bool, _LockLike] = ...) -> None: ...
    def get_lock(self) -> _LockLike: ...

# ----- multiprocessing function stubs -----
def active_children() -> List[Process]: ...
def allow_connection_pickling() -> None: ...
def cpu_count() -> int: ...
def get_logger() -> Logger: ...
def log_to_stderr(level: Optional[Union[str, int]] = ...) -> Logger: ...
def Manager() -> SyncManager: ...
def set_forkserver_preload(module_names: List[str]) -> None: ...
def get_all_start_methods() -> List[str]: ...
def get_context(method: Optional[str] = ...) -> BaseContext: ...
def get_start_method(allow_none: Optional[bool]) -> Optional[str]: ...
def set_start_method(method: str, force: Optional[bool] = ...) -> None: ...
