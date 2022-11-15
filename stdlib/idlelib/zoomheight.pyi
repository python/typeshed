from tkinter import BaseWidget, Event
from typing import Any, Union

from idlelib.editor import EditorWindow

class WmInfoGatheringError(Exception): ...

class ZoomHeight:
    editwin: EditorWindow
    top: BaseWidget
    def __init__(self, editwin: BaseWidget) -> None: ...
    def zoom_height_event(self, event: Union["Event[Any]", None] = ...) -> str: ...
    def zoom_height(self) -> bool | None: ...
    def get_max_height_and_y_coord(self) -> int: ...

def get_window_geometry(top: BaseWidget) -> tuple[int, int, int, int]: ...
def set_window_geometry(top: BaseWidget, geometry: tuple[int, int, int, int]) -> None: ...
