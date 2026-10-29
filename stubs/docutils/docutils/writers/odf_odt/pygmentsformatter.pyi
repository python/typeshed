from _typeshed import SupportsWrite
from collections.abc import Callable, Iterable
from typing import Any, Protocol, type_check_only

# A minimal stand-in for `pygments.formatter.Formatter[str]` (pygments is an optional dependency).
@type_check_only
class _Formatter:
    name: str | None
    aliases: list[str]
    filenames: list[str]
    unicodeoutput: bool
    style: type[object]
    full: bool
    title: str
    encoding: str | None
    options: dict[str, Any]  # arbitrary formatter options
    def __init__(self, *, encoding: None = None, outencoding: None = None, **options: object) -> None: ...
    def get_style_defs(self, arg: str = "") -> str: ...
    def format(self, tokensource: Iterable[tuple[object, str]], outfile: SupportsWrite[str]) -> None: ...

# `ODFTranslator.rststyle()`
@type_check_only
class _RstStyleFunction(Protocol):
    def __call__(self, name: str, parameters: tuple[object, ...] = ..., /) -> str: ...

class OdtPygmentsFormatter(_Formatter):
    rststyle_function: _RstStyleFunction
    escape_function: Callable[[str], str]
    def __init__(self, rststyle_function: _RstStyleFunction, escape_function: Callable[[str], str]) -> None: ...
    def rststyle(self, name: str, parameters: tuple[object, ...] = ()) -> str: ...

class OdtPygmentsProgFormatter(OdtPygmentsFormatter):
    def format(self, tokensource: Iterable[tuple[object, str]], outfile: SupportsWrite[str]) -> None: ...

class OdtPygmentsLaTeXFormatter(OdtPygmentsFormatter):
    def format(self, tokensource: Iterable[tuple[object, str]], outfile: SupportsWrite[str]) -> None: ...
