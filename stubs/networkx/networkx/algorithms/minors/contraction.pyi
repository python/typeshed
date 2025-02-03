from collections.abc import Callable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def equivalence_classes(iterable, relation): ...
@_dispatchable
def quotient_graph(
    G: Graph[_Node],
    partition,
    edge_relation=None,
    node_data: Callable = None,
    edge_data: Callable = None,
    weight: str | None = "weight",
    relabel: bool = False,
    create_using: Graph[_Node] | None = None,
): ...
@_dispatchable
def contracted_nodes(G: Graph[_Node], u, v, self_loops: bool = True, copy: bool = True): ...

identified_nodes = contracted_nodes

@_dispatchable
def contracted_edge(G: Graph[_Node], edge: tuple, self_loops: bool = True, copy: bool = True): ...
