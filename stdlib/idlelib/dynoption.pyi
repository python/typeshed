from typing import Any, Callable
from tkinter import OptionMenu, StringVar, BaseWidget

class DynOptionMenu(OptionMenu):
    variable: StringVar
    command: Callable[[], Any]
    def __init__(self, master: BaseWidget, variable: StringVar, value: str, *values: str, **kwargs: Any) -> None: ...
    def SetMenu(self, valueList: list[str], value: str | None = ...) -> None: ...
