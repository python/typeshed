from typing import Any

from jmespath.lexer import LexerTokenizeResults as _LexerTokenizeResults
from jmespath.visitor import TreeNode

class Parser:
    BINDING_POWER: dict[str, int]
    tokenizer: _LexerTokenizeResults
    def __init__(self, lookahead: int = ...) -> None: ...
    def parse(self, expression: str) -> ParsedResult: ...
    @classmethod
    def purge(cls) -> None: ...

class ParsedResult:
    expression: str
    parsed: TreeNode
    def __init__(self, expression: str, parsed: TreeNode) -> None: ...
    def search(self, value: Any, options: Any | None = ...) -> TreeNode: ...
