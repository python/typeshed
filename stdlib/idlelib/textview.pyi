from idlelib.colorizer import color_config as color_config
from tkinter import Event, Toplevel
from tkinter.ttk import Button, Frame, Scrollbar, Widget
from typing import Any

class AutoHideScrollbar(Scrollbar):
    def set(self, lo: float, hi: float) -> None: ...
    def pack(self, **kwargs: Any) -> None: ...  # type: ignore[override]
    def place(self, **kwargs: Any) -> None: ...  # type: ignore[override]

class ScrollableTextFrame(Frame):
    yscroll: AutoHideScrollbar
    xscroll: AutoHideScrollbar | None
    def __init__(self, master: Toplevel, wrap: str = ..., **kwargs: Any) -> None: ...

class ViewFrame(Frame):
    parent: Widget
    textframe: ScrollableTextFrame
    button_ok: Button
    def __init__(self, parent: Widget, contents: str, wrap: str = ...) -> None: ...
    def ok(self, event: "Event[Any] | None" = ...) -> None: ...

class ViewWindow(Toplevel):
    viewframe: ViewFrame
    button_ok: Button
    is_modal: bool
    def __init__(
        self,
        parent: Widget,
        title: str,
        contents: str,
        modal: bool = ...,
        wrap: str = ...,
        *,
        _htest: bool = ...,
        _utest: bool = ...,
    ) -> None: ...
    def ok(self, event: "Event[Any] | None" = ...) -> None: ...

def view_text(
    parent: Widget, title: str, contents: str, modal: bool = ..., wrap: str = ..., _utest: bool = ...
) -> ViewWindow: ...
def view_file(
    parent: Widget, title: str, filename: str, encoding: str, modal: bool = ..., wrap: str = ..., _utest: bool = ...
) -> ViewWindow | None: ...
