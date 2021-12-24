from collections.abc import Callable, Iterable, Mapping, Sequence
import signal
import sys
from bdb import Bdb
from cmd import Cmd
from inspect import _SourceObjectType
from types import CodeType, FrameType, TracebackType
from typing import IO, Any, ClassVar, TypeVar

_T = TypeVar("_T")

line_prefix: str  # undocumented

class Restart(Exception): ...

def run(statement: str, globals: dict[str, Any] | None = ..., locals: Mapping[str, Any] | None = ...) -> None: ...
def runeval(expression: str, globals: dict[str, Any] | None = ..., locals: Mapping[str, Any] | None = ...) -> Any: ...
def runctx(statement: str, globals: dict[str, Any], locals: Mapping[str, Any]) -> None: ...
def runcall(func: Callable[..., _T], *args: Any, **kwds: Any) -> _T | None: ...

if sys.version_info >= (3, 7):
    def set_trace(*, header: str | None = ...) -> None: ...

else:
    def set_trace() -> None: ...

def post_mortem(t: TracebackType | None = ...) -> None: ...
def pm() -> None: ...

class Pdb(Bdb, Cmd):
    # Everything here is undocumented, except for __init__

    commands_resuming: ClassVar[list[str]]

    aliases: dict[str, str]
    mainpyfile: str
    _wait_for_mainpyfile: bool
    rcLines: list[str]
    commands: dict[int, list[str]]
    commands_doprompt: dict[int, bool]
    commands_silent: dict[int, bool]
    commands_defining: bool
    commands_bnum: int | None
    lineno: int | None
    stack: list[tuple[FrameType, int]]
    curindex: int
    curframe: FrameType | None
    curframe_locals: Mapping[str, Any]
    def __init__(
        self,
        completekey: str = ...,
        stdin: IO[str] | None = ...,
        stdout: IO[str] | None = ...,
        skip: Iterable[str] | None = ...,
        nosigint: bool = ...,
        readrc: bool = ...,
    ) -> None: ...
    def forget(self) -> None: ...
    def setup(self, f: FrameType | None, tb: TracebackType | None) -> None: ...
    def execRcLines(self) -> None: ...
    def bp_commands(self, frame: FrameType) -> bool: ...
    def interaction(self, frame: FrameType | None, traceback: TracebackType | None) -> None: ...
    def displayhook(self, obj: object) -> None: ...
    def handle_command_def(self, line: str) -> bool: ...
    def defaultFile(self) -> str: ...
    def lineinfo(self, identifier: str) -> tuple[None, None, None] | tuple[str, str, int]: ...
    def checkline(self, filename: str, lineno: int) -> int: ...
    def _getval(self, arg: str) -> object: ...
    def print_stack_trace(self) -> None: ...
    def print_stack_entry(self, frame_lineno: tuple[FrameType, int], prompt_prefix: str = ...) -> None: ...
    def lookupmodule(self, filename: str) -> str | None: ...
    def _runscript(self, filename: str) -> None: ...
    def do_commands(self, arg: str) -> bool | None: ...
    def do_break(self, arg: str, temporary: bool = ...) -> bool | None: ...
    def do_tbreak(self, arg: str) -> bool | None: ...
    def do_enable(self, arg: str) -> bool | None: ...
    def do_disable(self, arg: str) -> bool | None: ...
    def do_condition(self, arg: str) -> bool | None: ...
    def do_ignore(self, arg: str) -> bool | None: ...
    def do_clear(self, arg: str) -> bool | None: ...
    def do_where(self, arg: str) -> bool | None: ...
    def do_up(self, arg: str) -> bool | None: ...
    def do_down(self, arg: str) -> bool | None: ...
    def do_until(self, arg: str) -> bool | None: ...
    def do_step(self, arg: str) -> bool | None: ...
    def do_next(self, arg: str) -> bool | None: ...
    def do_run(self, arg: str) -> bool | None: ...
    def do_return(self, arg: str) -> bool | None: ...
    def do_continue(self, arg: str) -> bool | None: ...
    def do_jump(self, arg: str) -> bool | None: ...
    def do_debug(self, arg: str) -> bool | None: ...
    def do_quit(self, arg: str) -> bool | None: ...
    def do_EOF(self, arg: str) -> bool | None: ...
    def do_args(self, arg: str) -> bool | None: ...
    def do_retval(self, arg: str) -> bool | None: ...
    def do_p(self, arg: str) -> bool | None: ...
    def do_pp(self, arg: str) -> bool | None: ...
    def do_list(self, arg: str) -> bool | None: ...
    def do_whatis(self, arg: str) -> bool | None: ...
    def do_alias(self, arg: str) -> bool | None: ...
    def do_unalias(self, arg: str) -> bool | None: ...
    def do_help(self, arg: str) -> bool | None: ...
    do_b = do_break
    do_cl = do_clear
    do_w = do_where
    do_bt = do_where
    do_u = do_up
    do_d = do_down
    do_unt = do_until
    do_s = do_step
    do_n = do_next
    do_restart = do_run
    do_r = do_return
    do_c = do_continue
    do_cont = do_continue
    do_j = do_jump
    do_q = do_quit
    do_exit = do_quit
    do_a = do_args
    do_rv = do_retval
    do_l = do_list
    do_h = do_help
    def help_exec(self) -> None: ...
    def help_pdb(self) -> None: ...
    def sigint_handler(self, signum: signal.Signals, frame: FrameType) -> None: ...
    def message(self, msg: str) -> None: ...
    def error(self, msg: str) -> None: ...
    def _select_frame(self, number: int) -> None: ...
    def _getval_except(self, arg: str, frame: FrameType | None = ...) -> object: ...
    def _print_lines(
        self, lines: Sequence[str], start: int, breaks: Sequence[int] = ..., frame: FrameType | None = ...
    ) -> None: ...
    def _cmdloop(self) -> None: ...
    def do_display(self, arg: str) -> bool | None: ...
    def do_interact(self, arg: str) -> bool | None: ...
    def do_longlist(self, arg: str) -> bool | None: ...
    def do_source(self, arg: str) -> bool | None: ...
    def do_undisplay(self, arg: str) -> bool | None: ...
    do_ll = do_longlist
    def _complete_location(self, text: str, line: str, begidx: int, endidx: int) -> list[str]: ...
    def _complete_bpnumber(self, text: str, line: str, begidx: int, endidx: int) -> list[str]: ...
    def _complete_expression(self, text: str, line: str, begidx: int, endidx: int) -> list[str]: ...
    def complete_undisplay(self, text: str, line: str, begidx: int, endidx: int) -> list[str]: ...
    def complete_unalias(self, text: str, line: str, begidx: int, endidx: int) -> list[str]: ...
    complete_commands = _complete_bpnumber
    complete_break = _complete_location
    complete_b = _complete_location
    complete_tbreak = _complete_location
    complete_enable = _complete_bpnumber
    complete_disable = _complete_bpnumber
    complete_condition = _complete_bpnumber
    complete_ignore = _complete_bpnumber
    complete_clear = _complete_location
    complete_cl = _complete_location
    complete_debug = _complete_expression
    complete_print = _complete_expression
    complete_p = _complete_expression
    complete_pp = _complete_expression
    complete_source = _complete_expression
    complete_whatis = _complete_expression
    complete_display = _complete_expression

    if sys.version_info >= (3, 7):
        def _runmodule(self, module_name: str) -> None: ...

# undocumented

def find_function(funcname: str, filename: str) -> tuple[str, str, int] | None: ...
def main() -> None: ...
def help() -> None: ...
def getsourcelines(obj: _SourceObjectType) -> tuple[list[str], int]: ...
def lasti2lineno(code: CodeType, lasti: int) -> int: ...

class _rstr(str):
    def __repr__(self) -> _rstr: ...
