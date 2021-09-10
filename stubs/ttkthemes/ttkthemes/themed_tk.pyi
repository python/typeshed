import tkinter
from typing import Any

from ._widget import ThemedWidget

class ThemedTk(tkinter.Tk, ThemedWidget):
    def __init__(
        self,
        # non-keyword-only args copied from tkinter.Tk
        toplevel: bool | None = ...,
        themebg: bool | None = ...,
        background: bool | None = ...,  # old alias for themebg
        gif_override: bool = ...,
        *,
        theme: str | None = ...,
        # fonts argument does nothing
        screenName: str | None = ...,
        baseName: str | None = ...,
        className: str = ...,
        useTk: bool = ...,
        sync: bool = ...,
        use: str | None = ...,
    ) -> None: ...
    def set_theme(self, theme_name, toplevel: bool | None = ..., themebg: bool | None = ...) -> None: ...
    # TODO: currently no good way to say "use the same big list of kwargs as parent class but also add these"
    def config(self, kw: Any | None = ..., **kwargs): ...
    def cget(self, k): ...
    def configure(self, kw: Any | None = ..., **kwargs): ...
    def __getitem__(self, k): ...
    def __setitem__(self, k, v): ...
