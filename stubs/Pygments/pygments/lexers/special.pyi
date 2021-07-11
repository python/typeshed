from pygments.lexer import Lexer
from typing import Any

class TextLexer(Lexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    priority: float = ...
    def get_tokens_unprocessed(self, text: Any) -> None: ...
    def analyse_text(text: Any): ...

class RawTokenLexer(Lexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    compress: Any = ...
    def __init__(self, **options: Any) -> None: ...
    def get_tokens(self, text: Any) -> None: ...
    def get_tokens_unprocessed(self, text: Any) -> None: ...
