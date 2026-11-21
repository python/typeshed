from _typeshed import FloatInt
from collections.abc import Collection, Mapping

import numpy as np
from networkx._typing import Array2D
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["pagerank", "google_matrix"]

@_dispatchable
def pagerank(
    G: Graph[_Node],
    alpha: FloatInt | None = 0.85,
    personalization: Mapping[_Node, FloatInt] | None = None,
    max_iter: int | None = 100,
    tol: FloatInt | None = 1e-06,
    nstart: Mapping[_Node, FloatInt] | None = None,
    weight: str | None = "weight",
    dangling: Mapping[_Node, FloatInt] | None = None,
) -> dict[_Node, float]: ...
@_dispatchable
def google_matrix(
    G: Graph[_Node],
    alpha: FloatInt = 0.85,
    personalization: Mapping[_Node, FloatInt] | None = None,
    nodelist: Collection[_Node] | None = None,
    weight: str | None = "weight",
    dangling: Mapping[_Node, FloatInt] | None = None,
) -> Array2D[np.float64]: ...
