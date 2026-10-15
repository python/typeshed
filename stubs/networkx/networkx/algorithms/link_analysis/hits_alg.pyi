from collections.abc import Mapping
from typing import Literal

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["hits"]

@_dispatchable
def hits(
    G: Graph[_Node],
    max_iter: int | None = 100,
    tol: float | None = 1e-08,
    nstart: Mapping[_Node, float] | None = None,
    normalized: bool = True,
    *,
    method: Literal["power_iteration", "svd"] = "power_iteration",
) -> tuple[dict[_Node, float], dict[_Node, float]]: ...
