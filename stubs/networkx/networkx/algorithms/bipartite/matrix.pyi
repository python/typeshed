from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def biadjacency_matrix(
    G: Graph[_Node],
    row_order: Iterable[_Node],
    column_order: Iterable | None = None,
    dtype=None,
    weight: str | None = "weight",
    format="csr",
): ...
@_dispatchable
def from_biadjacency_matrix(A, create_using: Graph[_Node] | None = None, edge_attribute: str = "weight"): ...
