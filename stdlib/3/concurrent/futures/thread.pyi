# Stubs for concurrent.futures.thread (Python 3.5)
#

from typing import Any, TypeVar, Callable, Iterable
from ._base import Executor, Future

_T = TypeVar('_T')

class ThreadPoolExecutor(Executor):
    def __init__(self, max_workers: int = None) -> None: ...
    def submit(self, fn: Callable[..., _T], *args: Any, **kwargs: Any) -> Future[_T]: ...
    def map(self, func: Callable[..., _T], *iterables: Any, timeout: float = None, chunksize:int = 1) -> Iterable[_T]: ...
    def shutdown(self, wait: bool = True) -> None: ...

