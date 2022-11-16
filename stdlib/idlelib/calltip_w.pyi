from idlelib.tooltip import TooltipBase as TooltipBase
from tkinter import Event, Label, Text
from typing import Any, Union

HIDE_EVENT: str
HIDE_SEQUENCES: tuple[str, str]
CHECKHIDE_EVENT: str
CHECKHIDE_SEQUENCES: tuple[str, str]
CHECKHIDE_TIME: int
MARK_RIGHT: str

class CalltipWindow(TooltipBase):
    label: Label | None
    text: str | None
    parenline: int | None
    parencol: int | None
    lastline: int | None
    hideid: str | None
    checkhide_after_id: str | None
    def __init__(self, text_widget: Text) -> None: ...
    def get_position(self) -> tuple[int, int]: ...
    def position_window(self) -> None: ...
    def showtip(self, text: str, parenleft: str, parenright: str) -> None: ...  # type: ignore
    def showcontents(self) -> None: ...
    def checkhide_event(self, event: "Event[Any] | None" = ...) -> str | None: ...
    def hide_event(self, event: "Event[Any]") -> str | None: ...
    def hidetip(self) -> None: ...
