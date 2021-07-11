from pygments.lexer import RegexLexer
from typing import Any

class VerilogLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    tokens: Any = ...
    def analyse_text(text: Any): ...

class SystemVerilogLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    tokens: Any = ...

class VhdlLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    flags: Any = ...
    tokens: Any = ...
