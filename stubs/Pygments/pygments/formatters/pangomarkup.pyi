from pygments.formatter import Formatter
from typing import Any

class PangoMarkupFormatter(Formatter):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    styles: Any = ...
    def __init__(self, **options: Any) -> None: ...
    def format_unencoded(self, tokensource: Any, outfile: Any) -> None: ...
