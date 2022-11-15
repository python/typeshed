from _typeshed import Incomplete

from idlelib import macosx as macosx, outwin as outwin, pyshell as pyshell
from idlelib.config import idleConf as idleConf
from idlelib.query import CustomRun as CustomRun

indent_message: str

class ScriptBinding:
    def __getattr__(self, name: str) -> Incomplete: ...  # Incomplete
    editwin: Incomplete
    flist: Incomplete
    root: Incomplete
    cli_args: Incomplete
    perf: float
    def __init__(self, editwin) -> None: ...
    def check_module_event(self, event): ...
    def tabnanny(self, filename): ...
    shell: Incomplete
    def checksyntax(self, filename): ...
    def run_custom_event(self, event): ...
    def run_module_event(self, event, *, customize: bool = ...): ...
    def getfilename(self): ...
    def ask_save_dialog(self): ...
    def errorbox(self, title, message) -> None: ...
