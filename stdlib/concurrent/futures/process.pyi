import multiprocessing as mp
import multiprocessing.connection
import multiprocessing.queues as mpq
import sys
import threading
import weakref
from collections.abc import Mapping
from concurrent.futures import _base
from types import TracebackType
from typing import Any, Callable, Iterable, Optional, Sequence, Tuple

_threads_wakeups: weakref.WeakKeyDictionary
_global_shutdown: bool

class _ThreadWakeup:
    _closed: bool
    _reader: multiprocessing.connection.PipeConnection
    _writer: multiprocessing.connection.PipeConnection
    def __init__(self) -> None: ...
    def close(self) -> None: ...
    def wakeup(self) -> None: ...
    def clear(self) -> None: ...

def _python_exit() -> None: ...

EXTRA_QUEUED_CALLS: int

_MAX_WINDOWS_WORKERS: int

class _RemoteTraceback(Exception):
    def __init__(self, tb: TracebackType) -> None: ...
    tb: TracebackType
    def __str__(self) -> str: ...

class _ExceptionWithTraceback:
    exc: BaseException
    tb: TracebackType
    def __init__(self, exc: BaseException, tb: TracebackType) -> None: ...
    def __reduce__(self) -> tuple: ...

def _rebuild_exc(exc, tb) -> Exception: ...

class _WorkItem(object):
    future: _base.Future
    fn: Callable
    args: Iterable[Any]
    kwargs: Mapping[str, Any]
    def __init__(self, future: _base.Future, fn: Callable, args: Iterable[Any], kwargs: Mapping[str, Any]) -> None: ...

class _ResultItem(object):
    work_id: int
    exception: Exception
    result: Any
    def __init__(self, work_id: int, exception: Optional[Exception], result: Optional[Any] = ...) -> None: ...

class _CallItem(object):
    work_id: int
    fn: Callable
    args: Tuple[Any, ...]
    kwargs: Mapping[str, Any]
    def __init__(
        self, work_id: int, fn: Callable = ..., args: Tuple[Any, ...] = ..., kwargs: Mapping[str, Any] = ...
    ) -> None: ...

class _SafeQueue(mpq.Queue):
    pending_work_items: dict[int, _WorkItem]
    shutdown_lock: threading.Lock
    thread_wakeup: _ThreadWakeup
    def __init__(
        self,
        max_size: Optional[int] = ...,
        *,
        ctx: mp.context.SpawnContext,
        pending_work_items: dict[int, _WorkItem],
        shutdown_lock: threading.Lock,
        thread_wakeup: _ThreadWakeup,
    ) -> None: ...
    def _on_queue_feeder_error(self, e, obj) -> None: ...

def _get_chunks(*iterables: Any, chunksize: int) -> tuple: ...
def _process_chunk(fn: Callable = ..., chunk: tuple = ...) -> Sequence: ...
def _sendback_result(
    result_queue: mpq.Queue[_ResultItem], work_id: int, result: Optional[Any] = ..., exception: Optional[Exception] = ...
) -> None: ...
def _process_worker(
    call_queue: mpq.Queue[_CallItem], result_queue: mpq.Queue[_ResultItem], initializer: Callable, initargs: Any
) -> None: ...

class _ExecutorManagerThread(threading.Thread):
    thread_wakeup: _ThreadWakeup
    shutdown_lock: threading.Lock
    executor_reference: weakref.ref
    processes: Mapping
    call_queue: mpq.Queue[_CallItem]
    result_queue: mpq.Queue[_ResultItem]
    work_ids_queue: mpq.Queue[int]
    pending_work_items: dict[int, _WorkItem]
    def __init__(self, executor: ProcessPoolExecutor) -> None: ...
    def run(self) -> None: ...
    def add_call_item_to_queue(self) -> None: ...
    def wait_result_broken_or_wakeup(self) -> tuple[Any, bool, str]: ...
    def process_result_item(self, result_item: Any) -> None: ...
    def is_shutting_down(self) -> bool: ...
    def terminate_broken(self, cause: str) -> None: ...
    def flag_executor_shutting_down(self) -> None: ...
    def shutdown_workers(self) -> None: ...
    def join_executor_internals(self) -> None: ...
    def get_n_children_alive(self) -> int: ...

_system_limits_checked: bool
_system_limited: Optional[bool]

def _check_system_limits() -> None: ...
def _chain_from_iterable_of_lists(iterable: Sequence) -> Any: ...

if sys.version_info >= (3, 7):
    from ._base import BrokenExecutor
    class BrokenProcessPool(BrokenExecutor): ...

else:
    class BrokenProcessPool(RuntimeError): ...

if sys.version_info >= (3, 7):
    from multiprocessing.context import BaseContext
    class ProcessPoolExecutor(_base.Executor):
        _shutdown_thread: bool
        _shutdown_lock: threading.Lock
        _idle_worker_semaphore: threading.Semaphore
        _broken: bool
        _queue_count: int
        _pending_work_items: dict[int, _WorkItem]
        _cancel_pending_futures: bool
        _executor_manager_thread_wakeup: _ThreadWakeup
        _result_queue = mpq.SimpleQueue
        _work_ids: mpq.Queue
        def __init__(
            self,
            max_workers: Optional[int] = ...,
            mp_context: Optional[BaseContext] = ...,
            initializer: Optional[Callable] = ...,
            initargs: Tuple[Any, ...] = ...,
        ) -> None: ...
        def _start_executor_manager_thread(self) -> None: ...
        def _adjust_process_count(self) -> None: ...
        def submit(self, fn, /, *args, **kwargs) -> _base.Future: ...
        def map(self, fn: Callable, *iterables: Any, timeout: float = ..., chunksize: int = ...) -> Sequence[Any]: ...
        def shutdown(self, wait: bool = ..., *, cancel_futures: bool = ...) -> None: ...

else:
    class ProcessPoolExecutor(_base.Executor):
        def __init__(self, max_workers: Optional[int] = ...) -> None: ...
