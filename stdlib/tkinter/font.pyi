import _tkinter
import itertools
import sys
import tkinter as tk
from typing import Any, ClassVar, Final, Literal, TypedDict, overload
from typing_extensions import TypeAlias, Unpack

if sys.version_info >= (3, 9):
    __all__ = ["NORMAL", "ROMAN", "BOLD", "ITALIC", "nametofont", "Font", "families", "names"]

NORMAL: Final = "normal"
ROMAN: Final = "roman"
BOLD: Final = "bold"
ITALIC: Final = "italic"

_FontDescription: TypeAlias = (
    str  # "Helvetica 12"
    | Font  # A font object constructed in Python
    | list[Any]  # ["Helvetica", 12, BOLD]
    | tuple[str]  # ("Liberation Sans",) needs wrapping in tuple/list to handle spaces
    # ("Liberation Sans", 12) or ("Liberation Sans", 12, "bold", "italic", "underline")
    | tuple[str, int, Unpack[tuple[str, ...]]]  # Any number of trailing options is permitted
    | tuple[str, int, list[str] | tuple[str, ...]]  # Options can also be passed as list/tuple
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
    counter: ClassVar[itertools.count[int]]  # undocumented
    def __init__(
        self,
        # In tkinter, 'root' refers to tkinter.Tk by convention, but the code
        # actually works with any tkinter widget so we use tkinter.Misc.
        root: tk.Misc | None = None,
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
    __hash__: ClassVar[None]  # type: ignore[assignment]
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
    def actual(self, option: Literal["family"], displayof: tk.Misc | None = None) -> str: ...
    @overload
    def actual(self, option: Literal["size"], displayof: tk.Misc | None = None) -> int: ...
    @overload
    def actual(self, option: Literal["weight"], displayof: tk.Misc | None = None) -> Literal["normal", "bold"]: ...
    @overload
    def actual(self, option: Literal["slant"], displayof: tk.Misc | None = None) -> Literal["roman", "italic"]: ...
    @overload
    def actual(self, option: Literal["underline", "overstrike"], displayof: tk.Misc | None = None) -> bool: ...
    @overload
    def actual(self, option: None, displayof: tk.Misc | None = None) -> _FontDict: ...
    @overload
    def actual(self, *, displayof: tk.Misc | None = None) -> _FontDict: ...
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
    def metrics(self, option: Literal["ascent", "descent", "linespace"], /, *, displayof: tk.Misc | None = ...) -> int: ...
    @overload
    def metrics(self, option: Literal["fixed"], /, *, displayof: tk.Misc | None = ...) -> bool: ...
    @overload
    def metrics(self, *, displayof: tk.Misc | None = ...) -> _MetricsDict: ...
    def measure(self, text: str, displayof: tk.Misc | None = None) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __del__(self) -> None: ...

def families(root: tk.Misc | None = None, displayof: tk.Misc | None = None) -> tuple[str, ...]: ...
def names(root: tk.Misc | None = None) -> tuple[str, ...]: ...

if sys.version_info >= (3, 10):
    def nametofont(name: str, root: tk.Misc | None = None) -> Font: ...

else:
    def nametofont(name: str) -> Font: ...
