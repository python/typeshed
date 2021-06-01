from _typeshed.tkinter import DndSource
from tkinter import Event, Misc, Tk
from typing import ClassVar

class DndHandler:
    root: ClassVar[Tk | None]
    def __init__(self, source: DndSource, event: Event[Misc]) -> None: ...
    def cancel(self, event: Event[Misc] | None = ...) -> None: ...
    def finish(self, event: Event[Misc] | None, commit: int = ...) -> None: ...
    def on_motion(self, event: Event[Misc]) -> None: ...
    def on_release(self, event: Event[Misc]) -> None: ...

def dnd_start(source, event) -> DndHandler | None: ...
