from _typeshed import Incomplete
from typing import Any, ClassVar

from yaml.error import Mark

# Any Unions: Avoid forcing the user to check for None when they know what Node was instanciated with
# Using generics may be overkill without support for default Generics
# Permissive Unions could also be useful here.
class Node:
    tag: str
    value: Incomplete
    start_mark: Mark | None | Any
    end_mark: Mark | None | Any
    def __init__(self, tag: str, value, start_mark: Mark | None, end_mark: Mark | None) -> None: ...

class ScalarNode(Node):
    id: ClassVar[str]
    style: str | None | Any
    def __init__(
        self, tag: str, value, start_mark: Mark | None = ..., end_mark: Mark | None = ..., style: str | None = ...
    ) -> None: ...

class CollectionNode(Node):
    flow_style: bool | None | Any
    def __init__(
        self, tag: str, value, start_mark: Mark | None = ..., end_mark: Mark | None = ..., flow_style: bool | None = ...
    ) -> None: ...

class SequenceNode(CollectionNode):
    id: ClassVar[str]

class MappingNode(CollectionNode):
    id: ClassVar[str]
