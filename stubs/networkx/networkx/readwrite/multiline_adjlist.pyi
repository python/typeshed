from _typeshed import Incomplete
from collections.abc import Generator

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["generate_multiline_adjlist", "write_multiline_adjlist", "parse_multiline_adjlist", "read_multiline_adjlist"]

def generate_multiline_adjlist(G: Graph[_Node], delimiter: str = " ") -> Generator[str, None, None]: ...
def write_multiline_adjlist(
    G: Graph[_Node], path: str, delimiter: str = " ", comments: str = "#", encoding: str = "utf-8"
) -> None: ...
@_dispatchable
def parse_multiline_adjlist(
    lines: list[Incomplete],
    comments: str = "#",
    delimiter: str = None,
    create_using: Graph[Incomplete] = None,
    nodetype: type[Incomplete] = None,
    edgetype: type[Incomplete] = None,
) -> Graph[Incomplete]: ...
@_dispatchable
def read_multiline_adjlist(
    path: str,
    comments: str = "#",
    delimiter: str = None,
    create_using: Graph[Incomplete] = None,
    nodetype: type[Incomplete] = None,
    edgetype: type[Incomplete] = None,
    encoding: str = "utf-8",
) -> Graph[Incomplete]: ...
