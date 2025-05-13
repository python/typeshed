from networkx.utils.backends import _dispatchable

from ..classes.graph import Graph

__all__ = ["ego_graph"]

@_dispatchable
def ego_graph(G: Graph[Incomplete], n, radius: float = 1, center: bool = True, undirected: bool = False, distance=None): ...
