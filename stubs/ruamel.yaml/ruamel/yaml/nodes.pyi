from _typeshed import Incomplete

class Node:
    ctag: Incomplete
    value: Incomplete
    start_mark: Incomplete
    end_mark: Incomplete
    comment: Incomplete
    anchor: Incomplete
    def __init__(
        self, tag, value, start_mark, end_mark, comment: Incomplete | None = None, anchor: Incomplete | None = None
    ) -> None: ...
    @property
    def tag(self) -> str | None: ...
    @tag.setter
    def tag(self, val) -> None: ...
    def dump(self, indent: int = 0) -> None: ...

class ScalarNode(Node):
    id: str
    style: Incomplete
    def __init__(
        self,
        tag,
        value,
        start_mark: Incomplete | None = None,
        end_mark: Incomplete | None = None,
        style: Incomplete | None = None,
        comment: Incomplete | None = None,
        anchor: Incomplete | None = None,
    ) -> None: ...

class CollectionNode(Node):
    flow_style: Incomplete
    anchor: Incomplete
    def __init__(
        self,
        tag,
        value,
        start_mark: Incomplete | None = None,
        end_mark: Incomplete | None = None,
        flow_style: Incomplete | None = None,
        comment: Incomplete | None = None,
        anchor: Incomplete | None = None,
    ) -> None: ...

class SequenceNode(CollectionNode):
    id: str

class MappingNode(CollectionNode):
    id: str
    merge: Incomplete
    def __init__(
        self,
        tag,
        value,
        start_mark: Incomplete | None = None,
        end_mark: Incomplete | None = None,
        flow_style: Incomplete | None = None,
        comment: Incomplete | None = None,
        anchor: Incomplete | None = None,
    ) -> None: ...
