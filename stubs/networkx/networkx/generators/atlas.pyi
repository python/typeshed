from _typeshed import Incomplete
from importlib.abc import Traversable
from typing import Final

from networkx.utils.backends import _dispatchable

from ..classes.graph import Graph

__all__ = ["graph_atlas", "graph_atlas_g"]

NUM_GRAPHS: Final = 1253

ATLAS_FILE: Traversable

@_dispatchable
def graph_atlas(i: int) -> Graph[Incomplete]: ...
@_dispatchable
def graph_atlas_g() -> list[Graph[Incomplete]]: ...
