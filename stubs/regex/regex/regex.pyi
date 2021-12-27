from typing import Any, AnyStr, Callable, NoReturn, Tuple, overload

import regex._regex as _regex

__version__: str

A: int
ASCII: int
B: int
BESTMATCH: int
D: int
DEBUG: int
E: int
ENHANCEMATCH: int
F: int
FULLCASE: int
I: int
IGNORECASE: int
L: int
LOCALE: int
M: int
MULTILINE: int
P: int
POSIX: int
R: int
REVERSE: int
T: int
TEMPLATE: int
S: int
DOTALL: int
U: int
UNICODE: int
V0: int
VERSION0: int
V1: int
VERSION1: int
W: int
WORD: int
X: int
VERBOSE: int

DEFAULT_VERSION: int

@overload
def compile(pattern: AnyStr, flags: int = ..., ignore_unused: bool = ..., **kwargs: Any) -> _regex.Pattern: ...
@overload
def compile(pattern: _regex.Pattern, flags: int = ..., ignore_unused: bool = ..., **kwargs: Any) -> _regex.Pattern: ...
@overload
def search(
    pattern: AnyStr,
    string: AnyStr,
    flags: int = ...,
    pos: int | None = ...,
    endpos: int | None = ...,
    partial: bool = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> _regex.Match | None: ...
@overload
def search(
    pattern: _regex.Pattern,
    string: AnyStr,
    flags: int = ...,
    pos: int | None = ...,
    endpos: int | None = ...,
    partial: bool = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> _regex.Match | None: ...
@overload
def match(
    pattern: AnyStr,
    string: AnyStr,
    flags: int = ...,
    pos: int | None = ...,
    endpos: int | None = ...,
    partial: bool = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> _regex.Match: ...
@overload
def match(
    pattern: _regex.Pattern,
    string: AnyStr,
    flags: int = ...,
    pos: int | None = ...,
    endpos: int | None = ...,
    partial: bool = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> _regex.Match: ...
@overload
def fullmatch(
    pattern: AnyStr,
    string: AnyStr,
    flags: int = ...,
    pos: int | None = ...,
    endpos: int | None = ...,
    partial: bool = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> _regex.Match: ...
@overload
def fullmatch(
    pattern: _regex.Pattern,
    string: AnyStr,
    flags: int = ...,
    pos: int | None = ...,
    endpos: int | None = ...,
    partial: bool = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> _regex.Match: ...
@overload
def split(
    pattern: AnyStr,
    string: AnyStr,
    maxsplit: int = ...,
    flags: int = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> list[AnyStr]: ...
@overload
def split(
    pattern: _regex.Pattern,
    string: AnyStr,
    maxsplit: int = ...,
    flags: int = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> list[AnyStr]: ...
@overload
def splititer(
    pattern: AnyStr,
    string: AnyStr,
    maxsplit: int = ...,
    flags: int = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> _regex.Splitter: ...
@overload
def splititer(
    pattern: _regex.Pattern,
    string: AnyStr,
    maxsplit: int = ...,
    flags: int = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> _regex.Splitter: ...
@overload
def findall(
    pattern: AnyStr,
    string: AnyStr,
    flags: int = ...,
    pos: int | None = ...,
    endpos: int | None = ...,
    overlapped: bool = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> list[str] | list[Tuple[str, ...]]: ...
@overload
def findall(
    pattern: _regex.Pattern,
    string: AnyStr,
    flags: int = ...,
    pos: int | None = ...,
    endpos: int | None = ...,
    overlapped: bool = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> list[str] | list[Tuple[str, ...]]: ...
@overload
def finditer(
    pattern: AnyStr,
    string: AnyStr,
    flags: int = ...,
    pos: int | None = ...,
    endpos: int | None = ...,
    overlapped: bool = ...,
    partial: bool = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> _regex.Scanner: ...
@overload
def finditer(
    pattern: _regex.Pattern,
    string: AnyStr,
    flags: int = ...,
    pos: int | None = ...,
    endpos: int | None = ...,
    overlapped: bool = ...,
    partial: bool = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> _regex.Scanner: ...
def purge() -> None: ...
@overload
def cache_all(value: bool = ...) -> NoReturn: ...
@overload
def cache_all(value: None = ...) -> bool: ...
def escape(pattern: AnyStr, special_only: bool = ..., literal_spaces: bool = ...) -> AnyStr: ...
@overload
def template(pattern: AnyStr, flags: int = ...) -> _regex.Pattern: ...
@overload
def template(pattern: _regex.Pattern, flags: int = ...) -> _regex.Pattern: ...
@overload
def sub(
    pattern: AnyStr,
    repl: AnyStr | Callable[[_regex.Match], AnyStr],
    string: AnyStr,
    count: int = ...,
    flags: int = ...,
    pos: int | None = ...,
    endpos: int | None = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> AnyStr: ...
@overload
def sub(
    pattern: _regex.Pattern,
    repl: AnyStr | Callable[[_regex.Match], AnyStr],
    string: AnyStr,
    count: int = ...,
    flags: int = ...,
    pos: int | None = ...,
    endpos: int | None = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> AnyStr: ...
@overload
def subf(
    pattern: AnyStr,
    format: AnyStr | Callable[[_regex.Match], AnyStr],
    string: AnyStr,
    count: int = ...,
    flags: int = ...,
    pos: int | None = ...,
    endpos: int | None = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> AnyStr: ...
@overload
def subf(
    pattern: _regex.Pattern,
    format: AnyStr | Callable[[_regex.Match], AnyStr],
    string: AnyStr,
    count: int = ...,
    flags: int = ...,
    pos: int | None = ...,
    endpos: int | None = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> AnyStr: ...
@overload
def subn(
    pattern: AnyStr,
    repl: AnyStr | Callable[[_regex.Match], AnyStr],
    string: AnyStr,
    count: int = ...,
    flags: int = ...,
    pos: int | None = ...,
    endpos: int | None = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> AnyStr: ...
@overload
def subn(
    pattern: _regex.Pattern,
    repl: AnyStr | Callable[[_regex.Match], AnyStr],
    string: AnyStr,
    count: int = ...,
    flags: int = ...,
    pos: int | None = ...,
    endpos: int | None = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> AnyStr: ...
@overload
def subfn(
    pattern: AnyStr,
    format: AnyStr | Callable[[_regex.Match], AnyStr],
    string: AnyStr,
    count: int = ...,
    flags: int = ...,
    pos: int | None = ...,
    endpos: int | None = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> tuple[AnyStr, int]: ...
@overload
def subfn(
    pattern: _regex.Pattern,
    format: AnyStr | Callable[[_regex.Match], AnyStr],
    string: AnyStr,
    count: int = ...,
    flags: int = ...,
    pos: int | None = ...,
    endpos: int | None = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> tuple[AnyStr, int]: ...

Pattern: _regex.Pattern
Match: _regex.Match
Regex = compile
