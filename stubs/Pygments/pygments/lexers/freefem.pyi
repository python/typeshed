from pygments.lexers.c_cpp import CppLexer
from typing import Any

class FreeFemLexer(CppLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    operators: Any = ...
    types: Any = ...
    fespaces: Any = ...
    preprocessor: Any = ...
    keywords: Any = ...
    functions: Any = ...
    parameters: Any = ...
    deprecated: Any = ...
    suppress_highlight: Any = ...
    def get_tokens_unprocessed(self, text: Any) -> None: ...
