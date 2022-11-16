from tkinter import Event, Misc
from typing import Any
from collections.abc import Callable, Iterable

MC_KEYPRESS: int
MC_KEYRELEASE: int
MC_BUTTONPRESS: int
MC_BUTTONRELEASE: int
MC_ACTIVATE: int
MC_CIRCULATE: int
MC_COLORMAP: int
MC_CONFIGURE: int
MC_DEACTIVATE: int
MC_DESTROY: int
MC_ENTER: int
MC_EXPOSE: int
MC_FOCUSIN: int
MC_FOCUSOUT: int
MC_GRAVITY: int
MC_LEAVE: int
MC_MAP: int
MC_MOTION: int
MC_MOUSEWHEEL: int
MC_PROPERTY: int
MC_REPARENT: int
MC_UNMAP: int
MC_VISIBILITY: int
MC_SHIFT: int
MC_CONTROL: int
MC_ALT: int
MC_META: int
MC_OPTION: int
MC_COMMAND: int
APPLICATION_GONE: str

class _SimpleBinder:
    type: int
    sequence: str
    widget: Misc
    widgetinst: Misc
    bindedfuncs: list[Callable[[Event[Any]], str | None]]
    handlerid: str | None
    def __init__(self, type: int, widget: Misc, widgetinst: Misc) -> None: ...
    def bind(self, triplet: tuple[int, int, str], func: Callable[[Event[Any]], str | None]) -> None: ...
    def unbind(self, triplet: tuple[int, int, str], func: Callable[[Event[Any]], str | None]) -> None: ...
    def __del__(self) -> None: ...

def expand_substates(states: Iterable[int]) -> list[list[int]]: ...

r: int
s: int

class _ComplexBinder:
    type: int
    typename: str
    widget: Misc
    widgetinst: Misc
    bindedfuncs: dict[str | None, list[list[Callable[[Event[Any]], str | None]]]]
    handlerids: list[tuple[str, str]]
    ishandlerrunning: list[list[bool]]
    doafterhandler: list[Callable[[], Any]]
    def __init__(self, type: int, widget: Misc, widgetinst: Misc) -> None: ...
    def bind(self, triplet: tuple[int, int, str], func: Callable[[Event[Any]], str | None]) -> None: ...
    def unbind(self, triplet: tuple[int, int, str], func: Callable[[Event[Any]], str | None]) -> None: ...
    def __del__(self) -> None: ...

def MultiCallCreator(widget: Misc) -> Misc: ...
