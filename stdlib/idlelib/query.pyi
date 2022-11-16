from tkinter import BaseWidget, BooleanVar, Button, Entry, Event, Frame, Label, StringVar, Toplevel
from tkinter.font import Font
from typing import Any
from collections.abc import Callable, Container

class Query(Toplevel):
    parent: BaseWidget
    message: str
    text0: str
    used_names: Container[str]
    def __init__(
        self,
        parent: BaseWidget,
        title: str,
        message: str,
        *,
        text0: str = ...,
        used_names: Container[str] = ...,
        _htest: bool = ...,
        _utest: bool = ...,
    ) -> None: ...
    frame: Frame  # type: ignore[assignment]
    entryvar: StringVar
    entry: Entry
    error_font: Font
    entry_error: Label
    button_ok: Button
    button_cancel: Button
    def create_widgets(self, ok_text: str = ...) -> None: ...
    def create_extra(self) -> None: ...
    def showerror(self, message: str, widget: BaseWidget | None = ...) -> None: ...
    def entry_ok(self) -> str | None: ...
    result: str | None
    def ok(self, event: Event[Any] | None = ...) -> None: ...
    def cancel(self, event: Event[Any] | None = ...) -> None: ...
    def destroy(self) -> None: ...

class SectionName(Query):
    def __init__(
        self, parent: BaseWidget, title: str, message: str, used_names: Container[str], *, _htest: bool = ..., _utest: bool = ...
    ) -> None: ...
    def entry_ok(self) -> str | None: ...

class ModuleName(Query):
    def __init__(
        self, parent: BaseWidget, title: str, message: str, text0: str, *, _htest: bool = ..., _utest: bool = ...
    ) -> None: ...
    def entry_ok(self) -> str | None: ...

class Goto(Query):
    def entry_ok(self) -> int | None: ...  # type: ignore[override]

class HelpSource(Query):
    filepath: str
    def __init__(
        self,
        parent: BaseWidget,
        title: str,
        *,
        menuitem: str = ...,
        filepath: str = ...,
        used_names: Container[str] = ...,
        _htest: bool = ...,
        _utest: bool = ...,
    ) -> None: ...
    pathvar: StringVar
    path: Entry
    path_error: Label
    def create_extra(self) -> None: ...
    def askfilename(self, filetypes: list[str], initdir: str, initfile: str) -> str: ...
    def browse_file(self) -> None: ...
    item_ok: Callable[[], str | None]
    def path_ok(self) -> str | None: ...
    def entry_ok(self) -> str | None: ...

class CustomRun(Query):
    def __init__(
        self, parent: BaseWidget, title: str, *, cli_args: list[str] = ..., _htest: bool = ..., _utest: bool = ...
    ) -> None: ...
    restartvar: BooleanVar
    args_error: Label
    def create_extra(self) -> None: ...
    def cli_args_ok(self) -> list[str]: ...
    def entry_ok(self) -> tuple[list[str], bool] | None: ...  # type: ignore
