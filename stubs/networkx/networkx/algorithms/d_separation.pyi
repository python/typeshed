from networkx.utils.backends import _dispatch

@_dispatch
def d_separated(G, x, y, z): ...
@_dispatch
def minimal_d_separator(G, u, v): ...
@_dispatch
def is_minimal_d_separator(G, u, v, z): ...
