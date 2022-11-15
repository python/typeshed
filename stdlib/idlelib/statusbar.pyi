from typing import Any
from tkinter import BaseWidget
from tkinter.ttk import Label, Frame

class MultiStatusBar(Frame):
    labels: dict[str, Label]
    def __init__(self, master: BaseWidget, **kw: Any) -> None: ...
    def set_label(self, name: str, text: str = ..., side: str = ..., width: int = ...) -> None: ...
