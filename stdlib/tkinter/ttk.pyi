import _tkinter
import tkinter as tk
from _typeshed import Incomplete, MaybeNone
from collections.abc import Callable
from tkinter.font import _FontDescription
from typing import Any, Literal, TypedDict, overload
from typing_extensions import TypeAlias

__all__ = [
    "Button",
    "Checkbutton",
    "Combobox",
    "Entry",
    "Frame",
    "Label",
    "Labelframe",
    "LabelFrame",
    "Menubutton",
    "Notebook",
    "Panedwindow",
    "PanedWindow",
    "Progressbar",
    "Radiobutton",
    "Scale",
    "Scrollbar",
    "Separator",
    "Sizegrip",
    "Style",
    "Treeview",
    "LabeledScale",
    "OptionMenu",
    "tclobjs_to_py",
    "setup_master",
    "Spinbox",
]

def tclobjs_to_py(adict: dict[Any, Any]) -> dict[Any, Any]: ...
def setup_master(master: Incomplete | None = None): ...

_Padding: TypeAlias = (
    tk._ScreenUnits
    | tuple[tk._ScreenUnits]
    | tuple[tk._ScreenUnits, tk._ScreenUnits]
    | tuple[tk._ScreenUnits, tk._ScreenUnits, tk._ScreenUnits]
    | tuple[tk._ScreenUnits, tk._ScreenUnits, tk._ScreenUnits, tk._ScreenUnits]
)

# from ttk_widget (aka ttk::widget) manual page, differs from tkinter._Compound
_TtkCompound: TypeAlias = Literal["", "text", "image", tk._Compound]

class Style:
    master: Incomplete
    tk: _tkinter.TkappType
    def __init__(self, master: tk.Misc | None = None) -> None: ...
    def configure(self, style, query_opt: Incomplete | None = None, **kw): ...
    def map(self, style, query_opt: Incomplete | None = None, **kw): ...
    def lookup(self, style, option, state: Incomplete | None = None, default: Incomplete | None = None): ...
    def layout(self, style, layoutspec: Incomplete | None = None): ...
    def element_create(self, elementname, etype, *args, **kw) -> None: ...
    def element_names(self): ...
    def element_options(self, elementname): ...
    def theme_create(self, themename, parent: Incomplete | None = None, settings: Incomplete | None = None) -> None: ...
    def theme_settings(self, themename, settings) -> None: ...
    def theme_names(self) -> tuple[str, ...]: ...
    @overload
    def theme_use(self, themename: str) -> None: ...
    @overload
    def theme_use(self, themename: None = None) -> str: ...

class Widget(tk.Widget):
    def __init__(self, master: tk.Misc | None, widgetname, kw: Incomplete | None = None) -> None: ...
    def identify(self, x: int, y: int) -> str: ...
    def instate(self, statespec, callback: Incomplete | None = None, *args, **kw): ...
    def state(self, statespec: Incomplete | None = None): ...

class Button(Widget):
    def __init__(
        self,
        master: tk.Misc | None = None,
        *,
        class_: str = "",
        command: tk._ButtonCommand = "",
        compound: _TtkCompound = "",
        cursor: tk._Cursor = "",
        default: Literal["normal", "active", "disabled"] = "normal",
        image: tk._ImageSpec = "",
        name: str = ...,
        padding=...,  # undocumented
        state: str = "normal",
        style: str = "",
        takefocus: tk._TakeFocusValue = ...,
        text: float | str = "",
        textvariable: tk.Variable = ...,
        underline: int = -1,
        width: int | Literal[""] = "",
    ) -> None: ...
    @overload
    def configure(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        command: tk._ButtonCommand = ...,
        compound: _TtkCompound = ...,
        cursor: tk._Cursor = ...,
        default: Literal["normal", "active", "disabled"] = ...,
        image: tk._ImageSpec = ...,
        padding=...,
        state: str = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
        text: float | str = ...,
        textvariable: tk.Variable = ...,
        underline: int = ...,
        width: int | Literal[""] = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def configure(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...
    config = configure
    def invoke(self) -> Any: ...

class Checkbutton(Widget):
    def __init__(
        self,
        master: tk.Misc | None = None,
        *,
        class_: str = "",
        command: tk._ButtonCommand = "",
        compound: _TtkCompound = "",
        cursor: tk._Cursor = "",
        image: tk._ImageSpec = "",
        name: str = ...,
        offvalue: Any = 0,
        onvalue: Any = 1,
        padding=...,  # undocumented
        state: str = "normal",
        style: str = "",
        takefocus: tk._TakeFocusValue = ...,
        text: float | str = "",
        textvariable: tk.Variable = ...,
        underline: int = -1,
        # Seems like variable can be empty string, but actually setting it to
        # empty string segfaults before Tcl 8.6.9. Search for ttk::checkbutton
        # here: https://sourceforge.net/projects/tcl/files/Tcl/8.6.9/tcltk-release-notes-8.6.9.txt/view
        variable: tk.Variable = ...,
        width: int | Literal[""] = "",
    ) -> None: ...
    @overload
    def configure(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        command: tk._ButtonCommand = ...,
        compound: _TtkCompound = ...,
        cursor: tk._Cursor = ...,
        image: tk._ImageSpec = ...,
        offvalue: Any = ...,
        onvalue: Any = ...,
        padding=...,
        state: str = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
        text: float | str = ...,
        textvariable: tk.Variable = ...,
        underline: int = ...,
        variable: tk.Variable = ...,
        width: int | Literal[""] = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def configure(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...
    config = configure
    def invoke(self) -> Any: ...

class Entry(Widget, tk.Entry):
    def __init__(
        self,
        master: tk.Misc | None = None,
        widget: str | None = None,
        *,
        background: str = ...,  # undocumented
        class_: str = "",
        cursor: tk._Cursor = ...,
        exportselection: bool = True,
        font: _FontDescription = "TkTextFont",
        foreground: str = "",
        invalidcommand: tk._EntryValidateCommand = "",
        justify: Literal["left", "center", "right"] = "left",
        name: str = ...,
        show: str = "",
        state: str = "normal",
        style: str = "",
        takefocus: tk._TakeFocusValue = ...,
        textvariable: tk.Variable = ...,
        validate: Literal["none", "focus", "focusin", "focusout", "key", "all"] = "none",
        validatecommand: tk._EntryValidateCommand = "",
        width: int = 20,
        xscrollcommand: tk._XYScrollCommand = "",
    ) -> None: ...
    @overload  # type: ignore[override]
    def configure(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        background: str = ...,
        cursor: tk._Cursor = ...,
        exportselection: bool = ...,
        font: _FontDescription = ...,
        foreground: str = ...,
        invalidcommand: tk._EntryValidateCommand = ...,
        justify: Literal["left", "center", "right"] = ...,
        show: str = ...,
        state: str = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
        textvariable: tk.Variable = ...,
        validate: Literal["none", "focus", "focusin", "focusout", "key", "all"] = ...,
        validatecommand: tk._EntryValidateCommand = ...,
        width: int = ...,
        xscrollcommand: tk._XYScrollCommand = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def configure(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...
    # config must be copy/pasted, otherwise ttk.Entry().config is mypy error (don't know why)
    @overload  # type: ignore[override]
    def config(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        background: str = ...,
        cursor: tk._Cursor = ...,
        exportselection: bool = ...,
        font: _FontDescription = ...,
        foreground: str = ...,
        invalidcommand: tk._EntryValidateCommand = ...,
        justify: Literal["left", "center", "right"] = ...,
        show: str = ...,
        state: str = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
        textvariable: tk.Variable = ...,
        validate: Literal["none", "focus", "focusin", "focusout", "key", "all"] = ...,
        validatecommand: tk._EntryValidateCommand = ...,
        width: int = ...,
        xscrollcommand: tk._XYScrollCommand = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def config(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...
    def bbox(self, index) -> tuple[int, int, int, int]: ...  # type: ignore[override]
    def identify(self, x: int, y: int) -> str: ...
    def validate(self): ...

class Combobox(Entry):
    def __init__(
        self,
        master: tk.Misc | None = None,
        *,
        background: str = ...,  # undocumented
        class_: str = "",
        cursor: tk._Cursor = "",
        exportselection: bool = True,
        font: _FontDescription = ...,  # undocumented
        foreground: str = ...,  # undocumented
        height: int = 10,
        invalidcommand: tk._EntryValidateCommand = ...,  # undocumented
        justify: Literal["left", "center", "right"] = "left",
        name: str = ...,
        postcommand: Callable[[], object] | str = "",
        show=...,  # undocumented
        state: str = "normal",
        style: str = "",
        takefocus: tk._TakeFocusValue = ...,
        textvariable: tk.Variable = ...,
        validate: Literal["none", "focus", "focusin", "focusout", "key", "all"] = ...,  # undocumented
        validatecommand: tk._EntryValidateCommand = ...,  # undocumented
        values: list[str] | tuple[str, ...] = ...,
        width: int = 20,
        xscrollcommand: tk._XYScrollCommand = ...,  # undocumented
    ) -> None: ...
    @overload  # type: ignore[override]
    def configure(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        background: str = ...,
        cursor: tk._Cursor = ...,
        exportselection: bool = ...,
        font: _FontDescription = ...,
        foreground: str = ...,
        height: int = ...,
        invalidcommand: tk._EntryValidateCommand = ...,
        justify: Literal["left", "center", "right"] = ...,
        postcommand: Callable[[], object] | str = ...,
        show=...,
        state: str = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
        textvariable: tk.Variable = ...,
        validate: Literal["none", "focus", "focusin", "focusout", "key", "all"] = ...,
        validatecommand: tk._EntryValidateCommand = ...,
        values: list[str] | tuple[str, ...] = ...,
        width: int = ...,
        xscrollcommand: tk._XYScrollCommand = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def configure(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...
    # config must be copy/pasted, otherwise ttk.Combobox().config is mypy error (don't know why)
    @overload  # type: ignore[override]
    def config(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        background: str = ...,
        cursor: tk._Cursor = ...,
        exportselection: bool = ...,
        font: _FontDescription = ...,
        foreground: str = ...,
        height: int = ...,
        invalidcommand: tk._EntryValidateCommand = ...,
        justify: Literal["left", "center", "right"] = ...,
        postcommand: Callable[[], object] | str = ...,
        show=...,
        state: str = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
        textvariable: tk.Variable = ...,
        validate: Literal["none", "focus", "focusin", "focusout", "key", "all"] = ...,
        validatecommand: tk._EntryValidateCommand = ...,
        values: list[str] | tuple[str, ...] = ...,
        width: int = ...,
        xscrollcommand: tk._XYScrollCommand = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def config(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...
    def current(self, newindex: int | None = None) -> int: ...
    def set(self, value: Any) -> None: ...

class Frame(Widget):
    # This should be kept in sync with tkinter.ttk.LabeledScale.__init__()
    # (all of these keyword-only arguments are also present there)
    def __init__(
        self,
        master: tk.Misc | None = None,
        *,
        border: tk._ScreenUnits = ...,
        borderwidth: tk._ScreenUnits = ...,
        class_: str = "",
        cursor: tk._Cursor = "",
        height: tk._ScreenUnits = 0,
        name: str = ...,
        padding: _Padding = ...,
        relief: tk._Relief = ...,
        style: str = "",
        takefocus: tk._TakeFocusValue = "",
        width: tk._ScreenUnits = 0,
    ) -> None: ...
    @overload
    def configure(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        border: tk._ScreenUnits = ...,
        borderwidth: tk._ScreenUnits = ...,
        cursor: tk._Cursor = ...,
        height: tk._ScreenUnits = ...,
        padding: _Padding = ...,
        relief: tk._Relief = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
        width: tk._ScreenUnits = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def configure(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...
    config = configure

class Label(Widget):
    def __init__(
        self,
        master: tk.Misc | None = None,
        *,
        anchor: tk._Anchor = ...,
        background: str = "",
        border: tk._ScreenUnits = ...,  # alias for borderwidth
        borderwidth: tk._ScreenUnits = ...,  # undocumented
        class_: str = "",
        compound: _TtkCompound = "",
        cursor: tk._Cursor = "",
        font: _FontDescription = ...,
        foreground: str = "",
        image: tk._ImageSpec = "",
        justify: Literal["left", "center", "right"] = ...,
        name: str = ...,
        padding: _Padding = ...,
        relief: tk._Relief = ...,
        state: str = "normal",
        style: str = "",
        takefocus: tk._TakeFocusValue = "",
        text: float | str = "",
        textvariable: tk.Variable = ...,
        underline: int = -1,
        width: int | Literal[""] = "",
        wraplength: tk._ScreenUnits = ...,
    ) -> None: ...
    @overload
    def configure(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        anchor: tk._Anchor = ...,
        background: str = ...,
        border: tk._ScreenUnits = ...,
        borderwidth: tk._ScreenUnits = ...,
        compound: _TtkCompound = ...,
        cursor: tk._Cursor = ...,
        font: _FontDescription = ...,
        foreground: str = ...,
        image: tk._ImageSpec = ...,
        justify: Literal["left", "center", "right"] = ...,
        padding: _Padding = ...,
        relief: tk._Relief = ...,
        state: str = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
        text: float | str = ...,
        textvariable: tk.Variable = ...,
        underline: int = ...,
        width: int | Literal[""] = ...,
        wraplength: tk._ScreenUnits = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def configure(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...
    config = configure

class Labelframe(Widget):
    def __init__(
        self,
        master: tk.Misc | None = None,
        *,
        border: tk._ScreenUnits = ...,
        borderwidth: tk._ScreenUnits = ...,  # undocumented
        class_: str = "",
        cursor: tk._Cursor = "",
        height: tk._ScreenUnits = 0,
        labelanchor: Literal["nw", "n", "ne", "en", "e", "es", "se", "s", "sw", "ws", "w", "wn"] = ...,
        labelwidget: tk.Misc = ...,
        name: str = ...,
        padding: _Padding = ...,
        relief: tk._Relief = ...,  # undocumented
        style: str = "",
        takefocus: tk._TakeFocusValue = "",
        text: float | str = "",
        underline: int = -1,
        width: tk._ScreenUnits = 0,
    ) -> None: ...
    @overload
    def configure(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        border: tk._ScreenUnits = ...,
        borderwidth: tk._ScreenUnits = ...,
        cursor: tk._Cursor = ...,
        height: tk._ScreenUnits = ...,
        labelanchor: Literal["nw", "n", "ne", "en", "e", "es", "se", "s", "sw", "ws", "w", "wn"] = ...,
        labelwidget: tk.Misc = ...,
        padding: _Padding = ...,
        relief: tk._Relief = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
        text: float | str = ...,
        underline: int = ...,
        width: tk._ScreenUnits = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def configure(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...
    config = configure

LabelFrame = Labelframe

class Menubutton(Widget):
    def __init__(
        self,
        master: tk.Misc | None = None,
        *,
        class_: str = "",
        compound: _TtkCompound = "",
        cursor: tk._Cursor = "",
        direction: Literal["above", "below", "left", "right", "flush"] = "below",
        image: tk._ImageSpec = "",
        menu: tk.Menu = ...,
        name: str = ...,
        padding=...,  # undocumented
        state: str = "normal",
        style: str = "",
        takefocus: tk._TakeFocusValue = ...,
        text: float | str = "",
        textvariable: tk.Variable = ...,
        underline: int = -1,
        width: int | Literal[""] = "",
    ) -> None: ...
    @overload
    def configure(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        compound: _TtkCompound = ...,
        cursor: tk._Cursor = ...,
        direction: Literal["above", "below", "left", "right", "flush"] = ...,
        image: tk._ImageSpec = ...,
        menu: tk.Menu = ...,
        padding=...,
        state: str = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
        text: float | str = ...,
        textvariable: tk.Variable = ...,
        underline: int = ...,
        width: int | Literal[""] = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def configure(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...
    config = configure

class Notebook(Widget):
    def __init__(
        self,
        master: tk.Misc | None = None,
        *,
        class_: str = "",
        cursor: tk._Cursor = "",
        height: int = 0,
        name: str = ...,
        padding: _Padding = ...,
        style: str = "",
        takefocus: tk._TakeFocusValue = ...,
        width: int = 0,
    ) -> None: ...
    @overload
    def configure(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        cursor: tk._Cursor = ...,
        height: int = ...,
        padding: _Padding = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
        width: int = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def configure(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...
    config = configure
    def add(
        self,
        child: tk.Widget,
        *,
        state: Literal["normal", "disabled", "hidden"] = ...,
        sticky: str = ...,  # consists of letters 'n', 's', 'w', 'e', no repeats, may be empty
        padding: _Padding = ...,
        text: str = ...,
        # `image` is a sequence of an image name, followed by zero or more
        # (sequences of one or more state names followed by an image name)
        image=...,
        compound: tk._Compound = ...,
        underline: int = ...,
    ) -> None: ...
    def forget(self, tab_id) -> None: ...
    def hide(self, tab_id) -> None: ...
    def identify(self, x: int, y: int) -> str: ...
    def index(self, tab_id): ...
    def insert(self, pos, child, **kw) -> None: ...
    def select(self, tab_id: Incomplete | None = None): ...
    def tab(self, tab_id, option: Incomplete | None = None, **kw): ...
    def tabs(self): ...
    def enable_traversal(self) -> None: ...

class Panedwindow(Widget, tk.PanedWindow):
    def __init__(
        self,
        master: tk.Misc | None = None,
        *,
        class_: str = "",
        cursor: tk._Cursor = "",
        # width and height for tkinter.ttk.Panedwindow are int but for tkinter.PanedWindow they are screen units
        height: int = 0,
        name: str = ...,
        orient: Literal["vertical", "horizontal"] = "vertical",  # can't be changed with configure()
        style: str = "",
        takefocus: tk._TakeFocusValue = "",
        width: int = 0,
    ) -> None: ...
    def add(self, child: tk.Widget, *, weight: int = ..., **kw) -> None: ...
    @overload  # type: ignore[override]
    def configure(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        cursor: tk._Cursor = ...,
        height: int = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
        width: int = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def configure(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...
    # config must be copy/pasted, otherwise ttk.Panedwindow().config is mypy error (don't know why)
    @overload  # type: ignore[override]
    def config(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        cursor: tk._Cursor = ...,
        height: int = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
        width: int = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def config(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...
    forget: Incomplete
    def insert(self, pos, child, **kw) -> None: ...
    def pane(self, pane, option: Incomplete | None = None, **kw): ...
    def sashpos(self, index, newpos: Incomplete | None = None): ...

PanedWindow = Panedwindow

class Progressbar(Widget):
    def __init__(
        self,
        master: tk.Misc | None = None,
        *,
        class_: str = "",
        cursor: tk._Cursor = "",
        length: tk._ScreenUnits = 100,
        maximum: float = 100,
        mode: Literal["determinate", "indeterminate"] = "determinate",
        name: str = ...,
        orient: Literal["horizontal", "vertical"] = "horizontal",
        phase: int = 0,  # docs say read-only but assigning int to this works
        style: str = "",
        takefocus: tk._TakeFocusValue = "",
        value: float = 0.0,
        variable: tk.IntVar | tk.DoubleVar = ...,
    ) -> None: ...
    @overload
    def configure(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        cursor: tk._Cursor = ...,
        length: tk._ScreenUnits = ...,
        maximum: float = ...,
        mode: Literal["determinate", "indeterminate"] = ...,
        orient: Literal["horizontal", "vertical"] = ...,
        phase: int = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
        value: float = ...,
        variable: tk.IntVar | tk.DoubleVar = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def configure(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...
    config = configure
    def start(self, interval: Literal["idle"] | int | None = None) -> None: ...
    def step(self, amount: float | None = None) -> None: ...
    def stop(self) -> None: ...

class Radiobutton(Widget):
    def __init__(
        self,
        master: tk.Misc | None = None,
        *,
        class_: str = "",
        command: tk._ButtonCommand = "",
        compound: _TtkCompound = "",
        cursor: tk._Cursor = "",
        image: tk._ImageSpec = "",
        name: str = ...,
        padding=...,  # undocumented
        state: str = "normal",
        style: str = "",
        takefocus: tk._TakeFocusValue = ...,
        text: float | str = "",
        textvariable: tk.Variable = ...,
        underline: int = -1,
        value: Any = "1",
        variable: tk.Variable | Literal[""] = ...,
        width: int | Literal[""] = "",
    ) -> None: ...
    @overload
    def configure(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        command: tk._ButtonCommand = ...,
        compound: _TtkCompound = ...,
        cursor: tk._Cursor = ...,
        image: tk._ImageSpec = ...,
        padding=...,
        state: str = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
        text: float | str = ...,
        textvariable: tk.Variable = ...,
        underline: int = ...,
        value: Any = ...,
        variable: tk.Variable | Literal[""] = ...,
        width: int | Literal[""] = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def configure(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...
    config = configure
    def invoke(self) -> Any: ...

# type ignore, because identify() methods of Widget and tkinter.Scale are incompatible
class Scale(Widget, tk.Scale):  # type: ignore[misc]
    def __init__(
        self,
        master: tk.Misc | None = None,
        *,
        class_: str = "",
        command: str | Callable[[str], object] = "",
        cursor: tk._Cursor = "",
        from_: float = 0,
        length: tk._ScreenUnits = 100,
        name: str = ...,
        orient: Literal["horizontal", "vertical"] = "horizontal",
        state: str = ...,  # undocumented
        style: str = "",
        takefocus: tk._TakeFocusValue = ...,
        to: float = 1.0,
        value: float = 0,
        variable: tk.IntVar | tk.DoubleVar = ...,
    ) -> None: ...
    @overload  # type: ignore[override]
    def configure(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        command: str | Callable[[str], object] = ...,
        cursor: tk._Cursor = ...,
        from_: float = ...,
        length: tk._ScreenUnits = ...,
        orient: Literal["horizontal", "vertical"] = ...,
        state: str = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
        to: float = ...,
        value: float = ...,
        variable: tk.IntVar | tk.DoubleVar = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def configure(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...
    # config must be copy/pasted, otherwise ttk.Scale().config is mypy error (don't know why)
    @overload  # type: ignore[override]
    def config(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        command: str | Callable[[str], object] = ...,
        cursor: tk._Cursor = ...,
        from_: float = ...,
        length: tk._ScreenUnits = ...,
        orient: Literal["horizontal", "vertical"] = ...,
        state: str = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
        to: float = ...,
        value: float = ...,
        variable: tk.IntVar | tk.DoubleVar = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def config(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...
    def get(self, x: int | None = None, y: int | None = None) -> float: ...

# type ignore, because identify() methods of Widget and tkinter.Scale are incompatible
class Scrollbar(Widget, tk.Scrollbar):  # type: ignore[misc]
    def __init__(
        self,
        master: tk.Misc | None = None,
        *,
        class_: str = "",
        command: Callable[..., tuple[float, float] | None] | str = "",
        cursor: tk._Cursor = "",
        name: str = ...,
        orient: Literal["horizontal", "vertical"] = "vertical",
        style: str = "",
        takefocus: tk._TakeFocusValue = "",
    ) -> None: ...
    @overload  # type: ignore[override]
    def configure(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        command: Callable[..., tuple[float, float] | None] | str = ...,
        cursor: tk._Cursor = ...,
        orient: Literal["horizontal", "vertical"] = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def configure(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...
    # config must be copy/pasted, otherwise ttk.Scrollbar().config is mypy error (don't know why)
    @overload  # type: ignore[override]
    def config(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        command: Callable[..., tuple[float, float] | None] | str = ...,
        cursor: tk._Cursor = ...,
        orient: Literal["horizontal", "vertical"] = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def config(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...

class Separator(Widget):
    def __init__(
        self,
        master: tk.Misc | None = None,
        *,
        class_: str = "",
        cursor: tk._Cursor = "",
        name: str = ...,
        orient: Literal["horizontal", "vertical"] = "horizontal",
        style: str = "",
        takefocus: tk._TakeFocusValue = "",
    ) -> None: ...
    @overload
    def configure(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        cursor: tk._Cursor = ...,
        orient: Literal["horizontal", "vertical"] = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def configure(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...
    config = configure

class Sizegrip(Widget):
    def __init__(
        self,
        master: tk.Misc | None = None,
        *,
        class_: str = "",
        cursor: tk._Cursor = ...,
        name: str = ...,
        style: str = "",
        takefocus: tk._TakeFocusValue = "",
    ) -> None: ...
    @overload
    def configure(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        cursor: tk._Cursor = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def configure(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...
    config = configure

class Spinbox(Entry):
    def __init__(
        self,
        master: tk.Misc | None = None,
        *,
        background: str = ...,  # undocumented
        class_: str = "",
        command: Callable[[], object] | str | list[str] | tuple[str, ...] = "",
        cursor: tk._Cursor = "",
        exportselection: bool = ...,  # undocumented
        font: _FontDescription = ...,  # undocumented
        foreground: str = ...,  # undocumented
        format: str = "",
        from_: float = 0,
        increment: float = 1,
        invalidcommand: tk._EntryValidateCommand = ...,  # undocumented
        justify: Literal["left", "center", "right"] = ...,  # undocumented
        name: str = ...,
        show=...,  # undocumented
        state: str = "normal",
        style: str = "",
        takefocus: tk._TakeFocusValue = ...,
        textvariable: tk.Variable = ...,  # undocumented
        to: float = 0,
        validate: Literal["none", "focus", "focusin", "focusout", "key", "all"] = "none",
        validatecommand: tk._EntryValidateCommand = "",
        values: list[str] | tuple[str, ...] = ...,
        width: int = ...,  # undocumented
        wrap: bool = False,
        xscrollcommand: tk._XYScrollCommand = "",
    ) -> None: ...
    @overload  # type: ignore[override]
    def configure(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        background: str = ...,
        command: Callable[[], object] | str | list[str] | tuple[str, ...] = ...,
        cursor: tk._Cursor = ...,
        exportselection: bool = ...,
        font: _FontDescription = ...,
        foreground: str = ...,
        format: str = ...,
        from_: float = ...,
        increment: float = ...,
        invalidcommand: tk._EntryValidateCommand = ...,
        justify: Literal["left", "center", "right"] = ...,
        show=...,
        state: str = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
        textvariable: tk.Variable = ...,
        to: float = ...,
        validate: Literal["none", "focus", "focusin", "focusout", "key", "all"] = ...,
        validatecommand: tk._EntryValidateCommand = ...,
        values: list[str] | tuple[str, ...] = ...,
        width: int = ...,
        wrap: bool = ...,
        xscrollcommand: tk._XYScrollCommand = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def configure(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...
    config = configure  # type: ignore[assignment]
    def set(self, value: Any) -> None: ...

class _TreeviewItemDict(TypedDict):
    text: str
    image: list[str] | Literal[""]  # no idea why it's wrapped in list
    values: list[Any] | Literal[""]
    open: bool  # actually 0 or 1
    tags: list[str] | Literal[""]

class _TreeviewTagDict(TypedDict):
    # There is also 'text' and 'anchor', but they don't seem to do anything, using them is likely a bug
    foreground: str
    background: str
    font: _FontDescription
    image: str  # not wrapped in list :D

class _TreeviewHeaderDict(TypedDict):
    text: str
    image: list[str] | Literal[""]
    anchor: tk._Anchor
    command: str
    state: str  # Doesn't seem to appear anywhere else than in these dicts

class _TreeviewColumnDict(TypedDict):
    width: int
    minwidth: int
    stretch: bool  # actually 0 or 1
    anchor: tk._Anchor
    id: str

class Treeview(Widget, tk.XView, tk.YView):
    def __init__(
        self,
        master: tk.Misc | None = None,
        *,
        class_: str = "",
        columns: str | list[str] | list[int] | list[str | int] | tuple[str | int, ...] = "",
        cursor: tk._Cursor = "",
        displaycolumns: str | int | list[str] | tuple[str, ...] | list[int] | tuple[int, ...] = ("#all",),
        height: int = 10,
        name: str = ...,
        padding: _Padding = ...,
        selectmode: Literal["extended", "browse", "none"] = "extended",
        # list/tuple of Literal don't actually work in mypy
        #
        # 'tree headings' is same as ['tree', 'headings'], and I wouldn't be
        # surprised if someone is using it.
        show: Literal["tree", "headings", "tree headings", ""] | list[str] | tuple[str, ...] = ("tree", "headings"),
        style: str = "",
        takefocus: tk._TakeFocusValue = ...,
        xscrollcommand: tk._XYScrollCommand = "",
        yscrollcommand: tk._XYScrollCommand = "",
    ) -> None: ...
    @overload
    def configure(
        self,
        cnf: dict[str, Any] | None = None,
        *,
        columns: str | list[str] | list[int] | list[str | int] | tuple[str | int, ...] = ...,
        cursor: tk._Cursor = ...,
        displaycolumns: str | int | list[str] | tuple[str, ...] | list[int] | tuple[int, ...] = ...,
        height: int = ...,
        padding: _Padding = ...,
        selectmode: Literal["extended", "browse", "none"] = ...,
        show: Literal["tree", "headings", "tree headings", ""] | list[str] | tuple[str, ...] = ...,
        style: str = ...,
        takefocus: tk._TakeFocusValue = ...,
        xscrollcommand: tk._XYScrollCommand = ...,
        yscrollcommand: tk._XYScrollCommand = ...,
    ) -> dict[str, tuple[str, str, str, Any, Any]] | None: ...
    @overload
    def configure(self, cnf: str) -> tuple[str, str, str, Any, Any]: ...
    config = configure
    def bbox(self, item: str | int, column: str | int | None = None) -> tuple[int, int, int, int] | Literal[""]: ...  # type: ignore[override]
    def get_children(self, item: str | int | None = None) -> tuple[str, ...]: ...
    def set_children(self, item: str | int, *newchildren: str | int) -> None: ...
    @overload
    def column(self, column: str | int, option: Literal["width", "minwidth"]) -> int: ...
    @overload
    def column(self, column: str | int, option: Literal["stretch"]) -> bool: ...  # actually 0 or 1
    @overload
    def column(self, column: str | int, option: Literal["anchor"]) -> _tkinter.Tcl_Obj: ...
    @overload
    def column(self, column: str | int, option: Literal["id"]) -> str: ...
    @overload
    def column(self, column: str | int, option: str) -> Any: ...
    @overload
    def column(
        self,
        column: str | int,
        option: None = None,
        *,
        width: int = ...,
        minwidth: int = ...,
        stretch: bool = ...,
        anchor: tk._Anchor = ...,
        # id is read-only
    ) -> _TreeviewColumnDict | None: ...
    def delete(self, *items: str | int) -> None: ...
    def detach(self, *items: str | int) -> None: ...
    def exists(self, item: str | int) -> bool: ...
    @overload  # type: ignore[override]
    def focus(self, item: None = None) -> str: ...  # can return empty string
    @overload
    def focus(self, item: str | int) -> Literal[""]: ...
    @overload
    def heading(self, column: str | int, option: Literal["text"]) -> str: ...
    @overload
    def heading(self, column: str | int, option: Literal["image"]) -> tuple[str] | str: ...
    @overload
    def heading(self, column: str | int, option: Literal["anchor"]) -> _tkinter.Tcl_Obj: ...
    @overload
    def heading(self, column: str | int, option: Literal["command"]) -> str: ...
    @overload
    def heading(self, column: str | int, option: str) -> Any: ...
    @overload
    def heading(self, column: str | int, option: None = None) -> _TreeviewHeaderDict: ...
    @overload
    def heading(
        self,
        column: str | int,
        option: None = None,
        *,
        text: str = ...,
        image: tk._ImageSpec = ...,
        anchor: tk._Anchor = ...,
        command: str | Callable[[], object] = ...,
    ) -> None: ...
    # Internal Method. Leave untyped:
    def identify(self, component, x, y): ...  # type: ignore[override]
    def identify_row(self, y: int) -> str: ...
    def identify_column(self, x: int) -> str: ...
    def identify_region(self, x: int, y: int) -> Literal["heading", "separator", "tree", "cell", "nothing"]: ...
    def identify_element(self, x: int, y: int) -> str: ...  # don't know what possible return values are
    def index(self, item: str | int) -> int: ...
    def insert(
        self,
        parent: str,
        index: int | Literal["end"],
        iid: str | int | None = None,
        *,
        id: str | int = ...,  # same as iid
        text: str = ...,
        image: tk._ImageSpec = ...,
        values: list[Any] | tuple[Any, ...] = ...,
        open: bool = ...,
        tags: str | list[str] | tuple[str, ...] = ...,
    ) -> str: ...
    @overload
    def item(self, item: str | int, option: Literal["text"]) -> str: ...
    @overload
    def item(self, item: str | int, option: Literal["image"]) -> tuple[str] | Literal[""]: ...
    @overload
    def item(self, item: str | int, option: Literal["values"]) -> tuple[Any, ...] | Literal[""]: ...
    @overload
    def item(self, item: str | int, option: Literal["open"]) -> bool: ...  # actually 0 or 1
    @overload
    def item(self, item: str | int, option: Literal["tags"]) -> tuple[str, ...] | Literal[""]: ...
    @overload
    def item(self, item: str | int, option: str) -> Any: ...
    @overload
    def item(self, item: str | int, option: None = None) -> _TreeviewItemDict: ...
    @overload
    def item(
        self,
        item: str | int,
        option: None = None,
        *,
        text: str = ...,
        image: tk._ImageSpec = ...,
        values: list[Any] | tuple[Any, ...] | Literal[""] = ...,
        open: bool = ...,
        tags: str | list[str] | tuple[str, ...] = ...,
    ) -> None: ...
    def move(self, item: str | int, parent: str, index: int | Literal["end"]) -> None: ...
    reattach = move
    def next(self, item: str | int) -> str: ...  # returning empty string means last item
    def parent(self, item: str | int) -> str: ...
    def prev(self, item: str | int) -> str: ...  # returning empty string means first item
    def see(self, item: str | int) -> None: ...
    def selection(self) -> tuple[str, ...]: ...
    @overload
    def selection_set(self, items: list[str] | tuple[str, ...] | list[int] | tuple[int, ...], /) -> None: ...
    @overload
    def selection_set(self, *items: str | int) -> None: ...
    @overload
    def selection_add(self, items: list[str] | tuple[str, ...] | list[int] | tuple[int, ...], /) -> None: ...
    @overload
    def selection_add(self, *items: str | int) -> None: ...
    @overload
    def selection_remove(self, items: list[str] | tuple[str, ...] | list[int] | tuple[int, ...], /) -> None: ...
    @overload
    def selection_remove(self, *items: str | int) -> None: ...
    @overload
    def selection_toggle(self, items: list[str] | tuple[str, ...] | list[int] | tuple[int, ...], /) -> None: ...
    @overload
    def selection_toggle(self, *items: str | int) -> None: ...
    @overload
    def set(self, item: str | int, column: None = None, value: None = None) -> dict[str, Any]: ...
    @overload
    def set(self, item: str | int, column: str | int, value: None = None) -> Any: ...
    @overload
    def set(self, item: str | int, column: str | int, value: Any) -> Literal[""]: ...
    # There's no tag_unbind() or 'add' argument for whatever reason.
    # Also, it's 'callback' instead of 'func' here.
    @overload
    def tag_bind(
        self, tagname: str, sequence: str | None = None, callback: Callable[[tk.Event[Treeview]], object] | None = None
    ) -> str: ...
    @overload
    def tag_bind(self, tagname: str, sequence: str | None, callback: str) -> None: ...
    @overload
    def tag_bind(self, tagname: str, *, callback: str) -> None: ...
    @overload
    def tag_configure(self, tagname: str, option: Literal["foreground", "background"]) -> str: ...
    @overload
    def tag_configure(self, tagname: str, option: Literal["font"]) -> _FontDescription: ...
    @overload
    def tag_configure(self, tagname: str, option: Literal["image"]) -> str: ...
    @overload
    def tag_configure(
        self,
        tagname: str,
        option: None = None,
        *,
        # There is also 'text' and 'anchor', but they don't seem to do anything, using them is likely a bug
        foreground: str = ...,
        background: str = ...,
        font: _FontDescription = ...,
        image: tk._ImageSpec = ...,
    ) -> _TreeviewTagDict | MaybeNone: ...  # can be None but annoying to check
    @overload
    def tag_has(self, tagname: str, item: None = None) -> tuple[str, ...]: ...
    @overload
    def tag_has(self, tagname: str, item: str | int) -> bool: ...

class LabeledScale(Frame):
    label: Label
    scale: Scale
    # This should be kept in sync with tkinter.ttk.Frame.__init__()
    # (all the keyword-only args except compound are from there)
    def __init__(
        self,
        master: tk.Misc | None = None,
        variable: tk.IntVar | tk.DoubleVar | None = None,
        from_: float = 0,
        to: float = 10,
        *,
        border: tk._ScreenUnits = ...,
        borderwidth: tk._ScreenUnits = ...,
        class_: str = "",
        compound: Literal["top", "bottom"] = "top",
        cursor: tk._Cursor = "",
        height: tk._ScreenUnits = 0,
        name: str = ...,
        padding: _Padding = ...,
        relief: tk._Relief = ...,
        style: str = "",
        takefocus: tk._TakeFocusValue = "",
        width: tk._ScreenUnits = 0,
    ) -> None: ...
    # destroy is overridden, signature does not change
    value: Any

class OptionMenu(Menubutton):
    def __init__(
        self,
        master: tk.Misc | None,
        variable: tk.StringVar,
        default: str | None = None,
        *values: str,
        # rest of these are keyword-only because *args syntax used above
        style: str = "",
        direction: Literal["above", "below", "left", "right", "flush"] = "below",
        command: Callable[[tk.StringVar], object] | None = None,
    ) -> None: ...
    # configure, config, cget, destroy are inherited from Menubutton
    # destroy and __setitem__ are overridden, signature does not change
    def set_menu(self, default: str | None = None, *values: str) -> None: ...
