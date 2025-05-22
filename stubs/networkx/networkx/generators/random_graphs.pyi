from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

from ..classes.graph import Graph, _Node

__all__ = [
    "fast_gnp_random_graph",
    "gnp_random_graph",
    "dense_gnm_random_graph",
    "gnm_random_graph",
    "erdos_renyi_graph",
    "binomial_graph",
    "newman_watts_strogatz_graph",
    "watts_strogatz_graph",
    "connected_watts_strogatz_graph",
    "random_regular_graph",
    "barabasi_albert_graph",
    "dual_barabasi_albert_graph",
    "extended_barabasi_albert_graph",
    "powerlaw_cluster_graph",
    "random_lobster",
    "random_shell_graph",
    "random_powerlaw_tree",
    "random_powerlaw_tree_sequence",
    "random_kernel_graph",
]

@_dispatchable
def fast_gnp_random_graph(n: int, p: float, seed=None, directed: bool = False): ...
@_dispatchable
def gnp_random_graph(n: int, p: float, seed=None, directed: bool = False): ...

binomial_graph = gnp_random_graph
erdos_renyi_graph = gnp_random_graph

@_dispatchable
def dense_gnm_random_graph(n: int, m: int, seed=None): ...
@_dispatchable
def gnm_random_graph(n: int, m: int, seed=None, directed: bool = False): ...
@_dispatchable
def newman_watts_strogatz_graph(n: int, k: int, p: float, seed=None): ...
@_dispatchable
def watts_strogatz_graph(n: int, k: int, p: float, seed=None): ...
@_dispatchable
def connected_watts_strogatz_graph(n: int, k: int, p: float, tries: int = 100, seed=None): ...
@_dispatchable
def random_regular_graph(d, n: int, seed=None): ...
@_dispatchable
def barabasi_albert_graph(n: int, m: int, seed=None, initial_graph: Graph[_Node] | None = None) -> Graph[_Node]: ...
@_dispatchable
def dual_barabasi_albert_graph(
    n: int, m1, m2, p: float, seed=None, initial_graph: Graph[_Node] | None = None
) -> Graph[_Node]: ...
@_dispatchable
def extended_barabasi_albert_graph(n: int, m: int, p: float, q, seed=None) -> Graph[Incomplete]: ...
@_dispatchable
def powerlaw_cluster_graph(n: int, m: int, p: float, seed=None): ...
@_dispatchable
def random_lobster(n: int, p1: float, p2: float, seed=None): ...
@_dispatchable
def random_shell_graph(constructor, seed=None): ...
@_dispatchable
def random_powerlaw_tree(n: int, gamma: float = 3, seed=None, tries: int = 100): ...
@_dispatchable
def random_powerlaw_tree_sequence(n: int, gamma: float = 3, seed=None, tries: int = 100): ...
@_dispatchable
def random_kernel_graph(n: int, kernel_integral, kernel_root=None, seed=None): ...
