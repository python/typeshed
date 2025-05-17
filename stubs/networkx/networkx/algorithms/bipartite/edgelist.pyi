from _typeshed import Incomplete
from collections.abc import Generator, Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["generate_edgelist", "write_edgelist", "parse_edgelist", "read_edgelist"]

@_dispatchable
def write_edgelist(
    G: Graph[Incomplete],
    path,
    comments: str = "#",
    delimiter: str = " ",
    data: bool | Iterable[Incomplete] = True,
    encoding: str = "utf-8",
) -> None: ...
@_dispatchable
def generate_edgelist(
    G: Graph[Incomplete], delimiter: str = " ", data: bool | Iterable[Incomplete] = True
) -> Generator[str, None, None]: ...
@_dispatchable
def parse_edgelist(
    lines,
    comments: str | None = "#",
    delimiter: str | None = None,
    create_using: Graph[_Node] | None = None,
    nodetype=None,
    data: bool | Iterable[Incomplete] = True,
): ...
@_dispatchable
def read_edgelist(
    path,
    comments: str | None = "#",
    delimiter: str | None = None,
    create_using=None,
    nodetype=None,
    data: bool | Iterable[Incomplete] = True,
    edgetype=None,
    encoding: str | None = "utf-8",
): ...
