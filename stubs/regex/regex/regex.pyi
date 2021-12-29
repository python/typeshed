from typing import Any, AnyStr, Callable, overload

import regex._regex as _regex
from regex._regex_core import *

__version__: str

@overload
def compile(pattern: AnyStr, flags: int = ..., ignore_unused: bool = ..., **kwargs: Any) -> _regex.Pattern[AnyStr]: ...
@overload
def compile(
    pattern: _regex.Pattern[AnyStr], flags: int = ..., ignore_unused: bool = ..., **kwargs: Any
) -> _regex.Pattern[AnyStr]: ...
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
) -> _regex.Match[AnyStr] | None: ...
@overload
def search(
    pattern: _regex.Pattern[AnyStr],
    string: AnyStr,
    flags: int = ...,
    pos: int | None = ...,
    endpos: int | None = ...,
    partial: bool = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> _regex.Match[AnyStr] | None: ...
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
) -> _regex.Match[AnyStr] | None: ...
@overload
def match(
    pattern: _regex.Pattern[AnyStr],
    string: AnyStr,
    flags: int = ...,
    pos: int | None = ...,
    endpos: int | None = ...,
    partial: bool = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> _regex.Match[AnyStr] | None: ...
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
) -> _regex.Match[AnyStr] | None: ...
@overload
def fullmatch(
    pattern: _regex.Pattern[AnyStr],
    string: AnyStr,
    flags: int = ...,
    pos: int | None = ...,
    endpos: int | None = ...,
    partial: bool = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> _regex.Match[AnyStr] | None: ...
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
    pattern: _regex.Pattern[AnyStr],
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
) -> _regex.Splitter[AnyStr]: ...
@overload
def splititer(
    pattern: _regex.Pattern[AnyStr],
    string: AnyStr,
    maxsplit: int = ...,
    flags: int = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> _regex.Splitter[AnyStr]: ...
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
) -> list[Any]: ...
@overload
def findall(
    pattern: _regex.Pattern[AnyStr],
    string: AnyStr,
    flags: int = ...,
    pos: int | None = ...,
    endpos: int | None = ...,
    overlapped: bool = ...,
    concurrent: bool | None = ...,
    timeout: int | None = ...,
    ignore_unused: bool = ...,
    **kwargs: Any,
) -> list[Any]: ...
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
) -> _regex.Scanner[AnyStr]: ...
@overload
def finditer(
    pattern: _regex.Pattern[AnyStr],
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
) -> _regex.Scanner[AnyStr]: ...
@overload
def sub(
    pattern: AnyStr,
    repl: AnyStr | Callable[[_regex.Match[AnyStr]], AnyStr],
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
    pattern: _regex.Pattern[AnyStr],
    repl: AnyStr | Callable[[_regex.Match[AnyStr]], AnyStr],
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
    format: AnyStr | Callable[[_regex.Match[AnyStr]], AnyStr],
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
    pattern: _regex.Pattern[AnyStr],
    format: AnyStr | Callable[[_regex.Match[AnyStr]], AnyStr],
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
    repl: AnyStr | Callable[[_regex.Match[AnyStr]], AnyStr],
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
    pattern: _regex.Pattern[AnyStr],
    repl: AnyStr | Callable[[_regex.Match[AnyStr]], AnyStr],
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
    format: AnyStr | Callable[[_regex.Match[AnyStr]], AnyStr],
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
    pattern: _regex.Pattern[AnyStr],
    format: AnyStr | Callable[[_regex.Match[AnyStr]], AnyStr],
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
def purge() -> None: ...
@overload
def cache_all(value: bool = ...) -> None: ...
@overload
def cache_all(value: None) -> bool: ...
def escape(pattern: AnyStr, special_only: bool = ..., literal_spaces: bool = ...) -> AnyStr: ...
@overload
def template(pattern: AnyStr, flags: int = ...) -> _regex.Pattern[AnyStr]: ...
@overload
def template(pattern: _regex.Pattern[AnyStr], flags: int = ...) -> _regex.Pattern[AnyStr]: ...

Pattern = _regex.Pattern
Match = _regex.Match
Regex = compile
