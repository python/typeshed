from networkx.classes.graph import _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def immediate_dominators(G, start: _Node): ...
@_dispatchable
def dominance_frontiers(G, start: _Node): ...
