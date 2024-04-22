from _typeshed import Incomplete
from numpy.random import RandomState

from networkx.classes.graph import Graph, _Node, _Edge
from networkx.utils.backends import _dispatch

@_dispatch
def betweenness_centrality(
    G: Graph[_Node],
    k: int | None = None,
    normalized: bool = True,
    weight: str | None = None,
    endpoints: bool = False,
    seed: int | RandomState | None = None,
) -> dict[_Node, float]: ...
@_dispatch
def edge_betweenness_centrality(
    G: Graph[_Node], k: int | None = None, normalized: bool = True, weight: str | None = None, seed: Incomplete | None = None
) -> dict[_Edge[_Node], float]: ...
