from typing import Any, TypeVar

from pygments.formatter import _TextFormatter

_T = TypeVar("_T", str, bytes)

class TerminalFormatter(_TextFormatter[_T]):
    name: str
    aliases: Any
    filenames: Any
    darkbg: Any
    colorscheme: Any
    linenos: Any
    def format(self, tokensource, outfile): ...
    def format_unencoded(self, tokensource, outfile) -> None: ...
