from collections.abc import Generator, Iterable
from typing_extensions import TypeVar

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import _Node
from networkx.utils.backends import _dispatchable

_DefaultT = TypeVar("_DefaultT")

__all__ = ["all_pairs_lowest_common_ancestor", "tree_all_pairs_lowest_common_ancestor", "lowest_common_ancestor"]

@_dispatchable
def all_pairs_lowest_common_ancestor(
    G: DiGraph[_Node], pairs: Iterable[tuple[_Node, _Node]] | None = None
) -> Generator[tuple[tuple[_Node, _Node], _Node | None]]: ...
@_dispatchable
def lowest_common_ancestor(
    G: DiGraph[_Node], node1: _Node, node2: _Node, default: _DefaultT | None = None
) -> _Node | _DefaultT: ...
@_dispatchable
def tree_all_pairs_lowest_common_ancestor(
    G: DiGraph[_Node], root: _Node | None = None, pairs: Iterable[tuple[_Node, _Node]] | None = None
) -> Generator[tuple[tuple[_Node, _Node], _Node]]: ...
