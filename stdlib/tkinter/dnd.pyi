import sys
from tkinter import Event, Misc, Tk, Widget
from typing import ClassVar, Protocol

if sys.version_info >= (3, 9):
    __all__ = ["dnd_start", "DndHandler"]

class _DndSource(Protocol):
    def dnd_end(self, target: Widget | None, event: Event[Misc] | None) -> None: ...

class DndHandler:
    root: ClassVar[Tk | None]
    def __init__(self, source: _DndSource, event: Event[Misc]) -> None: ...
    def cancel(self, event: Event[Misc] | None = ...) -> None: ...
    def finish(self, event: Event[Misc] | None, commit: int = ...) -> None: ...
    def on_motion(self, event: Event[Misc]) -> None: ...
    def on_release(self, event: Event[Misc]) -> None: ...

def dnd_start(source, event) -> DndHandler | None: ...
