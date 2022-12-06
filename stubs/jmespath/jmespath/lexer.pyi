from collections.abc import Iterator
from typing_extensions import TypeAlias, TypedDict

from jmespath.exceptions import EmptyExpressionError as EmptyExpressionError, LexerError as LexerError

class LexerTokenizeResult(TypedDict):
    type: str
    value: str
    start: int
    end: int

LexerTokenizeResults: TypeAlias = Iterator[LexerTokenizeResult]

class Lexer:
    START_IDENTIFIER: set[str]
    VALID_IDENTIFIER: set[str]
    VALID_NUMBER: set[str]
    WHITESPACE: set[str]
    SIMPLE_TOKENS: dict[str, str]
    def tokenize(self, expression: str) -> LexerTokenizeResults: ...
