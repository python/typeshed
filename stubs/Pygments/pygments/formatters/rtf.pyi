from typing import Any, TypeVar

from pygments.formatter import _TextFormatter

_T = TypeVar("_T", str, bytes)

class RtfFormatter(_TextFormatter[_T]):
    name: str
    aliases: Any
    filenames: Any
    fontface: Any
    fontsize: Any
    def format_unencoded(self, tokensource, outfile) -> None: ...
