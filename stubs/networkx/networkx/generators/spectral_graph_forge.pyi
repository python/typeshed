from networkx.utils.backends import _dispatchable

from ..classes.graph import Graph, _Node

__all__ = ["spectral_graph_forge"]

@_dispatchable
def spectral_graph_forge(G: Graph[_Node], alpha: float, transformation: str = "identity", seed=None) -> Graph[_Node]: ...
