from _typeshed import Incomplete
from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def degree_assortativity_coefficient(
    G: Graph[_Node], x: str = "out", y: str = "in", weight: str | None = None, nodes: Iterable[Incomplete] | None = None
): ...
@_dispatchable
def degree_pearson_correlation_coefficient(
    G: Graph[_Node], x: str = "out", y: str = "in", weight: str | None = None, nodes: Iterable[Incomplete] | None = None
): ...
@_dispatchable
def attribute_assortativity_coefficient(G: Graph[_Node], attribute: str, nodes: Iterable[Incomplete] | None = None): ...
@_dispatchable
def numeric_assortativity_coefficient(G: Graph[_Node], attribute: str, nodes: Iterable[Incomplete] | None = None): ...
