from collections.abc import Callable
from idlelib.pyshell import PyShellEditorWindow
from tkinter import Event
from typing import Any

class AutoExpand:
    wordchars: str
    text: PyShellEditorWindow
    bell: Callable[[], None]
    state: None
    def __init__(self, editwin: PyShellEditorWindow) -> None: ...
    def expand_word_event(self, event: Event[Any]) -> str: ...
    def getwords(self) -> list[str]: ...
    def getprevword(self) -> str: ...
