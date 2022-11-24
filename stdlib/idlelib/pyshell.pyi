from _typeshed import Incomplete
from code import InteractiveInterpreter
from idlelib import debugger as debugger, debugger_r as debugger_r, replace as replace, rpc as rpc
from idlelib.colorizer import ColorDelegator as ColorDelegator
from idlelib.config import idleConf as idleConf
from idlelib.delegator import Delegator as Delegator
from idlelib.editor import EditorWindow as EditorWindow, fixwordbreaks as fixwordbreaks
from idlelib.filelist import FileList as FileList
from idlelib.history import History as History
from idlelib.outwin import OutputWindow as OutputWindow
from idlelib.run import (
    StdInputFile as StdInputFile,
    StdOutputFile as StdOutputFile,
    fix_scaling as fix_scaling,
    idle_formatwarning as idle_formatwarning,
)
from idlelib.sidebar import ShellSidebar as ShellSidebar
from idlelib.squeezer import Squeezer as Squeezer
from idlelib.undo import UndoDelegator as UndoDelegator
from io import IOBase
from typing import Any, Callable
from tkinter import *
from tkinter import Event

root: Tk
use_subprocess: bool
HOST: str
PORT: int
eof: str
warning_stream: IOBase | None

def idle_showwarning(
    message: str, category: BaseException, filename: str, lineno: int, file: IOBase | None = ..., line: str | None = ...
) -> None: ...
def capture_warnings(capture: bool) -> None: ...
def extended_linecache_checkcache(filename: str | None = ..., orig_checkcache: Callable[[str], None]=...) -> None: ...

class PyShellEditorWindow(EditorWindow):
    breakpoints: list[int]
    breakpointPath: str
    def __init__(self, *args: Incomplete) -> None: ...
    rmenu_specs: list[tuple[str | None, str | None, str | None]]
    def color_breakpoint_text(self, color: bool = ...) -> None: ...
    def set_breakpoint(self, lineno: int) -> None: ...
    def set_breakpoint_here(self, event: Event[Any] | None = ...) -> None: ...
    def clear_breakpoint_here(self, event: Event[Any] | None = ...) -> None: ...
    def clear_file_breaks(self) -> None: ...
    def store_file_breaks(self) -> None: ...
    def restore_file_breaks(self) -> None: ...
    def update_breakpoints(self) -> None: ...
    def ranges_to_linenumbers(self, ranges: Incomplete) -> list[int]: ...

class PyShellFileList(FileList):
    EditorWindow: PyShellEditorWindow
    pyshell: PyShell | None
    def open_shell(self, event: Event[Any] | None = ...) -> PyShell | None: ...

class ModifiedColorDelegator(ColorDelegator):
    def recolorize_main(self) -> None: ...
    def removecolors(self) -> None: ...

class ModifiedUndoDelegator(UndoDelegator):
    def insert(self, index: str, chars: str, tags: str | None = ...) -> None: ...
    def delete(self, index1: str, index2: str | None = ...) -> None: ...
    def undo_event(self, event: Event[Any]) -> None: ...

class UserInputTaggingDelegator(Delegator):
    def insert(self, index: str, chars: str, tags: str | None = ...) -> None: ...

class MyRPCClient(rpc.RPCClient):
    def handle_EOF(self) -> None: ...

def restart_line(width: int, filename: str | None) -> str: ...

class ModifiedInterpreter(InteractiveInterpreter):
    tkconsole: Incomplete
    restarting: bool
    subprocess_arglist: Incomplete | None
    port: int
    original_compiler_flags: Incomplete
    def __init__(self, tkconsole: Incomplete) -> None: ...
    rpcclt: Incomplete
    rpcsubproc: Incomplete
    def spawn_subprocess(self) -> None: ...
    def build_subprocess_arglist(self) -> list[str]: ...
    def start_subprocess(self) -> MyRPCClient | None: ...
    def restart_subprocess(self, with_cwd: bool = ..., filename: str = ...) -> MyRPCClient | None: ...
    def interrupt_subprocess(self) -> None: ...
    def kill_subprocess(self) -> None: ...
    def terminate_subprocess(self) -> None: ...
    def transfer_path(self, with_cwd: bool = ...) -> None: ...
    active_seq: Incomplete | None
    def poll_subprocess(self) -> None: ...
    debugger: Incomplete | None
    def setdebugger(self, debugger: Incomplete | None) -> None: ...
    def getdebugger(self) -> Incomplete | None: ...
    def open_remote_stack_viewer(self) -> None: ...
    def remote_stack_viewer(self) -> None: ...
    gid: int
    def execsource(self, source: str) -> None: ...
    def execfile(self, filename: str, source: str | None = ...) -> None: ...
    def runsource(self, source: str) -> Incomplete: ...
    def stuffsource(self, source: str) -> str: ...
    def prepend_syspath(self, filename: str) -> None: ...
    def showsyntaxerror(self, filename: str | None = ...) -> None: ...
    def showtraceback(self) -> None: ...
    def checklinecache(self) -> None: ...
    def runcommand(self, code: Incomplete) -> int: ...
    def runcode(self, code: Incomplete) -> None: ...
    def write(self, s: str) -> int: ...
    def display_port_binding_error(self) -> None: ...
    def display_no_subprocess_error(self) -> None: ...
    def display_executing_dialog(self) -> None: ...

class PyShell(OutputWindow):
    def __getattr__(self, name: str) -> Incomplete: ...  # Incomplete
    shell_title: str
    ColorDelegator: ModifiedColorDelegator
    UndoDelegator: ModifiedUndoDelegator
    menu_specs: list[tuple[str, str]]
    rmenu_specs: list[tuple[str, str]]
    allow_line_numbers: bool
    user_input_insert_tags: str
    interp: ModifiedInterpreter
    shell_sidebar: ShellSidebar
    usetabs: bool
    indentwidth: int
    sys_ps1: str
    prompt_last_line: str
    prompt: str
    squeezer: Squeezer
    save_stdout: IOBase
    save_stderr: IOBase
    save_stdin: IOBase
    stdin: StdInputFile
    stdout: StdInputFile
    stderr: StdInputFile
    console: StdOutputFile
    history: History
    pollinterval: int
    def __init__(self, flist: PyShellFileList | None = ...) -> None: ...
    def ResetFont(self) -> None: ...
    def ResetColorizer(self) -> None: ...
    def replace_event(self, event: Any | None) -> str: ...
    def get_standard_extension_names(self) -> list[str]: ...
    def copy_with_prompts_callback(self, event: Any | None = ...) -> None: ...
    reading: bool
    executing: bool
    canceled: bool
    endoffile: bool
    closing: bool
    def set_warning_stream(self, stream: IOBase) -> None: ...
    def get_warning_stream(self): ...
    def toggle_debugger(self, event: Any | None = ...) -> str | None: ...
    def set_debugger_indicator(self) -> None: ...
    def toggle_jit_stack_viewer(self, event: Any | None = ...) -> None: ...
    def close_debugger(self) -> None: ...
    def open_debugger(self) -> None: ...
    def debug_menu_postcommand(self) -> None: ...
    def beginexecuting(self) -> None: ...
    def endexecuting(self) -> None: ...
    def close(self): ...
    def ispythonsource(self, filename: str) -> bool: ...
    def short_title(self) -> str: ...
    COPYRIGHT: str
    def begin(self) -> bool: ...
    def stop_readline(self) -> None: ...
    def readline(self) -> str: ...
    def isatty(self) -> bool: ...
    def cancel_callback(self, event: Any | None = ...) -> str | None: ...
    def eof_callback(self, event: Any) -> str | None: ...
    def linefeed_callback(self, event: Any) -> str: ...
    def enter_callback(self, event: Any) -> str | None: ...
    def recall(self, s: str, event: Any) -> None: ...
    def runit(self) -> None: ...
    def open_stack_viewer(self, event: Any | None = ...) -> Incomplete | None: ...
    def view_restart_mark(self, event: Any | None = ...) -> None: ...
    def restart_shell(self, event: Any | None = ...) -> None: ...
    def showprompt(self) -> None: ...
    def show_warning(self, msg: str) -> None: ...
    def resetoutput(self) -> None: ...
    def write(self, s: str, tags: str=...) -> int: ...
    def rmenu_check_cut(self) -> str | Incomplete: ...
    def rmenu_check_paste(self) -> str | None: ...
    def squeeze_current_text_event(self, event: Any | None = ...) -> None: ...
    def on_squeezed_expand(self, index: Any, text: Any, tags: Any) -> None: ...

def fix_x11_paste(root: Incomplete) -> None: ...

usage_msg: str

def main() -> None: ...
