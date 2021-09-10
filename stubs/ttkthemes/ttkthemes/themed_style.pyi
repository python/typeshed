from tkinter import ttk
from typing import Any

from ._widget import ThemedWidget as ThemedWidget

class ThemedStyle(ttk.Style, ThemedWidget):
    def __init__(self, *args, **kwargs) -> None: ...
    def theme_use(self, theme_name: Any | None = ...): ...
    def theme_names(self): ...
