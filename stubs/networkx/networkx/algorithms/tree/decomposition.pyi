from networkx import Graph
from networkx.utils.backends import _dispatchable

__all__ = ["junction_tree"]

@_dispatchable
def junction_tree(G: Graph) -> Graph: ...
