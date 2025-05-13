from _typeshed import Incomplete
from collections.abc import Generator

from networkx.utils.backends import _dispatchable

from ..classes.graph import Graph

__all__ = ["generate_adjlist", "write_adjlist", "parse_adjlist", "read_adjlist"]

def generate_adjlist(G: Graph[Incomplete], delimiter: str = " ") -> Generator[str, None, None]: ...
def write_adjlist(G: Graph[Incomplete], path, comments: str = "#", delimiter: str = " ", encoding: str = "utf-8") -> None: ...
@_dispatchable
def parse_adjlist(
    lines,
    comments: str = "#",
    delimiter: str | None = None,
    create_using: Incomplete | None = None,
    nodetype: Incomplete | None = None,
): ...
@_dispatchable
def read_adjlist(
    path,
    comments: str = "#",
    delimiter: str | None = None,
    create_using: Incomplete | None = None,
    nodetype: Incomplete | None = None,
    encoding: str = "utf-8",
): ...
