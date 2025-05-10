from _typeshed import Incomplete
from collections.abc import Collection

from networkx.utils.backends import _dispatchable

__all__ = ["incidence_matrix", "adjacency_matrix"]

@_dispatchable
def incidence_matrix(
    G,
    nodelist: Collection[Incomplete] | None = None,
    edgelist: Incomplete | None = None,
    oriented: bool = False,
    weight: Incomplete | None = None,
): ...
@_dispatchable
def adjacency_matrix(
    G, nodelist: Collection[Incomplete] | None = None, dtype: Incomplete | None = None, weight: str = "weight"
): ...
