from _typeshed import Incomplete
from idlelib import macosx as macosx
from idlelib.autocomplete import AutoComplete as AutoComplete
from idlelib.codecontext import CodeContext as CodeContext
from idlelib.config import ConfigChanges as ConfigChanges, idleConf as idleConf
from idlelib.config_key import GetKeysDialog as GetKeysDialog
from idlelib.dynoption import DynOptionMenu as DynOptionMenu
from idlelib.format import FormatParagraph as FormatParagraph
from idlelib.parenmatch import ParenMatch as ParenMatch
from idlelib.query import HelpSource as HelpSource, SectionName as SectionName
from idlelib.squeezer import Squeezer as Squeezer
from idlelib.textview import ScrollableTextFrame as ScrollableTextFrame, view_text as view_text
from tkinter import Toplevel
from tkinter.ttk import Frame, HighPage, LabelFrame, Notebook

changes: dict[str, dict]
reloadables: tuple

class ConfigDialog(Toplevel):
    def __getattr__(self, name: str) -> Incomplete: ...  # Incomplete
    parent: Incomplete
    def __init__(self, parent, title: str = ..., *, _htest: bool = ..., _utest: bool = ...) -> None: ...
    frame: Frame
    note: Notebook
    extpage: Incomplete
    highpage: "HighPage"
    fontpage: "FontPage"
    keyspage: "KeysPage"
    winpage: "WinPage"
    shedpage: "ShedPage"
    def create_widgets(self) -> None: ...
    buttons: dict[str, Button]
    def create_action_buttons(self) -> Frame: ...
    def ok(self) -> None: ...
    def apply(self) -> None: ...
    def cancel(self) -> None: ...
    def destroy(self) -> None: ...
    def help(self) -> None: ...
    def deactivate_current_config(self) -> None: ...
    def activate_config_changes(self) -> None: ...

font_sample_text: str

class FontPage(Frame):
    def __getattr__(self, name: str) -> Incomplete: ...  # Incomplete
    highlight_sample: Incomplete
    def __init__(self, master, highpage) -> None: ...
    font_name: Incomplete
    font_size: Incomplete
    font_bold: Incomplete
    fontlist: Incomplete
    sizelist: Incomplete
    bold_toggle: Incomplete
    font_sample: Incomplete
    def create_page_font(self) -> None: ...
    def load_font_cfg(self) -> None: ...
    def var_changed_font(self, *params) -> None: ...
    def on_fontlist_select(self, event) -> None: ...
    def set_samples(self, event: Incomplete | None = ...) -> None: ...

class HighPage(Frame):
    def __getattr__(self, name: str) -> Incomplete: ...  # Incomplete
    extpage: Incomplete
    cd: Incomplete
    style: Incomplete
    def __init__(self, master, extpage) -> None: ...
    theme_elements: Incomplete
    builtin_name: Incomplete
    custom_name: Incomplete
    fg_bg_toggle: Incomplete
    color: Incomplete
    theme_source: Incomplete
    highlight_target: Incomplete
    frame_color_set: Incomplete
    button_set_color: Incomplete
    targetlist: Incomplete
    fg_on: Incomplete
    bg_on: Incomplete
    button_save_custom: Incomplete
    builtin_theme_on: Incomplete
    custom_theme_on: Incomplete
    builtinlist: Incomplete
    customlist: Incomplete
    button_delete_custom: Incomplete
    theme_message: Incomplete
    def create_page_highlight(self): ...
    def load_theme_cfg(self): ...
    def var_changed_builtin_name(self, *params) -> None: ...
    def var_changed_custom_name(self, *params) -> None: ...
    def var_changed_theme_source(self, *params) -> None: ...
    def var_changed_color(self, *params) -> None: ...
    def var_changed_highlight_target(self, *params) -> None: ...
    def set_theme_type(self) -> None: ...
    def get_color(self) -> None: ...
    def on_new_color_set(self) -> None: ...
    def get_new_theme_name(self, message): ...
    def save_as_new_theme(self) -> None: ...
    def create_new(self, new_theme_name) -> None: ...
    def set_highlight_target(self) -> None: ...
    def set_color_sample_binding(self, *args) -> None: ...
    def set_color_sample(self) -> None: ...
    def paint_theme_sample(self) -> None: ...
    def save_new(self, theme_name, theme) -> None: ...
    def askyesno(self, *args, **kwargs): ...
    def delete_custom(self) -> None: ...

class KeysPage(Frame):
    def __getattr__(self, name: str) -> Incomplete: ...  # Incomplete
    extpage: Incomplete
    cd: Incomplete
    def __init__(self, master, extpage) -> None: ...
    builtin_name: Incomplete
    custom_name: Incomplete
    keyset_source: Incomplete
    keybinding: Incomplete
    bindingslist: Incomplete
    button_new_keys: Incomplete
    builtin_keyset_on: Incomplete
    custom_keyset_on: Incomplete
    builtinlist: Incomplete
    customlist: Incomplete
    button_delete_custom_keys: Incomplete
    button_save_custom_keys: Incomplete
    keys_message: Incomplete
    def create_page_keys(self) -> None: ...
    def load_key_cfg(self) -> None: ...
    def var_changed_builtin_name(self, *params) -> None: ...
    def var_changed_custom_name(self, *params) -> None: ...
    def var_changed_keyset_source(self, *params) -> None: ...
    def var_changed_keybinding(self, *params) -> None: ...
    def set_keys_type(self) -> None: ...
    def get_new_keys(self) -> None: ...
    def get_new_keys_name(self, message): ...
    def save_as_new_key_set(self) -> None: ...
    def on_bindingslist_select(self, event) -> None: ...
    def create_new_key_set(self, new_key_set_name) -> None: ...
    def load_keys_list(self, keyset_name) -> None: ...
    @staticmethod
    def save_new_key_set(keyset_name, keyset) -> None: ...
    def askyesno(self, *args, **kwargs): ...
    def delete_custom_keys(self) -> None: ...

class WinPage(Frame):
    def __getattr__(self, name: str) -> Incomplete: ...  # Incomplete
    def __init__(self, master) -> None: ...
    digits_only: Incomplete
    def init_validators(self): ...
    startup_edit: Incomplete
    win_width: Incomplete
    win_height: Incomplete
    indent_spaces: Incomplete
    cursor_blink: Incomplete
    autocomplete_wait: Incomplete
    paren_style: Incomplete
    flash_delay: Incomplete
    paren_bell: Incomplete
    format_width: Incomplete
    startup_editor_on: Incomplete
    startup_shell_on: Incomplete
    win_width_int: Incomplete
    win_height_int: Incomplete
    indent_chooser: Incomplete
    cursor_blink_bool: Incomplete
    auto_wait_int: Incomplete
    paren_style_type: Incomplete
    paren_flash_time: Incomplete
    bell_on: Incomplete
    format_width_int: Incomplete
    def create_page_windows(self) -> None: ...
    def load_windows_cfg(self) -> None: ...

class ShedPage(Frame):
    def __getattr__(self, name: str) -> Incomplete: ...  # Incomplete
    def __init__(self, master) -> None: ...
    digits_only: Incomplete
    def init_validators(self): ...
    auto_squeeze_min_lines: Incomplete
    autosave: Incomplete
    line_numbers_default: Incomplete
    context_lines: Incomplete
    auto_squeeze_min_lines_int: Incomplete
    save_ask_on: Incomplete
    save_auto_on: Incomplete
    line_numbers_default_bool: Incomplete
    context_int: Incomplete
    def create_page_shed(self) -> None: ...
    def load_shelled_cfg(self) -> None: ...

class ExtPage(Frame):
    def __getattr__(self, name: str) -> Incomplete: ...  # Incomplete
    ext_defaultCfg: Incomplete
    ext_userCfg: Incomplete
    is_int: Incomplete
    def __init__(self, master) -> None: ...
    extension_names: Incomplete
    frame_help: Incomplete
    extension_list: Incomplete
    details_frame: Incomplete
    config_frame: Incomplete
    current_extension: Incomplete
    outerframe: Incomplete
    tabbed_page_set: Incomplete
    def create_page_extensions(self) -> None: ...
    extensions: Incomplete
    def load_extensions(self) -> None: ...
    def extension_selected(self, event) -> None: ...
    def create_extension_frame(self, ext_name) -> None: ...
    def set_extension_value(self, section, opt): ...
    def save_all_changed_extensions(self) -> None: ...

class HelpFrame(LabelFrame):
    def __getattr__(self, name: str) -> Incomplete: ...  # Incomplete
    def __init__(self, master, **cfg) -> None: ...
    helplist: Incomplete
    button_helplist_edit: Incomplete
    button_helplist_add: Incomplete
    button_helplist_remove: Incomplete
    def create_frame_help(self) -> None: ...
    def help_source_selected(self, event) -> None: ...
    def set_add_delete_state(self) -> None: ...
    def helplist_item_add(self) -> None: ...
    def helplist_item_edit(self) -> None: ...
    def helplist_item_remove(self) -> None: ...
    def update_help_changes(self) -> None: ...
    user_helplist: Incomplete
    def load_helplist(self) -> None: ...

class VarTrace:
    def __getattr__(self, name: str) -> Incomplete: ...  # Incomplete
    untraced: Incomplete
    traced: Incomplete
    def __init__(self) -> None: ...
    def clear(self) -> None: ...
    def add(self, var, callback): ...
    @staticmethod
    def make_callback(var, config): ...
    def attach(self) -> None: ...
    def detach(self) -> None: ...

tracers: Incomplete
help_common: str
help_pages: Incomplete

def is_int(s): ...

class VerticalScrolledFrame(Frame):
    def __getattr__(self, name: str) -> Incomplete: ...  # Incomplete
    interior: Incomplete
    def __init__(self, parent, *args, **kw) -> None: ...
