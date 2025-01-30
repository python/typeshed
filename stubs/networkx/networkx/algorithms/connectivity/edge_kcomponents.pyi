from _typeshed import Incomplete
from collections.abc import Generator

from networkx.utils.backends import _dispatchable

@_dispatchable
def k_edge_components(G, k): ...
@_dispatchable
def k_edge_subgraphs(G, k): ...
@_dispatchable
def bridge_components(G) -> Generator[Incomplete, Incomplete, None]: ...

class EdgeComponentAuxGraph:
    A: Incomplete
    H: Incomplete

    @classmethod
    def construct(cls, G): ...
    def k_edge_components(self, k) -> Generator[Incomplete, Incomplete, None]: ...
    def k_edge_subgraphs(self, k) -> Generator[Incomplete, Incomplete, None]: ...
