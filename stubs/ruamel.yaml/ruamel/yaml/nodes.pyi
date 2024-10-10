from typing import Any, ClassVar, Literal
from typing_extensions import TypeAlias

from .anchor import Anchor
from .error import _Mark
from .tag import Tag
from .tokens import _CommentGroup, _ScalarStyle

_ScalarNodeStyle: TypeAlias = Literal["?", "-"] | _ScalarStyle

class Node:
    id: ClassVar[str]
    ctag: Tag
    value: Any
    start_mark: _Mark | None
    end_mark: _Mark | None
    comment: _CommentGroup | None
    anchor: Anchor | str | None
    def __init__(
        self,
        tag: Tag | str | None,
        value: Any,
        start_mark: _Mark | None,
        end_mark: _Mark | None,
        *,
        comment: _CommentGroup | None = None,
        anchor: Anchor | str | None = None,
    ) -> None: ...
    @property
    def tag(self) -> str | None: ...
    @tag.setter
    def tag(self, val: Tag | str | None, /) -> None: ...
    def dump(self, *, indent: int = 0) -> None: ...

class ScalarNode(Node):
    id: ClassVar[Literal["scalar"]]
    value: str
    style: _ScalarNodeStyle | None
    def __init__(
        self,
        tag: Tag | str | None,
        value: str,
        start_mark: _Mark | None = None,
        end_mark: _Mark | None = None,
        *,
        style: _ScalarNodeStyle | None = None,
        comment: _CommentGroup | None = None,
        anchor: Anchor | str | None = None,
    ) -> None: ...

class CollectionNode(Node):
    value: list[Any]
    flow_style: bool | None
    def __init__(
        self,
        tag: Tag | str | None,
        value: list[Any],
        start_mark: _Mark | None = None,
        end_mark: _Mark | None = None,
        *,
        flow_style: bool | None = None,
        comment: _CommentGroup | None = None,
        anchor: Anchor | str | None = None,
    ) -> None: ...

class SequenceNode(CollectionNode):
    id: ClassVar[Literal["sequence"]]
    value: list[Node]
    def __init__(
        self,
        tag: Tag | str | None,
        value: list[Node],
        start_mark: _Mark | None = None,
        end_mark: _Mark | None = None,
        *,
        flow_style: bool | None = None,
        comment: _CommentGroup | None = None,
        anchor: Anchor | str | None = None,
    ) -> None: ...

class MappingNode(CollectionNode):
    id: ClassVar[Literal["mapping"]]
    value: list[tuple[Node, Node]]
    merge: list[tuple[Node, Node]] | None
    def __init__(
        self,
        tag: Tag | str | None,
        value: list[tuple[Node, Node]],
        start_mark: _Mark | None = None,
        end_mark: _Mark | None = None,
        *,
        flow_style: bool | None = None,
        comment: _CommentGroup | None = None,
        anchor: Anchor | str | None = None,
    ) -> None: ...
