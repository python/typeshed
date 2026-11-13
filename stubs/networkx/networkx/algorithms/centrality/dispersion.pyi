from _typeshed import FloatInt
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["dispersion"]

@_dispatchable
def dispersion(
    G: Graph[_Node],
    u: _Node | None = None,
    v: _Node | None = None,
    normalized: bool = True,
    alpha: FloatInt = 1.0,
    b: FloatInt = 0.0,
    c: FloatInt = 0.0,
) -> dict[_Node, float] | dict[_Node, dict[_Node, float]]: ...
