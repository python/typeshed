from _io import _TextIOBase
from collections.abc import Iterator
from typing import Any, Generic, TypeVar, overload

from pygments.style import Style
from pygments.token import _TokenType

_T = TypeVar("_T", str, bytes)

class Formatter(Generic[_T]):
    name: str | None = None
    aliases: list[str]
    filenames: list[str]
    unicodeoutput: bool
    style: type[Style]
    full: bool
    title: str
    encoding: str
    options: dict[str, Any]
    @overload
    def __init__(self: Formatter[str], *, encoding: None = None, outencoding: None = None, **options: Any) -> None: ...
    @overload
    def __init__(self: Formatter[bytes], *, encoding: str, outencoding: None = None, **options: Any) -> None: ...
    @overload
    def __init__(self: Formatter[bytes], *, encoding: None = None, outencoding: str, **options: Any) -> None: ...
    def get_style_defs(self, arg: str = "") -> str: ...
    def format(self, tokensource: Iterator[tuple[_TokenType, str]], outfile: _TextIOBase) -> None: ...
