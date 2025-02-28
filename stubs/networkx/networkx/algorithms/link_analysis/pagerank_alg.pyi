from _typeshed import Incomplete, SupportsGetItem
from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def pagerank(
    G: Graph[_Node],
    alpha: float | None = 0.85,
    personalization: SupportsGetItem[Incomplete, Incomplete] | None = None,
    max_iter: int | None = 100,
    tol: float | None = 1e-06,
    nstart: SupportsGetItem[Incomplete, Incomplete] | None = None,
    weight: str | None = "weight",
    dangling: SupportsGetItem[Incomplete, Incomplete] | None = None,
): ...
@_dispatchable
def google_matrix(
    G: Graph[_Node],
    alpha: float = 0.85,
    personalization: SupportsGetItem[Incomplete, Incomplete] | None = None,
    nodelist: Iterable[Incomplete] | None = None,
    weight: str | None = "weight",
    dangling: SupportsGetItem[Incomplete, Incomplete] | None = None,
): ...
