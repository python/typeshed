# Stubs for contextlib

from typing import (
    Any, Callable, Generator, IO, Iterable, Iterator, Optional, Type,
    Generic, TypeVar,
)
from types import TracebackType
import sys
if sys.version_info >= (3, 7):
    from typing import AsyncIterator


_T = TypeVar('_T')

if sys.version_info >= (3, 7):
    from typing import AsyncContextManager as AbstractAsyncContextManager

from typing import ContextManager as AbstractContextManager
# Aliased here for backwards compatibility; TODO eventually remove this
ContextManager = AbstractContextManager

_ExitFunc = Callable[[Optional[Type[BaseException]],
                      Optional[BaseException],
                      Optional[TracebackType]], bool]
_CM_EF = TypeVar('_CM_EF', AbstractContextManager, _ExitFunc)

if sys.version_info >= (3, 2):
    class GeneratorContextManager(Generic[_T], AbstractContextManager[_T]):
        def __call__(self, func: Callable[..., _T]) -> Callable[..., _T]: ...
    def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., GeneratorContextManager[_T]]: ...
else:
    def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., AbstractContextManager[_T]]: ...

if sys.version_info >= (3, 7):
    def asynccontextmanager(func: Callable[..., AsyncIterator[_T]]) -> Callable[..., AbstractAsyncContextManager[_T]]: ...

if sys.version_info < (3,):
    def nested(*mgr: AbstractContextManager[Any]) -> AbstractContextManager[Iterable[Any]]: ...

class closing(Generic[_T], AbstractContextManager[_T]):
    def __init__(self, thing: _T) -> None: ...

if sys.version_info >= (3, 4):
    class suppress(AbstractContextManager[None]):
        def __init__(self, *exceptions: Type[BaseException]) -> None: ...

    class redirect_stdout(AbstractContextManager[None]):
        def __init__(self, new_target: IO[str]) -> None: ...

if sys.version_info >= (3, 5):
    class redirect_stderr(AbstractContextManager[None]):
        def __init__(self, new_target: IO[str]) -> None: ...

if sys.version_info >= (3,):
    class ContextDecorator:
        def __call__(self, func: Callable[..., None]) -> Callable[..., AbstractContextManager[None]]: ...

    class ExitStack(AbstractContextManager[ExitStack]):
        def __init__(self) -> None: ...
        def enter_context(self, cm: AbstractContextManager[_T]) -> _T: ...
        def push(self, exit: _CM_EF) -> _CM_EF: ...
        def callback(self, callback: Callable[..., None],
                     *args: Any, **kwds: Any) -> Callable[..., None]: ...
        def pop_all(self) -> ExitStack: ...
        def close(self) -> None: ...
