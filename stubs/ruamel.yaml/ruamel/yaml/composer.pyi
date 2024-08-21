from _typeshed import Incomplete

from .error import MarkedYAMLError

__all__ = ["Composer", "ComposerError"]

class ComposerError(MarkedYAMLError): ...

class Composer:
    loader: Incomplete
    anchors: Incomplete
    warn_double_anchors: bool
    def __init__(self, loader: Incomplete | None = None) -> None: ...
    @property
    def parser(self): ...
    @property
    def resolver(self): ...
    def check_node(self): ...
    def get_node(self): ...
    def get_single_node(self): ...
    def compose_document(self): ...
    def return_alias(self, a): ...
    def compose_node(self, parent, index): ...
    def compose_scalar_node(self, anchor): ...
    def compose_sequence_node(self, anchor): ...
    def compose_mapping_node(self, anchor): ...
    def check_end_doc_comment(self, end_event, node) -> None: ...
