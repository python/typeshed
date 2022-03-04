from typing import Any, TypeVar

from pygments.formatter import _TextFormatter

_T = TypeVar("_T", str, bytes)

class BBCodeFormatter(_TextFormatter[_T]):
    name: str
    aliases: Any
    filenames: Any
    styles: Any
    def format_unencoded(self, tokensource, outfile) -> None: ...
