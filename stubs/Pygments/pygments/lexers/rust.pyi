from pygments.lexer import RegexLexer
from typing import Any

class RustLexer(RegexLexer):
    name: str = ...
    filenames: Any = ...
    aliases: Any = ...
    mimetypes: Any = ...
    keyword_types: Any = ...
    builtin_funcs_types: Any = ...
    builtin_macros: Any = ...
    tokens: Any = ...
