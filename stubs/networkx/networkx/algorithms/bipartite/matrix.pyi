from _typeshed import Incomplete
from collections.abc import Iterable

import numpy as np
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable
from scipy.sparse import sparray  # type: ignore[import-untyped]  # pyright: ignore[reportMissingImports]

__all__ = ["biadjacency_matrix", "from_biadjacency_matrix"]

@_dispatchable
def biadjacency_matrix(
    G: Graph[_Node],
    row_order: Iterable[_Node],
    column_order: Iterable[Incomplete] | None = None,
    dtype: np.dtype[Incomplete] | None = None,
    weight: str | None = "weight",
    format: str = "csr",
) -> sparray: ...  # Return is a complex union of scipy classes depending on the format param
@_dispatchable
def from_biadjacency_matrix(
    A: sparray, create_using: Graph[_Node] | None = None, edge_attribute: str = "weight"
) -> Graph[Incomplete]: ...
