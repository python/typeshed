from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["tree_broadcast_center", "tree_broadcast_time"]

@_dispatchable
def tree_broadcast_center(G: Graph[_Node]) -> tuple[int, set[_Node]]: ...
@_dispatchable
def tree_broadcast_time(G: Graph[_Node], node: int | None = None) -> int: ...
