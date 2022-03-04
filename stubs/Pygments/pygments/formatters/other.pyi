from typing import Any, TypeVar

from pygments.formatter import _TextFormatter

_T = TypeVar("_T", str, bytes)

class NullFormatter(_TextFormatter[_T]):
    name: str
    aliases: Any
    filenames: Any
    def format(self, tokensource, outfile) -> None: ...

class RawTokenFormatter(_TextFormatter[_T]):
    name: str
    aliases: Any
    filenames: Any
    unicodeoutput: bool
    encoding: str
    compress: Any
    error_color: Any
    def format(self, tokensource, outfile) -> None: ...

class TestcaseFormatter(_TextFormatter[_T]):
    name: str
    aliases: Any
    def format(self, tokensource, outfile) -> None: ...
