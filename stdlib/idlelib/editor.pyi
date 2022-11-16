from _typeshed import Incomplete
from idlelib import (
    configdialog as configdialog,
    grep as grep,
    help as help,
    help_about as help_about,
    macosx as macosx,
    mainmenu as mainmenu,
    pyparse as pyparse,
    query as query,
    replace as replace,
    search as search,
    window as window,
)
from idlelib.autocomplete import AutoComplete as AutoComplete
from idlelib.autoexpand import AutoExpand as AutoExpand
from idlelib.calltip import Calltip as Calltip
from idlelib.codecontext import CodeContext as CodeContext
from idlelib.colorizer import ColorDelegator as ColorDelegator, color_config as color_config
from idlelib.config import idleConf as idleConf
from idlelib.format import FormatParagraph as FormatParagraph, FormatRegion as FormatRegion, Indents as Indents, Rstrip as Rstrip
from idlelib.iomenu import IOBinding as IOBinding, encoding as encoding
from idlelib.multicall import MultiCallCreator as MultiCallCreator
from idlelib.parenmatch import ParenMatch as ParenMatch
from idlelib.percolator import Percolator as Percolator
from idlelib.sidebar import LineNumbers as LineNumbers
from idlelib.statusbar import MultiStatusBar as MultiStatusBar
from idlelib.tree import wheel_event as wheel_event
from idlelib.undo import UndoDelegator as UndoDelegator
from idlelib.util import py_extensions as py_extensions
from idlelib.zoomheight import ZoomHeight as ZoomHeight
from tkinter import *
from tkinter import Event
from typing import Any

TK_TABWIDTH_DEFAULT: int
darwin: bool

class EditorWindow:
    def __getattr__(self, name: str) -> Incomplete: ...  # Incomplete
    filesystemencoding: str
    help_url: str | None
    allow_code_context: bool
    allow_line_numbers: bool
    user_input_insert_tags: str | None
    flist: Incomplete
    root: Incomplete
    menubar: Incomplete
    top: window.ListedToplevel
    tkinter_vars: Incomplete
    recent_files_path: Incomplete
    prompt_last_line: str
    text_frame: Incomplete
    vbar: Incomplete
    text: Incomplete
    fregion: Incomplete
    usetabs: bool
    tabwidth: int
    indentwidth: Incomplete
    num_context_lines: Incomplete
    per: Incomplete
    undo: Incomplete
    io: Incomplete
    good_load: bool
    color: Incomplete
    code_context: Incomplete
    line_numbers: Incomplete
    wmenu_end: Incomplete
    askinteger: Incomplete
    askyesno: Incomplete
    showerror: Incomplete
    ctip: Incomplete
    def __init__(
        self,
        flist: Incomplete | None = ...,
        filename: Incomplete | None = ...,
        key: Incomplete | None = ...,
        root: Incomplete | None = ...,
    ): ...
    def handle_winconfig(self, event: "Event[Any] | None" = ...) -> None: ...
    width: Incomplete
    def set_width(self) -> None: ...
    def new_callback(self, event: "Event[Any]"): ...
    def home_callback(self, event: "Event[Any]"): ...
    status_bar: Incomplete
    def set_status_bar(self) -> None: ...
    def set_line_and_column(self, event: "Event[Any] | None" = ...) -> None: ...
    menu_specs: Incomplete
    menudict: Incomplete
    recent_files_menu: Incomplete
    base_helpmenu_length: Incomplete
    def createmenubar(self) -> None: ...
    def postwindowsmenu(self) -> None: ...
    def update_menu_label(self, menu, index, label) -> None: ...
    def update_menu_state(self, menu, index, state) -> None: ...
    def handle_yview(self, event, *args): ...
    rmenu: Incomplete
    event: Incomplete
    def right_menu_event(self, event: "Event[Any]"): ...
    rmenu_specs: Incomplete
    def make_rmenu(self) -> None: ...
    def rmenu_check_cut(self): ...
    def rmenu_check_copy(self): ...
    def rmenu_check_paste(self): ...
    def about_dialog(self, event: "Event[Any] | None" = ...): ...
    def config_dialog(self, event: "Event[Any] | None" = ...): ...
    def help_dialog(self, event: "Event[Any] | None" = ...): ...
    def python_docs(self, event: "Event[Any] | None" = ...): ...
    def cut(self, event: "Event[Any]"): ...
    def copy(self, event: "Event[Any]"): ...
    def paste(self, event: "Event[Any]"): ...
    def select_all(self, event: "Event[Any] | None" = ...): ...
    def remove_selection(self, event: "Event[Any] | None" = ...): ...
    def move_at_edge_if_selection(self, edge_index): ...
    def del_word_left(self, event: "Event[Any]"): ...
    def del_word_right(self, event: "Event[Any]"): ...
    def find_event(self, event: "Event[Any]"): ...
    def find_again_event(self, event: "Event[Any]"): ...
    def find_selection_event(self, event: "Event[Any]"): ...
    def find_in_files_event(self, event: "Event[Any]"): ...
    def replace_event(self, event: "Event[Any]"): ...
    def goto_line_event(self, event: "Event[Any]"): ...
    def open_module(self): ...
    def open_module_event(self, event: "Event[Any]"): ...
    def open_module_browser(self, event: "Event[Any] | None" = ...): ...
    def open_path_browser(self, event: "Event[Any] | None" = ...): ...
    def open_turtle_demo(self, event: "Event[Any] | None" = ...): ...
    def gotoline(self, lineno) -> None: ...
    def ispythonsource(self, filename): ...
    def close_hook(self) -> None: ...
    def set_close_hook(self, close_hook) -> None: ...
    def filename_change_hook(self) -> None: ...
    def ResetColorizer(self) -> None: ...
    IDENTCHARS: Incomplete
    def colorize_syntax_error(self, text, pos) -> None: ...
    def update_cursor_blink(self) -> None: ...
    def ResetFont(self) -> None: ...
    def RemoveKeybindings(self) -> None: ...
    def ApplyKeybindings(self) -> None: ...
    def set_notabs_indentwidth(self) -> None: ...
    def reset_help_menu_entries(self) -> None: ...
    def update_recent_files_list(self, new_file: Incomplete | None = ...) -> None: ...
    def saved_change_hook(self) -> None: ...
    def get_saved(self): ...
    def set_saved(self, flag) -> None: ...
    def reset_undo(self) -> None: ...
    def short_title(self): ...
    def long_title(self): ...
    def center_insert_event(self, event: "Event[Any]"): ...
    def center(self, mark: str = ...) -> None: ...
    def getwindowlines(self): ...
    def getlineno(self, mark: str = ...): ...
    def get_geometry(self): ...
    def close_event(self, event: "Event[Any]"): ...
    def maybesave(self): ...
    def close(self): ...
    extensions: Incomplete
    def load_extensions(self) -> None: ...
    def unload_extensions(self) -> None: ...
    def load_standard_extensions(self) -> None: ...
    def get_standard_extension_names(self): ...
    extfiles: Incomplete
    def load_extension(self, name) -> None: ...
    def apply_bindings(self, keydefs: Incomplete | None = ...) -> None: ...
    def fill_menus(self, menudefs: Incomplete | None = ..., keydefs: Incomplete | None = ...) -> None: ...
    def getvar(self, name): ...
    def setvar(self, name, value, vartype: Incomplete | None = ...) -> None: ...
    def get_var_obj(self, name, vartype: Incomplete | None = ...): ...
    def is_char_in_string(self, text_index): ...
    def get_selection_indices(self): ...
    def get_tk_tabwidth(self): ...
    def set_tk_tabwidth(self, newtabwidth) -> None: ...
    def set_indentation_params(self, is_py_src, guess: bool = ...) -> None: ...
    def smart_backspace_event(self, event: "Event[Any]"): ...
    def smart_indent_event(self, event: "Event[Any]"): ...
    def newline_and_indent_event(self, event: "Event[Any]"): ...
    def reindent_to(self, column) -> None: ...
    def guess_indent(self): ...
    def toggle_line_numbers_event(self, event: "Event[Any] | None" = ...) -> None: ...

def index2line(index): ...
def get_line_indent(line, tabwidth): ...

class IndentSearcher:
    def __getattr__(self, name: str) -> Incomplete: ...  # Incomplete
    text: Incomplete
    tabwidth: Incomplete
    i: int
    blkopenline: Incomplete
    def __init__(self, text, tabwidth) -> None: ...
    def readline(self): ...
    indentedline: Incomplete
    finished: int
    def tokeneater(self, type, token, start, end, line, INDENT=..., NAME=..., OPENERS=...) -> None: ...
    def run(self): ...

def prepstr(s): ...

keynames: Incomplete

def get_accelerator(keydefs: dict[str, str], eventname: str) -> str: ...
def fixwordbreaks(root) -> None: ...
