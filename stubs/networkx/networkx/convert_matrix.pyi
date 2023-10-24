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
    nodelist: list[_Node] | None = None,
    dtype: numpy.dtype[Incomplete] | None = None,
    order: Literal["C", "F"] | None = None,
    multigraph_weight: Callable[[Iterable[float]], float] = ...,
    weight: str = "weight",
    nonedge: float = 0.0,
) -> _DataFrame: ...
def from_pandas_adjacency(df: _DataFrame, create_using: type[Graph[Incomplete]] | None = None) -> Graph[Incomplete]: ...
def to_pandas_edgelist(
    G: Graph[_Node],
    source: str | int = "source",
    target: str | int = "target",
    nodelist: list[_Node] | None = None,
    dtype: _ExtensionDtype | None = None,
    edge_key: str | int | None = None,
) -> _DataFrame: ...
def from_pandas_edgelist(
    df: _DataFrame,
    source: str | int = "source",
    target: str | int = "target",
    edge_attr: str | int | Iterable[str | int] | Literal[True] | None = None,
    create_using: type[Graph[Incomplete]] | None = None,
) -> Graph[Incomplete]: ...
def to_numpy_array(
    G: Graph[_Node],
    nodelist: list[_Node] | None = None,
    dtype: numpy.dtype[Incomplete] | None = None,
    order: Literal["C", "F"] | None = None,
    multigraph_weight: Callable[[Iterable[float]], float] = ...,
    weight: str = "weight",
    nonedge: float = 0.0,
) -> numpy.ndarray[Incomplete, numpy.dtype[Incomplete]]: ...
def from_numpy_array(
    A: numpy.ndarray[Incomplete, Incomplete], parallel_edges: bool = False, create_using: type[Graph[Incomplete]] | None = None
) -> Graph[Incomplete]: ...
