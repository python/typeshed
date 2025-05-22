from networkx.utils.backends import _dispatchable

from ..classes.graph import Graph, _Node

__all__ = [
    "laplacian_spectrum",
    "adjacency_spectrum",
    "modularity_spectrum",
    "normalized_laplacian_spectrum",
    "bethe_hessian_spectrum",
]

@_dispatchable
def laplacian_spectrum(G: Graph[_Node], weight: str = "weight"): ...
@_dispatchable
def normalized_laplacian_spectrum(G: Graph[_Node], weight: str = "weight"): ...
@_dispatchable
def adjacency_spectrum(G: Graph[_Node], weight: str = "weight"): ...
@_dispatchable
def modularity_spectrum(G: Graph[_Node]): ...
@_dispatchable
def bethe_hessian_spectrum(G: Graph[_Node], r: float | None = None): ...
