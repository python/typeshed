from collections.abc import Generator
from random import Random
from typing import Literal

from networkx._typing import Seed
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["leiden_communities", "leiden_partitions"]

@_dispatchable
def leiden_communities(
    G: Graph[_Node],
    *,
    weight: str | None = "weight",
    resolution: float = 1.0,
    max_level: int | None = None,
    seed: Seed | Random | None = None,
    metric: Literal["cpm", "modularity"] = "cpm",
    theta: float = 0.01,
) -> list[set[_Node]]: ...
@_dispatchable
def leiden_partitions(
    G: Graph[_Node],
    *,
    weight: str | None = "weight",
    metric: Literal["cpm", "modularity"] = "cpm",
    resolution: float = 1.0,
    seed: Seed | Random | None = None,
    theta: float = 0.01,
) -> Generator[list[set[_Node]]]: ...
