from _typeshed import Incomplete
from collections.abc import Generator

from ijson import common

LEXEME_RE: Incomplete
UNARY_LEXEMES: Incomplete
EOF: Incomplete

class UnexpectedSymbol(common.JSONError):
    def __init__(self, symbol, pos) -> None: ...

def utf8_encoder(target) -> Generator[None, Incomplete]: ...
def Lexer(target) -> Generator[None, Incomplete]: ...

inf: Incomplete

def parse_value(target, multivalue, use_float) -> Generator[None, Incomplete]: ...
def parse_string(symbol): ...
def basic_parse_basecoro(target, multiple_values: bool = False, allow_comments: bool = False, use_float: bool = False): ...
