from pygments.formatter import Formatter
from typing import Any

class BBCodeFormatter(Formatter):
    name: str
    aliases: Any
    filenames: Any
    styles: Any
    def __init__(self, **options) -> None: ...
    def format_unencoded(self, tokensource, outfile) -> None: ...
