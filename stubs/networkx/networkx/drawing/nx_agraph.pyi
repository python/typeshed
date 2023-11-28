from _typeshed import Incomplete
from collections.abc import Callable, Hashable
from io import TextIOBase
from typing_extensions import TypeAlias

from networkx.classes.graph import Graph, _Node

# from pygraphviz.agraph import AGraph as _AGraph
_AGraph: TypeAlias = Incomplete

def from_agraph(A, create_using: Incomplete | None = None) -> Graph[Incomplete]: ...
def to_agraph(N: Graph[Hashable]) -> _AGraph: ...
def write_dot(G: Graph[Hashable], path: str | TextIOBase) -> None: ...
def read_dot(path: str | TextIOBase) -> Graph[Incomplete]: ...
def graphviz_layout(
    G: Graph[_Node], prog: str = "neato", root: str | None = None, args: str = ""
) -> dict[_Node, tuple[float, float]]: ...

pygraphviz_layout = graphviz_layout

def view_pygraphviz(
    G: Graph[_Node],
    edgelabel: str | Callable[[_Node], str] | None = None,
    prog: str = "dot",
    args: str = "",
    suffix: str = "",
    path: str | None = None,
    show: bool = True,
): ...
