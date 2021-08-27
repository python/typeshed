import queue
import sys
import threading
import weakref
from collections.abc import Iterable, Mapping, Set
from concurrent.futures import _base
from typing import Any, Callable, Optional, Tuple

_threads_queues: Mapping[Any, Any]
_shutdown: bool
_global_shutdown_lock: threading.Lock

def _python_exit() -> None: ...

if sys.version_info >= (3, 9):
    from types import GenericAlias

class _WorkItem(object):
    future: _base.Future[Any]
    fn: Callable[..., Any]
    args: Iterable[Any]
    kwargs: Mapping[str, Any]
    def __init__(
        self, future: _base.Future[Any], fn: Callable[..., Any], args: Iterable[Any], kwargs: Mapping[str, Any]
    ) -> None: ...
    def run(self) -> None: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...

if sys.version_info >= (3, 7):
    def _worker(
        executor_reference: weakref.ref[Any, Callable],
        work_queue: queue.SimpleQueue[Any],
        initializer: Optional[Callable[..., None]],
        initargs: Tuple[Any, ...],
    ) -> None: ...

else:
    def _worker(
        executor_reference: weakref.ref[Any, Callable],
        work_queue: queue.Queue[Any],
        initializer: Optional[Callable[..., None]],
        initargs: Tuple[Any, ...],
    ) -> None: ...

if sys.version_info >= (3, 7):
    from ._base import BrokenExecutor
    class BrokenThreadPool(BrokenExecutor): ...

class ThreadPoolExecutor(_base.Executor):
    _max_workers: int
    _idle_semaphore: threading.Semaphore
    _threads: Set[threading.Thread]
    _broken: bool
    _shutdown: bool
    _shutdown_lock: threading.Lock
    _thread_name_prefix: Optional[str] = ...
    _initializer: Optional[Callable[..., None]] = ...
    _initargs: Tuple[Any, ...] = ...
    if sys.version_info >= (3, 7):
        _work_queue: queue.SimpleQueue[_WorkItem]
    else:
        _work_queue: queue.Queue[_WorkItem]
    if sys.version_info >= (3, 7):
        def __init__(
            self,
            max_workers: int | None = ...,
            thread_name_prefix: str = ...,
            initializer: Callable[..., None] | None = ...,
            initargs: Tuple[Any, ...] = ...,
        ) -> None: ...
    else:
        def __init__(self, max_workers: int | None = ..., thread_name_prefix: str = ...) -> None: ...
    def _adjust_thread_count(self) -> None: ...
    def _initializer_failed(self) -> None: ...
