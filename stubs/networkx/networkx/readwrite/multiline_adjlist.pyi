from _typeshed import Incomplete, StrPath, SupportsRead, SupportsWrite
from collections.abc import Callable, Generator, Iterator

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["generate_multiline_adjlist", "write_multiline_adjlist", "parse_multiline_adjlist", "read_multiline_adjlist"]

def generate_multiline_adjlist(G: Graph[_Node], delimiter: str = " ") -> Generator[str]: ...
def write_multiline_adjlist(
    G: Graph[_Node], path: StrPath | SupportsWrite[bytes], delimiter: str = " ", comments: str = "#", encoding: str = "utf-8"
) -> None: ...
@_dispatchable
def parse_multiline_adjlist(
    lines: Iterator[str],
    comments: str = "#",
    delimiter: str | None = None,
    create_using: Graph[Incomplete] | type[Graph[Incomplete]] | None = None,
    nodetype: Callable[[str], Incomplete] | None = None,
    edgetype: Callable[[str], Incomplete] | None = None,
) -> Graph[Incomplete]: ...
@_dispatchable
def read_multiline_adjlist(
    path: StrPath | SupportsRead[bytes],
    comments: str = "#",
    delimiter: str | None = None,
    create_using: Graph[Incomplete] | type[Graph[Incomplete]] | None = None,
    nodetype: Callable[[str], Incomplete] | None = None,
    edgetype: Callable[[str], Incomplete] | None = None,
    encoding: str = "utf-8",
) -> Graph[Incomplete]: ...
