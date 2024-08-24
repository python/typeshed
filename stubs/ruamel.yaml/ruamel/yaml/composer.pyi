from typing import Any

from .error import MarkedYAMLError
from .main import YAML
from .nodes import MappingNode, Node, ScalarNode, SequenceNode
from .parser import Parser
from .resolver import BaseResolver

__all__ = ["Composer", "ComposerError"]

class ComposerError(MarkedYAMLError): ...

class Composer:
    loader: YAML
    anchors: dict[Any, Node]
    warn_double_anchors: bool
    def __init__(self, loader: YAML | None = None) -> None: ...
    @property
    def parser(self) -> Parser: ...
    @property
    def resolver(self) -> BaseResolver: ...
    def check_node(self) -> bool: ...
    def get_node(self) -> Node | None: ...
    def get_single_node(self) -> Node | None: ...
    def compose_document(self) -> Node | None: ...
    def return_alias(self, a: Node | None) -> Node | None: ...
    def compose_node(self, parent: Node | None, index: int) -> Node | None: ...
    def compose_scalar_node(self, anchor: dict[Any, Node]) -> ScalarNode: ...
    def compose_sequence_node(self, anchor: dict[Any, Node]) -> SequenceNode: ...
    def compose_mapping_node(self, anchor: dict[Any, Node]) -> MappingNode: ...
    def check_end_doc_comment(self, end_event, node) -> None: ...
