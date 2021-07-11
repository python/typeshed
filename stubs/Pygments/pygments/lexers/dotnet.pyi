from pygments.lexer import DelegatingLexer, RegexLexer
from typing import Any

class CSharpLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    flags: Any = ...
    levels: Any = ...
    tokens: Any = ...
    token_variants: bool = ...
    def __init__(self, **options: Any) -> None: ...

class NemerleLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    flags: Any = ...
    levels: Any = ...
    tokens: Any = ...
    token_variants: bool = ...
    def __init__(self, **options: Any) -> None: ...
    def analyse_text(text: Any): ...

class BooLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    tokens: Any = ...

class VbNetLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    uni_name: Any = ...
    flags: Any = ...
    tokens: Any = ...
    def analyse_text(text: Any): ...

class GenericAspxLexer(RegexLexer):
    name: str = ...
    filenames: Any = ...
    mimetypes: Any = ...
    flags: Any = ...
    tokens: Any = ...

class CSharpAspxLexer(DelegatingLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    def __init__(self, **options: Any) -> None: ...
    def analyse_text(text: Any): ...

class VbNetAspxLexer(DelegatingLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    def __init__(self, **options: Any) -> None: ...
    def analyse_text(text: Any): ...

class FSharpLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    keywords: Any = ...
    keyopts: Any = ...
    operators: str = ...
    word_operators: Any = ...
    prefix_syms: str = ...
    infix_syms: str = ...
    primitives: Any = ...
    tokens: Any = ...
    def analyse_text(text: Any): ...
