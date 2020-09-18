from tkinter import Event, Widget, Misc
from typing import Optional, Protocol

class DndSource(Protocol):
    def dnd_end(self, target: Optional[Widget], event: Optional[Event[Misc]]) -> None: ...
