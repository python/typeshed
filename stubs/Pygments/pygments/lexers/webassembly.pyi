from pygments.lexer import RegexLexer
from typing import Any

class WatLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    tokens: Any = ...
