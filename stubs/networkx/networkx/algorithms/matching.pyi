from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = [
    "is_matching",
    "is_maximal_matching",
    "is_perfect_matching",
    "max_weight_matching",
    "min_weight_matching",
    "maximal_matching",
]

@_dispatchable
def maximal_matching(G: Graph[_Node]): ...
@_dispatchable
def is_matching(G: Graph[_Node], matching): ...
@_dispatchable
def is_maximal_matching(G: Graph[_Node], matching): ...
@_dispatchable
def is_perfect_matching(G: Graph[_Node], matching): ...
@_dispatchable
def min_weight_matching(G: Graph[_Node], weight: str | None = "weight"): ...
@_dispatchable
def max_weight_matching(G: Graph[_Node], maxcardinality: bool | None = False, weight: str | None = "weight"): ...
