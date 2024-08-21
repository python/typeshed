import sys
from _typeshed import SupportsNoArgReadline
from collections import deque
from collections.abc import Iterable
from io import TextIOWrapper
from typing import Literal, Protocol, overload, type_check_only
from typing_extensions import Self, deprecated

__all__ = ["shlex", "split", "quote", "join"]

@type_check_only
class _ShlexInstream(SupportsNoArgReadline[object], Protocol):
    def read(self, size: Literal[1], /) -> str: ...
    def close(self) -> object: ...

if sys.version_info >= (3, 12):
    def split(s: str | _ShlexInstream, comments: bool = False, posix: bool = True) -> list[str]: ...

else:
    @overload
    def split(s: str | _ShlexInstream, comments: bool = False, posix: bool = True) -> list[str]: ...
    @overload
    @deprecated("Passing None for 's' to shlex.split() is deprecated and will raise an error in Python 3.12.")
    def split(s: None, comments: bool = False, posix: bool = True) -> list[str]: ...

def join(split_command: Iterable[str]) -> str: ...
def quote(s: str) -> str: ...

# TODO: Make generic over infile once PEP 696 is implemented.
class shlex(Iterable[str]):
    commenters: str
    wordchars: str
    whitespace: str
    escape: str
    quotes: str
    escapedquotes: str
    whitespace_split: bool
    infile: str | None
    instream: _ShlexInstream
    source: str
    debug: int
    lineno: int
    token: str
    filestack: deque[tuple[str | None, _ShlexInstream, int]]
    eof: str | None
    @property
    def punctuation_chars(self) -> str: ...
    def __init__(
        self,
        instream: str | _ShlexInstream | None = None,
        infile: str | None = None,
        posix: bool = False,
        punctuation_chars: bool | str = False,
    ) -> None: ...
    def get_token(self) -> str | None: ...
    def push_token(self, tok: str) -> None: ...
    def read_token(self) -> str | None: ...
    def sourcehook(self, newfile: str) -> tuple[str, TextIOWrapper] | None: ...
    def push_source(self, newstream: str | _ShlexInstream, newfile: str | None = None) -> None: ...
    def pop_source(self) -> None: ...
    def error_leader(self, infile: str | None = None, lineno: int | None = None) -> str: ...
    def __iter__(self) -> Self: ...
    def __next__(self) -> str: ...
