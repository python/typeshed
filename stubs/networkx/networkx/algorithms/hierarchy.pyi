from networkx.utils.backends import _dispatchable

from ..classes.digraph import DiGraph
from ..classes.graph import _Node
from ..classes.multidigraph import MultiDiGraph

__all__ = ["flow_hierarchy"]

@_dispatchable
def flow_hierarchy(G: DiGraph[_Node] | MultiDiGraph[_Node], weight: str | None = None) -> float: ...
