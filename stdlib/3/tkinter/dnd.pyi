from _typeshed.tkinter import DndSource
from tkinter import Event, Tk
from typing import ClassVar, Optional

class DndHandler:
    root: ClassVar[Optional[Tk]]
    def __init__(self, source: DndSource, event: Event) -> None: ...
    def cancel(self, event: Optional[Event] = ...) -> None: ...
    def finish(self, event: Optional[Event], commit: int = ...) -> None: ...
    def on_motion(self, event: Event) -> None: ...
    def on_release(self, event: Event) -> None: ...

def dnd_start(source, event) -> Optional[DndHandler]: ...
