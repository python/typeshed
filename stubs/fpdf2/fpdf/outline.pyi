from typing import Any, NamedTuple

from .structure_tree import StructElem
from .syntax import Destination, PDFObject

class OutlineSection(NamedTuple):
    name: str
    level: str
    page_number: int
    dest: Destination
    struct_elem: StructElem | None

class OutlineItemDictionary(PDFObject):
    title: Any
    parent: Any
    prev: Any
    next: Any
    first: Any
    last: Any
    count: int
    dest: Any
    struct_elem: Any
    def __init__(self, title: str, dest: str = ..., struct_elem: StructElem = ..., **kwargs) -> None: ...

class OutlineDictionary(PDFObject):
    type: str
    first: Any
    last: Any
    count: int
    def __init__(self, **kwargs) -> None: ...

def serialize_outline(sections, first_object_id: int = ..., fpdf: Any | None = ...): ...
