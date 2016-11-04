from typing import (Any, TypeVar, Set, Dict, List, TextIO, Union, Tuple, Generic, Callable,
                    Generator, Iterable, Awaitable, overload, Sequence, Iterator, Optional)

__all__ = ... # type: str

from .events import AbstractEventLoop
from .futures import Future

_T = TypeVar('_T')

FIRST_EXCEPTION = 'FIRST_EXCEPTION'
FIRST_COMPLETED = 'FIRST_COMPLETED'
ALL_COMPLETED = 'ALL_COMPLETED'

def as_completed(fs: Sequence[Future[_T]], *, loop: AbstractEventLoop = ...,
                 timeout=None) -> Iterator[Generator[Any, None, _T]]: ...
def ensure_future(coro_or_future: Union[Future[_T], Generator[Any, None, _T]],
                  *, loop: AbstractEventLoop = ...) -> Future[_T]: ...
def gather(*coros_or_futures: Union[Future[_T], Generator[Any, None, _T], Awaitable[_T]],
           loop: AbstractEventLoop = ..., return_exceptions: bool = False) -> Future[List[_T]]: ...
def run_coroutine_threadsafe(coro: Generator[Any, None, _T],
                             loop: AbstractEventLoop) -> Future[_T]: ...
def shield(arg: Union[Future[_T], Generator[Any, None, _T]],
           *, loop: AbstractEventLoop = ...) -> Future[_T]: ...
def sleep(delay: float, result: _T = ..., loop: AbstractEventLoop = ...) -> Future[_T]: ...
def wait(fs: List[Task[_T]], *, loop: AbstractEventLoop = ...,
    timeout: float = ...,
         return_when: str = ...) -> Future[Tuple[Set[Future[_T]], Set[Future[_T]]]]: ...
def wait_for(fut: Union[Future[_T], Generator[Any, None, _T]], timeout: Optional[float],
             *, loop: AbstractEventLoop = ...) -> Future[_T]: ...

class Task(Future[_T], Generic[_T]):
    _all_tasks = ...  # type: Set[Task]
    _current_tasks = ...  # type: Dict[AbstractEventLoop, Task]
    @classmethod
    def current_task(cls, loop: AbstractEventLoop = ...) -> Task: ...
    @classmethod
    def all_tasks(cls, loop: AbstractEventLoop = ...) -> Set[Task]: ...

    # Can't use a union, see mypy issue #1873.
    @overload
    def __init__(self, coro: Generator[Any, None, _T],
                 *, loop: AbstractEventLoop = ...) -> None: ...
    @overload
    def __init__(self, coro: Awaitable[_T], *, loop: AbstractEventLoop = ...) -> None: ...

    def __repr__(self) -> str: ...
    def get_stack(self, *, limit: int = ...) -> List[Any]: ...  # return List[stackframe]
    def print_stack(self, *, limit: int = ..., file: TextIO = ...) -> None: ...
    def cancel(self) -> bool: ...
    def _step(self, value: Any = ..., exc: Exception = ...) -> None: ...
    def _wakeup(self, future: Future[Any]) -> None: ...

