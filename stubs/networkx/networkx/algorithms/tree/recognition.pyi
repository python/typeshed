from networkx.utils.backends import _dispatch

@_dispatch
def is_arborescence(G): ...
@_dispatch
def is_branching(G): ...
@_dispatch
def is_forest(G): ...
@_dispatch
def is_tree(G): ...
