from pygments.lexer import RegexLexer
from typing import Any

class WhileyLexer(RegexLexer):
    name: str = ...
    filenames: Any = ...
    aliases: Any = ...
    mimetypes: Any = ...
    tokens: Any = ...
