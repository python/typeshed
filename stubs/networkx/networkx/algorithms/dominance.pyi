from networkx.utils.backends import _dispatch

@_dispatch
def immediate_dominators(G, start): ...
@_dispatch
def dominance_frontiers(G, start): ...
