from collections.abc import Generator
from idlelib import macosx as macosx
from idlelib.config import idleConf as idleConf
from idlelib.delegator import Delegator as Delegator
from idlelib.pyshell import PyShellEditorWindow
from tkinter import BaseWidget, Canvas, Event, Text
from typing import Any, Callable, Union

def get_lineno(text: Text, index: str) -> int | None: ...
def get_end_linenumber(text: Text) -> int | None: ...
def get_displaylines(text: Text, index: str) -> int: ...
def get_widget_padding(widget: BaseWidget) -> tuple[int, int]: ...
def temp_enable_text_widget(text: Text) -> Generator[None, None, None]: ...

class BaseSideBar:
    editwin: PyShellEditorWindow
    parent: BaseWidget
    text: Text
    is_shown: bool
    main_widget: BaseWidget
    def __init__(self, editwin: PyShellEditorWindow) -> None: ...
    def init_widgets(self) -> BaseWidget: ...
    def update_font(self) -> None: ...
    def update_colors(self) -> None: ...
    def grid(self) -> None: ...
    def show_sidebar(self) -> None: ...
    def hide_sidebar(self) -> None: ...
    def yscroll_event(self, *args: Any, **kwargs: Any) -> str | None: ...
    def redirect_yscroll_event(self, *args: Any, **kwargs: Any) -> str | None: ...
    def redirect_focusin_event(self, event: Union["Event[Any]", None]) -> str: ...
    def redirect_mousebutton_event(self, event: Union["Event[Any]", None], event_name: str) -> str: ...
    def redirect_mousewheel_event(self, event: Union["Event[Any]", None]) -> str: ...
    def bind_events(self) -> None: ...

class EndLineDelegator(Delegator):
    changed_callback: Callable[[int | None], Any]
    def __init__(self, changed_callback: Callable[[int | None], Any]) -> None: ...
    def insert(self, index: str, chars: str, tags: str | None = ...) -> None: ...
    def delete(self, index1: str, index2: str | None = ...) -> None: ...

class LineNumbers(BaseSideBar):
    def __init__(self, editwin: PyShellEditorWindow) -> None: ...
    sidebar_text: Text
    prev_end: int
    def init_widgets(self) -> Text: ...
    def grid(self) -> None: ...
    def update_font(self) -> None: ...
    def update_colors(self) -> None: ...
    def update_sidebar_text(self, end: int | None) -> None: ...
    def yscroll_event(self, *args: Any, **kwargs: Any) -> str: ...

class WrappedLineHeightChangeDelegator(Delegator):
    callback: Callable[[], Any]
    def __init__(self, callback: Callable[[], Any]) -> None: ...
    def insert(self, index: str, chars: str, tags: str | None = ...) -> None: ...
    def delete(self, index1: str, index2: str | None = ...) -> None: ...

class ShellSidebar(BaseSideBar):
    canvas: Canvas
    line_prompts: dict[int, str]
    is_shown: bool
    def __init__(self, editwin: PyShellEditorWindow) -> None: ...
    def init_widgets(self) -> Canvas: ...
    def bind_events(self) -> None: ...
    def context_menu_event(self, event: Union["Event[Any]", None]) -> str: ...
    def grid(self) -> None: ...
    def change_callback(self) -> None: ...
    def update_sidebar(self) -> None: ...
    def yscroll_event(self, *args: Any, **kwargs: Any) -> str: ...
    font: str
    def update_font(self) -> None: ...
    colors: tuple[str, str]
    def update_colors(self) -> None: ...
