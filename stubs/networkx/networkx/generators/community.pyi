from collections.abc import Sequence
from typing import Literal, overload

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _Node
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
def caveman_graph(l: int, k: int) -> Graph[int]: ...
@_dispatchable
def connected_caveman_graph(l: int, k: int) -> Graph[int]: ...
@_dispatchable
def relaxed_caveman_graph(l: int, k: int, p: float, seed=None) -> Graph[int]: ...

# @_dispatchable adds the backend arguments, but we can't use this decorator with @overload
@overload
def random_partition_graph(
    sizes: Sequence[int], p_in: float, p_out: float, seed=None, *, directed: Literal[True], backend=None, **backend_kwargs
) -> DiGraph[int]: ...
@overload
def random_partition_graph(
    sizes: Sequence[int], p_in: float, p_out: float, seed, directed: Literal[True], *, backend=None, **backend_kwargs
) -> DiGraph[int]: ...
@overload
def random_partition_graph(
    sizes: Sequence[int], p_in: float, p_out: float, seed=None, directed: bool = False, *, backend=None, **backend_kwargs
) -> Graph[int]: ...

@overload
def planted_partition_graph(
    l: int, k: int, p_in: float, p_out: float, seed=None, *, directed: Literal[True], backend=None, **backend_kwargs
) -> DiGraph[int]: ...
@overload
def planted_partition_graph(
    l: int, k: int, p_in: float, p_out: float, seed, directed: Literal[True], *, backend=None, **backend_kwargs
) -> DiGraph[int]: ...
@overload
def planted_partition_graph(
    l: int, k: int, p_in: float, p_out: float, seed=None, directed: bool = False, *, backend=None, **backend_kwargs
) -> Graph[int]: ...

@overload
def gaussian_random_partition_graph(
    n: int, s: float, v: float, p_in: float, p_out: float, directed: Literal[True], seed=None, *, backend=None, **backend_kwargs
) -> DiGraph[int]: ...
@overload
def gaussian_random_partition_graph(
    n: int, s: float, v: float, p_in: float, p_out: float, directed: bool = False, seed=None, *, backend=None, **backend_kwargs
) -> Graph[int]: ...

@_dispatchable
def ring_of_cliques(num_cliques: int, clique_size: int) -> Graph[int]: ...
@_dispatchable
def windmill_graph(n: int, k: int) -> Graph[int]: ...

@overload
def stochastic_block_model(
    sizes: Sequence[int],
    p: Sequence[Sequence[float]],
    nodelist: None = None,
    seed=None,
    *,
    directed: Literal[True],
    selfloops: bool = False,
    sparse: bool = True,
    backend=None,
    **backend_kwargs,
) -> DiGraph[int]: ...
@overload
def stochastic_block_model(
    sizes: Sequence[int],
    p: Sequence[Sequence[float]],
    nodelist: None,
    seed,
    directed: Literal[True],
    selfloops: bool = False,
    sparse: bool = True,
    *,
    backend=None,
    **backend_kwargs,
) -> DiGraph[int]: ...
@overload
def stochastic_block_model(
    sizes: Sequence[int],
    p: Sequence[Sequence[float]],
    nodelist: Sequence[_Node],
    seed=None,
    *,
    directed: Literal[True],
    selfloops: bool = False,
    sparse: bool = True,
    backend=None,
    **backend_kwargs,
) -> DiGraph[_Node]: ...
@overload
def stochastic_block_model(
    sizes: Sequence[int],
    p: Sequence[Sequence[float]],
    nodelist: Sequence[_Node],
    seed,
    directed: Literal[True],
    selfloops: bool = False,
    sparse: bool = True,
    *,
    backend=None,
    **backend_kwargs,
) -> DiGraph[_Node]: ...
@overload
def stochastic_block_model(
    sizes: Sequence[int],
    p: Sequence[Sequence[float]],
    nodelist: None = None,
    seed=None,
    directed: bool = False,
    selfloops: bool = False,
    sparse: bool = True,
    *,
    backend=None,
    **backend_kwargs,
) -> Graph[int]: ...
@overload
def stochastic_block_model(
    sizes: Sequence[int],
    p: Sequence[Sequence[float]],
    nodelist: Sequence[_Node],
    seed=None,
    directed: bool = False,
    selfloops: bool = False,
    sparse: bool = True,
    *,
    backend=None,
    **backend_kwargs,
) -> Graph[_Node]: ...

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
    tol: float = 1e-07,
    max_iters: int = 500,
    seed=None,
) -> Graph[int]: ...
