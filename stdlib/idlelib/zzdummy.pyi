from idlelib.config import idleConf as idleConf
from idlelib.editor import EditorWindow
from idlelib.format import FormatRegion
from tkinter import Event, Text
from typing import Any, Callable

def format_selection(format_line: Callable[["ZzDummy", str], str]) -> Callable[[Event[Any] | None], str]: ...

class ZzDummy:
    menudefs: list[tuple[str, list[tuple[str, str]]]]
    editwin: EditorWindow
    text: Text
    formatter: FormatRegion
    def __init__(self, editwin: EditorWindow) -> None: ...
    @classmethod
    def reload(cls) -> None: ...
    def z_in_event(self, line: str) -> str: ...
    def z_out_event(self, line: str) -> str: ...
