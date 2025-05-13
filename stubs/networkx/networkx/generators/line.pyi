from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

from ..classes.graph import Graph

__all__ = ["line_graph", "inverse_line_graph"]

@_dispatchable
def line_graph(G: Graph[Incomplete], create_using: Incomplete | None = None): ...
@_dispatchable
def inverse_line_graph(G: Graph[Incomplete]): ...
