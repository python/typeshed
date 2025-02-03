from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable
from numpy.random import RandomState

@_dispatchable
def leiden_communities(
    G: Graph[_Node],
    weight: str | None = "weight",
    resolution: float | None = 1,
    max_level: int | None = None,
    seed: int | RandomState | None = None,
): ...
@_dispatchable
def leiden_partitions(
    G: Graph[_Node], weight: str | None = "weight", resolution: float | None = 1, seed: int | RandomState | None = None
): ...
