from networkx.classes.graph import Graph, _Node, _Edge
from networkx.utils.backends import _dispatch

@_dispatch
def betweenness_centrality_subset(G: Graph[_Node], sources: list[_Node], targets: list[_Node], normalized: bool = False, weight: str | None = None) -> dict[_Node, float]: ...
@_dispatch
def edge_betweenness_centrality_subset(G: Graph[_Node], sources: list[_Node], targets: list[_Node], normalized: bool = False, weight: str | None = None) -> dict[_Edge[_Node], float]: ...
