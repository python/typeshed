from jmespath import ast as ast, exceptions as exceptions, lexer as lexer, visitor as visitor
from jmespath.compat import with_repr_method as with_repr_method
from typing import Any

class Parser:
    BINDING_POWER: Any
    tokenizer: Any
    def __init__(self, lookahead: int = ...) -> None: ...
    def parse(self, expression): ...
    @classmethod
    def purge(cls) -> None: ...

class ParsedResult:
    expression: Any
    parsed: Any
    def __init__(self, expression, parsed) -> None: ...
    def search(self, value, options: Any | None = ...): ...
