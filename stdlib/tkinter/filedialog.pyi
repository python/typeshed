from _typeshed import Incomplete
import sys
from _typeshed import StrOrBytesPath
from collections.abc import Iterable
from tkinter import Button, Entry, Frame, Listbox, Misc, Scrollbar, StringVar, Toplevel, commondialog
from typing import IO, Any, ClassVar
from typing_extensions import Literal

if sys.version_info >= (3, 9):
    __all__ = [
        "FileDialog",
        "LoadFileDialog",
        "SaveFileDialog",
        "Open",
        "SaveAs",
        "Directory",
        "askopenfilename",
        "asksaveasfilename",
        "askopenfilenames",
        "askopenfile",
        "askopenfiles",
        "asksaveasfile",
        "askdirectory",
    ]

dialogstates: dict[Incomplete, tuple[Incomplete, Incomplete]]

class FileDialog:
    title: str
    master: Incomplete
    directory: Incomplete | None
    top: Toplevel
    botframe: Frame
    selection: Entry
    filter: Entry
    midframe: Entry
    filesbar: Scrollbar
    files: Listbox
    dirsbar: Scrollbar
    dirs: Listbox
    ok_button: Button
    filter_button: Button
    cancel_button: Button
    def __init__(
        self, master, title: Incomplete | None = ...
    ) -> None: ...  # title is usually a str or None, but e.g. int doesn't raise en exception either
    how: Incomplete | None
    def go(self, dir_or_file: Incomplete = ..., pattern: str = ..., default: str = ..., key: Incomplete | None = ...): ...
    def quit(self, how: Incomplete | None = ...) -> None: ...
    def dirs_double_event(self, event) -> None: ...
    def dirs_select_event(self, event) -> None: ...
    def files_double_event(self, event) -> None: ...
    def files_select_event(self, event) -> None: ...
    def ok_event(self, event) -> None: ...
    def ok_command(self) -> None: ...
    def filter_command(self, event: Incomplete | None = ...) -> None: ...
    def get_filter(self): ...
    def get_selection(self): ...
    def cancel_command(self, event: Incomplete | None = ...) -> None: ...
    def set_filter(self, dir, pat) -> None: ...
    def set_selection(self, file) -> None: ...

class LoadFileDialog(FileDialog):
    title: str
    def ok_command(self) -> None: ...

class SaveFileDialog(FileDialog):
    title: str
    def ok_command(self) -> None: ...

class _Dialog(commondialog.Dialog): ...

class Open(_Dialog):
    command: ClassVar[str]

class SaveAs(_Dialog):
    command: ClassVar[str]

class Directory(commondialog.Dialog):
    command: ClassVar[str]

# TODO: command kwarg available on macos
def asksaveasfilename(
    *,
    confirmoverwrite: bool | None = ...,
    defaultextension: str | None = ...,
    filetypes: Iterable[tuple[str, str | list[str] | tuple[str, ...]]] | None = ...,
    initialdir: StrOrBytesPath | None = ...,
    initialfile: StrOrBytesPath | None = ...,
    parent: Misc | None = ...,
    title: str | None = ...,
    typevariable: StringVar | str | None = ...,
) -> str: ...  # can be empty string
def askopenfilename(
    *,
    defaultextension: str | None = ...,
    filetypes: Iterable[tuple[str, str | list[str] | tuple[str, ...]]] | None = ...,
    initialdir: StrOrBytesPath | None = ...,
    initialfile: StrOrBytesPath | None = ...,
    parent: Misc | None = ...,
    title: str | None = ...,
    typevariable: StringVar | str | None = ...,
) -> str: ...  # can be empty string
def askopenfilenames(
    *,
    defaultextension: str | None = ...,
    filetypes: Iterable[tuple[str, str | list[str] | tuple[str, ...]]] | None = ...,
    initialdir: StrOrBytesPath | None = ...,
    initialfile: StrOrBytesPath | None = ...,
    parent: Misc | None = ...,
    title: str | None = ...,
    typevariable: StringVar | str | None = ...,
) -> Literal[""] | tuple[str, ...]: ...
def askdirectory(
    *, initialdir: StrOrBytesPath | None = ..., mustexist: bool | None = ..., parent: Misc | None = ..., title: str | None = ...
) -> str: ...  # can be empty string

# TODO: If someone actually uses these, overload to have the actual return type of open(..., mode)
def asksaveasfile(
    mode: str = ...,
    *,
    confirmoverwrite: bool | None = ...,
    defaultextension: str | None = ...,
    filetypes: Iterable[tuple[str, str | list[str] | tuple[str, ...]]] | None = ...,
    initialdir: StrOrBytesPath | None = ...,
    initialfile: StrOrBytesPath | None = ...,
    parent: Misc | None = ...,
    title: str | None = ...,
    typevariable: StringVar | str | None = ...,
) -> IO[Incomplete] | None: ...
def askopenfile(
    mode: str = ...,
    *,
    defaultextension: str | None = ...,
    filetypes: Iterable[tuple[str, str | list[str] | tuple[str, ...]]] | None = ...,
    initialdir: StrOrBytesPath | None = ...,
    initialfile: StrOrBytesPath | None = ...,
    parent: Misc | None = ...,
    title: str | None = ...,
    typevariable: StringVar | str | None = ...,
) -> IO[Incomplete] | None: ...
def askopenfiles(
    mode: str = ...,
    *,
    defaultextension: str | None = ...,
    filetypes: Iterable[tuple[str, str | list[str] | tuple[str, ...]]] | None = ...,
    initialdir: StrOrBytesPath | None = ...,
    initialfile: StrOrBytesPath | None = ...,
    parent: Misc | None = ...,
    title: str | None = ...,
    typevariable: StringVar | str | None = ...,
) -> tuple[IO[Incomplete], ...]: ...  # can be empty tuple
def test() -> None: ...
