import concurrent.futures
import sys
from typing import (Any, TypeVar, Set, Dict, List, TextIO, Union, Tuple, Generic, Callable,
                    Coroutine, Generator, Iterable, Awaitable, overload, Sequence, Iterator,
                    Optional)
from types import FrameType
from .events import AbstractEventLoop
from .futures import Future

__all__: List[str]

_T = TypeVar('_T')
_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')
_T3 = TypeVar('_T3')
_T4 = TypeVar('_T4')
_T5 = TypeVar('_T5')
_FutureT = Union[Future[_T], Generator[Any, None, _T], Awaitable[_T]]

FIRST_EXCEPTION: str
FIRST_COMPLETED: str
ALL_COMPLETED: str

def as_completed(fs: Sequence[_FutureT[_T]], *, loop: AbstractEventLoop = ...,
                 timeout: Optional[float] = ...) -> Iterator[Future[_T]]: ...
def ensure_future(coro_or_future: _FutureT[_T],
                  *, loop: AbstractEventLoop = ...) -> Future[_T]: ...
# Prior to Python 3.7 'async' was an alias for 'ensure_future'.
# It became a keyword in 3.7.
@overload
def gather(coro_or_future1: _FutureT[_T1],
           *, loop: AbstractEventLoop = ..., return_exceptions: bool = ...) -> Future[Tuple[_T1]]: ...
@overload
def gather(coro_or_future1: _FutureT[_T1], coro_or_future2: _FutureT[_T2],
           *, loop: AbstractEventLoop = ..., return_exceptions: bool = ...) -> Future[Tuple[_T1, _T2]]: ...
@overload
def gather(coro_or_future1: _FutureT[_T1], coro_or_future2: _FutureT[_T2], coro_or_future3: _FutureT[_T3],
           *, loop: AbstractEventLoop = ..., return_exceptions: bool = ...) -> Future[Tuple[_T1, _T2, _T3]]: ...
@overload
def gather(coro_or_future1: _FutureT[_T1], coro_or_future2: _FutureT[_T2], coro_or_future3: _FutureT[_T3],
           coro_or_future4: _FutureT[_T4],
           *, loop: AbstractEventLoop = ..., return_exceptions: bool = ...) -> Future[Tuple[_T1, _T2, _T3, _T4]]: ...
@overload
def gather(coro_or_future1: _FutureT[_T1], coro_or_future2: _FutureT[_T2], coro_or_future3: _FutureT[_T3],
           coro_or_future4: _FutureT[_T4], coro_or_future5: _FutureT[_T5],
           *, loop: AbstractEventLoop = ..., return_exceptions: bool = ...) -> Future[Tuple[_T1, _T2, _T3, _T4, _T5]]: ...
@overload
def gather(coro_or_future1: _FutureT[Any], coro_or_future2: _FutureT[Any], coro_or_future3: _FutureT[Any],
           coro_or_future4: _FutureT[Any], coro_or_future5: _FutureT[Any], coro_or_future6: _FutureT[Any],
           *coros_or_futures: _FutureT[Any],
           loop: AbstractEventLoop = ..., return_exceptions: bool = ...) -> Future[Tuple[Any, ...]]: ...
def run_coroutine_threadsafe(coro: _FutureT[_T],
                             loop: AbstractEventLoop) -> concurrent.futures.Future[_T]: ...
def shield(arg: _FutureT[_T], *, loop: AbstractEventLoop = ...) -> Future[_T]: ...
def sleep(delay: float, result: _T = ..., loop: AbstractEventLoop = ...) -> Future[_T]: ...
def wait(fs: Iterable[_FutureT[_T]], *, loop: AbstractEventLoop = ..., timeout: Optional[float] = ...,
         return_when: str = ...) -> Future[Tuple[Set[Future[_T]], Set[Future[_T]]]]: ...
def wait_for(fut: _FutureT[_T], timeout: Optional[float],
             *, loop: AbstractEventLoop = ...) -> Future[_T]: ...

class Task(Future[_T], Generic[_T]):
    @classmethod
    def current_task(cls, loop: AbstractEventLoop = ...) -> Task: ...
    @classmethod
    def all_tasks(cls, loop: AbstractEventLoop = ...) -> Set[Task]: ...
    def __init__(self, coro: Union[Generator[Any, None, _T], Awaitable[_T]], *, loop: AbstractEventLoop = ...) -> None: ...
    def __repr__(self) -> str: ...
    def get_stack(self, *, limit: int = ...) -> List[FrameType]: ...
    def print_stack(self, *, limit: int = ..., file: TextIO = ...) -> None: ...
    def cancel(self) -> bool: ...
    def _step(self, value: Any = ..., exc: Exception = ...) -> None: ...
    def _wakeup(self, future: Future[Any]) -> None: ...

if sys.version_info >= (3, 7):
    def all_tasks(loop: Optional[AbstractEventLoop] = ...) -> Set[Task]: ...
    def create_task(coro: Union[Generator[Any, None, _T], Awaitable[_T]]) -> Task: ...
    def current_task(loop: Optional[AbstractEventLoop] = ...) -> Optional[Task]: ...
