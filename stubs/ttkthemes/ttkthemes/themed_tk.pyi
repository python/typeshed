import tkinter
from _typeshed import FloatInt
from collections.abc import Callable
from typing import Any, Literal

from ._widget import ThemedWidget

class ThemedTk(tkinter.Tk, ThemedWidget):
    def __init__(
        self,
        # non-keyword-only args copied from tkinter.Tk
        screenName: str | None = None,
        baseName: str | None = None,
        className: str = "Tk",
        useTk: bool = True,
        sync: bool = False,
        use: str | None = None,
        theme: str | None = None,
        # fonts argument does nothing
        toplevel: bool | None = None,
        themebg: bool | None = None,
        background: bool | None = None,  # old alias for themebg
        gif_override: bool = False,
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
        bd: FloatInt | str = ...,
        bg: str = ...,
        border: FloatInt | str = ...,
        borderwidth: FloatInt | str = ...,
        cursor: tkinter._Cursor = ...,
        height: FloatInt | str = ...,
        highlightbackground: str = ...,
        highlightcolor: str = ...,
        highlightthickness: FloatInt | str = ...,
        menu: tkinter.Menu = ...,
        padx: FloatInt | str = ...,
        pady: FloatInt | str = ...,
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
        takefocus: bool | Literal[0, 1, ""] | Callable[[str], bool | None] = ...,
        width: FloatInt | str = ...,
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
        bd: FloatInt | str = ...,
        bg: str = ...,
        border: FloatInt | str = ...,
        borderwidth: FloatInt | str = ...,
        cursor: tkinter._Cursor = ...,
        height: FloatInt | str = ...,
        highlightbackground: str = ...,
        highlightcolor: str = ...,
        highlightthickness: FloatInt | str = ...,
        menu: tkinter.Menu = ...,
        padx: FloatInt | str = ...,
        pady: FloatInt | str = ...,
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
        takefocus: bool | Literal[0, 1, ""] | Callable[[str], bool | None] = ...,
        width: FloatInt | str = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    def __getitem__(self, k: str) -> Any: ...
    def __setitem__(self, k: str, v: Any) -> None: ...
