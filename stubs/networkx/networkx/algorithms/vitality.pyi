from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def closeness_vitality(G: Graph[_Node], node: object = None, weight: str = None, wiener_index: float = None): ...
