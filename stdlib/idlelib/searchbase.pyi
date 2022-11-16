from idlelib.searchengine import SearchEngine
from tkinter import BaseWidget, Button, Entry, Event, Frame, Label, Text, Tk, Variable
from typing import Any, Callable, Union

class SearchDialogBase:
    title: str
    icon: str
    needwrapbutton: int
    root: Tk
    bell: Callable[[], None]
    engine: SearchEngine
    top: BaseWidget | None
    def __init__(self, root: Tk, engine: SearchEngine) -> None: ...
    text: Text
    def open(self, text: Text, searchphrase: str | None = ...) -> None: ...
    def close(self, event: "Event[Any] | None" = ...) -> None: ...
    frame: Frame
    row: int
    def create_widgets(self) -> None: ...
    def make_entry(self, label_text: str, var: Variable) -> tuple[Entry, Label]: ...
    ent: tuple[Entry, Label]
    def create_entries(self) -> None: ...
    def make_frame(self, labeltext: str | None = ...) -> tuple[Frame, Label | str]: ...
    def create_option_buttons(self) -> tuple[Frame, list[tuple[Variable, str]]]: ...
    def create_other_buttons(self) -> tuple[Frame, list[tuple[int, str]]]: ...
    def make_button(self, label: str, command: Callable[["Event[Any] | None"], None], isdef: int = ...) -> Button: ...
    def create_command_buttons(self) -> None: ...

class _searchbase(SearchDialogBase):
    root: Tk
    engine: SearchEngine
    def __init__(self, parent: BaseWidget) -> None: ...
    def default_command(self, dummy: Any) -> None: ...
