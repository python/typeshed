from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

from ..classes.digraph import DiGraph
from ..classes.multidigraph import MultiDiGraph

__all__ = ["flow_hierarchy"]

@_dispatchable
def flow_hierarchy(G: DiGraph[Incomplete] | MultiDiGraph[Incomplete], weight: str | None = None) -> float: ...
