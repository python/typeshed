import tkinter
from typing import Any, Literal

from ._widget import ThemedWidget

class ThemedTk(tkinter.Tk, ThemedWidget):
    def __init__(
        self,
        # non-keyword-only args copied from tkinter.Tk
        screenName: str | None = ...,
        baseName: str | None = ...,
        className: str = ...,
        useTk: bool = ...,
        sync: bool = ...,
        use: str | None = ...,
        *,
        theme: str | None = ...,
        # fonts argument does nothing
        toplevel: bool | None = ...,
        themebg: bool | None = ...,
        background: bool | None = ...,  # old alias for themebg
        gif_override: bool = ...,
    ) -> None: ...
    def set_theme(self, theme_name: str, toplevel: bool | None = None, themebg: bool | None = None) -> None: ...
    # Keep this in sync with tkinter.Tk
    def config(  # type: ignore[override]
        self,
        kw: dict[str, Any] | None = None,
        *,
        themebg: bool | None = ...,
        toplevel: bool | None = ...,
        theme: str | None = ...,
        background: str = ...,
        bd: str | float = ...,
        bg: str = ...,
        border: str | float = ...,
        borderwidth: str | float = ...,
        cursor: tkinter._Cursor = ...,
        height: str | float = ...,
        highlightbackground: str = ...,
        highlightcolor: str = ...,
        highlightthickness: str | float = ...,
        menu: tkinter.Menu = ...,
        padx: str | float = ...,
        pady: str | float = ...,
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
        takefocus: tkinter._TakeFocusValue = ...,
        width: str | float = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    def cget(self, k: str) -> Any: ...
    def configure(  # type: ignore[override]
        self,
        kw: dict[str, Any] | None = None,
        *,
        themebg: bool | None = ...,
        toplevel: bool | None = ...,
        theme: str | None = ...,
        background: str = ...,
        bd: str | float = ...,
        bg: str = ...,
        border: str | float = ...,
        borderwidth: str | float = ...,
        cursor: tkinter._Cursor = ...,
        height: str | float = ...,
        highlightbackground: str = ...,
        highlightcolor: str = ...,
        highlightthickness: str | float = ...,
        menu: tkinter.Menu = ...,
        padx: str | float = ...,
        pady: str | float = ...,
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
        takefocus: tkinter._TakeFocusValue = ...,
        width: str | float = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    def __getitem__(self, k: str) -> Any: ...
    def __setitem__(self, k: str, v: Any) -> None: ...
