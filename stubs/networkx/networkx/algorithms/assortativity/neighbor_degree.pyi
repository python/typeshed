from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def average_neighbor_degree(
    G: Graph[_Node],
    source: str | None = "out",
    target: str | None = "out",
    nodes: Iterable | None = None,
    weight: str | None = None,
): ...
