import functools
from _typeshed import Incomplete
import networkx as nx

__all__ = [
    "edge_betweenness_partition",
    "edge_current_flow_betweenness_partition"
]


@nx._dispatchable(edge_attrs="weight")
def edge_betweenness_partition(G, number_of_sets: int, *, weight: Incomplete | None=None) -> list[Incomplete]: ...

@nx._dispatchable(edge_attrs="weight")
def edge_current_flow_betweenness_partition(G, number_of_sets: int, *, weight: Incomplete | None=None) -> list[Incomplete]: ...
