from _typeshed import Incomplete
from typing import TypeVar

from pygments.formatter import Formatter

_T = TypeVar("_T", str, bytes)

__all__ = ["RtfFormatter"]

class RtfFormatter(Formatter[_T]):
    name: str
    aliases: Incomplete
    filenames: Incomplete
    fontface: Incomplete
    fontsize: Incomplete
    @staticmethod
    def hex_to_rtf_color(hex_color: str) -> str: ...
    def format_unencoded(self, tokensource, outfile) -> None: ...
