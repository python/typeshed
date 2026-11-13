from _typeshed import FloatInt
from _typeshed import Incomplete
from collections.abc import Mapping

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["eigenvector_centrality", "eigenvector_centrality_numpy"]

@_dispatchable
def eigenvector_centrality(
    G: Graph[_Node],
    max_iter: int | None = 100,
    tol: FloatInt | None = 1e-06,
    nstart: Mapping[Incomplete, Incomplete] | None = None,
    weight: str | None = None,
) -> dict[Incomplete, float]: ...
@_dispatchable
def eigenvector_centrality_numpy(
    G: Graph[_Node], weight: str | None = None, max_iter: int | None = 50, tol: FloatInt | None = 0
) -> dict[Incomplete, Incomplete]: ...
