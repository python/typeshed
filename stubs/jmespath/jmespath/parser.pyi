from collections.abc import Iterator, Mapping
from typing import Any, ClassVar
from typing_extensions import TypeAlias

from jmespath.lexer import _LexerTokenizeResult
from jmespath.visitor import Options, _TreeNode

_TreeNodeDict: TypeAlias = Mapping[str, Any]

class Parser:
    BINDING_POWER: ClassVar[dict[str, int]]
    tokenizer: Iterator[_LexerTokenizeResult] | None
    def __init__(self, lookahead: int = ...) -> None: ...
    def parse(self, expression: str) -> ParsedResult: ...
    @classmethod
    def purge(cls) -> None: ...

class ParsedResult:
    expression: str
    parsed: _TreeNode
    def __init__(self, expression: str, parsed: _TreeNodeDict) -> None: ...
    def search(self, value: Any, options: Options | None = ...) -> Any: ...
