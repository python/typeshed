from typing import Any, NewType
from typing_extensions import assert_type

from networkx import Graph

Node = NewType("Node", str)


def test_atlas_copy() -> None:
    # Arrange
    g: Graph[Node] = Graph()
    for s in ["spam", "bacon", "eggs"]:
        g.add_node(Node(s))

    g.add_edge(Node("spam"), Node("bacon"), weight=1)
    g.add_edge(Node("spam"), Node("eggs"), weight=10)

    # Act
    atlas = g[Node("spam")]

    # Assert
    assert_type(atlas.copy(), dict[Node, dict[str, Any]])
