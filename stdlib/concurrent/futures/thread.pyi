import multiprocessing.queues as mpq
import sys
import threading
import weakref
from collections.abc import Mapping
from concurrent.futures import _base
from types import TracebackType
from typing import Any, Callable, Iterable, Optional, Sequence, Tuple

_threads_queues: weakref.WeakKeyDictionary
_shutdown: bool
_global_shutdown_lock: threading.Lock

def _python_exit() -> None: ...

if sys.version_info >= (3, 9):
    from types import GenericAlias

class _WorkItem(object):
    future: _base.Future
    fn: Callable
    args: Iterable[Any]
    kwargs: Mapping[str, Any]
    def __init__(self, future: _base.Future, fn: Callable, args: Iterable[Any], kwargs: Mapping[str, Any]) -> None: ...
    def run(self) -> None: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...

def _worker(executor_reference: weakref.ref, work_queue: mpq.Queue[Any], initializer: Callable, initargs: Any) -> None: ...

if sys.version_info >= (3, 7):
    from ._base import BrokenExecutor
    class BrokenThreadPool(BrokenExecutor): ...

class ThreadPoolExecutor(_base.Executor):
    if sys.version_info >= (3, 7):
        _work_queue: mpq.SimpleQueue[_WorkItem]
    else:
        _work_queue: mpq.Queue[_WorkItem]
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
    def submit(self, fn, /, *args, **kwargs) -> _base.Future: ...
    def _adjust_process_count(self) -> None: ...
    def _initializer_failed(self) -> None: ...
    def shutdown(self, wait: bool = ..., *, cancel_futures: bool = ...) -> None: ...
