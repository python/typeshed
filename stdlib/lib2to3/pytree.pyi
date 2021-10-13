from lib2to3.pgen2.grammar import Grammar
from typing import Any, Callable, Dict, Iterator, List, Optional, Tuple, TypeVar, Union

_P = TypeVar("_P")
_NL = Union[Node, Leaf]
_Context = Tuple[str, int, int]
_Results = Dict[str, _NL]
_RawNode = Tuple[int, str, _Context, Optional[List[_NL]]]
_Convert = Callable[[Grammar, _RawNode], Any]

HUGE: int

def type_repr(type_num: int) -> str: ...

class Base:
    type: int
    parent: Node | None
    prefix: str
    children: list[_NL]
    was_changed: bool
    was_checked: bool
    def __eq__(self, other: Any) -> bool: ...
    def _eq(self: _P, other: _P) -> bool: ...
    def clone(self: _P) -> _P: ...
    def post_order(self) -> Iterator[_NL]: ...
    def pre_order(self) -> Iterator[_NL]: ...
    def replace(self, new: _NL | list[_NL]) -> None: ...
    def get_lineno(self) -> int: ...
    def changed(self) -> None: ...
    def remove(self) -> int | None: ...
    @property
    def next_sibling(self) -> _NL | None: ...
    @property
    def prev_sibling(self) -> _NL | None: ...
    def leaves(self) -> Iterator[Leaf]: ...
    def depth(self) -> int: ...
    def get_suffix(self) -> str: ...

class Node(Base):
    fixers_applied: list[Any]
    def __init__(
        self,
        type: int,
        children: list[_NL],
        context: Any | None = ...,
        prefix: str | None = ...,
        fixers_applied: list[Any] | None = ...,
    ) -> None: ...
    def set_child(self, i: int, child: _NL) -> None: ...
    def insert_child(self, i: int, child: _NL) -> None: ...
    def append_child(self, child: _NL) -> None: ...

class Leaf(Base):
    lineno: int
    column: int
    value: str
    fixers_applied: list[Any]
    def __init__(
        self, type: int, value: str, context: _Context | None = ..., prefix: str | None = ..., fixers_applied: list[Any] = ...
    ) -> None: ...

def convert(gr: Grammar, raw_node: _RawNode) -> _NL: ...

class BasePattern:
    type: int
    content: str | None
    name: str | None
    def optimize(self) -> BasePattern: ...  # sic, subclasses are free to optimize themselves into different patterns
    def match(self, node: _NL, results: _Results | None = ...) -> bool: ...
    def match_seq(self, nodes: list[_NL], results: _Results | None = ...) -> bool: ...
    def generate_matches(self, nodes: list[_NL]) -> Iterator[tuple[int, _Results]]: ...

class LeafPattern(BasePattern):
    def __init__(self, type: int | None = ..., content: str | None = ..., name: str | None = ...) -> None: ...

class NodePattern(BasePattern):
    wildcards: bool
    def __init__(self, type: int | None = ..., content: str | None = ..., name: str | None = ...) -> None: ...

class WildcardPattern(BasePattern):
    min: int
    max: int
    def __init__(self, content: str | None = ..., min: int = ..., max: int = ..., name: str | None = ...) -> None: ...

class NegatedPattern(BasePattern):
    def __init__(self, content: str | None = ...) -> None: ...

def generate_matches(patterns: list[BasePattern], nodes: list[_NL]) -> Iterator[tuple[int, _Results]]: ...
