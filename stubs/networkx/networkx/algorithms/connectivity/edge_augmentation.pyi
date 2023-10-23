from collections.abc import Hashable, Iterable
from typing import TypeVar

from networkx.classes.graph import Graph

_N = TypeVar("_N")

def is_k_edge_connected(G: Graph[Hashable], k: int): ...
def is_locally_k_edge_connected(G, s, t, k): ...
def k_edge_augmentation(
    G: Graph[_N],
    k: int,
    avail: tuple[_N, _N] | tuple[_N, _N, dict[str, int]] | None = None,
    weight: str | None = None,
    partial: bool = False,
) -> Iterable[tuple[_N, _N]]: ...
