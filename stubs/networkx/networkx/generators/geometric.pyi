from _typeshed import Incomplete

def geometric_edges(G, radius, p: int = 2): ...
def random_geometric_graph(
    n, radius, dim: int = 2, pos: Incomplete | None = None, p: int = 2, seed: Incomplete | None = None
): ...
def soft_random_geometric_graph(
    n,
    radius,
    dim: int = 2,
    pos: Incomplete | None = None,
    p: int = 2,
    p_dist: Incomplete | None = None,
    seed: Incomplete | None = None,
): ...
def geographical_threshold_graph(
    n,
    theta,
    dim: int = 2,
    pos: Incomplete | None = None,
    weight: Incomplete | None = None,
    metric: Incomplete | None = None,
    p_dist: Incomplete | None = None,
    seed: Incomplete | None = None,
): ...
def waxman_graph(
    n,
    beta: float = 0.4,
    alpha: float = 0.1,
    L: Incomplete | None = None,
    domain=(0, 0, 1, 1),
    metric: Incomplete | None = None,
    seed: Incomplete | None = None,
): ...
def navigable_small_world_graph(n, p: int = 1, q: int = 1, r: int = 2, dim: int = 2, seed: Incomplete | None = None): ...
def thresholded_random_geometric_graph(
    n,
    radius,
    theta,
    dim: int = 2,
    pos: Incomplete | None = None,
    weight: Incomplete | None = None,
    p: int = 2,
    seed: Incomplete | None = None,
): ...
