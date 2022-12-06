from typing import Iterator
from typing_extensions import TypedDict

from jmespath.exceptions import EmptyExpressionError as EmptyExpressionError, LexerError as LexerError

class LexerTokenizeResult(TypedDict):
    type: str
    value: str
    start: int
    end: int

LexerTokenizeResults = Iterator[LexerTokenizeResult]

class Lexer:
    START_IDENTIFIER: set[str]
    VALID_IDENTIFIER: set[str]
    VALID_NUMBER: set[str]
    WHITESPACE: set[str]
    SIMPLE_TOKENS: dict[str, str]
    def tokenize(self, expression: str) -> LexerTokenizeResults: ...
