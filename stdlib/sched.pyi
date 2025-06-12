import sys
from collections.abc import Callable, Mapping
from typing import Any, ClassVar, Generic, NamedTuple, TypeVar, overload, type_check_only
from typing_extensions import Never, TypeAlias, TypeVarTuple, Unpack

__all__ = ["scheduler"]

_KwargValue = TypeVar("_KwargValue")
_R = TypeVar("_R")
_Args = TypeVarTuple("_Args")

class _MyCallable(Generic[Unpack[_Args], _KwargValue, _R]):
    def __call__(self, args: tuple[Unpack[_Args]], kwargs: Mapping[str, _KwargValue]) -> _R: ...

_ActionCallback: TypeAlias = Callable[..., Any]

if sys.version_info >= (3, 10):
    class Event(NamedTuple):
        time: float
        priority: Any
        sequence: int
        action: _ActionCallback
        argument: tuple[Any, ...]
        kwargs: dict[str, Any]

else:
    @type_check_only
    class _EventBase(NamedTuple):
        time: float
        priority: Any
        action: _ActionCallback
        argument: tuple[Any, ...]
        kwargs: dict[str, Any]

    class Event(_EventBase):
        __hash__: ClassVar[None]  # type: ignore[assignment]

class scheduler:
    timefunc: Callable[[], float]
    delayfunc: Callable[[float], object]

    def __init__(self, timefunc: Callable[[], float] = ..., delayfunc: Callable[[float], object] = ...) -> None: ...
    @overload
    def enterabs(
        self,
        time: float,
        priority: Any,
        action: Callable[[], object],
        argument: tuple[()] = ...,
        kwargs: Mapping[Never, Never] = ...,
    ) -> Event: ...
    @overload
    def enterabs(
        self,
        time: float,
        priority: Any,
        action: _MyCallable[Unpack[_Args], _KwargValue, object],
        argument: tuple[Unpack[_Args]] = ...,
        kwargs: Mapping[str, _KwargValue] = ...,
    ) -> Event: ...
    @overload
    def enter(
        self,
        delay: float,
        priority: Any,
        action: Callable[[], object],
        argument: tuple[()] = ...,
        kwargs: Mapping[Never, Never] = ...,
    ) -> Event: ...
    @overload
    def enter(
        self,
        delay: float,
        priority: Any,
        action: _MyCallable[Unpack[_Args], _KwargValue, object],
        argument: tuple[Unpack[_Args]] = ...,
        kwargs: Mapping[str, _KwargValue] = ...,
    ) -> Event: ...
    def run(self, blocking: bool = True) -> float | None: ...
    def cancel(self, event: Event) -> None: ...
    def empty(self) -> bool: ...
    @property
    def queue(self) -> list[Event]: ...
