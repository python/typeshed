from pygments.lexer import RegexLexer
from typing import Any

class ElmLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    validName: str = ...
    specialName: str = ...
    builtinOps: Any = ...
    reservedWords: Any = ...
    tokens: Any = ...
