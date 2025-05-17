from _typeshed import Incomplete
from collections.abc import Generator

from networkx.utils.backends import _dispatchable

from ..classes.graph import Graph

__all__ = [
    "generate_edgelist",
    "write_edgelist",
    "parse_edgelist",
    "read_edgelist",
    "read_weighted_edgelist",
    "write_weighted_edgelist",
]

def generate_edgelist(
    G: Graph[Incomplete], delimiter: str = " ", data: bool | Incomplete = True
) -> Generator[Incomplete, None, None]: ...
def write_edgelist(
    G: Graph[Incomplete], path, comments: str = "#", delimiter: str = " ", data: bool | Incomplete = True, encoding: str = "utf-8"
) -> None: ...
@_dispatchable
def parse_edgelist(
    lines, comments: str = "#", delimiter: str | None = None, create_using=None, nodetype=None, data: bool | Incomplete = True
): ...
@_dispatchable
def read_edgelist(
    path,
    comments: str = "#",
    delimiter: str | None = None,
    create_using=None,
    nodetype=None,
    data: bool | Incomplete = True,
    edgetype=None,
    encoding: str = "utf-8",
): ...
def write_weighted_edgelist(
    G: Graph[Incomplete], path, comments: str = "#", delimiter: str = " ", encoding: str = "utf-8"
) -> None: ...
@_dispatchable
def read_weighted_edgelist(
    path, comments: str = "#", delimiter: str | None = None, create_using=None, nodetype=None, encoding: str = "utf-8"
): ...
