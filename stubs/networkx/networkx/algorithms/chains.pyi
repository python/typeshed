from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node

def chain_decomposition(G: Graph[_Node], root: _Node | None = None) -> Iterable[tuple[_Node, _Node]]: ...
