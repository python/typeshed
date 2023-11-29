from collections.abc import Generator, Hashable

from networkx.classes.graph import Graph, _Node

def is_k_edge_connected(G: Graph[Hashable], k: int): ...
def is_locally_k_edge_connected(G, s, t, k): ...
def k_edge_augmentation(
    G: Graph[_Node],
    k: int,
    avail: tuple[_Node, _Node] | tuple[_Node, _Node, dict[str, int]] | None = None,
    weight: str | None = None,
    partial: bool = False,
) -> Generator[tuple[_Node, _Node], None, None]: ...
