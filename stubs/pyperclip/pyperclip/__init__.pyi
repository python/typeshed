__all__ = ["copy", "paste", "set_clipboard", "determine_clipboard"]

from collections.abc import Callable
from typing import Any, Literal, TypeAlias, Protocol


class PyperclipException(RuntimeError): ...

class PyperclipWindowsException(PyperclipException):
    def __init__(self, message: str) -> None: ...

class PyperclipTimeoutException(PyperclipException): ...


class WinDLLUser32Function(Protocol):
    def __call__(self, *args: Any) -> Any: ...


# Wrapper for ctypes calls, should not be exposed to the developer
class CheckedCall:
    def __init__(self, f: WinDLLUser32Function) -> None: ...
    def __call__(self, *args: Any): ...
    def __setattr__(self, key: str, value: Any) -> None: ...

ClipboardMechanismName: TypeAlias = Literal["pbcopy", "pyobjc", "qt", "xclip", "xsel", "wl-clipboard", "klipper", "windows", "no"]
ClipboardCopyMechanism: TypeAlias = Callable[[str], None]
ClipboardPasteMechanism: TypeAlias = Callable[[], str]

def copy(text: str) -> None: ...
def paste() -> str: ...
def set_clipboard(clipboard: ClipboardMechanismName) -> None: ...
def determine_clipboard() -> tuple[ClipboardCopyMechanism, ClipboardPasteMechanism]: ...
