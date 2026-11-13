from _typeshed import FloatInt
from _typeshed import Incomplete
from collections.abc import Callable

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph
from networkx.utils.backends import _dispatchable

from ..classes import MultiDiGraph

__all__ = ["gn_graph", "gnc_graph", "gnr_graph", "random_k_out_graph", "scale_free_graph"]

@_dispatchable
def gn_graph(
    n: int, kernel: Callable[..., Incomplete] | None = None, create_using: DiGraph[Incomplete] | None = None, seed=None
): ...
@_dispatchable
def gnr_graph(n: int, p: FloatInt, create_using: DiGraph[Incomplete] | type[DiGraph[Incomplete]] | None = None, seed=None): ...
@_dispatchable
def gnc_graph(n: int, create_using: DiGraph[Incomplete] | type[DiGraph[Incomplete]] | None = None, seed=None): ...
@_dispatchable
def scale_free_graph(
    n: int,
    alpha: FloatInt = 0.41,
    beta: FloatInt = 0.54,
    gamma: FloatInt = 0.05,
    delta_in: FloatInt = 0.2,
    delta_out: FloatInt = 0,
    create_using=None,
    seed=None,
    initial_graph: MultiDiGraph[Incomplete] | None = None,
) -> MultiDiGraph[Incomplete]: ...
@_dispatchable
def random_uniform_k_out_graph(
    n: int, k: int, self_loops: bool = True, with_replacement: bool = True, seed=None
) -> Graph[Incomplete]: ...
@_dispatchable
def random_k_out_graph(n: int, k: int, alpha: FloatInt, self_loops: bool = True, seed=None) -> MultiDiGraph[Incomplete]: ...
