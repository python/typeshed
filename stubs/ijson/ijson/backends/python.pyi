from _typeshed import Incomplete
from collections.abc import Generator
from re import Pattern
from typing import Literal

from ijson import common

inf = float("inf")
LEXEME_RE: Pattern[str]
UNARY_LEXEMES: set[str]
EOF: tuple[Literal[-1], None]

class UnexpectedSymbol(common.JSONError):
    def __init__(self, symbol: str, pos: int) -> None: ...

def utf8_encoder(target: Incomplete) -> Generator[None, bytes]: ...
def Lexer(target: Generator[Incomplete, bytes]) -> Generator[None, tuple[int, str]]: ...
def parse_value(
    target: Generator[Incomplete, tuple[str, object]], multivalue: bool, use_float: bool
) -> Generator[None, tuple[int, str | None]]: ...
def parse_string(symbol: str) -> str: ...
def basic_parse_basecoro(
    target: Generator[None, tuple[int, str | None]],
    multiple_values: bool = False,
    allow_comments: bool = False,
    use_float: bool = False,
) -> Generator[None, bytes]: ...
