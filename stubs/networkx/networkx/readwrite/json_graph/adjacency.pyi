from _typeshed import Incomplete
from collections.abc import Mapping
from typing import Any

from networkx.utils.backends import _dispatchable

from ...classes.graph import Graph

__all__ = ["adjacency_data", "adjacency_graph"]

# Any: Complex type union
def adjacency_data(G: Graph[Incomplete], attrs: Mapping[str, Incomplete] = {"id": "id", "key": "key"}) -> dict[str, Any]: ...
@_dispatchable
def adjacency_graph(
    data, directed: bool = False, multigraph: bool = True, attrs: Mapping[str, Incomplete] = {"id": "id", "key": "key"}
): ...
