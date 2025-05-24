from _typeshed import Incomplete
from collections.abc import Collection

from networkx.utils.backends import _dispatchable

from ..classes.graph import Graph, _Node

__all__ = ["bethe_hessian_matrix"]

@_dispatchable
def bethe_hessian_matrix(G: Graph[_Node], r: float | None = None, nodelist: Collection[Incomplete] | None = None): ...
