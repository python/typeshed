from networkx.utils.backends import _dispatchable

from ..classes.graph import Graph, _Node

__all__ = ["stochastic_graph"]

@_dispatchable
def stochastic_graph(G: Graph[_Node], copy: bool = True, weight: str = "weight"): ...
