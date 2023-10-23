from _typeshed import Incomplete
from collections.abc import Callable, Iterable
from typing_extensions import Literal, TypeAlias

import numpy
from networkx.classes.graph import Graph, _Node

# stub_uploader won't allow pandas-stubs in the requires field https://github.com/typeshed-internal/stub_uploader/issues/90
# from pandas import DataFrame
_DataFrame: TypeAlias = Incomplete
# from pandas.core.dtypes.base import ExtensionDtype
_ExtensionDtype: TypeAlias = Incomplete

def to_pandas_adjacency(
    G: Graph[_Node],
    nodelist: list[_Node] | None = ...,
    dtype: numpy.dtype[Incomplete] | None = ...,
    order: Literal["C", "F"] | None = ...,
    multigraph_weight: Callable[[Iterable[float]], float] = ...,
    weight: str = ...,
    nonedge: float = ...,
) -> _DataFrame: ...
def from_pandas_adjacency(df: _DataFrame, create_using: type[Graph[Incomplete]] = ...) -> Graph[Incomplete]: ...
def to_pandas_edgelist(
    G: Graph[_Node],
    source: str | int = ...,
    target: str | int = ...,
    nodelist: list[_Node] | None = ...,
    dtype: _ExtensionDtype | None = ...,
    edge_key: str | int | None = ...,
) -> _DataFrame: ...
def from_pandas_edgelist(
    df: _DataFrame,
    source: str | int = ...,
    target: str | int = ...,
    edge_attr: str | int | Iterable[str | int] | Literal[True] | None = ...,
    create_using: type[Graph[Incomplete]] = ...,
) -> Graph[Incomplete]: ...
def to_numpy_array(
    G: Graph[_Node],
    nodelist: list[_Node] | None = ...,
    dtype: numpy.dtype[Incomplete] | None = ...,
    order: Literal["C", "F"] | None = ...,
    multigraph_weight: Callable[[Iterable[float]], float] = ...,
    weight: str = ...,
    nonedge: float = ...,
) -> numpy.ndarray[Incomplete, numpy.dtype[Incomplete]]: ...
def from_numpy_array(
    A: numpy.ndarray[Incomplete, Incomplete], parallel_edges: bool = ..., create_using: type[Graph[Incomplete]] = ...
) -> Graph[Incomplete]: ...
