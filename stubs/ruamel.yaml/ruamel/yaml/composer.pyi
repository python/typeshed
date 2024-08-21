from _typeshed import Incomplete
from typing import Any

from ruamel.yaml.error import MarkedYAMLError

__all__ = ["Composer", "ComposerError"]

class ComposerError(MarkedYAMLError): ...

class Composer:
    loader: Incomplete
    anchors: Incomplete
    warn_double_anchors: bool
    def __init__(self, loader: Any = None) -> None: ...
    @property
    def parser(self) -> Any: ...
    @property
    def resolver(self) -> Any: ...
    def check_node(self) -> Any: ...
    def get_node(self) -> Any: ...
    def get_single_node(self) -> Any: ...
    def compose_document(self) -> Any: ...
    def return_alias(self, a: Any) -> Any: ...
    def compose_node(self, parent: Any, index: Any) -> Any: ...
    def compose_scalar_node(self, anchor: Any) -> Any: ...
    def compose_sequence_node(self, anchor: Any) -> Any: ...
    def compose_mapping_node(self, anchor: Any) -> Any: ...
    def check_end_doc_comment(self, end_event: Any, node: Any) -> None: ...
