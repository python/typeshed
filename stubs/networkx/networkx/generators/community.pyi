from _typeshed import Incomplete
from collections.abc import Collection

from networkx.utils.backends import _dispatchable

__all__ = [
    "caveman_graph",
    "connected_caveman_graph",
    "relaxed_caveman_graph",
    "random_partition_graph",
    "planted_partition_graph",
    "gaussian_random_partition_graph",
    "ring_of_cliques",
    "windmill_graph",
    "stochastic_block_model",
    "LFR_benchmark_graph",
]

@_dispatchable
def caveman_graph(l: int, k: int): ...
@_dispatchable
def connected_caveman_graph(l: int, k: int): ...
@_dispatchable
def relaxed_caveman_graph(l: int, k: int, p: float, seed=None): ...
@_dispatchable
def random_partition_graph(sizes: Collection[int], p_in: float, p_out: float, seed=None, directed=False): ...
@_dispatchable
def planted_partition_graph(l: int, k: int, p_in: float, p_out: float, seed=None, directed=False): ...
@_dispatchable
def gaussian_random_partition_graph(n: int, s: float, v: float, p_in: float, p_out: float, directed=False, seed=None): ...
@_dispatchable
def ring_of_cliques(num_cliques: int, clique_size: int): ...
@_dispatchable
def windmill_graph(n: int, k: int): ...
@_dispatchable
def stochastic_block_model(
    sizes: Collection[int],
    p,
    nodelist: Collection[Incomplete] | None = None,
    seed=None,
    directed: bool = False,
    selfloops: bool = False,
    sparse: bool = True,
): ...
@_dispatchable
def LFR_benchmark_graph(
    n: int,
    tau1: float,
    tau2: float,
    mu: float,
    average_degree: float | None = None,
    min_degree: int | None = None,
    max_degree: int | None = None,
    min_community: int | None = None,
    max_community: int | None = None,
    tol: float = 1.0e-7,
    max_iters: int = 500,
    seed=None,
): ...
