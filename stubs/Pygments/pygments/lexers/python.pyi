from pygments.lexer import Lexer, RegexLexer
from typing import Any

class PythonLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    flags: Any = ...
    uni_name: Any = ...
    def innerstring_rules(ttype: Any): ...
    def fstring_rules(ttype: Any): ...
    tokens: Any = ...
    def analyse_text(text: Any): ...
Python3Lexer = PythonLexer

class Python2Lexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    def innerstring_rules(ttype: Any): ...
    tokens: Any = ...
    def analyse_text(text: Any): ...

class PythonConsoleLexer(Lexer):
    name: str = ...
    aliases: Any = ...
    mimetypes: Any = ...
    python3: Any = ...
    def __init__(self, **options: Any) -> None: ...
    def get_tokens_unprocessed(self, text: Any) -> None: ...

class PythonTracebackLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    tokens: Any = ...
Python3TracebackLexer = PythonTracebackLexer

class Python2TracebackLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    tokens: Any = ...

class CythonLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    tokens: Any = ...

class DgLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    tokens: Any = ...

class NumPyLexer(PythonLexer):
    name: str = ...
    aliases: Any = ...
    mimetypes: Any = ...
    filenames: Any = ...
    EXTRA_KEYWORDS: Any = ...
    def get_tokens_unprocessed(self, text: Any) -> None: ...
    def analyse_text(text: Any): ...
