from pygments.lexer import DelegatingLexer, RegexLexer
from typing import Any

class RagelLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    tokens: Any = ...

class RagelEmbeddedLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    tokens: Any = ...
    def analyse_text(text: Any): ...

class RagelRubyLexer(DelegatingLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    def __init__(self, **options: Any) -> None: ...
    def analyse_text(text: Any): ...

class RagelCLexer(DelegatingLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    def __init__(self, **options: Any) -> None: ...
    def analyse_text(text: Any): ...

class RagelDLexer(DelegatingLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    def __init__(self, **options: Any) -> None: ...
    def analyse_text(text: Any): ...

class RagelCppLexer(DelegatingLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    def __init__(self, **options: Any) -> None: ...
    def analyse_text(text: Any): ...

class RagelObjectiveCLexer(DelegatingLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    def __init__(self, **options: Any) -> None: ...
    def analyse_text(text: Any): ...

class RagelJavaLexer(DelegatingLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    def __init__(self, **options: Any) -> None: ...
    def analyse_text(text: Any): ...

class AntlrLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    tokens: Any = ...
    def analyse_text(text: Any): ...

class AntlrCppLexer(DelegatingLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    def __init__(self, **options: Any) -> None: ...
    def analyse_text(text: Any): ...

class AntlrObjectiveCLexer(DelegatingLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    def __init__(self, **options: Any) -> None: ...
    def analyse_text(text: Any): ...

class AntlrCSharpLexer(DelegatingLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    def __init__(self, **options: Any) -> None: ...
    def analyse_text(text: Any): ...

class AntlrPythonLexer(DelegatingLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    def __init__(self, **options: Any) -> None: ...
    def analyse_text(text: Any): ...

class AntlrJavaLexer(DelegatingLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    def __init__(self, **options: Any) -> None: ...
    def analyse_text(text: Any): ...

class AntlrRubyLexer(DelegatingLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    def __init__(self, **options: Any) -> None: ...
    def analyse_text(text: Any): ...

class AntlrPerlLexer(DelegatingLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    def __init__(self, **options: Any) -> None: ...
    def analyse_text(text: Any): ...

class AntlrActionScriptLexer(DelegatingLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    def __init__(self, **options: Any) -> None: ...
    def analyse_text(text: Any): ...

class TreetopBaseLexer(RegexLexer):
    tokens: Any = ...

class TreetopLexer(DelegatingLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    def __init__(self, **options: Any) -> None: ...

class EbnfLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    tokens: Any = ...
