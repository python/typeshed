from collections.abc import Callable
from typing import IO, Any
from typing_extensions import Literal

__all__ = ["Cmd"]

PROMPT: Literal["(Cmd) "]
IDENTCHARS: str  # Too big to be `Literal`

class Cmd:
    prompt: str
    identchars: str
    ruler: str
    lastcmd: str
    intro: Any | None
    doc_leader: str
    doc_header: str
    misc_header: str
    undoc_header: str
    nohelp: str
    use_rawinput: bool
    stdin: IO[str]
    stdout: IO[str]
    cmdqueue: list[str]
    completekey: str
    def __init__(self, completekey: str = "tab", stdin: IO[str] | None = None, stdout: IO[str] | None = None) -> None: ...
    old_completer: Callable[[str, int], str | None] | None
    def cmdloop(self, intro: Any | None = None) -> None: ...
    def precmd(self, line: str) -> str: ...
    def postcmd(self, stop: bool, line: str) -> bool: ...
    def preloop(self) -> None: ...
    def postloop(self) -> None: ...
    def parseline(self, line: str) -> tuple[str | None, str | None, str]: ...
    def onecmd(self, line: str) -> bool: ...
    def emptyline(self) -> bool: ...
    def default(self, line: str) -> None: ...
    def completedefault(self, *ignored: Any) -> list[str]: ...
    def completenames(self, text: str, *ignored: Any) -> list[str]: ...
    completion_matches: list[str] | None
    def complete(self, text: str, state: int) -> list[str] | None: ...
    def get_names(self) -> list[str]: ...
    # Only the first element of args matters.
    def complete_help(self, *args: Any) -> list[str]: ...
    def do_help(self, arg: str) -> bool | None: ...
    def print_topics(self, header: str, cmds: list[str] | None, cmdlen: Any, maxcol: int) -> None: ...
    def columnize(self, list: list[str] | None, displaywidth: int = 80) -> None: ...
