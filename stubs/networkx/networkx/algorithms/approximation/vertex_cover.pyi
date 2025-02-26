from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def min_weighted_vertex_cover(G: Graph[_Node], weight: str | None = None): ...
