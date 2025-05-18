from collections.abc import Generator, Iterable
from typing import Any, Literal
from typing_extensions import Self, TypeAlias

from docutils import ApplicationError

_TonkenNames: TypeAlias = Literal["long", "short", "none"]

# _TokenType from types-pygments
class _TokenType(tuple[str, ...]):
    parent: _TokenType | None
    def split(self) -> list[_TokenType]: ...
    subtypes: set[_TokenType]
    def __contains__(self, val: _TokenType) -> bool: ...  # type: ignore[override]
    def __getattr__(self, name: str) -> _TokenType: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, memo: Any) -> Self: ...

with_pygments: bool
unstyled_tokens: list[str]

class LexerError(ApplicationError): ...

class Lexer:
    code: str
    language: str
    tokennames: _TonkenNames
    lexer: Lexer | None
    def __init__(self, code: str, language: str, tokennames: _TonkenNames = "short") -> None: ...
    def merge(self, tokens: Iterable[_TokenType]) -> Generator[tuple[str, str]]: ...
    def __iter__(self): ...

class NumberLines:
    tokens: Iterable[_TokenType]
    startline: int
    fmt_str: str
    def __init__(self, tokens: Iterable[_TokenType], startline: int, endline: int) -> None: ...
    def __iter__(self) -> Generator[tuple[list[str], str] | tuple[str, str]]: ...
