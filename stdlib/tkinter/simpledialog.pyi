from tkinter import Event, Misc, Toplevel
from typing import Any, List, Optional

class Dialog(Toplevel):
    def __init__(self, parent: Misc | None, title: str | None = ...) -> None: ...
    def body(self, master) -> None: ...
    def buttonbox(self): ...

class SimpleDialog:
    def __init__(
        self,
        master: Misc | None,
        text: str = ...,
        buttons: List[str] = ...,
        default: int | None = ...,
        cancel: int | None = ...,
        title: str | None = ...,
        class_: str | None = ...,
    ) -> None: ...
    def go(self) -> int | None: ...
    def return_event(self, event: Event[Misc]) -> None: ...
    def wm_delete_window(self) -> None: ...
    def done(self, num: int) -> None: ...

def askfloat(title: str | None, prompt: str, **kwargs: Any) -> float: ...
def askinteger(title: str | None, prompt: str, **kwargs: Any) -> int: ...
def askstring(title: str | None, prompt: str, **kwargs: Any) -> str: ...
