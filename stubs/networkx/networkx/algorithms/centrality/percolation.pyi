from _typeshed import SupportsGetItem

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def percolation_centrality(
    G: Graph[_Node], attribute: str | None = "percolation", states: SupportsGetItem | None = None, weight: str | None = None
): ...
