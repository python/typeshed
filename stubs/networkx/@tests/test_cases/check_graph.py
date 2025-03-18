from typing import Any, NewType
from typing_extensions import assert_type

from networkx import Graph
from networkx.classes.coreviews import AtlasView

Node = NewType("Node", str)


def test_graph_getitem() -> None:
    # Arrange
    g: Graph[Node] = Graph()
    for s in ["spam", "bacon", "eggs"]:
        g.add_node(Node(s))

    g.add_edge(Node("spam"), Node("bacon"), weight=1)
    g.add_edge(Node("spam"), Node("eggs"), weight=10)

    # Act
    atlas = g[Node("spam")]

    # Assert
    assert_type(atlas, AtlasView[Node, str, Any])
    assert_type(dict(atlas), dict[Node, dict[str, Any]])
