# Stubs for multiprocessing

from typing import (
    Any, Callable, ContextManager, Iterable, Mapping, Optional, Dict, List,
    Union, TypeVar, Sequence, Tuple
)

from logging import Logger
from multiprocessing import pool, synchronize
from multiprocessing.context import BaseContext
from multiprocessing.managers import SyncManager
from multiprocessing.process import current_process as current_process
import queue
import sys

_T = TypeVar('_T')

# N.B. The functions below are generated at runtime by partially applying
# multiprocessing.context.BaseContext's methods, so the two signatures should
# be identical (modulo self).

# Sychronization primitives
_LockLike = Union[synchronize.Lock, synchronize.RLock]
def Barrier(parties: int,
            action: Optional[Callable] = ...,
            timeout: Optional[float] = ...) -> synchronize.Barrier: ...
def BoundedSemaphore(value: int = ...) -> synchronize.BoundedSemaphore: ...
def Condition(lock: Optional[_LockLike] = ...) -> synchronize.Condition: ...
def Event(lock: Optional[_LockLike] = ...) -> synchronize.Event: ...
def Lock() -> synchronize.Lock: ...
def RLock() -> synchronize.RLock: ...
def Semaphore(value: int = ...) -> synchronize.Semaphore: ...

class Connection:
    def close(self) -> None: ...
    def fileno(self) -> int: ...
    def poll(self, timeout: float = ...) -> bool: ...
    def recv(self) -> Any: ...
    def recv_bytes(self, maxlength: int = ...) -> bytes: ...
    def recv_bytes_into(self, buf: Any, offset: int = ...) -> int: ...
    def send(self, obj: Any) -> None: ...
    def send_bytes(self,
                   buf: Any,  # this should be a "byte-like type"
                   offset: int = ...,
                   size: int = ...) -> None: ...

def Pipe(duplex: bool = ...) -> Tuple[Connection, Connection]: ...

def Pool(processes: Optional[int] = ...,
         initializer: Optional[Callable[..., Any]] = ...,
         initargs: Iterable[Any] = ...,
         maxtasksperchild: Optional[int] = ...) -> pool.Pool: ...

class Process():
    name: str
    daemon: bool
    pid: Optional[int]
    exitcode: Optional[int]
    authkey: bytes
    sentinel: int
    # TODO: set type of group to None
    def __init__(self,
                 group: Any = ...,
                 target: Optional[Callable] = ...,
                 name: Optional[str] = ...,
                 args: Iterable[Any] = ...,
                 kwargs: Mapping[Any, Any] = ...,
                 *,
                 daemon: Optional[bool] = ...) -> None: ...
    def start(self) -> None: ...
    def run(self) -> None: ...
    def terminate(self) -> None: ...
    def is_alive(self) -> bool: ...
    def join(self, timeout: Optional[float] = ...) -> None: ...

class Queue(queue.Queue[_T]):
    def __init__(self, maxsize: int = ...) -> None: ...
    def get(self, block: bool = ..., timeout: Optional[float] = ...) -> _T: ...
    def put(self, item: _T, block: bool = ..., timeout: Optional[float] = ...) -> None: ...
    def qsize(self) -> int: ...
    def empty(self) -> bool: ...
    def full(self) -> bool: ...
    def put_nowait(self, item: _T) -> None: ...
    def get_nowait(self) -> _T: ...
    def close(self) -> None: ...
    def join_thread(self) -> None: ...
    def cancel_join_thread(self) -> None: ...

class Value():
    value: Any = ...
    def __init__(self, typecode_or_type: str, *args: Any, lock: bool = ...) -> None: ...

class Array():
    def __init__(self,
                 typecode_or_type: str,
                 size_or_intializer: Union[int, Sequence[Any]],
                 *args: Any,
                 lock: bool = ...) -> None: ...

# ----- multiprocessing function stubs -----
def active_children() -> List[Process]: ...
def allow_connection_pickling() -> None: ...
def cpu_count() -> int: ...
def freeze_support() -> None: ...
def get_logger() -> Logger: ...
def log_to_stderr(level: Optional[Union[str, int]] = ...) -> Logger: ...
def Manager() -> SyncManager: ...
def set_forkserver_preload(module_names: List[str]) -> None: ...
if sys.platform == 'win32' or sys.version_info >= (3, 4):
    def set_executable(executable: str) -> None: ...
if sys.version_info >= (3, 4):
    def get_all_start_methods() -> List[str]: ...
    def get_context(method: Optional[str] = ...) -> BaseContext: ...
    def get_start_method(allow_none: Optional[bool]) -> Optional[str]: ...
    def set_start_method(method: str, force: Optional[bool] = ...) -> None: ...
