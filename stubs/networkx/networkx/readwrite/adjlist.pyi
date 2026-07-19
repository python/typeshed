from _typeshed import Incomplete
from collections.abc import Generator

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["generate_adjlist", "write_adjlist", "parse_adjlist", "read_adjlist"]

def generate_adjlist(G: Graph[_Node], delimiter: str = " ") -> Generator[str, None, None]: ...
def write_adjlist(G: Graph[_Node], path: str, comments: str = "#", delimiter: str = " ", encoding: str = "utf-8") -> None: ...
@_dispatchable
def parse_adjlist(
    lines: list[Incomplete],
    comments: str = "#",
    delimiter: str | None = None,
    create_using: Graph[Incomplete] | None = None,
    nodetype: type[Incomplete] | None = None,
) -> Graph[Incomplete]: ...
@_dispatchable
def read_adjlist(
    path: str,
    comments: str = "#",
    delimiter: str | None = None,
    create_using: Graph[Incomplete] | None = None,
    nodetype: type[Incomplete] | None = None,
    encoding: str = "utf-8",
) -> Graph[Incomplete]: ...
