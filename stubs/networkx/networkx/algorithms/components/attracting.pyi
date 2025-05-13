from _typeshed import Incomplete
from collections.abc import Generator

from networkx.utils.backends import _dispatchable

from ...classes.digraph import DiGraph

__all__ = ["number_attracting_components", "attracting_components", "is_attracting_component"]

@_dispatchable
def attracting_components(G: DiGraph) -> Generator[Incomplete, None, None]: ...
@_dispatchable
def number_attracting_components(G: DiGraph) -> int: ...
@_dispatchable
def is_attracting_component(G: DiGraph) -> bool: ...
