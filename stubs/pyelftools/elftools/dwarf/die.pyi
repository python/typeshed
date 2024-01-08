from _typeshed import Incomplete
from collections.abc import Generator
from typing import NamedTuple

class AttributeValue(NamedTuple):
    name: Incomplete
    form: Incomplete
    value: Incomplete
    raw_value: Incomplete
    offset: Incomplete
    indirection_length: Incomplete

class DIE:
    cu: Incomplete
    dwarfinfo: Incomplete
    stream: Incomplete
    offset: Incomplete
    attributes: Incomplete
    tag: Incomplete
    has_children: Incomplete
    abbrev_code: Incomplete
    size: int
    def __init__(self, cu, stream, offset) -> None: ...
    def is_null(self): ...
    def get_DIE_from_attribute(self, name): ...
    def get_parent(self): ...
    def get_full_path(self): ...
    def iter_children(self): ...
    def iter_siblings(self) -> Generator[Incomplete, None, None]: ...
    def set_parent(self, die) -> None: ...
