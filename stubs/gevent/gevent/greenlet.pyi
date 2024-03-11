import weakref
from collections.abc import Callable, Iterable, Sequence
from types import FrameType, TracebackType
from typing import Any, ClassVar, Generic, TypeVar, overload
from typing_extensions import ParamSpec, Self

import greenlet
from gevent._types import _Loop
from gevent._util import readproperty

_T = TypeVar("_T")
_G = TypeVar("_G", bound=greenlet.greenlet)
_P = ParamSpec("_P")

class Greenlet(greenlet.greenlet, Generic[_P, _T]):
    # we can't use _P.args/_P.kwargs here because pyright will complain
    # mypy doesn't seem to mind though
    args: tuple[Any, ...]
    kwargs: dict[str, Any]
    value: _T | None
    @overload
    def __init__(self: Greenlet[_P, _T], run: Callable[_P, _T], *args: _P.args, **kwargs: _P.kwargs) -> None: ...
    @overload
    def __init__(self: Greenlet[[], None]) -> None: ...
    @readproperty
    def name(self) -> str: ...
    @property
    def minimal_ident(self) -> int: ...
    @property
    def loop(self) -> _Loop: ...
    @property
    def dead(self) -> bool: ...
    @property
    def started(self) -> bool: ...
    @property
    def exception(self) -> BaseException | None: ...
    @property
    def exc_info(self) -> tuple[type[BaseException], BaseException, TracebackType | None] | None: ...
    @staticmethod
    def add_spawn_callback(callback: Callable[[Greenlet[..., Any]], object]) -> None: ...
    @staticmethod
    def remove_spawn_callback(callback: Callable[[Greenlet[..., Any]], object]) -> None: ...
    def get(self, block: bool = True, timeout: float | None = None) -> _T: ...
    def has_links(self) -> bool: ...
    def join(self, timeout: float | None = None) -> None: ...
    def kill(
        self, exception: type[BaseException] | BaseException = ..., block: bool = True, timeout: float | None = None
    ) -> None: ...
    def link(self, callback: Callable[[Self], object]) -> None: ...
    def link_exception(self, callback: Callable[[Self], object]) -> None: ...
    def link_value(self, callback: Callable[[Self], object]) -> None: ...
    def rawlink(self, callback: Callable[[Self], object]) -> None: ...
    def unlink(self, callback: Callable[[Self], Any]) -> None: ...
    def unlink_all(self) -> None: ...
    def ready(self) -> bool: ...
    def run(self) -> Any: ...
    @overload
    @classmethod
    def spawn(cls, run: Callable[_P, _T], /, *args: _P.args, **kwargs: _P.kwargs) -> Self: ...
    @overload
    @classmethod
    def spawn(cls) -> Greenlet[[], None]: ...
    @overload
    @classmethod
    def spawn_later(cls, seconds: float, run: Callable[_P, _T], *args: _P.args, **kwargs: _P.kwargs) -> Self: ...
    @overload
    @classmethod
    def spawn_later(cls, seconds: float) -> Greenlet[[], None]: ...
    def start(self) -> None: ...
    def start_later(self, seconds: float) -> None: ...
    def successful(self) -> bool: ...
    def __bool__(self) -> bool: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, t: type[BaseException] | None, v: BaseException | None, tb: TracebackType | None) -> None: ...

    # since these are for instrumentation which is disabled by default, we could
    # consider just not annotating them...
    spawning_stack_limit: ClassVar[int]
    spawn_tree_locals: dict[str, Any] | None
    spawning_greenlet: weakref.ref[greenlet.greenlet] | None
    # not quite accurate, since it may be an internal dummy type instead
    # but since it has all the same fields as FrameType we shouldn't care
    spawning_stack: FrameType | None

def joinall(
    greenlets: Sequence[_G], timeout: float | None = None, raise_error: bool = False, count: int | None = None
) -> list[_G]: ...
def killall(
    greenlets: Iterable[greenlet.greenlet],
    exception: type[BaseException] | BaseException = ...,
    block: bool = True,
    timeout: float | None = None,
) -> None: ...
