from _typeshed import Incomplete
from idlelib.autocomplete import ATTRS as ATTRS, FILES as FILES
from idlelib.multicall import MC_SHIFT as MC_SHIFT
from tkinter import *
from tkinter import Event, Listbox, Scrollbar, Text, Toplevel, Widget
from typing import Any, Union

HIDE_VIRTUAL_EVENT_NAME: str
HIDE_FOCUS_OUT_SEQUENCE: str
HIDE_SEQUENCES: Incomplete
KEYPRESS_VIRTUAL_EVENT_NAME: str
KEYPRESS_SEQUENCES: tuple[str, str, str, str, str, str, str, str, str, str, str]
KEYRELEASE_VIRTUAL_EVENT_NAME: str
KEYRELEASE_SEQUENCE: str
LISTUPDATE_SEQUENCE: str
WINCONFIG_SEQUENCE: str
DOUBLECLICK_SEQUENCE: str

class AutoCompleteWindow:
    widget: Text
    tags: tuple[str, ...]
    autocompletewindow: Toplevel
    origselforeground: str
    completions: list[str] | None
    morecompletions: list[str] | None
    mode: int | None
    start: str | None
    startindex: int | None
    lasttypedstart: int | None
    userwantswindow: bool | None
    hideid: int
    keypressid: int
    listupdateid: int
    winconfigid: int
    keyreleaseid: int
    doubleclickid: int
    lastkey_was_tab: bool
    is_configuring: bool
    def __init__(self, widget: Widget, tags: tuple[str, ...]) -> None: ...
    scrollbar: Scrollbar
    listbox: Listbox
    origselbackground: str
    hideaid: str
    hidewid: str
    def show_window(
        self, comp_lists: tuple[list[str], list[str]], index: int, complete: bool, mode: int, userWantsWin: bool
    ) -> None: ...
    def winconfig_event(self, event: "Event[Any] | None") -> None: ...
    def hide_event(self, event: "Event[Any] | None") -> None: ...
    def listselect_event(self, event: "Event[Any] | None") -> None: ...
    def doubleclick_event(self, event: "Event[Any] | None") -> None: ...
    def keypress_event(self, event: "Event[Any] | None") -> str | None: ...
    def keyrelease_event(self, event: "Event[Any] | None") -> None: ...
    def is_active(self) -> bool: ...
    def complete(self) -> None: ...
    def hide_window(self) -> None: ...
