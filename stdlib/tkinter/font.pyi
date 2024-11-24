import _tkinter
import sys
import tkinter
from typing import Any, Final, Literal, TypedDict, overload
from typing_extensions import TypeAlias

if sys.version_info >= (3, 9):
    __all__ = ["BOLD", "ITALIC", "NORMAL", "ROMAN", "Font", "families", "names", "nametofont"]

NORMAL: Final = "normal"
ROMAN: Final = "roman"
BOLD: Final = "bold"
ITALIC: Final = "italic"

_FontDescription: TypeAlias = (
    str  # "Helvetica 12"
    | Font  # A font object constructed in Python
    | list[Any]  # ["Helvetica", 12, BOLD]
    | tuple[str]  # ("Liberation Sans",) needs wrapping in tuple/list to handle spaces
    | tuple[str, int]  # ("Liberation Sans", 12)
    | tuple[str, int, str]  # ("Liberation Sans", 12, "bold")
    | tuple[str, int, list[str] | tuple[str, ...]]  # e.g. bold and italic
    | _tkinter.Tcl_Obj  # A font object constructed in Tcl
)

class _FontDict(TypedDict):
    family: str
    size: int
    weight: Literal["normal", "bold"]
    slant: Literal["roman", "italic"]
    underline: bool
    overstrike: bool

class _MetricsDict(TypedDict):
    ascent: int
    descent: int
    linespace: int
    fixed: bool

class Font:
    name: str
    delete_font: bool
    def __init__(
        self,
        # In tkinter, 'root' refers to tkinter.Tk by convention, but the code
        # actually works with any tkinter widget so we use tkinter.Misc.
        root: tkinter.Misc | None = None,
        font: _FontDescription | None = None,
        name: str | None = None,
        exists: bool = False,
        *,
        family: str = ...,
        size: int = ...,
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = ...,
        overstrike: bool = ...,
    ) -> None: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    @overload
    def cget(self, option: Literal["family"]) -> str: ...
    @overload
    def cget(self, option: Literal["size"]) -> int: ...
    @overload
    def cget(self, option: Literal["weight"]) -> Literal["normal", "bold"]: ...
    @overload
    def cget(self, option: Literal["slant"]) -> Literal["roman", "italic"]: ...
    @overload
    def cget(self, option: Literal["underline", "overstrike"]) -> bool: ...
    @overload
    def cget(self, option: str) -> Any: ...
    __getitem__ = cget
    @overload
    def actual(self, option: Literal["family"], displayof: tkinter.Misc | None = None) -> str: ...
    @overload
    def actual(self, option: Literal["size"], displayof: tkinter.Misc | None = None) -> int: ...
    @overload
    def actual(self, option: Literal["weight"], displayof: tkinter.Misc | None = None) -> Literal["normal", "bold"]: ...
    @overload
    def actual(self, option: Literal["slant"], displayof: tkinter.Misc | None = None) -> Literal["roman", "italic"]: ...
    @overload
    def actual(self, option: Literal["underline", "overstrike"], displayof: tkinter.Misc | None = None) -> bool: ...
    @overload
    def actual(self, option: None, displayof: tkinter.Misc | None = None) -> _FontDict: ...
    @overload
    def actual(self, *, displayof: tkinter.Misc | None = None) -> _FontDict: ...
    def config(
        self,
        *,
        family: str = ...,
        size: int = ...,
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = ...,
        overstrike: bool = ...,
    ) -> _FontDict | None: ...
    configure = config
    def copy(self) -> Font: ...
    @overload
    def metrics(self, option: Literal["ascent", "descent", "linespace"], /, *, displayof: tkinter.Misc | None = ...) -> int: ...
    @overload
    def metrics(self, option: Literal["fixed"], /, *, displayof: tkinter.Misc | None = ...) -> bool: ...
    @overload
    def metrics(self, *, displayof: tkinter.Misc | None = ...) -> _MetricsDict: ...
    def measure(self, text: str, displayof: tkinter.Misc | None = None) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __del__(self) -> None: ...

def families(root: tkinter.Misc | None = None, displayof: tkinter.Misc | None = None) -> tuple[str, ...]: ...
def names(root: tkinter.Misc | None = None) -> tuple[str, ...]: ...

if sys.version_info >= (3, 10):
    def nametofont(name: str, root: tkinter.Misc | None = None) -> Font: ...

else:
    def nametofont(name: str) -> Font: ...
