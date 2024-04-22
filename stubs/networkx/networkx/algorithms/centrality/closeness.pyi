from networkx.classes.graph import Graph, _Node, _Edge
from networkx.utils.backends import _dispatch

@_dispatch
def closeness_centrality(G: Graph[_Node], u: _Node | None = None, distance: str | None = None, wf_improved: bool = True) -> dict[_Node, float]: ...
@_dispatch
def incremental_closeness_centrality(
    G: Graph[_Node], edge: _Edge[_Node], prev_cc: dict[_Node, float] | None = None, insertion: bool = True, wf_improved: bool = True
) -> dict[_Node, float]: ...
