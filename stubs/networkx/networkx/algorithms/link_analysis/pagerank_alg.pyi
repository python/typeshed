from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def pagerank(
    G: Graph[_Node],
    alpha: float | None = 0.85,
    personalization: dict | None = None,
    max_iter: int | None = 100,
    tol: float | None = 1e-06,
    nstart: dict | None = None,
    weight: str | None = "weight",
    dangling: dict | None = None,
): ...
@_dispatchable
def google_matrix(
    G: Graph[_Node],
    alpha: float = 0.85,
    personalization: dict | None = None,
    nodelist: list | None = None,
    weight: str | None = "weight",
    dangling: dict | None = None,
): ...
