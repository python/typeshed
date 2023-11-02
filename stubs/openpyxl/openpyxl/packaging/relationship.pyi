from _typeshed import Incomplete, Unused
from collections.abc import Generator
from typing import ClassVar, overload
from typing_extensions import Literal

from openpyxl.descriptors.base import Alias, String
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.xml.functions import Element

class Relationship(Serialisable):
    tagname: ClassVar[str]
    Type: String[Literal[False]]
    Target: String[Literal[False]]
    target: Alias
    TargetMode: String[Literal[True]]
    Id: String[Literal[True]]
    id: Alias
    @overload
    def __init__(
        self, Id: str, Type: Unused = None, *, type: str, Target: str | None = None, TargetMode: str | None = None
    ) -> None: ...
    @overload
    def __init__(self, Id: str, Type: Unused, type: str, Target: str | None = None, TargetMode: str | None = None) -> None: ...
    @overload
    def __init__(
        self, Id: str, Type: str, type: None = None, Target: str | None = None, TargetMode: str | None = None
    ) -> None: ...

class RelationshipList(Serialisable):
    tagname: ClassVar[str]
    Relationship: Incomplete
    def __init__(self, Relationship=()) -> None: ...
    def append(self, value) -> None: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def find(self, content_type) -> Generator[Incomplete, None, None]: ...
    def __getitem__(self, key): ...
    def to_tree(self) -> Element: ...  # type:ignore[override]

def get_rels_path(path): ...
def get_dependents(archive, filename): ...
def get_rel(archive, deps, id: Incomplete | None = None, cls: Incomplete | None = None): ...
