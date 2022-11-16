from collections.abc import Callable
from tkinter import BaseWidget, OptionMenu, StringVar
from typing import Any

class DynOptionMenu(OptionMenu):
    variable: StringVar
    command: Callable[[], Any]
    def __init__(self, master: BaseWidget, variable: StringVar, value: str, *values: str, **kwargs: Any) -> None: ...
    def SetMenu(self, valueList: list[str], value: str | None = ...) -> None: ...
