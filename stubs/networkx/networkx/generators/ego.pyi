from networkx.classes.graph import Graph, _EdgeData, _Node, _NodeData
from networkx.utils.backends import _dispatchable

__all__ = ["ego_graph"]

@_dispatchable
def ego_graph(
    G: Graph[_Node, _NodeData, _EdgeData], n, radius: float = 1, center: bool = True, undirected: bool = False, distance=None
): ...
