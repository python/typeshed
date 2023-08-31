from _typeshed import Incomplete

from networkx.algorithms.flow import edmonds_karp

default_flow_func = edmonds_karp

def minimum_st_edge_cut(
    G, s, t, flow_func: Incomplete | None = None, auxiliary: Incomplete | None = None, residual: Incomplete | None = None
): ...
def minimum_st_node_cut(
    G, s, t, flow_func: Incomplete | None = None, auxiliary: Incomplete | None = None, residual: Incomplete | None = None
): ...
def minimum_node_cut(G, s: Incomplete | None = None, t: Incomplete | None = None, flow_func: Incomplete | None = None): ...
def minimum_edge_cut(G, s: Incomplete | None = None, t: Incomplete | None = None, flow_func: Incomplete | None = None): ...
