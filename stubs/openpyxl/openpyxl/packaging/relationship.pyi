from _typeshed import Incomplete
from collections.abc import Generator

from openpyxl.descriptors.base import Alias
from openpyxl.descriptors.serialisable import Serialisable

class Relationship(Serialisable):
    tagname: str
    Type: Incomplete
    Target: Incomplete
    target: Alias
    TargetMode: Incomplete
    Id: Incomplete
    id: Alias
    def __init__(
        self,
        Id: Incomplete | None = None,
        Type: Incomplete | None = None,
        type: Incomplete | None = None,
        Target: Incomplete | None = None,
        TargetMode: Incomplete | None = None,
    ) -> None: ...

class RelationshipList(Serialisable):
    tagname: str
    Relationship: Incomplete
    def __init__(self, Relationship=()) -> None: ...
    def append(self, value) -> None: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def find(self, content_type) -> Generator[Incomplete, None, None]: ...
    def __getitem__(self, key): ...
    def to_tree(self): ...

def get_rels_path(path): ...
def get_dependents(archive, filename): ...
def get_rel(archive, deps, id: Incomplete | None = None, cls: Incomplete | None = None): ...
