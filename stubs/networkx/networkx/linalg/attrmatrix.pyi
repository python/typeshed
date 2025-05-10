from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

__all__ = ["attr_matrix", "attr_sparse_matrix"]

@_dispatchable
def attr_matrix(
    G,
    edge_attr: Incomplete | None = None,
    node_attr: Incomplete | None = None,
    normalized: bool = False,
    rc_order: Incomplete | None = None,
    dtype: Incomplete | None = None,
    order: Incomplete | None = None,
): ...
@_dispatchable
def attr_sparse_matrix(
    G,
    edge_attr: Incomplete | None = None,
    node_attr: Incomplete | None = None,
    normalized: bool = False,
    rc_order: Incomplete | None = None,
    dtype: Incomplete | None = None,
): ...
