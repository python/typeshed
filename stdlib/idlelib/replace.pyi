from tkinter import Entry, Event, StringVar, Text, Tk
from typing import Any, Union

from idlelib import searchengine as searchengine
from idlelib.searchbase import SearchDialogBase as SearchDialogBase

def replace(text: Text, insert_tags: str | None = ...) -> None: ...

class ReplaceDialog(SearchDialogBase):
    title: str
    icon: str
    replvar: StringVar
    insert_tags: str | None
    def __init__(self, root: Tk, engine: searchengine.SearchEngine) -> None: ...
    ok: bool
    def open(self, text: Text, insert_tags: str | None = ...) -> None: ...
    replent: Entry
    def create_entries(self) -> None: ...
    def create_command_buttons(self) -> None: ...
    def find_it(self, event: Union["Event[Any]", None] = ...) -> None: ...
    def replace_it(self, event: Union["Event[Any]", None] = ...) -> None: ...
    def default_command(self, event: Union["Event[Any]", None] = ...) -> None: ...
    def replace_all(self, event: Union["Event[Any]", None] = ...) -> None: ...
    def do_find(self, ok: bool = ...) -> bool: ...
    def do_replace(self) -> bool: ...
    def show_hit(self, first: str, last: str) -> None: ...
    def close(self, event: Union["Event[Any]", None] = ...) -> None: ...
