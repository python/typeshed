from _typeshed import Incomplete
from collections import defaultdict
from collections.abc import Generator, Iterable

from .syntax import PDFArray, PDFObject, PDFString

class NumberTree(PDFObject):
    nums: defaultdict[Incomplete, list[Incomplete]]
    def __init__(self) -> None: ...
    def serialize(self, obj_dict: object = ...) -> str: ...

class StructTreeRoot(PDFObject):
    type: str
    parent_tree: NumberTree
    k: PDFArray
    def __init__(self) -> None: ...

class StructElem(PDFObject):
    type: str
    s: str
    p: PDFObject
    k: PDFArray
    t: PDFString | None
    alt: PDFString | None
    pg: Incomplete | None
    def __init__(
        self,
        struct_type: str,
        parent: PDFObject,
        kids: Iterable[int] | Iterable[StructElem],
        page_number: int | None = ...,
        title: str | None = ...,
        alt: str | None = ...,
    ) -> None: ...
    def page_number(self) -> int | None: ...

class StructureTreeBuilder:
    struct_tree_root: Incomplete
    doc_struct_elem: Incomplete
    struct_elem_per_mc: Incomplete
    def __init__(self) -> None: ...
    def add_marked_content(
        self, page_number: int, struct_type: str, mcid: int | None = ..., title: str | None = ..., alt_text: str | None = ...
    ) -> tuple[Incomplete, Incomplete]: ...
    def next_mcid_for_page(self, page_number: int) -> int: ...
    def empty(self) -> bool: ...
    def __iter__(self) -> Generator[Incomplete, None, None]: ...
