from collections.abc import Iterator
from typing import Any

from jmespath.lexer import _LexerTokenizeResult
from jmespath.visitor import Options, _TreeNode

class Parser:
    BINDING_POWER: dict[str, int]
    tokenizer: Iterator[_LexerTokenizeResult]
    def __init__(self, lookahead: int = ...) -> None: ...
    def parse(self, expression: str) -> ParsedResult: ...
    @classmethod
    def purge(cls) -> None: ...

class ParsedResult:
    expression: str
    parsed: _TreeNode
    def __init__(self, expression: str, parsed: _TreeNode) -> None: ...
    def search(self, value: Any, options: Options | None = ...) -> _TreeNode: ...
