from re import Pattern
from typing import Final, Literal

from .compat import VersionType
from .emitter import Emitter
from .error import YAMLError
from .main import YAML
from .nodes import CollectionNode, Node
from .resolver import BaseResolver
from .tag import _TagHandleToPrefix
from .tokens import _VersionTuple

__all__ = ["Serializer", "SerializerError"]

class SerializerError(YAMLError): ...

class Serializer:
    ANCHOR_TEMPLATE: Final[str]
    ANCHOR_RE: Final[Pattern[str]]
    dumper: YAML | None
    use_encoding: str | None
    use_explicit_start: bool | None
    use_explicit_end: bool | None
    use_version: _VersionTuple | None
    use_tags: _TagHandleToPrefix | None
    serialized_nodes: dict[Node, Literal[True]]
    anchors: dict[Node, str | None]
    last_anchor_id: int
    closed: bool | None
    def __init__(
        self,
        encoding: str | None = None,
        explicit_start: bool | None = None,
        explicit_end: bool | None = None,
        version: VersionType | None = None,
        tags: _TagHandleToPrefix | None = None,
        dumper: YAML | None = None,
    ) -> None: ...
    @property
    def emitter(self) -> Emitter: ...
    @property
    def resolver(self) -> BaseResolver: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def serialize(self, node: Node) -> None: ...
    def anchor_node(self, node: Node) -> None: ...
    def generate_anchor(self, node: Node) -> str: ...
    def serialize_node(self, node: Node, parent: CollectionNode | None, index: int | Node | None) -> None: ...
