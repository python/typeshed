from _typeshed import Incomplete
from typing import Any

class Node:
    ctag: Incomplete
    value: Incomplete
    start_mark: Incomplete
    end_mark: Incomplete
    comment: Incomplete
    anchor: Incomplete
    def __init__(self, tag: Any, value: Any, start_mark: Any, end_mark: Any, comment: Any = None, anchor: Any = None) -> None: ...
    @property
    def tag(self) -> str | None: ...
    @tag.setter
    def tag(self, val: Any) -> None: ...
    def dump(self, indent: int = 0) -> None: ...

class ScalarNode(Node):
    id: str
    style: Incomplete
    def __init__(
        self,
        tag: Any,
        value: Any,
        start_mark: Any = None,
        end_mark: Any = None,
        style: Any = None,
        comment: Any = None,
        anchor: Any = None,
    ) -> None: ...

class CollectionNode(Node):
    flow_style: Incomplete
    anchor: Incomplete
    def __init__(
        self,
        tag: Any,
        value: Any,
        start_mark: Any = None,
        end_mark: Any = None,
        flow_style: Any = None,
        comment: Any = None,
        anchor: Any = None,
    ) -> None: ...

class SequenceNode(CollectionNode):
    id: str

class MappingNode(CollectionNode):
    id: str
    merge: Incomplete
    def __init__(
        self,
        tag: Any,
        value: Any,
        start_mark: Any = None,
        end_mark: Any = None,
        flow_style: Any = None,
        comment: Any = None,
        anchor: Any = None,
    ) -> None: ...
