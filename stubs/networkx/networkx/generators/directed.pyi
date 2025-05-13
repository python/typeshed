from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

from ..classes import MultiDiGraph

__all__ = ["gn_graph", "gnc_graph", "gnr_graph", "random_k_out_graph", "scale_free_graph"]

@_dispatchable
def gn_graph(
    n: int, kernel: Incomplete | None = None, create_using: Incomplete | None = None, seed: Incomplete | None = None
): ...
@_dispatchable
def gnr_graph(n: int, p: float, create_using: Incomplete | None = None, seed: Incomplete | None = None): ...
@_dispatchable
def gnc_graph(n: int, create_using: Incomplete | None = None, seed: Incomplete | None = None): ...
@_dispatchable
def scale_free_graph(
    n,
    alpha: float = 0.41,
    beta: float = 0.54,
    gamma: float = 0.05,
    delta_in: float = 0.2,
    delta_out: float = 0,
    create_using: Incomplete | None = None,
    seed: Incomplete | None = None,
    initial_graph: Incomplete | None = None,
): ...
@_dispatchable
def random_uniform_k_out_graph(n: int, k: int, self_loops: bool = True, with_replacement: bool = True, seed=None): ...
@_dispatchable
def random_k_out_graph(n: int, k: int, alpha: float, self_loops: bool = True, seed: Incomplete | None = None) -> MultiDiGraph: ...
