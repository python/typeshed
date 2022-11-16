from collections.abc import Iterable
from html.parser import HTMLParser
from idlelib.config import idleConf as idleConf
from tkinter import Text, Tk, Toplevel
from tkinter.ttk import Frame, Menubutton, Scrollbar, Style

class HelpParser(HTMLParser):
    text: Text
    tags: str
    chartags: str
    show: bool
    hdrlink: bool
    level: int
    pre: bool
    hprefix: str
    nested_dl: bool
    simplelist: bool
    toc: list[tuple[str, str]]
    header: str
    prevtag: tuple[bool, str]
    def __init__(self, text: Text) -> None: ...
    def indent(self, amt: int = ...) -> None: ...
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None: ...
    def handle_endtag(self, tag: str) -> None: ...
    def handle_data(self, data: str) -> None: ...

class HelpText(Text):
    parser: HelpParser
    def __init__(self, parent: Tk, filename: str) -> None: ...
    def findfont(self, names: Iterable[str]) -> str | None: ...

class HelpFrame(Frame):
    text: HelpText
    style: Style
    toc: Menubutton
    scroll: Scrollbar
    def __init__(self, parent: Tk, filename: str) -> None: ...
    def toc_menu(self, text: HelpText) -> Menubutton: ...

class HelpWindow(Toplevel):
    def __init__(self, parent: Tk, filename: str, title: str) -> None: ...

def copy_strip() -> None: ...
def show_idlehelp(parent: Tk) -> None: ...
