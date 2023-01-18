from _typeshed import Incomplete
from typing import Any, ClassVar

from yaml.error import Mark

class Node:
    tag: str
    value: Any
    start_mark: Mark | Incomplete
    end_mark: Mark | Incomplete
    def __init__(self, tag: str, value, start_mark: Mark | None, end_mark: Mark | None) -> None: ...

class ScalarNode(Node):
    id: ClassVar[str]
    style: str | Incomplete
    def __init__(
        self, tag: str, value, start_mark: Mark | None = ..., end_mark: Mark | None = ..., style: str | None = ...
    ) -> None: ...

class CollectionNode(Node):
    flow_style: bool | Incomplete
    def __init__(
        self, tag: str, value, start_mark: Mark | None = ..., end_mark: Mark | None = ..., flow_style: bool | None = ...
    ) -> None: ...

class SequenceNode(CollectionNode):
    id: ClassVar[str]

class MappingNode(CollectionNode):
    id: ClassVar[str]
