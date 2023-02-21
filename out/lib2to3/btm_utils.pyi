from . import pytree as pytree
from .pgen2 import grammar as grammar, token as token
from .pygram import pattern_symbols as pattern_symbols, python_symbols as python_symbols
from _typeshed import Incomplete
from collections.abc import Generator

syms = pattern_symbols
pysyms = python_symbols
tokens: Incomplete
token_labels = token
TYPE_ANY: int
TYPE_ALTERNATIVES: int
TYPE_GROUP: int

class MinNode:
    type: Incomplete
    name: Incomplete
    children: Incomplete
    leaf: bool
    parent: Incomplete
    alternatives: Incomplete
    group: Incomplete
    def __init__(self, type: Incomplete | None = ..., name: Incomplete | None = ...) -> None: ...
    def leaf_to_root(self): ...
    def get_linear_subpattern(self): ...
    def leaves(self) -> Generator[Incomplete, None, None]: ...

def reduce_tree(node, parent: Incomplete | None = ...): ...
def get_characteristic_subpattern(subpatterns): ...
def rec_test(sequence, test_func) -> Generator[Incomplete, None, None]: ...
