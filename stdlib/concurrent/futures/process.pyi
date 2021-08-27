import multiprocessing as mp
import multiprocessing.connection as mpconn
import multiprocessing.context as mpcont
import multiprocessing.queues as mpq
import sys
import threading
import weakref
from collections.abc import Generator, Iterable, Mapping, MutableMapping, MutableSequence
from concurrent.futures import _base
from types import TracebackType
from typing import Any, Callable, Optional, Tuple, Union

_threads_wakeups: Mapping[Any, Any]
_global_shutdown: bool

class _ThreadWakeup:
    _closed: bool
    _reader: mpconn.Connection
    _writer: mpconn.Connection
    def __init__(self) -> None: ...
    def close(self) -> None: ...
    def wakeup(self) -> None: ...
    def clear(self) -> None: ...

def _python_exit() -> None: ...

EXTRA_QUEUED_CALLS: int

_MAX_WINDOWS_WORKERS: int

class _RemoteTraceback(Exception):
    tb: str
    def __init__(self, tb: TracebackType) -> None: ...
    def __str__(self) -> str: ...

class _ExceptionWithTraceback:
    exc: BaseException
    tb: TracebackType
    def __init__(self, exc: BaseException, tb: TracebackType) -> None: ...
    def __reduce__(self) -> Union[str, Tuple[Any, ...]]: ...

def _rebuild_exc(exc: Exception, tb: str) -> Exception: ...

class _WorkItem(object):
    future: _base.Future[Any]
    fn: Callable[..., Any]
    args: Iterable[Any]
    kwargs: Mapping[str, Any]
    def __init__(self, future: _base.Future[Any], fn: Callable[..., Any], args: Iterable[Any], kwargs: Mapping[str, Any]) -> None: ...

class _ResultItem(object):
    work_id: int
    exception: Exception
    result: Any
    def __init__(self, work_id: int, exception: Optional[Exception] = ..., result: Optional[Any] = ...) -> None: ...

class _CallItem(object):
    work_id: int
    fn: Callable[..., Any]
    args: Iterable[Any]
    kwargs: Mapping[str, Any]
    def __init__(self, work_id: int, fn: Callable[..., Any], args: Iterable[Any], kwargs: Mapping[str, Any]) -> None: ...

class _SafeQueue(mpq.Queue):
    pending_work_items: MutableMapping[int, _WorkItem]
    shutdown_lock: threading.Lock
    thread_wakeup: _ThreadWakeup
    def __init__(
        self,
        max_size: Optional[int] = ...,
        *,
        ctx: mpcont.BaseContext,
        pending_work_items: MutableMapping[int, _WorkItem],
        shutdown_lock: threading.Lock,
        thread_wakeup: _ThreadWakeup,
    ) -> None: ...
    def _on_queue_feeder_error(self, e: Exception, obj: _CallItem) -> None: ...

def _get_chunks(*iterables: Any, chunksize: int) -> Generator[Tuple[Any], None, None]: ...
def _process_chunk(fn: Callable[..., Any], chunk: Tuple[Any, None, None]) -> Generator[Any, None, None]: ...
def _sendback_result(
    result_queue: mpq.SimpleQueue[_WorkItem], work_id: int, result: Optional[Any] = ..., exception: Optional[Exception] = ...
) -> None: ...
def _process_worker(
    call_queue: mpq.Queue[_CallItem],
    result_queue: mpq.SimpleQueue[_ResultItem],
    initializer: Optional[Callable[..., None]],
    initargs: Tuple[Any, ...],
) -> None: ...

class _ExecutorManagerThread(threading.Thread):
    thread_wakeup: _ThreadWakeup
    shutdown_lock: threading.Lock
    executor_reference: weakref.ref[Any, Callable]
    processes: MutableMapping[int, mpcont.Process]
    call_queue: mpq.Queue[_CallItem]
    result_queue: mpq.SimpleQueue[_ResultItem]
    work_ids_queue: mpq.Queue[int]
    pending_work_items: MutableMapping[int, _WorkItem]
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
def _chain_from_iterable_of_lists(iterable: Iterable[MutableSequence[Any]]) -> Any: ...

if sys.version_info >= (3, 7):
    from ._base import BrokenExecutor
    class BrokenProcessPool(BrokenExecutor): ...

else:
    class BrokenProcessPool(RuntimeError): ...

class ProcessPoolExecutor(_base.Executor):
    _mp_context: Optional[mpcont.BaseContext]
    _initializer: Optional[Callable[..., None]] = ...
    _initargs: Tuple[Any, ...] = ...
    _executor_manager_thread: _ThreadWakeup
    _processes: MutableMapping[int, mpcont.Process]
    _shutdown_thread: bool
    _shutdown_lock: threading.Lock
    _idle_worker_semaphore: threading.Semaphore
    _broken: bool
    _queue_count: int
    _pending_work_items: MutableMapping[int, _WorkItem]
    _cancel_pending_futures: bool
    _executor_manager_thread_wakeup: _ThreadWakeup
    _result_queue: mpq.SimpleQueue[Any]
    _work_ids: mpq.Queue[Any]
    if sys.version_info >= (3, 7):
        def __init__(
            self,
            max_workers: int | None = ...,
            mp_context: mpcont.BaseContext | None = ...,
            initializer: Callable[..., None] | None = ...,
            initargs: Tuple[Any, ...] = ...,
        ) -> None: ...
    else:
        def __init__(self, max_workers: int | None = ...) -> None: ...
    def _start_executor_manager_thread(self) -> None: ...
    def _adjust_process_count(self) -> None: ...
