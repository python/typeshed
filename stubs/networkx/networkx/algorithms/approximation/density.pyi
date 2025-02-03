from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def densest_subgraph(G: Graph[_Node], iterations: int | None = 1, *, method: str | None = "greedy++"): ...
