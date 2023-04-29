import sys
from collections.abc import Iterable
from typing import TextIO
from typing_extensions import Self

if sys.version_info >= (3, 8):
    __all__ = ["shlex", "split", "quote", "join"]
else:
    __all__ = ["shlex", "split", "quote"]

def split(s: str, comments: bool = False, posix: bool = True) -> list[str]: ...

if sys.version_info >= (3, 8):
    def join(split_command: Iterable[str]) -> str: ...

def quote(s: str) -> str: ...

class shlex(Iterable[str]):
    commenters: str
    wordchars: str
    whitespace: str
    escape: str
    quotes: str
    escapedquotes: str
    whitespace_split: bool
    infile: str | None
    instream: TextIO
    source: str
    debug: int
    lineno: int
    token: str
    eof: str | None
    @property
    def punctuation_chars(self) -> str: ...
    def __init__(
        self,
        instream: str | TextIO | None = None,
        infile: str | None = None,
        posix: bool = False,
        punctuation_chars: bool | str = False,
    ) -> None: ...
    def get_token(self) -> str | None: ...
    def push_token(self, tok: str) -> None: ...
    def read_token(self) -> str | None: ...
    def sourcehook(self, newfile: str) -> tuple[str, TextIO] | None: ...
    def push_source(self, newstream: str | TextIO, newfile: str | None = None) -> None: ...
    def pop_source(self) -> None: ...
    def error_leader(self, infile: str | None = None, lineno: int | None = None) -> str: ...
    def __iter__(self) -> Self: ...
    def __next__(self) -> str: ...
