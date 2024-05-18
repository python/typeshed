import enum
from collections.abc import Callable
from typing import Any, AnyStr, Final, Generic
from typing_extensions import TypeAlias

from .regex import Pattern

class error(Exception):
    def __init__(self, message: str, pattern: AnyStr | None = None, pos: int | None = None) -> None: ...

class RegexFlag(enum.IntFlag):
    A = 0x80
    ASCII = A
    B = 0x1000
    BESTMATCH = B
    D = 0x200
    DEBUG = D
    E = 0x8000
    ENHANCEMATCH = E
    F = 0x4000
    FULLCASE = F
    I = 0x2
    IGNORECASE = I
    L = 0x4
    LOCALE = L
    M = 0x8
    MULTILINE = M
    P = 0x10000
    POSIX = P
    R = 0x400
    REVERSE = R
    T = 0x1
    TEMPLATE = T
    S = 0x10
    DOTALL = S
    U = 0x20
    UNICODE = U
    V0 = 0x2000
    VERSION0 = V0
    V1 = 0x100
    VERSION1 = V1
    W = 0x800
    WORD = W
    X = 0x40
    VERBOSE = X

A: Final = RegexFlag.A
ASCII: Final = RegexFlag.ASCII
B: Final = RegexFlag.B
BESTMATCH: Final = RegexFlag.BESTMATCH
D: Final = RegexFlag.D
DEBUG: Final = RegexFlag.DEBUG
E: Final = RegexFlag.E
ENHANCEMATCH: Final = RegexFlag.ENHANCEMATCH
F: Final = RegexFlag.F
FULLCASE: Final = RegexFlag.FULLCASE
I: Final = RegexFlag.I
IGNORECASE: Final = RegexFlag.IGNORECASE
L: Final = RegexFlag.L
LOCALE: Final = RegexFlag.LOCALE
M: Final = RegexFlag.M
MULTILINE: Final = RegexFlag.MULTILINE
P: Final = RegexFlag.P
POSIX: Final = RegexFlag.POSIX
R: Final = RegexFlag.R
REVERSE: Final = RegexFlag.REVERSE
T: Final = RegexFlag.T
TEMPLATE: Final = RegexFlag.TEMPLATE
S: Final = RegexFlag.S
DOTALL: Final = RegexFlag.DOTALL
U: Final = RegexFlag.U
UNICODE: Final = RegexFlag.UNICODE
V0: Final = RegexFlag.V0
VERSION0: Final = RegexFlag.VERSION0
V1: Final = RegexFlag.V1
VERSION1: Final = RegexFlag.VERSION1
W: Final = RegexFlag.W
WORD: Final = RegexFlag.WORD
X: Final = RegexFlag.X
VERBOSE: Final = RegexFlag.VERBOSE

DEFAULT_VERSION: RegexFlag

_Lexicon: TypeAlias = list[tuple[AnyStr, Callable[[Scanner[AnyStr], AnyStr], Any]]]

class Scanner(Generic[AnyStr]):
    lexicon: _Lexicon[AnyStr]
    scanner: Pattern[AnyStr]

    def __init__(self, lexicon: _Lexicon[AnyStr], flags: int = 0) -> None: ...
    def scan(self, string: AnyStr) -> tuple[list[Any], AnyStr]: ...
