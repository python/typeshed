from typing import Any, AnyStr, Callable, Iterator, Match, Pattern, overload

# ----- re variables and constants -----
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

class error(Exception): ...

@overload
def compile(pattern: AnyStr, flags: int = ...) -> Pattern[AnyStr]: ...
@overload
def compile(pattern: Pattern[AnyStr], flags: int = ...) -> Pattern[AnyStr]: ...
@overload
def search(pattern: str | unicode, string: AnyStr, flags: int = ...) -> Match[AnyStr] | None: ...
@overload
def search(pattern: Pattern[str] | Pattern[unicode], string: AnyStr, flags: int = ...) -> Match[AnyStr] | None: ...
@overload
def match(pattern: str | unicode, string: AnyStr, flags: int = ...) -> Match[AnyStr] | None: ...
@overload
def match(pattern: Pattern[str] | Pattern[unicode], string: AnyStr, flags: int = ...) -> Match[AnyStr] | None: ...
@overload
def split(pattern: str | unicode, string: AnyStr, maxsplit: int = ..., flags: int = ...) -> list[AnyStr]: ...
@overload
def split(pattern: Pattern[str] | Pattern[unicode], string: AnyStr, maxsplit: int = ..., flags: int = ...) -> list[AnyStr]: ...
@overload
def findall(pattern: str | unicode, string: AnyStr, flags: int = ...) -> list[Any]: ...
@overload
def findall(pattern: Pattern[str] | Pattern[unicode], string: AnyStr, flags: int = ...) -> list[Any]: ...

# Return an iterator yielding match objects over all non-overlapping matches
# for the RE pattern in string. The string is scanned left-to-right, and
# matches are returned in the order found. Empty matches are included in the
# result unless they touch the beginning of another match.
@overload
def finditer(pattern: str | unicode, string: AnyStr, flags: int = ...) -> Iterator[Match[AnyStr]]: ...
@overload
def finditer(pattern: Pattern[str] | Pattern[unicode], string: AnyStr, flags: int = ...) -> Iterator[Match[AnyStr]]: ...
@overload
def sub(pattern: str | unicode, repl: AnyStr, string: AnyStr, count: int = ..., flags: int = ...) -> AnyStr: ...
@overload
def sub(
    pattern: str | unicode, repl: Callable[[Match[AnyStr]], AnyStr], string: AnyStr, count: int = ..., flags: int = ...
) -> AnyStr: ...
@overload
def sub(pattern: Pattern[str] | Pattern[unicode], repl: AnyStr, string: AnyStr, count: int = ..., flags: int = ...) -> AnyStr: ...
@overload
def sub(
    pattern: Pattern[str] | Pattern[unicode],
    repl: Callable[[Match[AnyStr]], AnyStr],
    string: AnyStr,
    count: int = ...,
    flags: int = ...,
) -> AnyStr: ...
@overload
def subn(pattern: str | unicode, repl: AnyStr, string: AnyStr, count: int = ..., flags: int = ...) -> tuple[AnyStr, int]: ...
@overload
def subn(
    pattern: str | unicode, repl: Callable[[Match[AnyStr]], AnyStr], string: AnyStr, count: int = ..., flags: int = ...
) -> tuple[AnyStr, int]: ...
@overload
def subn(
    pattern: Pattern[str] | Pattern[unicode], repl: AnyStr, string: AnyStr, count: int = ..., flags: int = ...
) -> tuple[AnyStr, int]: ...
@overload
def subn(
    pattern: Pattern[str] | Pattern[unicode],
    repl: Callable[[Match[AnyStr]], AnyStr],
    string: AnyStr,
    count: int = ...,
    flags: int = ...,
) -> tuple[AnyStr, int]: ...
def escape(string: AnyStr) -> AnyStr: ...
def purge() -> None: ...
def template(pattern: AnyStr | Pattern[AnyStr], flags: int = ...) -> Pattern[AnyStr]: ...
