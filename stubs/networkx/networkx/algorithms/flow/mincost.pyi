from networkx.utils.backends import _dispatch

@_dispatch
def min_cost_flow_cost(G, demand: str = "demand", capacity: str = "capacity", weight: str = "weight"): ...
@_dispatch
def min_cost_flow(G, demand: str = "demand", capacity: str = "capacity", weight: str = "weight"): ...
@_dispatch
def cost_of_flow(G, flowDict, weight: str = "weight"): ...
@_dispatch
def max_flow_min_cost(G, s, t, capacity: str = "capacity", weight: str = "weight"): ...
