from collections.abc import Callable, Iterable, Iterator
from typing_extensions import TypeAlias

from .pgen2.token import *

__all__ = [
    "AMPER",
    "AMPEREQUAL",
    "ASYNC",
    "AT",
    "ATEQUAL",
    "AWAIT",
    "BACKQUOTE",
    "CIRCUMFLEX",
    "CIRCUMFLEXEQUAL",
    "COLON",
    "COMMA",
    "COMMENT",
    "DEDENT",
    "DOT",
    "DOUBLESLASH",
    "DOUBLESLASHEQUAL",
    "DOUBLESTAR",
    "DOUBLESTAREQUAL",
    "ENDMARKER",
    "EQEQUAL",
    "EQUAL",
    "ERRORTOKEN",
    "GREATER",
    "GREATEREQUAL",
    "INDENT",
    "ISEOF",
    "ISNONTERMINAL",
    "ISTERMINAL",
    "LBRACE",
    "LEFTSHIFT",
    "LEFTSHIFTEQUAL",
    "LESS",
    "LESSEQUAL",
    "LPAR",
    "LSQB",
    "MINEQUAL",
    "MINUS",
    "NAME",
    "NEWLINE",
    "NL",
    "NOTEQUAL",
    "NT_OFFSET",
    "NUMBER",
    "N_TOKENS",
    "OP",
    "PERCENT",
    "PERCENTEQUAL",
    "PLUS",
    "PLUSEQUAL",
    "RARROW",
    "RBRACE",
    "RIGHTSHIFT",
    "RIGHTSHIFTEQUAL",
    "RPAR",
    "RSQB",
    "SEMI",
    "SLASH",
    "SLASHEQUAL",
    "STAR",
    "STAREQUAL",
    "STRING",
    "TILDE",
    "VBAR",
    "VBAREQUAL",
    "tok_name",
    "tokenize",
    "generate_tokens",
    "untokenize",
    "COLONEQUAL",
]

_Coord: TypeAlias = tuple[int, int]
_TokenEater: TypeAlias = Callable[[int, str, _Coord, _Coord, str], object]
_TokenInfo: TypeAlias = tuple[int, str, _Coord, _Coord, str]

class TokenError(Exception): ...
class StopTokenizing(Exception): ...

def tokenize(readline: Callable[[], str], tokeneater: _TokenEater = ...) -> None: ...

class Untokenizer:
    tokens: list[str]
    prev_row: int
    prev_col: int
    def add_whitespace(self, start: _Coord) -> None: ...
    def untokenize(self, iterable: Iterable[_TokenInfo]) -> str: ...
    def compat(self, token: tuple[int, str], iterable: Iterable[_TokenInfo]) -> None: ...

def untokenize(iterable: Iterable[_TokenInfo]) -> str: ...
def generate_tokens(readline: Callable[[], str]) -> Iterator[_TokenInfo]: ...
