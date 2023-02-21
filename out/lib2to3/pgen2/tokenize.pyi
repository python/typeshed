from lib2to3.pgen2.token import *
from _typeshed import Incomplete
from collections.abc import Generator

bytes = str

class TokenError(Exception): ...
class StopTokenizing(Exception): ...

def tokenize(readline, tokeneater=...) -> None: ...

class Untokenizer:
    tokens: Incomplete
    prev_row: int
    prev_col: int
    def __init__(self) -> None: ...
    def add_whitespace(self, start) -> None: ...
    def untokenize(self, iterable): ...
    def compat(self, token, iterable) -> None: ...

def untokenize(iterable): ...
def generate_tokens(readline) -> Generator[Incomplete, None, None]: ...

# Names in __all__ with no definition:
#   AMPER
#   AMPEREQUAL
#   ASYNC
#   AT
#   ATEQUAL
#   AWAIT
#   BACKQUOTE
#   CIRCUMFLEX
#   CIRCUMFLEXEQUAL
#   COLON
#   COLONEQUAL
#   COMMA
#   COMMENT
#   DEDENT
#   DOT
#   DOUBLESLASH
#   DOUBLESLASHEQUAL
#   DOUBLESTAR
#   DOUBLESTAREQUAL
#   ENDMARKER
#   EQEQUAL
#   EQUAL
#   ERRORTOKEN
#   GREATER
#   GREATEREQUAL
#   INDENT
#   ISEOF
#   ISNONTERMINAL
#   ISTERMINAL
#   LBRACE
#   LEFTSHIFT
#   LEFTSHIFTEQUAL
#   LESS
#   LESSEQUAL
#   LPAR
#   LSQB
#   MINEQUAL
#   MINUS
#   NAME
#   NEWLINE
#   NL
#   NOTEQUAL
#   NT_OFFSET
#   NUMBER
#   N_TOKENS
#   OP
#   PERCENT
#   PERCENTEQUAL
#   PLUS
#   PLUSEQUAL
#   RARROW
#   RBRACE
#   RIGHTSHIFT
#   RIGHTSHIFTEQUAL
#   RPAR
#   RSQB
#   SEMI
#   SLASH
#   SLASHEQUAL
#   STAR
#   STAREQUAL
#   STRING
#   TILDE
#   VBAR
#   VBAREQUAL
#   tok_name
