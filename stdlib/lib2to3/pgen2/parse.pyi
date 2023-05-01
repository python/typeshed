from _typeshed import Incomplete
from collections.abc import Sequence
from typing_extensions import TypeAlias

from ..pytree import _NL, _RawNode
from . import _Convert
from .grammar import _DFAS, Grammar

_Context: TypeAlias = Sequence[Incomplete]

class ParseError(Exception):
    msg: str
    type: int
    value: str | None
    context: _Context
    def __init__(self, msg: str, type: int, value: str | None, context: _Context) -> None: ...

class Parser:
    grammar: Grammar
    convert: _Convert
    stack: list[tuple[_DFAS, int, _RawNode]]
    rootnode: _NL | None
    used_names: set[str]
    def __init__(self, grammar: Grammar, convert: _Convert | None = None) -> None: ...
    def setup(self, start: int | None = None) -> None: ...
    def addtoken(self, type: int, value: str | None, context: _Context) -> bool: ...
    def classify(self, type: int, value: str | None, context: _Context) -> int: ...
    def shift(self, type: int, value: str | None, newstate: int, context: _Context) -> None: ...
    def push(self, type: int, newdfa: _DFAS, newstate: int, context: _Context) -> None: ...
    def pop(self) -> None: ...
