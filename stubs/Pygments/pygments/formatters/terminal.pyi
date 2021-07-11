from pygments.formatter import Formatter
from typing import Any

class TerminalFormatter(Formatter):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    darkbg: Any = ...
    colorscheme: Any = ...
    linenos: Any = ...
    def __init__(self, **options: Any) -> None: ...
    def format(self, tokensource: Any, outfile: Any): ...
    def format_unencoded(self, tokensource: Any, outfile: Any) -> None: ...
