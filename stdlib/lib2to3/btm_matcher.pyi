from _typeshed import Incomplete, SupportsGetItem
from collections import defaultdict
from collections.abc import Iterable
from lib2to3.fixer_base import BaseFix
from lib2to3.pytree import Leaf, Node
from typing import TypeVar

_T = TypeVar("_T")

class BMNode:
    count: Incomplete
    transition_table: Incomplete
    fixers: Incomplete
    id: Incomplete
    content: str
    def __init__(self) -> None: ...

class BottomMatcher:
    match: Incomplete
    root: Incomplete
    nodes: Incomplete
    fixers: Incomplete
    logger: Incomplete
    def __init__(self) -> None: ...
    def add_fixer(self, fixer: BaseFix) -> None: ...
    def add(self, pattern: SupportsGetItem[int | slice, Incomplete] | None, start: BMNode) -> list[BMNode]: ...
    def run(self, leaves: Iterable[Leaf]) -> defaultdict[BaseFix, list[Node | Leaf]]: ...
    def print_ac(self) -> None: ...

def type_repr(type_num: _T) -> _T: ...
