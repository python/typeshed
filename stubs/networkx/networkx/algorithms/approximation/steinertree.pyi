from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def metric_closure(G: Graph[_Node], weight="weight"): ...
@_dispatchable
def steiner_tree(G: Graph[_Node], terminal_nodes: list, weight: str = "weight", method: str | None = None): ...
