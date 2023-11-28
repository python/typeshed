from collections.abc import Iterable
from typing import Any, TypeVar, overload

from networkx import MultiGraph
from networkx.classes.graph import Graph

_G = TypeVar("_G", bound=Graph[int])

@overload
def random_clustered_graph(
    joint_degree_sequence: Iterable[tuple[int, int]], create_using: None = None, seed: int | tuple[Any, ...] | None = None
) -> MultiGraph[int]: ...
@overload
def random_clustered_graph(
    joint_degree_sequence: Iterable[tuple[int, int]], create_using: type[_G], seed: int | tuple[Any, ...] | None = None
) -> _G: ...
