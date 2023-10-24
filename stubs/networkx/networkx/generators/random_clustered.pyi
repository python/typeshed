from typing import Any, TypeVar, overload

from networkx import MultiGraph

_G = TypeVar("_G", bound=MultiGraph[int])

@overload
def random_clustered_graph(
    joint_degree_sequence: list[tuple[int, int]], create_using: None = None, seed: int | tuple[Any, ...] | None = None
) -> MultiGraph[int]: ...
@overload
def random_clustered_graph(
    joint_degree_sequence: list[tuple[int, int]], create_using: type[_G], seed: int | tuple[Any, ...] | None = None
) -> _G: ...
