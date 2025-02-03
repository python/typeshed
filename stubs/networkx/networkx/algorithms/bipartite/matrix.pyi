from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def biadjacency_matrix(
    G: Graph[_Node],
    row_order: list[_Node],
    column_order: list | None = None,
    dtype=None,
    weight: str | None = "weight",
    format="csr",
): ...
@_dispatchable
def from_biadjacency_matrix(A, create_using: Graph[_Node] = None, edge_attribute: str = "weight"): ...
