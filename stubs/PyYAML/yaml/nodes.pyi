from typing import Any, ClassVar

from yaml.error import Mark as Mark

class Node:
    tag: str
    value: Any
    start_mark: Mark | Any
    end_mark: Mark | Any
    def __init__(self, tag: str, value: Any, start_mark: Mark | None, end_mark: Mark | None) -> None: ...

class ScalarNode(Node):
    id: ClassVar[str]
    tag: str
    value: Any
    start_mark: Mark | Any
    end_mark: Mark | Any
    style: str | Any
    def __init__(
        self, tag: str, value: Any, start_mark: Mark | None = ..., end_mark: Mark | None = ..., style: str | None = ...
    ) -> None: ...

class CollectionNode(Node):
    tag: str
    value: Any
    start_mark: Mark | Any
    end_mark: Mark | Any
    flow_style: bool | Any
    def __init__(
        self, tag: str, value: Any, start_mark: Mark | None = ..., end_mark: Mark | None = ..., flow_style: bool | None = ...
    ) -> None: ...

class SequenceNode(CollectionNode):
    id: ClassVar[str]

class MappingNode(CollectionNode):
    id: ClassVar[str]
