from collections.abc import Iterable, Set as AbstractSet

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["modularity"]

@_dispatchable
def modularity(
    G: Graph[_Node],
    communities: Iterable[AbstractSet[_Node]],
    nodes: Iterable[_Node],
    *,
    weight: str | None = "weight",
    resolution: float = 1,
) -> float: ...
