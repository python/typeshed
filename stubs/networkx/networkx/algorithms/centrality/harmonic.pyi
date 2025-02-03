from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def harmonic_centrality(G: Graph[_Node], nbunch: Iterable | None = None, distance=None, sources: Iterable | None = None): ...
