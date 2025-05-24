from _typeshed import Incomplete
from collections.abc import Iterable, Mapping

from networkx.classes.graph import Graph
from networkx.utils.backends import _dispatchable

__all__ = [
    "geometric_edges",
    "geographical_threshold_graph",
    "navigable_small_world_graph",
    "random_geometric_graph",
    "soft_random_geometric_graph",
    "thresholded_random_geometric_graph",
    "waxman_graph",
    "geometric_soft_configuration_graph",
]

@_dispatchable
def geometric_edges(G, radius: float, p: float = 2): ...
@_dispatchable
def random_geometric_graph(
    n: int | Iterable[Incomplete],
    radius: float,
    dim: int = 2,
    pos: Mapping[Incomplete, Incomplete] | None = None,
    p: float = 2,
    seed=None,
): ...
@_dispatchable
def soft_random_geometric_graph(
    n: int | Iterable[Incomplete],
    radius: float,
    dim: int = 2,
    pos: Mapping[Incomplete, Incomplete] | None = None,
    p: float = 2,
    p_dist=None,
    seed=None,
): ...
@_dispatchable
def geographical_threshold_graph(
    n: int | Iterable[Incomplete],
    theta,
    dim: int = 2,
    pos: Mapping[Incomplete, Incomplete] | None = None,
    weight: Mapping[Incomplete, Incomplete] | None = None,
    metric=None,
    p_dist=None,
    seed=None,
): ...
@_dispatchable
def waxman_graph(
    n: int | Iterable[Incomplete],
    beta: float = 0.4,
    alpha: float = 0.1,
    L: float | None = None,
    domain=(0, 0, 1, 1),
    metric=None,
    seed=None,
) -> Graph[Incomplete]: ...

# docstring marks p as int, but it still works with floats. So I think it's better for consistency
@_dispatchable
def navigable_small_world_graph(n: int, p: float = 1, q: int = 1, r: float = 2, dim: int = 2, seed=None): ...
@_dispatchable
def thresholded_random_geometric_graph(
    n: int | Iterable[Incomplete],
    radius: float,
    theta: float,
    dim: int = 2,
    pos: Mapping[Incomplete, Incomplete] | None = None,
    weight: Mapping[Incomplete, Incomplete] | None = None,
    p: float = 2,
    seed=None,
): ...
@_dispatchable
def geometric_soft_configuration_graph(
    *, beta, n=None, gamma=None, mean_degree=None, kappas=None, seed=None
) -> Graph[Incomplete]: ...
