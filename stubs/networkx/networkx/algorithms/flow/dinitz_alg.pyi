from _typeshed import FloatInt
from _typeshed import Incomplete

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["dinitz"]

@_dispatchable
def dinitz(
    G: Graph[_Node],
    s: _Node,
    t: _Node,
    capacity: str = "capacity",
    residual: Graph[_Node] | None = None,
    value_only: bool = False,
    cutoff: FloatInt | None = None,
) -> DiGraph[Incomplete]: ...
