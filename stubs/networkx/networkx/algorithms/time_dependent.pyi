from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def cd_index(G: Graph[_Node], node: _Node, time_delta, *, time: str = "time", weight: str = None): ...
