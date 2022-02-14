import enum
import sys
from sre_constants import error as error
from typing import Any, Callable, Iterator, Union, overload, RegexString

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
def compile(pattern: RegexString, flags: _FlagsType = ...) -> Pattern[RegexString]: ...
@overload
def compile(pattern: Pattern[RegexString], flags: _FlagsType = ...) -> Pattern[RegexString]: ...
@overload
def search(pattern: RegexString, string: RegexString, flags: _FlagsType = ...) -> Match[RegexString] | None: ...
@overload
def search(pattern: Pattern[RegexString], string: RegexString, flags: _FlagsType = ...) -> Match[RegexString] | None: ...
@overload
def match(pattern: RegexString, string: RegexString, flags: _FlagsType = ...) -> Match[RegexString] | None: ...
@overload
def match(pattern: Pattern[RegexString], string: RegexString, flags: _FlagsType = ...) -> Match[RegexString] | None: ...

# New in Python 3.4
@overload
def fullmatch(pattern: RegexString, string: RegexString, flags: _FlagsType = ...) -> Match[RegexString] | None: ...
@overload
def fullmatch(pattern: Pattern[RegexString], string: RegexString, flags: _FlagsType = ...) -> Match[RegexString] | None: ...
@overload
def split(pattern: RegexString, string: RegexString, maxsplit: int = ..., flags: _FlagsType = ...) -> list[RegexString | Any]: ...
@overload
def split(pattern: Pattern[RegexString], string: RegexString, maxsplit: int = ..., flags: _FlagsType = ...) -> list[RegexString | Any]: ...
@overload
def findall(pattern: RegexString, string: RegexString, flags: _FlagsType = ...) -> list[Any]: ...
@overload
def findall(pattern: Pattern[RegexString], string: RegexString, flags: _FlagsType = ...) -> list[Any]: ...

# Return an iterator yielding match objects over all non-overlapping matches
# for the RE pattern in string. The string is scanned left-to-right, and
# matches are returned in the order found. Empty matches are included in the
# result unless they touch the beginning of another match.
@overload
def finditer(pattern: RegexString, string: RegexString, flags: _FlagsType = ...) -> Iterator[Match[RegexString]]: ...
@overload
def finditer(pattern: Pattern[RegexString], string: RegexString, flags: _FlagsType = ...) -> Iterator[Match[RegexString]]: ...
@overload
def sub(pattern: RegexString, repl: RegexString, string: RegexString, count: int = ..., flags: _FlagsType = ...) -> RegexString: ...
@overload
def sub(
    pattern: RegexString, repl: Callable[[Match[RegexString]], RegexString], string: RegexString, count: int = ..., flags: _FlagsType = ...
) -> RegexString: ...
@overload
def sub(pattern: Pattern[RegexString], repl: RegexString, string: RegexString, count: int = ..., flags: _FlagsType = ...) -> RegexString: ...
@overload
def sub(
    pattern: Pattern[RegexString], repl: Callable[[Match[RegexString]], RegexString], string: RegexString, count: int = ..., flags: _FlagsType = ...
) -> RegexString: ...
@overload
def subn(pattern: RegexString, repl: RegexString, string: RegexString, count: int = ..., flags: _FlagsType = ...) -> tuple[RegexString, int]: ...
@overload
def subn(
    pattern: RegexString, repl: Callable[[Match[RegexString]], RegexString], string: RegexString, count: int = ..., flags: _FlagsType = ...
) -> tuple[RegexString, int]: ...
@overload
def subn(
    pattern: Pattern[RegexString], repl: RegexString, string: RegexString, count: int = ..., flags: _FlagsType = ...
) -> tuple[RegexString, int]: ...
@overload
def subn(
    pattern: Pattern[RegexString], repl: Callable[[Match[RegexString]], RegexString], string: RegexString, count: int = ..., flags: _FlagsType = ...
) -> tuple[RegexString, int]: ...
def escape(pattern: RegexString) -> RegexString: ...
def purge() -> None: ...
def template(pattern: RegexString | Pattern[RegexString], flags: _FlagsType = ...) -> Pattern[RegexString]: ...
