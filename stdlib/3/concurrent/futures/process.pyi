# Stubs for concurrent.futures.process (Python 3.5)
#

from typing import Any, Callable, TypeVar, Iterable
from ._base import Future, Executor

EXTRA_QUEUED_CALLS = ... # type: Any

class BrokenProcessPool(RuntimeError): ...

_T = TypeVar('_T')

class ProcessPoolExecutor(Executor):
    def __init__(self, max_workers: int = None) -> None: ...
    def submit(self, fn: Callable[..., _T], *args: Any, **kwargs: Any) -> Future[_T]: ...
    def map(self, func: Callable[..., _T], *iterables: Any, timeout: float = None, chunksize:int = 1) -> Iterable[_T]: ...
    def shutdown(self, wait: bool = True) -> None: ...

