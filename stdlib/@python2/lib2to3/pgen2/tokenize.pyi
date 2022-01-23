from lib2to3.pgen2.token import *  # noqa
from typing import Callable, Iterable, Iterator, Protocol, Text

_Coord = tuple[int, int]
_TokenEater = Callable[[int, Text, _Coord, _Coord, Text], None]
_TokenInfo = tuple[int, Text, _Coord, _Coord, Text]

class TokenError(Exception): ...
class StopTokenizing(Exception): ...

class _Readline(Protocol):
    def __call__(self, __size: int | None = ...) -> Text: ...

def tokenize(readline: _Readline, tokeneater: _TokenEater = ...) -> None: ...

class Untokenizer:
    tokens: list[Text]
    prev_row: int
    prev_col: int
    def __init__(self) -> None: ...
    def add_whitespace(self, start: _Coord) -> None: ...
    def untokenize(self, iterable: Iterable[_TokenInfo]) -> Text: ...
    def compat(self, token: tuple[int, Text], iterable: Iterable[_TokenInfo]) -> None: ...

def untokenize(iterable: Iterable[_TokenInfo]) -> Text: ...
def generate_tokens(readline: _Readline) -> Iterator[_TokenInfo]: ...
