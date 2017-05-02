# Stubs for contextlib

from typing import (
    Any, Callable, Generator, IO, Iterable, Iterator, Optional, Type,
    Generic, TypeVar,
)
from types import TracebackType
import sys


_T = TypeVar('_T')

if sys.version_info >= (3, 7):
    from typing import AsyncContextManager as AbstractAsyncContextManager

if sys.version_info >= (3, 6):
    from typing import ContextManager as AbstractContextManager
    _ContextManager = AbstractContextManager
else:
    class _ContextManager(Generic[_T]):
        def __enter__(self) -> _T: ...
        def __exit__(self, exc_type: Optional[Type[BaseException]],
                     exc_val: Optional[BaseException],
                     exc_tb: Optional[TracebackType]) -> bool: ...

_ExitFunc = Callable[[Optional[Type[BaseException]],
                      Optional[BaseException],
                      Optional[TracebackType]], bool]
_CM_EF = TypeVar('_CM_EF', _ContextManager, _ExitFunc)

if sys.version_info >= (3, 2):
    class GeneratorContextManager(Generic[_T], _ContextManager[_T]):
        def __call__(self, func: Callable[..., _T]) -> Callable[..., _T]: ...
    def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., GeneratorContextManager[_T]]: ...
else:
    def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., _ContextManager[_T]]: ...

if sys.version_info < (3,):
    def nested(*mgr: _ContextManager[Any]) -> _ContextManager[Iterable[Any]]: ...

class closing(Generic[_T], _ContextManager[_T]):
    def __init__(self, thing: _T) -> None: ...

if sys.version_info >= (3, 4):
    class suppress(_ContextManager[None]):
        def __init__(self, *exceptions: Type[BaseException]) -> None: ...

    class redirect_stdout(_ContextManager[None]):
        def __init__(self, new_target: IO[str]) -> None: ...

if sys.version_info >= (3, 5):
    class redirect_stderr(_ContextManager[None]):
        def __init__(self, new_target: IO[str]) -> None: ...

if sys.version_info >= (3,):
    class ContextDecorator:
        def __call__(self, func: Callable[..., None]) -> Callable[..., _ContextManager[None]]: ...

    class ExitStack(_ContextManager[ExitStack]):
        def __init__(self) -> None: ...
        def enter_context(self, cm: _ContextManager[_T]) -> _T: ...
        def push(self, exit: _CM_EF) -> _CM_EF: ...
        def callback(self, callback: Callable[..., None],
                     *args: Any, **kwds: Any) -> Callable[..., None]: ...
        def pop_all(self) -> ExitStack: ...
        def close(self) -> None: ...
