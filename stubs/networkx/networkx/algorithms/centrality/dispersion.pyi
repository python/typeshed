from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def dispersion(
    G: Graph[_Node], u: _Node | None = None, v: _Node | None = None, normalized: bool = True, alpha=1.0, b=0.0, c=0.0
) -> dict[_Node, float] | dict[_Node, dict[_Node, float]]: ...
