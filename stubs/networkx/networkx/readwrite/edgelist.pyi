from _typeshed import Incomplete
from collections.abc import Generator

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = [
    "generate_edgelist",
    "write_edgelist",
    "parse_edgelist",
    "read_edgelist",
    "read_weighted_edgelist",
    "write_weighted_edgelist",
]

def generate_edgelist(G: Graph[_Node], delimiter: str = " ", data: bool = True) -> Generator[Incomplete]: ...
def write_edgelist(
    G: Graph[_Node], path: str, comments: str = "#", delimiter: str = " ", data: bool = True, encoding: str = "utf-8"
) -> None: ...
@_dispatchable
def parse_edgelist(
    lines: list[Incomplete],
    comments: str = "#",
    delimiter: str | None = None,
    create_using: Graph[Incomplete] | None = None,
    nodetype: type[Incomplete] | None = None,
    data: bool = True,
) -> Graph[Incomplete]: ...
@_dispatchable
def read_edgelist(
    path: str,
    comments: str = "#",
    delimiter: str | None = None,
    create_using: Graph[Incomplete] | None = None,
    nodetype=None,
    data: bool = True,
    edgetype=None,
    encoding: str = "utf-8",
) -> Graph[Incomplete]: ...
def write_weighted_edgelist(
    G: Graph[_Node], path: str, comments: str = "#", delimiter: str = " ", encoding: str = "utf-8"
) -> None: ...
@_dispatchable
def read_weighted_edgelist(
    path: str,
    comments: str = "#",
    delimiter: str | None = None,
    create_using: Graph[Incomplete] | None = None,
    nodetype=None,
    encoding: str = "utf-8",
) -> Graph[Incomplete]: ...
