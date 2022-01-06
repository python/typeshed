from _typeshed import SupportsWrite
from typing import Any, TypeVar, overload

from .formatter import Formatter

_T = TypeVar("_T", str, bytes)

def lex(code, lexer): ...
@overload
def format(tokens, formatter: Formatter[_T], outfile: SupportsWrite[_T]) -> None: ...
@overload
def format(tokens, formatter: Formatter[_T], outfile: None = ...) -> _T: ...
@overload
def highlight(code, lexer, formatter, outfile: SupportsWrite[Any]) -> None: ...
@overload
def highlight(code, lexer, formatter, outfile: None = ...) -> str: ...
