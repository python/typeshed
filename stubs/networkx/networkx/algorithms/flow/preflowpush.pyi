from _typeshed import Incomplete

from networkx.algorithms.flow.utils import _CapacityFunc
from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["preflow_push"]

@_dispatchable
def preflow_push(
    G: Graph[_Node],
    s: _Node,
    t: _Node,
    capacity: str | _CapacityFunc[_Node] = "capacity",
    residual: Graph[_Node] | None = None,
    global_relabel_freq: float = 1,
    value_only: bool = False,
) -> DiGraph[Incomplete]: ...
