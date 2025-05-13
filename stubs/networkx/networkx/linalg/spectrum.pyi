from networkx.utils.backends import _dispatchable

from ..classes.graph import Graph

__all__ = [
    "laplacian_spectrum",
    "adjacency_spectrum",
    "modularity_spectrum",
    "normalized_laplacian_spectrum",
    "bethe_hessian_spectrum",
]

@_dispatchable
def laplacian_spectrum(G: Graph[Incomplete], weight: str = "weight"): ...
@_dispatchable
def normalized_laplacian_spectrum(G: Graph[Incomplete], weight: str = "weight"): ...
@_dispatchable
def adjacency_spectrum(G: Graph[Incomplete], weight: str = "weight"): ...
@_dispatchable
def modularity_spectrum(G: Graph[Incomplete]): ...
@_dispatchable
def bethe_hessian_spectrum(G: Graph[Incomplete], r: float | None = None): ...
