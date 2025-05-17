from _typeshed import Incomplete
from collections.abc import Callable

from networkx.utils.backends import _dispatchable

from ..classes.graph import Graph

__all__ = ["attr_matrix", "attr_sparse_matrix"]

@_dispatchable
def attr_matrix(
    G: Graph[Incomplete],
    edge_attr: str | Callable[[Incomplete, Incomplete], Incomplete] | None = None,
    node_attr: str | Callable[[Incomplete], Incomplete] | None = None,
    normalized: bool = False,
    rc_order=None,
    dtype=None,
    order=None,
): ...
@_dispatchable
def attr_sparse_matrix(
    G: Graph[Incomplete],
    edge_attr: str | Callable[[Incomplete, Incomplete], Incomplete] | None = None,
    node_attr: str | Callable[[Incomplete], Incomplete] | None = None,
    normalized: bool = False,
    rc_order=None,
    dtype=None,
): ...
