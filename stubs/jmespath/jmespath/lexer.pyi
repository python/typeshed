from jmespath.exceptions import EmptyExpressionError as EmptyExpressionError, LexerError as LexerError
from typing import Any

class Lexer:
    START_IDENTIFIER: Any
    VALID_IDENTIFIER: Any
    VALID_NUMBER: Any
    WHITESPACE: Any
    SIMPLE_TOKENS: Any
    def tokenize(self, expression) -> None: ...
