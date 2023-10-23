from _typeshed import Incomplete
from collections.abc import Callable, Hashable
from io import TextIOBase
from typing import TypeVar
from typing_extensions import TypeAlias

from networkx.classes.graph import Graph

# from pygraphviz.agraph import AGraph as _AGraph

_AGraph: TypeAlias = Incomplete
_T = TypeVar("_T")

def from_agraph(A, create_using: Incomplete | None = ...) -> Graph[Incomplete]: ...
def to_agraph(N: Graph[Hashable]) -> _AGraph: ...
def write_dot(G: Graph[Hashable], path: str | TextIOBase) -> None: ...
def read_dot(path: str | TextIOBase) -> Graph[Incomplete]: ...
def graphviz_layout(G: Graph[_T], prog: str = ..., root: str | None = ..., args: str = ...) -> dict[_T, tuple[float, float]]: ...

pygraphviz_layout = graphviz_layout

def view_pygraphviz(
    G: Graph[_T],
    edgelabel: str | Callable[[_T], str] | None = ...,
    prog: str = ...,
    args: str = ...,
    suffix: str = ...,
    path: str | None = ...,
): ...
