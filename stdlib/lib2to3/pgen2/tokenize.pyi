import sys
from lib2to3.pgen2.token import *
from typing import Callable, Iterable, Iterator

# fmt: off
if sys.version_info >= (3, 8):
    __all__ = [
        "AMPER", "AMPEREQUAL", "ASYNC", "AT", "ATEQUAL", "AWAIT", "BACKQUOTE",
        "CIRCUMFLEX", "CIRCUMFLEXEQUAL", "COLON", "COLONEQUAL", "COMMA",
        "COMMENT", "DEDENT", "DOT", "DOUBLESLASH", "DOUBLESLASHEQUAL",
        "DOUBLESTAR", "DOUBLESTAREQUAL", "ENDMARKER", "EQEQUAL", "EQUAL",
        "ERRORTOKEN", "GREATER", "GREATEREQUAL", "INDENT", "ISEOF",
        "ISNONTERMINAL", "ISTERMINAL", "LBRACE", "LEFTSHIFT", "LEFTSHIFTEQUAL",
        "LESS", "LESSEQUAL", "LPAR", "LSQB", "MINEQUAL", "MINUS", "NAME",
        "NEWLINE", "NL", "NOTEQUAL", "NT_OFFSET", "NUMBER", "N_TOKENS", "OP",
        "PERCENT", "PERCENTEQUAL", "PLUS", "PLUSEQUAL", "RARROW", "RBRACE",
        "RIGHTSHIFT", "RIGHTSHIFTEQUAL", "RPAR", "RSQB", "SEMI", "SLASH",
        "SLASHEQUAL", "STAR", "STAREQUAL", "STRING", "TILDE", "VBAR", "VBAREQUAL",
        "tok_name", "tokenize", "generate_tokens", "untokenize"
    ]
else:
    __all__ = [
        "AMPER", "AMPEREQUAL", "ASYNC", "AT", "ATEQUAL", "AWAIT", "BACKQUOTE",
        "CIRCUMFLEX", "CIRCUMFLEXEQUAL", "COLON", "COMMA",
        "COMMENT", "DEDENT", "DOT", "DOUBLESLASH", "DOUBLESLASHEQUAL",
        "DOUBLESTAR", "DOUBLESTAREQUAL", "ENDMARKER", "EQEQUAL", "EQUAL",
        "ERRORTOKEN", "GREATER", "GREATEREQUAL", "INDENT", "ISEOF",
        "ISNONTERMINAL", "ISTERMINAL", "LBRACE", "LEFTSHIFT", "LEFTSHIFTEQUAL",
        "LESS", "LESSEQUAL", "LPAR", "LSQB", "MINEQUAL", "MINUS", "NAME",
        "NEWLINE", "NL", "NOTEQUAL", "NT_OFFSET", "NUMBER", "N_TOKENS", "OP",
        "PERCENT", "PERCENTEQUAL", "PLUS", "PLUSEQUAL", "RARROW", "RBRACE",
        "RIGHTSHIFT", "RIGHTSHIFTEQUAL", "RPAR", "RSQB", "SEMI", "SLASH",
        "SLASHEQUAL", "STAR", "STAREQUAL", "STRING", "TILDE", "VBAR", "VBAREQUAL",
        "tok_name", "tokenize", "generate_tokens", "untokenize"
    ]
# fmt: on

_Coord = tuple[int, int]
_TokenEater = Callable[[int, str, _Coord, _Coord, str], None]
_TokenInfo = tuple[int, str, _Coord, _Coord, str]

class TokenError(Exception): ...
class StopTokenizing(Exception): ...

def tokenize(readline: Callable[[], str], tokeneater: _TokenEater = ...) -> None: ...

class Untokenizer:
    tokens: list[str]
    prev_row: int
    prev_col: int
    def __init__(self) -> None: ...
    def add_whitespace(self, start: _Coord) -> None: ...
    def untokenize(self, iterable: Iterable[_TokenInfo]) -> str: ...
    def compat(self, token: tuple[int, str], iterable: Iterable[_TokenInfo]) -> None: ...

def untokenize(iterable: Iterable[_TokenInfo]) -> str: ...
def generate_tokens(readline: Callable[[], str]) -> Iterator[_TokenInfo]: ...
