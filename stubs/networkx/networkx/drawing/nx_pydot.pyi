from os import PathLike
from typing import IO, Any
from typing_extensions import TypeAlias

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable
from pydot import Dot  # type: ignore[import-not-found]  # pyright: ignore[reportMissingImports]

__all__ = ["write_dot", "read_dot", "graphviz_layout", "pydot_layout", "to_pydot", "from_pydot"]

_File: TypeAlias = str | PathLike[Any] | IO[str]

def write_dot(G: Graph[_Node], path: _File) -> None: ...
@_dispatchable
def read_dot(path: _File) -> Graph[str]: ...
@_dispatchable
def from_pydot(P: Dot): ...
def to_pydot(N: Graph[_Node]) -> Dot: ...
def graphviz_layout(G: Graph[_Node], prog: str = "neato", root: _Node | None = None): ...
def pydot_layout(G: Graph[_Node], prog: str = "neato", root: _Node | None = None): ...
