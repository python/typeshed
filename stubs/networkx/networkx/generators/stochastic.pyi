from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

from ..classes.graph import Graph

__all__ = ["stochastic_graph"]

@_dispatchable
def stochastic_graph(G: Graph[Incomplete], copy: bool = True, weight: str = "weight"): ...
