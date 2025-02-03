from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def non_randomness(G: Graph[_Node], k: int = None, weight: str | None = "weight"): ...
