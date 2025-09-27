from collections.abc import Generator

from networkx.utils.backends import _dispatchable

from ..classes.graph import Graph, _Node

__all__ = ["generate_multiline_adjlist", "write_multiline_adjlist", "parse_multiline_adjlist", "read_multiline_adjlist"]

def generate_multiline_adjlist(G: Graph[_Node], delimiter: str = " ") -> Generator[str, None, None]: ...
def write_multiline_adjlist(
    G: Graph[_Node], path, delimiter: str = " ", comments: str = "#", encoding: str = "utf-8"
) -> None: ...
@_dispatchable
def parse_multiline_adjlist(
    lines, comments: str = "#", delimiter: str | None = None, create_using=None, nodetype=None, edgetype=None
): ...
@_dispatchable
def read_multiline_adjlist(
    path,
    comments: str = "#",
    delimiter: str | None = None,
    create_using=None,
    nodetype=None,
    edgetype=None,
    encoding: str = "utf-8",
): ...
