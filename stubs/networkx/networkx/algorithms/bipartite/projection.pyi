from _typeshed import Incomplete
from collections.abc import Callable, Collection

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = [
    "projected_graph",
    "weighted_projected_graph",
    "collaboration_weighted_projected_graph",
    "overlap_weighted_projected_graph",
    "generic_weighted_projected_graph",
]

@_dispatchable
def projected_graph(
    B: Graph[_Node],
    nodes: Collection[Incomplete],  # Not Iterable: iterated more than once, one-shot iterables give wrong results
    multigraph: bool = False,
) -> Graph[Incomplete]: ...
@_dispatchable
def weighted_projected_graph(B: Graph[_Node], nodes: Collection[Incomplete], ratio: bool = False) -> Graph[Incomplete]: ...
@_dispatchable
def collaboration_weighted_projected_graph(
    B: Graph[_Node], nodes: Collection[Incomplete]  # Not Iterable: iterated more than once, one-shot iterables give wrong results
) -> Graph[Incomplete]: ...
@_dispatchable
def overlap_weighted_projected_graph(
    B: Graph[_Node],
    nodes: Collection[Incomplete],  # Not Iterable: iterated more than once, one-shot iterables give wrong results
    jaccard: bool = True,
) -> Graph[Incomplete]: ...
@_dispatchable
def generic_weighted_projected_graph(
    B: Graph[_Node],
    nodes: Collection[Incomplete],  # Not Iterable: iterated more than once, one-shot iterables give wrong results
    weight_function: Callable[..., Incomplete] | None = None,
) -> Graph[Incomplete]: ...
