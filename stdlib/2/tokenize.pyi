# Automatically generated by pytype, manually fixed up. May still contain errors.

from typing import Any, Callable, Dict, Generator, Iterator, List, Tuple, Union, Iterable

__author__ = ...  # type: str
__credits__ = ...  # type: str

AMPER = ...  # type: int
AMPEREQUAL = ...  # type: int
AT = ...  # type: int
BACKQUOTE = ...  # type: int
Binnumber = ...  # type: str
Bracket = ...  # type: str
CIRCUMFLEX = ...  # type: int
CIRCUMFLEXEQUAL = ...  # type: int
COLON = ...  # type: int
COMMA = ...  # type: int
COMMENT = ...  # type: int
Comment = ...  # type: str
ContStr = ...  # type: str
DEDENT = ...  # type: int
DOT = ...  # type: int
DOUBLESLASH = ...  # type: int
DOUBLESLASHEQUAL = ...  # type: int
DOUBLESTAR = ...  # type: int
DOUBLESTAREQUAL = ...  # type: int
Decnumber = ...  # type: str
Double = ...  # type: str
Double3 = ...  # type: str
ENDMARKER = ...  # type: int
EQEQUAL = ...  # type: int
EQUAL = ...  # type: int
ERRORTOKEN = ...  # type: int
Expfloat = ...  # type: str
Exponent = ...  # type: str
Floatnumber = ...  # type: str
Funny = ...  # type: str
GREATER = ...  # type: int
GREATEREQUAL = ...  # type: int
Hexnumber = ...  # type: str
INDENT = ...  # type: int

def ISEOF(x: int) -> bool: ...
def ISNONTERMINAL(x: int) -> bool: ...
def ISTERMINAL(x: int) -> bool: ...

Ignore = ...  # type: str
Imagnumber = ...  # type: str
Intnumber = ...  # type: str
LBRACE = ...  # type: int
LEFTSHIFT = ...  # type: int
LEFTSHIFTEQUAL = ...  # type: int
LESS = ...  # type: int
LESSEQUAL = ...  # type: int
LPAR = ...  # type: int
LSQB = ...  # type: int
MINEQUAL = ...  # type: int
MINUS = ...  # type: int
NAME = ...  # type: int
NEWLINE = ...  # type: int
NL = ...  # type: int
NOTEQUAL = ...  # type: int
NT_OFFSET = ...  # type: int
NUMBER = ...  # type: int
N_TOKENS = ...  # type: int
Name = ...  # type: str
Number = ...  # type: str
OP = ...  # type: int
Octnumber = ...  # type: str
Operator = ...  # type: str
PERCENT = ...  # type: int
PERCENTEQUAL = ...  # type: int
PLUS = ...  # type: int
PLUSEQUAL = ...  # type: int
PlainToken = ...  # type: str
Pointfloat = ...  # type: str
PseudoExtras = ...  # type: str
PseudoToken = ...  # type: str
RBRACE = ...  # type: int
RIGHTSHIFT = ...  # type: int
RIGHTSHIFTEQUAL = ...  # type: int
RPAR = ...  # type: int
RSQB = ...  # type: int
SEMI = ...  # type: int
SLASH = ...  # type: int
SLASHEQUAL = ...  # type: int
STAR = ...  # type: int
STAREQUAL = ...  # type: int
STRING = ...  # type: int
Single = ...  # type: str
Single3 = ...  # type: str
Special = ...  # type: str
String = ...  # type: str
TILDE = ...  # type: int
Token = ...  # type: str
Triple = ...  # type: str
VBAR = ...  # type: int
VBAREQUAL = ...  # type: int
Whitespace = ...  # type: str
chain = ...  # type: type
double3prog = ...  # type: type
endprogs = ...  # type: Dict[str, Any]
pseudoprog = ...  # type: type
single3prog = ...  # type: type
single_quoted = ...  # type: Dict[str, str]
t = ...  # type: str
tabsize = ...  # type: int
tok_name = ...  # type: Dict[int, str]
tokenprog = ...  # type: type
triple_quoted = ...  # type: Dict[str, str]
x = ...  # type: str

_Pos = Tuple[int, int]
_TokenType = Tuple[int, str, _Pos, _Pos, str]

def any(*args, **kwargs) -> str: ...
def generate_tokens(readline: Callable[[], str]) -> Generator[_TokenType, None, None]: ...
def group(*args: str) -> str: ...
def maybe(*args: str) -> str: ...
def printtoken(type: int, token: str, srow_scol: _Pos, erow_ecol: _Pos, line: str) -> None: ...
def tokenize(readline: Callable[[], str], tokeneater: Callable[[Tuple[int, str, _Pos, _Pos, str]], None]) -> None: ...
def tokenize_loop(readline: Callable[[], str], tokeneater: Callable[[Tuple[int, str, _Pos, _Pos, str]], None]) -> None: ...
def untokenize(iterable: Iterable[_TokenType]) -> str: ...

class StopTokenizing(Exception):
    pass

class TokenError(Exception):
    pass

class Untokenizer:
    prev_col = ...  # type: int
    prev_row = ...  # type: int
    tokens = ...  # type: List[str]
    def __init__(self) -> None: ...
    def add_whitespace(self, _Pos) -> None: ...
    def compat(self, token: Tuple[int, Any], iterable: Iterator[_TokenType]) -> None: ...
    def untokenize(self, iterable: Iterable[_TokenType]) -> str: ...
