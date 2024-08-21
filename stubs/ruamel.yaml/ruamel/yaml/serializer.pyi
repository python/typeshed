from _typeshed import Incomplete

from .compat import VersionType
from .error import YAMLError

__all__ = ["Serializer", "SerializerError"]

class SerializerError(YAMLError): ...

class Serializer:
    ANCHOR_TEMPLATE: str
    ANCHOR_RE: Incomplete
    dumper: Incomplete
    use_encoding: Incomplete
    use_explicit_start: Incomplete
    use_explicit_end: Incomplete
    use_version: Incomplete
    use_tags: Incomplete
    serialized_nodes: Incomplete
    anchors: Incomplete
    last_anchor_id: int
    closed: Incomplete
    def __init__(
        self,
        encoding: Incomplete | None = None,
        explicit_start: bool | None = None,
        explicit_end: bool | None = None,
        version: VersionType | None = None,
        tags: Incomplete | None = None,
        dumper: Incomplete | None = None,
    ) -> None: ...
    @property
    def emitter(self): ...
    @property
    def resolver(self): ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def serialize(self, node) -> None: ...
    def anchor_node(self, node) -> None: ...
    def generate_anchor(self, node): ...
    def serialize_node(self, node, parent, index) -> None: ...
