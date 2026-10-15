from _typeshed import Incomplete
from collections.abc import Generator
from random import Random

from networkx._typing import Seed
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["random_walk", "number_of_walks"]

@_dispatchable
def number_of_walks(G: Graph[_Node], walk_length: int) -> dict[Incomplete, Incomplete]: ...
@_dispatchable
def random_walk(
    G: Graph[_Node], *, start: _Node, weight: str | None = None, seed: Seed | Random | None = None
) -> Generator[_Node]: ...
