from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def closeness_vitality(
    G: Graph[_Node], node: object | None = None, weight: str | None = None, wiener_index: float | None = None
): ...
