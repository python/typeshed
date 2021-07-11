from pygments.lexer import RegexLexer
from typing import Any

class CFamilyLexer(RegexLexer):
    tokens: Any = ...
    stdlib_types: Any = ...
    c99_types: Any = ...
    linux_types: Any = ...
    c11_atomic_types: Any = ...
    stdlibhighlighting: Any = ...
    c99highlighting: Any = ...
    c11highlighting: Any = ...
    platformhighlighting: Any = ...
    def __init__(self, **options: Any) -> None: ...
    def get_tokens_unprocessed(self, text: Any) -> None: ...

class CLexer(CFamilyLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    priority: float = ...
    tokens: Any = ...
    def analyse_text(text: Any): ...

class CppLexer(CFamilyLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    priority: float = ...
    tokens: Any = ...
    def analyse_text(text: Any): ...
