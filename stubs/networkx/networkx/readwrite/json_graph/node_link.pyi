from _typeshed import Incomplete
from collections.abc import Mapping

from networkx.utils.backends import _dispatchable

from ...classes.graph import Graph

__all__ = ["node_link_data", "node_link_graph"]

def node_link_data(
    G: Graph[Incomplete],
    *,
    source: str = "source",
    target: str = "target",
    name: str = "id",
    key: str = "key",
    edges: str | None = None,
    nodes: str = "nodes",
    link: str | None = None,
): ...
@_dispatchable
def node_link_graph(
    data: Mapping[str, Incomplete],
    directed: bool = False,
    multigraph: bool = True,
    *,
    source: str = "source",
    target: str = "target",
    name: str = "id",
    key: str = "key",
    edges: str | None = None,
    nodes: str = "nodes",
    link: str | None = None,
): ...
