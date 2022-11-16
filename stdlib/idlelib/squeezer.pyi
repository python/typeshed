import tkinter as tk
from idlelib import macosx as macosx
from idlelib.config import idleConf as idleConf
from idlelib.pyshell import PyShellEditorWindow
from idlelib.textview import view_text as view_text
from idlelib.tooltip import Hovertip as Hovertip
from tkinter import Event, Text
from typing import Any

def count_lines_with_wrapping(s: str, linewidth: int = ...) -> int: ...

class ExpandingButton(tk.Button):
    s: str
    tags: str | None
    numoflines: int
    squeezer: Squeezer
    editwin: PyShellEditorWindow
    text: Text
    base_text: Text
    is_dangerous: bool
    def __init__(self, s: str, tags: str | None, numoflines: int, squeezer: Squeezer) -> None: ...
    def set_is_dangerous(self) -> None: ...
    def expand(self, event: Event[Any] | None = ...) -> str | None: ...
    def copy(self, event: Event[Any] | None = ...) -> None: ...
    def view(self, event: Event[Any] | None = ...) -> None: ...
    rmenu_specs: tuple[tuple[str, str]]
    def context_menu_event(self, event: Event[Any] | None) -> str: ...

class Squeezer:
    @classmethod
    def reload(cls) -> None: ...
    editwin: PyShellEditorWindow
    text: Text
    base_text: Text
    window_width_delta: int
    expandingbuttons: list[ExpandingButton]
    def __init__(self, editwin: PyShellEditorWindow) -> None: ...
    def count_lines(self, s: str) -> int: ...
    def squeeze_current_text(self) -> str: ...
