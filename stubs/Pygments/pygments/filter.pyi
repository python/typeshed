from collections.abc import Callable, Generator, Iterable, Iterator
from typing import Any

from pygments.lexer import Lexer
from pygments.token import _TokenType

def apply_filters(
    stream: Callable[[], Iterator[tuple[_TokenType, str]]], filters: list[Filter], lexer: Lexer | None = None
) -> Generator[tuple[_TokenType, str], None, tuple[_TokenType, str]]: ...
def simplefilter(f: Callable[..., Any]) -> type[FunctionFilter]: ...

class Filter:
    options: dict[str, Any]
    # options are kept as a dict on the instance
    def __init__(self, **options: Any) -> None: ...
    def filter(self, lexer: Lexer, stream: Iterable[tuple[_TokenType, str]]) -> Iterator[tuple[_TokenType, str]]: ...

class FunctionFilter(Filter):
    function: Callable[..., Any] | None = None
    # options are forwarded to Filter's constructor
    def __init__(self, **options: Any) -> None: ...
    def filter(self, lexer: Lexer, stream: Iterable[tuple[_TokenType, str]]) -> Iterator[tuple[_TokenType, str]]: ...
