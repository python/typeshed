from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

__all__ = ["bethe_hessian_matrix"]

@_dispatchable
def bethe_hessian_matrix(G, r: Incomplete | None = None, nodelist: Incomplete | None = None): ...
