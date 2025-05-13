from networkx.utils.backends import _dispatchable

from ..classes.digraph import DiGraph

__all__ = ["flow_hierarchy"]

@_dispatchable
def flow_hierarchy(G: DiGraph, weight: str | None = None) -> float: ...
