from typing import Any

from yaml.error import MarkedYAMLError
from yaml.nodes import MappingNode, Node, ScalarNode, SequenceNode

class ComposerError(MarkedYAMLError): ...

class Composer:
    anchors: dict[Any, Node]
    def __init__(self) -> None: ...
    def check_node(self) -> bool: ...
    def get_node(self) -> Node | None: ...
    def get_single_node(self) -> Node | None: ...
    def compose_document(self) -> Node | None: ...
    def compose_node(self, parent: Node | None, index: int) -> Node | None: ...
    def compose_scalar_node(self, anchor: dict[Any, Node]) -> ScalarNode: ...
    def compose_sequence_node(self, anchor: dict[Any, Node]) -> SequenceNode: ...
    def compose_mapping_node(self, anchor: dict[Any, Node]) -> MappingNode: ...

__all__ = ["Composer", "ComposerError"]
