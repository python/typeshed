from typing import NamedTuple, TypeAlias

class DeleteNode(NamedTuple):
    node: str

class InsertNode(NamedTuple):
    target: str
    tag: str
    position: int

class RenameNode(NamedTuple):
    node: str
    tag: str

class MoveNode(NamedTuple):
    node: str
    target: str
    position: int

class UpdateTextIn(NamedTuple):
    node: str
    text: str | None
    oldtext: str | None = None

class UpdateTextAfter(NamedTuple):
    node: str
    text: str | None
    oldtext: str | None = None

class UpdateAttrib(NamedTuple):
    node: str
    name: str
    value: str

class DeleteAttrib(NamedTuple):
    node: str
    name: str

class InsertAttrib(NamedTuple):
    node: str
    name: str
    value: str

class RenameAttrib(NamedTuple):
    node: str
    oldname: str
    newname: str

class InsertComment(NamedTuple):
    target: str
    position: int
    text: str | None

class InsertNamespace(NamedTuple):
    prefix: str | None
    uri: str

class DeleteNamespace(NamedTuple):
    prefix: str | None

_Action: TypeAlias = (  # noqa: Y047  # Used in other modules
    DeleteNode
    | InsertNode
    | RenameNode
    | MoveNode
    | UpdateTextIn
    | UpdateTextAfter
    | UpdateAttrib
    | DeleteAttrib
    | InsertAttrib
    | RenameAttrib
    | InsertComment
    | InsertNamespace
    | DeleteNamespace
)
