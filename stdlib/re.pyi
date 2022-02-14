import enum
import sys
from sre_constants import error as error
from typing import Any, Callable, Iterator, Union, overload
from _typeshed import StrOrBuffer

# ----- re variables and constants -----
if sys.version_info >= (3, 7):
    from typing import Match as Match, Pattern as Pattern
else:
    from typing import Match, Pattern

class RegexFlag(enum.IntFlag):
    A: int
    ASCII: int
    DEBUG: int
    I: int
    IGNORECASE: int
    L: int
    LOCALE: int
    M: int
    MULTILINE: int
    S: int
    DOTALL: int
    X: int
    VERBOSE: int
    U: int
    UNICODE: int
    T: int
    TEMPLATE: int

A = RegexFlag.A
ASCII = RegexFlag.ASCII
DEBUG = RegexFlag.DEBUG
I = RegexFlag.I
IGNORECASE = RegexFlag.IGNORECASE
L = RegexFlag.L
LOCALE = RegexFlag.LOCALE
M = RegexFlag.M
MULTILINE = RegexFlag.MULTILINE
S = RegexFlag.S
DOTALL = RegexFlag.DOTALL
X = RegexFlag.X
VERBOSE = RegexFlag.VERBOSE
U = RegexFlag.U
UNICODE = RegexFlag.UNICODE
T = RegexFlag.T
TEMPLATE = RegexFlag.TEMPLATE
_FlagsType = Union[int, RegexFlag]

if sys.version_info < (3, 7):
    # undocumented
    _pattern_type: type

@overload
def compile(pattern: StrOrBuffer, flags: _FlagsType = ...) -> Pattern[StrOrBuffer]: ...
@overload
def compile(pattern: Pattern[StrOrBuffer], flags: _FlagsType = ...) -> Pattern[StrOrBuffer]: ...
@overload
def search(pattern: StrOrBuffer, string: StrOrBuffer, flags: _FlagsType = ...) -> Match[StrOrBuffer] | None: ...
@overload
def search(pattern: Pattern[StrOrBuffer], string: StrOrBuffer, flags: _FlagsType = ...) -> Match[StrOrBuffer] | None: ...
@overload
def match(pattern: StrOrBuffer, string: StrOrBuffer, flags: _FlagsType = ...) -> Match[StrOrBuffer] | None: ...
@overload
def match(pattern: Pattern[StrOrBuffer], string: StrOrBuffer, flags: _FlagsType = ...) -> Match[StrOrBuffer] | None: ...

# New in Python 3.4
@overload
def fullmatch(pattern: StrOrBuffer, string: StrOrBuffer, flags: _FlagsType = ...) -> Match[StrOrBuffer] | None: ...
@overload
def fullmatch(pattern: Pattern[StrOrBuffer], string: StrOrBuffer, flags: _FlagsType = ...) -> Match[StrOrBuffer] | None: ...
@overload
def split(pattern: StrOrBuffer, string: StrOrBuffer, maxsplit: int = ..., flags: _FlagsType = ...) -> list[StrOrBuffer | Any]: ...
@overload
def split(
    pattern: Pattern[StrOrBuffer], string: StrOrBuffer, maxsplit: int = ..., flags: _FlagsType = ...
) -> list[StrOrBuffer | Any]: ...
@overload
def findall(pattern: StrOrBuffer, string: StrOrBuffer, flags: _FlagsType = ...) -> list[Any]: ...
@overload
def findall(pattern: Pattern[StrOrBuffer], string: StrOrBuffer, flags: _FlagsType = ...) -> list[Any]: ...

# Return an iterator yielding match objects over all non-overlapping matches
# for the RE pattern in string. The string is scanned left-to-right, and
# matches are returned in the order found. Empty matches are included in the
# result unless they touch the beginning of another match.
@overload
def finditer(pattern: StrOrBuffer, string: StrOrBuffer, flags: _FlagsType = ...) -> Iterator[Match[StrOrBuffer]]: ...
@overload
def finditer(pattern: Pattern[StrOrBuffer], string: StrOrBuffer, flags: _FlagsType = ...) -> Iterator[Match[StrOrBuffer]]: ...
@overload
def sub(
    pattern: StrOrBuffer, repl: StrOrBuffer, string: StrOrBuffer, count: int = ..., flags: _FlagsType = ...
) -> StrOrBuffer: ...
@overload
def sub(
    pattern: StrOrBuffer,
    repl: Callable[[Match[StrOrBuffer]], StrOrBuffer],
    string: StrOrBuffer,
    count: int = ...,
    flags: _FlagsType = ...,
) -> StrOrBuffer: ...
@overload
def sub(
    pattern: Pattern[StrOrBuffer], repl: StrOrBuffer, string: StrOrBuffer, count: int = ..., flags: _FlagsType = ...
) -> StrOrBuffer: ...
@overload
def sub(
    pattern: Pattern[StrOrBuffer],
    repl: Callable[[Match[StrOrBuffer]], StrOrBuffer],
    string: StrOrBuffer,
    count: int = ...,
    flags: _FlagsType = ...,
) -> StrOrBuffer: ...
@overload
def subn(
    pattern: StrOrBuffer, repl: StrOrBuffer, string: StrOrBuffer, count: int = ..., flags: _FlagsType = ...
) -> tuple[StrOrBuffer, int]: ...
@overload
def subn(
    pattern: StrOrBuffer,
    repl: Callable[[Match[StrOrBuffer]], StrOrBuffer],
    string: StrOrBuffer,
    count: int = ...,
    flags: _FlagsType = ...,
) -> tuple[StrOrBuffer, int]: ...
@overload
def subn(
    pattern: Pattern[StrOrBuffer], repl: StrOrBuffer, string: StrOrBuffer, count: int = ..., flags: _FlagsType = ...
) -> tuple[StrOrBuffer, int]: ...
@overload
def subn(
    pattern: Pattern[StrOrBuffer],
    repl: Callable[[Match[StrOrBuffer]], StrOrBuffer],
    string: StrOrBuffer,
    count: int = ...,
    flags: _FlagsType = ...,
) -> tuple[StrOrBuffer, int]: ...
def escape(pattern: StrOrBuffer) -> StrOrBuffer: ...
def purge() -> None: ...
def template(pattern: StrOrBuffer | Pattern[StrOrBuffer], flags: _FlagsType = ...) -> Pattern[StrOrBuffer]: ...
