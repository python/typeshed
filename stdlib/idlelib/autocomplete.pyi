from idlelib import autocomplete_w as autocomplete_w
from idlelib.config import idleConf as idleConf
from idlelib.editor import EditorWindow
from idlelib.hyperparser import HyperParser as HyperParser
from tkinter import Event, Text
from typing import Any, Union

completion_kwds: list[str]
ATTRS: int
FILES: int
FORCE: tuple[bool, bool, bool, None]
TAB: tuple[bool, bool, bool, None]
TRY_A: tuple[bool, bool, bool, int]
TRY_F: tuple[bool, bool, bool, int]
ID_CHARS: str
SEPS: str
TRIGGERS: str

class AutoComplete:
    editwin: EditorWindow | None
    text: Text | None
    tags: None | str
    autocompletewindow: None
    def __init__(self, editwin: EditorWindow | None = ..., tags: str | None = ...) -> None: ...
    @classmethod
    def reload(cls) -> None: ...
    def force_open_completions_event(self, event: Union["Event[Any]", None]) -> str: ...
    def autocomplete_event(self, event: Union["Event[Any]", None]) -> str | None: ...
    def try_open_completions_event(self, event: Union["Event[Any]", None] = ...) -> None: ...
    def open_completions(self, args: tuple[bool, bool, bool, None | int]) -> bool | None: ...
    def fetch_completions(self, what: str, mode: int) -> tuple[list[str], list[str]]: ...
    def get_entity(self, name: str) -> Any: ...
