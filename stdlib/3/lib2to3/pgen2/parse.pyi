# Stubs for lib2to3.pgen2.parse (Python 3.6)

from typing import Any, List, Optional, Sequence, Set, Tuple

from lib2to3.pgen2.driver import _Convert, _RawNode
from lib2to3.pgen2.grammar import Grammar, _States
from lib2to3.pytree import _NL

_Context = Sequence[Any]

class ParseError(Exception):
    msg: str
    type: int
    value: Optional[str]
    context: _Context
    def __init__(self, msg: str, type: int, value: Optional[str], context: _Context) -> None: ...

class Parser:
    grammar: Grammar
    convert: _Convert
    stack: List[Tuple[_States, int, _RawNode]]
    rootnode: Optional[_NL]
    used_names: Set[str]
    def __init__(self, grammar: Grammar, convert: Optional[_Convert] = ...) -> None: ...
    def setup(self, start: Optional[int] = ...) -> None: ...
    def addtoken(self, type: int, value: Optional[str], context: _Context) -> bool: ...
    def classify(self, type: int, value: Optional[str], context: _Context) -> int: ...
    def shift(self, type: int, value: Optional[str], newstate: int, context: _Context) -> None: ...
    def push(self, type: int, newdfa: _States, newstate: int, context: _Context) -> None: ...
    def pop(self) -> None: ...
