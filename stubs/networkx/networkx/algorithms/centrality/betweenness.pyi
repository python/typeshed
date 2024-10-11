from _typeshed import Incomplete

from networkx.classes.graph import Graph, _Edge, _Node
from networkx.utils.backends import _dispatchable
from numpy.random import RandomState

@_dispatchable
def betweenness_centrality(
    G: Graph[_Node],
    k: int | None = None,
    normalized: bool = True,
    weight: str | None = None,
    endpoints: bool = False,
    seed: int | RandomState | None = None,
) -> dict[_Node, float]: ...
@_dispatchable
def edge_betweenness_centrality(
    G: Graph[_Node], k: int | None = None, normalized: bool = True, weight: str | None = None, seed: Incomplete | None = None
) -> dict[_Edge[_Node], float]: ...
