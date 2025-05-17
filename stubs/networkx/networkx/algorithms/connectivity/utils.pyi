from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

from ...classes.graph import Graph

__all__ = ["build_auxiliary_node_connectivity", "build_auxiliary_edge_connectivity"]

@_dispatchable
def build_auxiliary_node_connectivity(G: Graph[Incomplete]): ...
@_dispatchable
def build_auxiliary_edge_connectivity(G: Graph[Incomplete]): ...
