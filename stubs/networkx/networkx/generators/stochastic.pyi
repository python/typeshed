from networkx.classes.digraph import DiGraph
from networkx.classes.graph import _EdgeData, _Node, _NodeData
from networkx.utils.backends import _dispatchable

__all__ = ["stochastic_graph"]

@_dispatchable
def stochastic_graph(G: DiGraph[_Node, _NodeData, _EdgeData], copy: bool = True, weight: str = "weight"): ...
