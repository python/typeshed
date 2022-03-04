from typing import Any, TypeVar

from pygments.formatter import _TextFormatter

_T = TypeVar("_T", str, bytes)

class SvgFormatter(_TextFormatter[_T]):
    name: str
    aliases: Any
    filenames: Any
    nowrap: Any
    fontfamily: Any
    fontsize: Any
    xoffset: Any
    yoffset: Any
    ystep: Any
    spacehack: Any
    linenos: Any
    linenostart: Any
    linenostep: Any
    linenowidth: Any
    def format_unencoded(self, tokensource, outfile) -> None: ...
