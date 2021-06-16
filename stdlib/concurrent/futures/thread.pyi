import queue
import sys
import threading
import weakref
from collections.abc import Generator, Iterable, Mapping, Sequence
from concurrent.futures import _base
from types import TracebackType
from typing import Any, Callable, Generic, Optional, Tuple, TypeVar

_WI = TypeVar["_WI"]

_threads_queues: weakref.WeakKeyDictionary
_shutdown: bool
_global_shutdown_lock: threading.Lock

def _python_exit() -> None: ...

if sys.version_info >= (3, 9):
    from types import GenericAlias

class _WorkItem(Generic[_WI]):
    future: _base.Future[_WI]
    fn: Callable[..., _WI]
    args: Iterable[Any]
    kwargs: Mapping[str, Any]
    def __init__(self, future: _base.Future, fn: Callable, args: Iterable[Any], kwargs: Mapping[str, Any]) -> None: ...
    def run(self) -> None: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...

def _worker(
    executor_reference: weakref.ref,
    work_queue: queue.SimpleQueue[Any],
    initializer: Optional[Callable[..., None]],
    initargs: Tuple[Any, ...],
) -> None: ...

if sys.version_info >= (3, 7):
    from ._base import BrokenExecutor
    class BrokenThreadPool(BrokenExecutor): ...

class ThreadPoolExecutor(_base.Executor):
    _max_workers: int
    _idle_semaphore: threading.Semaphore
    _threads: set
    _broken: bool
    _shutdown: bool
    _shutdown_lock: threading.Lock
    _thread_name_prefix: Optional[str] = ...
    _initializer: Optional[Callable[..., None]] = ...
    _initargs: Tuple[Any, ...] = ...
    if sys.version_info >= (3, 7):
        _work_queue: queue.SimpleQueue[Generic[_WI]]
    else:
        _work_queue: queue.Queue[Generic[_WI]]
    if sys.version_info >= (3, 7):
        def __init__(
            self,
            max_workers: Optional[int] = ...,
            thread_name_prefix: str = ...,
            initializer: Optional[Callable[..., None]] = ...,
            initargs: Tuple[Any, ...] = ...,
        ) -> None: ...
    else:
        def __init__(self, max_workers: Optional[int] = ..., thread_name_prefix: str = ...) -> None: ...
    def _adjust_thread_count(self) -> None: ...
    def _initializer_failed(self) -> None: ...
    def submit(self, fn: Callable, /, *args: Any, **kwargs: Any) -> _base.Future: ...
    def map(self, fn: Callable, *iterables: Any, timeout: float = ..., chunksize: int = ...) -> Sequence[Any]: ...
    def shutdown(self, wait: bool = ..., *, cancel_futures: bool = ...) -> None: ...
