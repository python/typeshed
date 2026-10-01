from collections.abc import Collection

from networkx.classes.graph import Graph, _EdgeData, _Node, _NodeData
from networkx.utils.backends import _dispatchable
from scipy.sparse import csr_array  # type: ignore[import-untyped]  # pyright: ignore[reportMissingImports]

__all__ = ["bethe_hessian_matrix"]

@_dispatchable
def bethe_hessian_matrix(
    G: Graph[_Node, _NodeData, _EdgeData], r: float | None = None, nodelist: Collection[_Node] | None = None
) -> csr_array: ...
