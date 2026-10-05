from _typeshed import Incomplete
from collections.abc import Callable, Generator

from networkx.classes.graph import Graph, _EdgeData, _Node, _NodeData

__all__ = ["cuthill_mckee_ordering", "reverse_cuthill_mckee_ordering"]

def cuthill_mckee_ordering(
    G: Graph[_Node, _NodeData, _EdgeData], heuristic: Callable[..., Incomplete] | None = None
) -> Generator[Incomplete, Incomplete]: ...
def reverse_cuthill_mckee_ordering(
    G: Graph[_Node, _NodeData, _EdgeData], heuristic: Callable[..., Incomplete] | None = None
) -> Generator[Incomplete, Incomplete, Incomplete]: ...
def connected_cuthill_mckee_ordering(G: Graph[_Node, _NodeData, _EdgeData], heuristic=None): ...
def pseudo_peripheral_node(G: Graph[_Node, _NodeData, _EdgeData]): ...
