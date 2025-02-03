from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def dedensify(G: Graph[_Node], threshold: int, prefix=None, copy: bool | None = True): ...
@_dispatchable
def snap_aggregation(
    G: Graph[_Node],
    node_attributes,
    edge_attributes: Iterable | None = (),
    prefix: str = "Supernode-",
    supernode_attribute: str = "group",
    superedge_attribute: str = "types",
): ...
