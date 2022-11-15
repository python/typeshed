from _typeshed import Incomplete
from idlelib.config import idleConf as idleConf
from idlelib.util import py_extensions as py_extensions

encoding: str
errors: Incomplete

class IOBinding:
    def __getattr__(self, name: str) -> Incomplete: ...  # Incomplete
    editwin: Incomplete
    text: Incomplete
    fileencoding: str
    def __init__(self, editwin) -> None: ...
    filename_change_hook: Incomplete
    def close(self) -> None: ...
    def get_saved(self): ...
    def set_saved(self, flag) -> None: ...
    def reset_undo(self) -> None: ...
    def set_filename_change_hook(self, hook) -> None: ...
    filename: Incomplete
    dirname: Incomplete
    def set_filename(self, filename) -> None: ...
    def open(self, event: Incomplete | None = ..., editFile: Incomplete | None = ...): ...
    eol_convention: Incomplete
    def loadfile(self, filename): ...
    def maybesave(self): ...
    def save(self, event): ...
    def save_as(self, event): ...
    def save_a_copy(self, event): ...
    def writefile(self, filename): ...
    def fixnewlines(self): ...
    def encode(self, chars): ...
    def print_window(self, event): ...
    opendialog: Incomplete
    savedialog: Incomplete
    filetypes: Incomplete
    defaultextension: Incomplete
    def askopenfile(self): ...
    def defaultfilename(self, mode: str = ...): ...
    def asksavefile(self): ...
    def updaterecentfileslist(self, filename) -> None: ...
