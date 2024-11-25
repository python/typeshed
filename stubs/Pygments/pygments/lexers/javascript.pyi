from collections.abc import Iterator
from typing import Final

from ..lexer import Lexer, RegexLexer
from ..token import _TokenType

__all__ = [
    "CoffeeScriptLexer",
    "DartLexer",
    "EarlGreyLexer",
    "JavascriptLexer",
    "JuttleLexer",
    "KalLexer",
    "LassoLexer",
    "LiveScriptLexer",
    "MaskLexer",
    "NodeConsoleLexer",
    "ObjectiveJLexer",
    "TypeScriptLexer",
]

JS_IDENT_START: Final[str]
JS_IDENT_PART: Final[str]
JS_IDENT: Final[str]

class JavascriptLexer(RegexLexer): ...
class TypeScriptLexer(JavascriptLexer): ...
class KalLexer(RegexLexer): ...
class LiveScriptLexer(RegexLexer): ...
class DartLexer(RegexLexer): ...

class LassoLexer(RegexLexer):
    def get_tokens_unprocessed(self, text: str) -> Iterator[tuple[int, _TokenType, str]]: ...  # type: ignore[override]

class ObjectiveJLexer(RegexLexer): ...
class CoffeeScriptLexer(RegexLexer): ...
class MaskLexer(RegexLexer): ...
class EarlGreyLexer(RegexLexer): ...
class JuttleLexer(RegexLexer): ...
class NodeConsoleLexer(Lexer): ...
