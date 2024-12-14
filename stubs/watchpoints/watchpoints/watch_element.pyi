import ast
from collections.abc import Callable, Iterable
from types import FrameType
from typing import Any, Literal, TypeVar
from typing_extensions import TypeAlias

from .watch_print import WatchPrint

_T = TypeVar("_T")
_TrackKind: TypeAlias = Literal["object", "variable"] | list[Literal["object", "variable"]]

class WatchElement:
    alias: str | None
    attr: str | None
    cmp: Callable[[Any, Any], bool] | None
    copy: Callable[[Any], object] | None
    default_alias: str | None
    deepcopy: bool
    exist: bool
    frame: FrameType
    localvar: str | None
    obj: Any
    parent: Any
    prev_obj: Any
    prev_obj_repr: str
    subscr: Any
    watch_print: WatchPrint
    when: Callable[[Any], bool] | None

    def __init__(
        self,
        frame: FrameType,
        node: ast.expr,
        *,
        alias: str | None = ...,
        callback: Callable[[FrameType, WatchElement, tuple[str, str, int | None]], None] | None = ...,
        cmp: Callable[[Any, Any], bool] | None = ...,
        copy: Callable[[_T], _T] | None = ...,
        deepcopy: bool = False,
        default_alias: str | None = ...,
        track: _TrackKind = ...,
        watch_print: WatchPrint = ...,
        when: Callable[[Any], bool] | None = ...,
    ) -> None: ...
    def belong_to(self, lst: Iterable[Any]) -> bool: ...
    def changed(self, frame: FrameType) -> tuple[bool, bool]: ...
    def obj_changed(self, other: Any) -> bool: ...
    def same(self, other: Any) -> bool: ...
    @property
    def track(self) -> _TrackKind: ...
    @track.setter
    def track(self, val: _TrackKind) -> None: ...
    def update(self) -> None: ...
