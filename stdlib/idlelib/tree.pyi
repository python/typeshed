from idlelib import zoomheight as zoomheight
from idlelib.config import idleConf as idleConf
from tkinter import *
from tkinter import Canvas, Event, Frame, PhotoImage, Scrollbar, Tk, Widget
from typing import Any, Union

ICONDIR: str

def listicons(icondir: str = ...) -> None: ...
def wheel_event(event: "Event[Any]", widget: Widget | None = ...) -> str: ...

class TreeNode:
    canvas: Canvas
    parent: Union["TreeNode", None]
    item: "TreeItem"
    state: str
    selected: bool
    children: list["TreeNode"]
    x: int | None
    iconimages: dict[str, PhotoImage]
    def __init__(self, canvas: Canvas, parent: "TreeItem | None", item: "TreeItem") -> None: ...
    def destroy(self) -> None: ...
    def geticonimage(self, name: str) -> PhotoImage: ...
    def select(self, event: "Event[Any] | None" = ...) -> None: ...
    def deselect(self, event: "Event[Any] | None" = ...) -> None: ...
    def deselectall(self) -> None: ...
    def deselecttree(self) -> None: ...
    def flip(self, event: "Event[Any] | None" = ...) -> str: ...
    def expand(self, event: "Event[Any] | None" = ...) -> None: ...
    def collapse(self, event: "Event[Any] | None" = ...) -> None: ...
    def view(self) -> None: ...
    def lastvisiblechild(self) -> "TreeNode": ...
    def update(self) -> None: ...
    def draw(self, x: int, y: int) -> int: ...
    image_id: int
    def drawicon(self) -> None: ...
    label: Label
    text_id: int
    def drawtext(self) -> None: ...
    def select_or_edit(self, event: "Event[Any] | None" = ...) -> None: ...
    entry: None | Entry
    def edit(self, event: "Event[Any] | None" = ...) -> None: ...
    def edit_finish(self, event: "Event[Any] | None" = ...) -> None: ...
    def edit_cancel(self, event: "Event[Any] | None" = ...) -> None: ...

class TreeItem:
    def __init__(self) -> None: ...
    def GetText(self) -> str | None: ...
    def GetLabelText(self) -> str | None: ...
    expandable: int | bool | None
    def IsExpandable(self) -> int | bool: ...
    def IsEditable(self) -> bool: ...
    def SetText(self, text: str) -> None: ...
    def GetIconName(self) -> str | None: ...
    def GetSelectedIconName(self) -> str: ...
    def GetSubList(self) -> list["TreeItem"]: ...
    def OnDoubleClick(self) -> None: ...

class FileTreeItem(TreeItem):
    path: str
    def __init__(self, path: str) -> None: ...
    def GetText(self) -> str: ...
    def IsEditable(self) -> bool: ...
    def SetText(self, text: str) -> None: ...
    def GetIconName(self) -> str | None: ...
    def IsExpandable(self) -> bool: ...
    def GetSubList(self) -> list["TreeItem"]: ...

class ScrolledCanvas:
    master: Tk
    frame: Frame
    canvas: Canvas
    vbar: Scrollbar
    hbar: Scrollbar
    def __init__(self, master: Tk, **opts: dict[str, Any]) -> None: ...
    def page_up(self, event: "Event[Any]") -> str: ...
    def page_down(self, event: "Event[Any]") -> str: ...
    def unit_up(self, event: "Event[Any]") -> str: ...
    def unit_down(self, event: "Event[Any]") -> str: ...
    def zoom_height(self, event: "Event[Any]") -> str: ...
