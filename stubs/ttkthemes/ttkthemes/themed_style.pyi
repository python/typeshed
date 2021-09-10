import tkinter
from tkinter import ttk

from ._widget import ThemedWidget

class ThemedStyle(ttk.Style, ThemedWidget):
    def __init__(
        self, master: tkinter.Misc | None, *, theme: str | None = ..., gif_override: bool | None = ..., **kwargs
    ) -> None: ...
    # Unlike ttk.Style, can't return None
    def theme_use(self, theme_name: str | None = ...) -> str: ...  # type: ignore
    def theme_names(self) -> list[str]: ...  # type: ignore
