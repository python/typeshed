import sys
from typing import Optional, Protocol

from tkinter import Event, Misc, Widget
class DndSource(Protocol):
    def dnd_end(self, target: Optional[Widget], event: Optional[Event[Misc]]) -> None: ...
