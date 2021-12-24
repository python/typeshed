from collections.abc import Mapping
from tkinter import Widget
from typing import Any

DIALOG_ICON: str

class Dialog(Widget):
    widgetName: str
    num: int
    def __init__(self, master: Any | None = ..., cnf: Mapping[str, Any] = ..., **kw) -> None: ...
    def destroy(self) -> None: ...
