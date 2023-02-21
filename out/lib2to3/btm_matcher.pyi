from . import pytree as pytree
from .btm_utils import reduce_tree as reduce_tree
from _typeshed import Incomplete

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
    def add_fixer(self, fixer) -> None: ...
    def add(self, pattern, start): ...
    def run(self, leaves): ...
    def print_ac(self) -> None: ...

def type_repr(type_num): ...
