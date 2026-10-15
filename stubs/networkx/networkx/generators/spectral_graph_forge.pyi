from _typeshed import Incomplete

from networkx.classes.graph import Graph, _EdgeData, _Node, _NodeData
from networkx.utils.backends import _dispatchable

__all__ = ["spectral_graph_forge"]

@_dispatchable
def spectral_graph_forge(
    G: Graph[_Node, _NodeData, _EdgeData], alpha: float, transformation: str = "identity", seed=None
) -> Graph[Incomplete]: ...
