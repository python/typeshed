from networkx.utils.backends import _dispatch

@_dispatch
def efficiency(G, u, v): ...
@_dispatch
def global_efficiency(G): ...
@_dispatch
def local_efficiency(G): ...
