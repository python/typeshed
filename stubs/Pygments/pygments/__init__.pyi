from typing import Any, TypeVar, overload
from _typeshed import SupportsWrite

from pygments.formatters import Formatter

_T = TypeVar("_T", str, bytes)

def lex(code, lexer): ...
@overload
def format(tokens, formatter: Formatter[Any], outfile: SupportsWrite) -> None: ...
@overload
def format(tokens, formatter: Formatter[_T], outfile: None = ...) -> _T: ...
@overload
def highlight(code, lexer, formatter, outfile: SupportsWrite) -> None: ...
@overload
def highlight(code, lexer, formatter, outfile: None = ...) -> str: ...
