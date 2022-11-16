from idlelib import searchengine as searchengine
from idlelib.searchbase import SearchDialogBase as SearchDialogBase
from tkinter import Event, Text
from typing import Any, Union

def find(text: Text) -> None: ...
def find_again(text: Text) -> bool: ...
def find_selection(text: Text) -> bool: ...

class SearchDialog(SearchDialogBase):
    def create_widgets(self) -> None: ...
    def default_command(self, event: "Event[Any] | None" = ...) -> None: ...
    def find_again(self, text: Text) -> bool: ...
    def find_selection(self, text: Text) -> bool: ...
