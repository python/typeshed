from pygments.formatter import Formatter
from typing import Any

class RtfFormatter(Formatter):
    name: str
    aliases: Any
    filenames: Any
    fontface: Any
    fontsize: Any
    def __init__(self, **options) -> None: ...
    def format_unencoded(self, tokensource, outfile) -> None: ...
