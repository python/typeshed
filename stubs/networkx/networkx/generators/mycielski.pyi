from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

from ..classes.graph import Graph

__all__ = ["mycielskian", "mycielski_graph"]

@_dispatchable
def mycielskian(G: Graph[Incomplete], iterations: int = 1): ...
@_dispatchable
def mycielski_graph(n: int): ...
