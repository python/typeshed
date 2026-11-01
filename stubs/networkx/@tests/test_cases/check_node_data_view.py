from __future__ import annotations

from typing import Any
from typing_extensions import assert_type

import networkx as nx

G: nx.Graph[int] = nx.Graph()

# `data=True` yields each node's whole data dictionary.
for _, node_data in G.nodes(data=True):
    assert_type(node_data, dict[str, Any])
assert_type(G.nodes(data=True)[1], dict[str, Any])
for _, node_data in G.nodes.data():
    assert_type(node_data, dict[str, Any])

# `data="<attr>"` yields the value of that attribute, or `default` when it is missing.
for _, weight in G.nodes(data="weight"):
    assert_type(weight, Any)
for _, weight_or_default in G.nodes(data="weight", default=0):
    assert_type(weight_or_default, Any | int)
for _, weight in G.nodes.data("weight"):
    assert_type(weight, Any)
for _, weight_or_default in G.nodes.data("weight", default=0):
    assert_type(weight_or_default, Any | int)
assert_type(G.nodes(data="weight", default=0)[1], Any | int)
