from collections.abc import Callable
from contextvars import Context
from types import FrameType, TracebackType
from typing import Any, overload
from typing_extensions import Literal, TypeAlias

_TraceEvent: TypeAlias = Literal["switch", "throw"]
_TraceCallback: TypeAlias = Callable[[_TraceEvent, tuple[greenlet, greenlet]], object]

CLOCKS_PER_SEC: int
GREENLET_USE_CONTEXT_VARS: bool
GREENLET_USE_GC: bool
GREENLET_USE_STANDARD_THREADING: bool
GREENLET_USE_TRACING: bool
# this is a PyCapsule, it may be used to pass the gevent C-API to another C-extension
# there isn't a runtime type for this, since it's only an opaque wrapper around void*
# but it's probably still better than pretending it doesn't exist, so people that need
# to pass this around, can still pass it around without having to ignore type errors...
_C_API: object

class GreenletExit(BaseException): ...
class error(Exception): ...

class greenlet:
    @property
    def _stack_saved(self) -> int: ...
    @property
    def dead(self) -> bool: ...
    @property
    def gr_context(self) -> Context | None: ...
    @gr_context.setter
    def gr_context(self, value: Context | None) -> None: ...
    @property
    def gr_frame(self) -> FrameType | None: ...
    @property
    def parent(self) -> greenlet | None: ...
    @parent.setter
    def parent(self, value: greenlet | None) -> None: ...
    @property
    def run(self) -> Callable[..., Any]: ...
    @run.setter
    def run(self, value: Callable[..., Any]) -> None: ...
    def __init__(self, run: Callable[..., Any] | None, parent: greenlet | None) -> None: ...
    def switch(self, *args: Any, **kwargs: Any) -> Any: ...
    @overload
    def throw(
        self, __typ: type[BaseException] = ..., __val: BaseException | object = None, __tb: TracebackType | None = None
    ) -> Any: ...
    @overload
    def throw(self, __typ: BaseException = ..., __val: None = None, __tb: TracebackType | None = None) -> Any: ...
    def __bool__(self) -> bool: ...

    # aliases for some module attributes/methods
    GreenletExit: type[GreenletExit]
    error: type[error]
    @staticmethod
    def getcurrent() -> greenlet: ...
    @staticmethod
    def gettrace() -> _TraceCallback | None: ...
    @staticmethod
    def settrace(callback: _TraceCallback | None) -> _TraceCallback | None: ...

def enable_optional_cleanup(__enabled: bool) -> None: ...
def get_clocks_used_doing_optional_cleanup() -> int: ...
def get_pending_cleanup_count() -> int: ...
def get_total_main_greenlets() -> int: ...
def get_tstate_trash_delete_nesting() -> int: ...
def getcurrent() -> greenlet: ...
def gettrace() -> _TraceCallback | None: ...
def set_thread_local(key, value) -> None: ...
def settrace(callback: _TraceCallback | None) -> _TraceCallback | None: ...
