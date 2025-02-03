from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def attribute_mixing_dict(G: Graph[_Node], attribute: str, nodes: Iterable = None, normalized: bool = False): ...
@_dispatchable
def attribute_mixing_matrix(
    G: Graph[_Node], attribute: str, nodes: Iterable = None, mapping: dict | None = None, normalized: bool = True
): ...
@_dispatchable
def degree_mixing_dict(
    G: Graph[_Node], x: str = "out", y: str = "in", weight: str | None = None, nodes=None, normalized: bool = False
): ...
@_dispatchable
def degree_mixing_matrix(
    G: Graph[_Node],
    x: str = "out",
    y: str = "in",
    weight: str | None = None,
    nodes: Iterable = None,
    normalized: bool = True,
    mapping: dict | None = None,
): ...
@_dispatchable
def mixing_dict(xy, normalized: bool = False): ...
