from networkx.utils.backends import _dispatch

@_dispatch
def tutte_polynomial(G): ...
@_dispatch
def chromatic_polynomial(G): ...
