from _typeshed import SupportsGetItem

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def hits(
    G: Graph[_Node],
    max_iter: int | None = 100,
    tol: float | None = 1e-08,
    nstart: SupportsGetItem | None = None,
    normalized: bool = True,
): ...
