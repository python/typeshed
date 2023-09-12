from _typeshed import Incomplete, Unused
from collections.abc import Generator
from typing import ClassVar, TypeVar, overload
from typing_extensions import Literal
from zipfile import ZipFile

from openpyxl.descriptors.base import Alias, String
from openpyxl.descriptors.serialisable import Serialisable

_SerialisableT = TypeVar("_SerialisableT", bound=Serialisable)

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
    def to_tree(self): ...

def get_rels_path(path): ...
def get_dependents(archive: ZipFile, filename: str) -> RelationshipList: ...
@overload
def get_rel(
    archive: ZipFile, deps: RelationshipList, id: str, cls: type[_SerialisableT]
) -> _SerialisableT: ...  # incomplete: this could be restricted further from "Serialisable"
@overload
def get_rel(
    archive: ZipFile, deps: RelationshipList, id: str | None = None, *, cls: type[_SerialisableT]
) -> _SerialisableT: ...  # incomplete: this could be restricted further from "Serialisable"
