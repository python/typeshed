from tkinter import Misc
from tkinter.commondialog import Dialog
from typing import ClassVar, Final, Literal
from typing_extensions import TypeAlias

__all__ = ["showinfo", "showwarning", "showerror", "askquestion", "askokcancel", "askyesno", "askyesnocancel", "askretrycancel"]

ERROR: Final = "error"
INFO: Final = "info"
QUESTION: Final = "question"
WARNING: Final = "warning"
ABORTRETRYIGNORE: Final = "abortretryignore"
OK: Final = "ok"
OKCANCEL: Final = "okcancel"
RETRYCANCEL: Final = "retrycancel"
YESNO: Final = "yesno"
YESNOCANCEL: Final = "yesnocancel"
ABORT: Final = "abort"
RETRY: Final = "retry"
IGNORE: Final = "ignore"
CANCEL: Final = "cancel"
YES: Final = "yes"
NO: Final = "no"

class Message(Dialog):
    command: ClassVar[str]

_Icon: TypeAlias = Literal["error", "info", "question", "warning"]
_Type: TypeAlias = Literal["abortretryignore", "ok", "okcancel", "retrycancel", "yesno", "yesnocancel"]
_Default: TypeAlias = Literal["abort", "retry", "ignore", "ok", "cancel", "yes", "no"]

def showinfo(
    title: str | None = None,
    message: str | None = None,
    *,
    detail: str = ...,
    icon: _Icon = ...,
    type: _Type = ...,
    default: _Default = ...,
    parent: Misc = ...,
) -> str: ...
def showwarning(
    title: str | None = None,
    message: str | None = None,
    *,
    detail: str = ...,
    icon: _Icon = ...,
    type: _Type = ...,
    default: _Default = ...,
    parent: Misc = ...,
) -> str: ...
def showerror(
    title: str | None = None,
    message: str | None = None,
    *,
    detail: str = ...,
    icon: _Icon = ...,
    type: _Type = ...,
    default: _Default = ...,
    parent: Misc = ...,
) -> str: ...
def askquestion(
    title: str | None = None,
    message: str | None = None,
    *,
    detail: str = ...,
    icon: _Icon = ...,
    type: _Type = ...,
    default: _Default = ...,
    parent: Misc = ...,
) -> str: ...
def askokcancel(
    title: str | None = None,
    message: str | None = None,
    *,
    detail: str = ...,
    icon: _Icon = ...,
    type: _Type = ...,
    default: _Default = ...,
    parent: Misc = ...,
) -> bool: ...
def askyesno(
    title: str | None = None,
    message: str | None = None,
    *,
    detail: str = ...,
    icon: _Icon = ...,
    type: _Type = ...,
    default: _Default = ...,
    parent: Misc = ...,
) -> bool: ...
def askyesnocancel(
    title: str | None = None,
    message: str | None = None,
    *,
    detail: str = ...,
    icon: _Icon = ...,
    type: _Type = ...,
    default: _Default = ...,
    parent: Misc = ...,
) -> bool | None: ...
def askretrycancel(
    title: str | None = None,
    message: str | None = None,
    *,
    detail: str = ...,
    icon: _Icon = ...,
    type: _Type = ...,
    default: _Default = ...,
    parent: Misc = ...,
) -> bool: ...
