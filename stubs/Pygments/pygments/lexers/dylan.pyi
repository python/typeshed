from pygments.lexer import Lexer, RegexLexer
from typing import Any

class DylanLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    flags: Any = ...
    builtins: Any = ...
    keywords: Any = ...
    operators: Any = ...
    functions: Any = ...
    valid_name: str = ...
    def get_tokens_unprocessed(self, text: Any) -> None: ...
    tokens: Any = ...

class DylanLidLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    flags: Any = ...
    tokens: Any = ...

class DylanConsoleLexer(Lexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    def get_tokens_unprocessed(self, text: Any) -> None: ...
