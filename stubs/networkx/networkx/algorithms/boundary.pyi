from collections.abc import Iterable
from typing import TypeVar, overload
from _typeshed import Incomplete

from networkx.classes.graph import Graph
from typing_extensions import Literal

_T = TypeVar("_T")
_U = TypeVar("_U")

@overload
def edge_boundary(
    G: Graph[_T],
    nbunch1: Iterable[_T],
    nbunch2: Iterable[_T] | None = ...,
    data: Literal[False] = ...,
    keys: Literal[False] = ...,
    default: Incomplete = ...,
) -> Iterable[tuple[_T, _T]]: ...
@overload
def edge_boundary(
    G: Graph[_T],
    nbunch1: Iterable[_T],
    nbunch2: Iterable[_T] | None = ...,
    data: Literal[True] = ...,
    keys: Literal[False] = ...,
    default: Incomplete = ...,
) -> Iterable[tuple[_T, _T, dict[str, Incomplete]]]: ...
@overload
def edge_boundary(
    G: Graph[_T],
    nbunch1: Iterable[_T],
    nbunch2: Iterable[_T] | None = ...,
    data: str = ...,
    keys: Literal[False] = ...,
    default: _U | None = None,
) -> Iterable[tuple[_T, _T, dict[str, _U]]]: ...
@overload
def edge_boundary(
    G: Graph[_T],
    nbunch1: Iterable[_T],
    nbunch2: Iterable[_T] | None = ...,
    data: Literal[False] = ...,
    keys: Literal[True] = ...,
    default: Incomplete = ...,
) -> Iterable[tuple[_T, _T, int]]: ...
@overload
def edge_boundary(
    G: Graph[_T],
    nbunch1: Iterable[_T],
    nbunch2: Iterable[_T] | None = ...,
    data: Literal[True] = ...,
    keys: Literal[True] = ...,
    default: Incomplete = ...,
) -> Iterable[tuple[_T, _T, int, dict[str, Incomplete]]]: ...
@overload
def edge_boundary(
    G: Graph[_T],
    nbunch1: Iterable[_T],
    nbunch2: Iterable[_T] | None = ...,
    data: str = ...,
    keys: Literal[True] = ...,
    default: _U | None = None,
) -> Iterable[tuple[_T, _T, int, dict[str, _U]]]: ...
def node_boundary(
    G: Graph[_T], nbunch1: Iterable[_T], nbunch2: Iterable[_T] | None = ...
) -> Iterable[_T]: ...
