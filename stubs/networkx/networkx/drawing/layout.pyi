from _typeshed import FloatInt
from collections.abc import Collection, Mapping
from typing import Any, Literal, TypeAlias

import numpy as np
from networkx._typing import Array1D, Array2D, ArrayLike1D, Seed
from networkx.classes.graph import Graph, _EdgeData, _Node, _NodeData
from networkx.utils.backends import _dispatchable
from numpy.typing import NDArray

__all__ = [
    "bipartite_layout",
    "circular_layout",
    "forceatlas2_layout",
    "kamada_kawai_layout",
    "random_layout",
    "rescale_layout",
    "rescale_layout_dict",
    "shell_layout",
    "spring_layout",
    "spectral_layout",
    "planar_layout",
    "fruchterman_reingold_layout",
    "spiral_layout",
    "multipartite_layout",
    "bfs_layout",
    "arf_layout",
]

_FloatArrayLike1D: TypeAlias = ArrayLike1D[FloatInt, np.number[Any]]  # Any because we don't care about the bit base

def random_layout(
    G: Graph[_Node, _NodeData, _EdgeData],
    center: _FloatArrayLike1D | None = None,
    dim: int = 2,
    seed: Seed | None = None,
    store_pos_as: str | None = None,
) -> dict[_Node, Array1D[np.float32]]: ...
def circular_layout(
    G: Graph[_Node, _NodeData, _EdgeData],
    scale: FloatInt = 1,
    center: _FloatArrayLike1D | None = None,
    dim: int = 2,
    store_pos_as: str | None = None,
) -> dict[_Node, Array1D[np.float64]]: ...
def shell_layout(
    G: Graph[_Node, _NodeData, _EdgeData],
    nlist: Collection[Collection[_Node]] | None = None,
    rotate: FloatInt | None = None,
    scale: FloatInt = 1,
    center: _FloatArrayLike1D | None = None,
    dim: int = 2,
    store_pos_as: str | None = None,
) -> dict[_Node, Array1D[np.float64]]: ...
def bipartite_layout(
    G: Graph[_Node, _NodeData, _EdgeData],
    nodes: Collection[_Node] | None = None,
    align: Literal["vertical", "horizontal"] = "vertical",
    scale: FloatInt = 1,
    center: _FloatArrayLike1D | None = None,
    aspect_ratio: FloatInt = ...,
    store_pos_as: str | None = None,
) -> dict[_Node, Array1D[np.float64]]: ...
def spring_layout(
    G: Graph[_Node, _NodeData, _EdgeData],
    k: FloatInt | None = None,
    pos: Mapping[_Node, Collection[FloatInt]] | None = None,
    fixed: Collection[_Node] | None = None,
    iterations: int = 50,
    threshold: FloatInt = 0.0001,
    weight: str | None = "weight",
    scale: FloatInt | None = 1,
    center: _FloatArrayLike1D | None = None,
    dim: int = 2,
    seed: Seed | None = None,
    store_pos_as: str | None = None,
    *,
    method: Literal["auto", "force", "energy"] = "auto",
    gravity: FloatInt = 1.0,
) -> dict[_Node, Array1D[np.float64]]: ...

fruchterman_reingold_layout = spring_layout

def kamada_kawai_layout(
    G: Graph[_Node, _NodeData, _EdgeData],
    dist: Mapping[_Node, Mapping[_Node, FloatInt]] | None = None,
    pos: Mapping[_Node, Collection[FloatInt]] | None = None,
    weight: str | None = "weight",
    scale: FloatInt = 1,
    center: _FloatArrayLike1D | None = None,
    dim: int = 2,
    store_pos_as: str | None = None,
) -> dict[_Node, Array1D[np.float64]]: ...
def spectral_layout(
    G: Graph[_Node, _NodeData, _EdgeData],
    weight: str | None = "weight",
    scale: FloatInt = 1,
    center: _FloatArrayLike1D | None = None,
    dim: int = 2,
    store_pos_as: str | None = None,
) -> dict[_Node, Array1D[np.float64]]: ...
def planar_layout(
    G: Graph[_Node, _NodeData, _EdgeData],
    scale: FloatInt = 1,
    center: _FloatArrayLike1D | None = None,
    dim: int = 2,
    store_pos_as: str | None = None,
) -> dict[_Node, Array1D[np.float64]]: ...
def spiral_layout(
    G: Graph[_Node, _NodeData, _EdgeData],
    scale: FloatInt = 1,
    center: _FloatArrayLike1D | None = None,
    dim: int = 2,
    resolution: FloatInt = 0.35,
    equidistant: bool = False,
    store_pos_as: str | None = None,
) -> dict[_Node, Array1D[np.float64]]: ...
def multipartite_layout(
    G: Graph[_Node, _NodeData, _EdgeData],
    subset_key: str | Mapping[Any, Collection[_Node]] = "subset",  # layers can be "any" hashable
    align: Literal["vertical", "horizontal"] = "vertical",
    scale: FloatInt = 1,
    center: _FloatArrayLike1D | None = None,
    store_pos_as: str | None = None,
) -> dict[_Node, Array1D[np.float64]]: ...
def arf_layout(
    G: Graph[_Node, _NodeData, _EdgeData],
    pos: Mapping[_Node, Collection[FloatInt]] | None = None,
    scaling: FloatInt = 1,
    a: FloatInt = 1.1,
    etol: FloatInt = 1e-06,
    dt: FloatInt = 0.001,
    max_iter: int = 1000,
    *,
    seed: Seed | None = None,
    store_pos_as: str | None = None,
) -> dict[_Node, Array1D[np.float32]]: ...
@_dispatchable
def forceatlas2_layout(
    G: Graph[_Node, _NodeData, _EdgeData],
    pos: Mapping[_Node, Collection[FloatInt]] | None = None,
    *,
    max_iter: int = 100,
    jitter_tolerance: FloatInt = 1.0,
    scaling_ratio: FloatInt = 2.0,
    gravity: FloatInt = 1.0,
    distributed_action: bool = False,
    strong_gravity: bool = False,
    node_mass: Mapping[_Node, FloatInt] | None = None,
    node_size: Mapping[_Node, FloatInt] | None = None,
    weight: str | None = None,
    linlog: bool = False,
    seed: Seed | None = None,
    dim: int = 2,
    store_pos_as: str | None = None,
) -> dict[_Node, Array1D[np.float32]]: ...
def rescale_layout(pos: NDArray[np.number[Any]], scale: FloatInt = 1) -> Array2D[np.float64]: ...  # ignore the bit base
def rescale_layout_dict(pos: Mapping[_Node, Collection[FloatInt]], scale: FloatInt = 1) -> dict[_Node, Array1D[np.float64]]: ...
def bfs_layout(
    G: Graph[_Node, _NodeData, _EdgeData],
    start: _Node,
    *,
    align: Literal["vertical", "horizontal"] = "vertical",
    scale: FloatInt = 1,
    center: _FloatArrayLike1D | None = None,
    store_pos_as: str | None = None,
) -> dict[_Node, Array1D[np.float64]]: ...
