from collections.abc import Callable

from networkx.algorithms.flow import edmonds_karp
from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["minimum_st_node_cut", "minimum_node_cut", "minimum_st_edge_cut", "minimum_edge_cut"]
default_flow_func = edmonds_karp

@_dispatchable
def minimum_st_edge_cut(
    G: Graph[_Node],
    s: _Node,
    t: _Node,
    flow_func: Callable = None,
    auxiliary: DiGraph[_Node] = None,
    residual: DiGraph[_Node] = None,
): ...
@_dispatchable
def minimum_st_node_cut(
    G: Graph[_Node],
    s: _Node,
    t: _Node,
    flow_func: Callable = None,
    auxiliary: DiGraph[_Node] = None,
    residual: DiGraph[_Node] = None,
): ...
@_dispatchable
def minimum_node_cut(G: Graph[_Node], s: _Node = None, t: _Node = None, flow_func: Callable = None): ...
@_dispatchable
def minimum_edge_cut(G: Graph[_Node], s: _Node = None, t: _Node = None, flow_func: Callable = None): ...
