from _typeshed import SupportsGetItem
from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def hopcroft_karp_matching(G: Graph[_Node], top_nodes: Iterable[_Node] = None): ...
@_dispatchable
def eppstein_matching(G: Graph[_Node], top_nodes: Iterable = None): ...
@_dispatchable
def to_vertex_cover(G: Graph[_Node], matching: SupportsGetItem, top_nodes: Iterable = None): ...

maximum_matching = hopcroft_karp_matching

@_dispatchable
def minimum_weight_full_matching(G: Graph[_Node], top_nodes: Iterable = None, weight: str | None = "weight"): ...
