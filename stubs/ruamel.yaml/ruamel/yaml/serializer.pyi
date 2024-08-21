from _typeshed import Incomplete
from typing import Any

from ruamel.yaml.compat import VersionType
from ruamel.yaml.error import YAMLError

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
        encoding: Any = None,
        explicit_start: bool | None = None,
        explicit_end: bool | None = None,
        version: VersionType | None = None,
        tags: Any = None,
        dumper: Any = None,
    ) -> None: ...
    @property
    def emitter(self) -> Any: ...
    @property
    def resolver(self) -> Any: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def serialize(self, node: Any) -> None: ...
    def anchor_node(self, node: Any) -> None: ...
    def generate_anchor(self, node: Any) -> Any: ...
    def serialize_node(self, node: Any, parent: Any, index: Any) -> None: ...
