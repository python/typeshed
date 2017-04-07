import sys
from typing import Dict

ENDMARKER = 0
NAME = 0
NUMBER = 0
STRING = 0
NEWLINE = 0
INDENT = 0
DEDENT = 0
LPAR = 0
RPAR = 0
LSQB = 0
RSQB = 0
COLON = 0
COMMA = 0
SEMI = 0
PLUS = 0
MINUS = 0
STAR = 0
SLASH = 0
VBAR = 0
AMPER = 0
LESS = 0
GREATER = 0
EQUAL = 0
DOT = 0
PERCENT = 0
if sys.version_info < (3,):
    BACKQUOTE = 0
LBRACE = 0
RBRACE = 0
EQEQUAL = 0
NOTEQUAL = 0
LESSEQUAL = 0
GREATEREQUAL = 0
TILDE = 0
CIRCUMFLEX = 0
LEFTSHIFT = 0
RIGHTSHIFT = 0
DOUBLESTAR = 0
PLUSEQUAL = 0
MINEQUAL = 0
STAREQUAL = 0
SLASHEQUAL = 0
PERCENTEQUAL = 0
AMPEREQUAL = 0
VBAREQUAL = 0
CIRCUMFLEXEQUAL = 0
LEFTSHIFTEQUAL = 0
RIGHTSHIFTEQUAL = 0
DOUBLESTAREQUAL = 0
DOUBLESLASH = 0
DOUBLESLASHEQUAL = 0
AT = 0
if sys.version_info >= (3,):
    RARROW = 0
    ELLIPSIS = 0
if sys.version_info >= (3, 5):
    ATEQUAL = ...  # type: int
    AWAIT = ...  # type: int
    ASYNC = ...  # type: int
OP = 0
ERRORTOKEN = 0
N_TOKENS = 0
NT_OFFSET = 0
tok_name = ...  # type: Dict[int, str]

def ISTERMINAL(x: int) -> bool: ...
def ISNONTERMINAL(x: int) -> bool: ...
def ISEOF(x: int) -> bool: ...
