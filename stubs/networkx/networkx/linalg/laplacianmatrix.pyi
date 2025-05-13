from _typeshed import Incomplete
from collections.abc import Collection

from networkx.utils.backends import _dispatchable

from ..classes.digraph import DiGraph
from ..classes.graph import Graph

__all__ = [
    "laplacian_matrix",
    "normalized_laplacian_matrix",
    "total_spanning_tree_weight",
    "directed_laplacian_matrix",
    "directed_combinatorial_laplacian_matrix",
]

@_dispatchable
def laplacian_matrix(G: Graph[Incomplete], nodelist: Collection[Incomplete] | None = None, weight: str = "weight"): ...
@_dispatchable
def normalized_laplacian_matrix(G: Graph[Incomplete], nodelist: Collection[Incomplete] | None = None, weight: str = "weight"): ...
@_dispatchable
def total_spanning_tree_weight(G: Graph[Incomplete], weight: str | None = None) -> float: ...
@_dispatchable
def directed_laplacian_matrix(
    G: DiGraph[Incomplete],
    nodelist: Collection[Incomplete] | None = None,
    weight: str = "weight",
    walk_type: Incomplete | None = None,
    alpha: float = 0.95,
): ...
@_dispatchable
def directed_combinatorial_laplacian_matrix(
    G: DiGraph[Incomplete],
    nodelist: Collection[Incomplete] | None = None,
    weight: str = "weight",
    walk_type: Incomplete | None = None,
    alpha: float = 0.95,
): ...
