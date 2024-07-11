import sys
from tkinter.commondialog import Dialog
from typing import ClassVar, Final

if sys.version_info >= (3, 9):
    __all__ = [
        "showinfo",
        "showwarning",
        "showerror",
        "askquestion",
        "askokcancel",
        "askyesno",
        "askyesnocancel",
        "askretrycancel",
    ]

ERROR: Final[str]
INFO: Final[str]
QUESTION: Final[str]
WARNING: Final[str]
ABORTRETRYIGNORE: Final[str]
OK: Final[str]
OKCANCEL: Final[str]
RETRYCANCEL: Final[str]
YESNO: Final[str]
YESNOCANCEL: Final[str]
ABORT: Final[str]
RETRY: Final[str]
IGNORE: Final[str]
CANCEL: Final[str]
YES: Final[str]
NO: Final[str]

class Message(Dialog):
    command: ClassVar[str]

def showinfo(title: str | None = None, message: str | None = None, **options) -> str: ...
def showwarning(title: str | None = None, message: str | None = None, **options) -> str: ...
def showerror(title: str | None = None, message: str | None = None, **options) -> str: ...
def askquestion(title: str | None = None, message: str | None = None, **options) -> str: ...
def askokcancel(title: str | None = None, message: str | None = None, **options) -> bool: ...
def askyesno(title: str | None = None, message: str | None = None, **options) -> bool: ...
def askyesnocancel(title: str | None = None, message: str | None = None, **options) -> bool | None: ...
def askretrycancel(title: str | None = None, message: str | None = None, **options) -> bool: ...
