from _typeshed import Incomplete

from networkx.classes.graph import Graph
from networkx.utils.backends import _dispatchable

__all__ = ["read_leda", "parse_leda"]

@_dispatchable
def read_leda(path: str, encoding: str = "UTF-8") -> Graph[Incomplete]: ...
@_dispatchable
def parse_leda(lines: str) -> Graph[Incomplete]: ...
