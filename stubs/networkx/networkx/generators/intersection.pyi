from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

__all__ = ["uniform_random_intersection_graph", "k_random_intersection_graph", "general_random_intersection_graph"]

@_dispatchable
def uniform_random_intersection_graph(n, m, p, seed: Incomplete | None = None): ...
@_dispatchable
def k_random_intersection_graph(n, m, k, seed: Incomplete | None = None): ...
@_dispatchable
def general_random_intersection_graph(n, m, p, seed: Incomplete | None = None): ...
