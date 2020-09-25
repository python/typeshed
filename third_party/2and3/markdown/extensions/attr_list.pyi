from . import Extension
from ..treeprocessors import Treeprocessor
from typing import Any

def get_attrs(str: Any): ...
def isheader(elem: Any): ...

class AttrListTreeprocessor(Treeprocessor):
    BASE_RE: str = ...
    HEADER_RE: Any = ...
    BLOCK_RE: Any = ...
    INLINE_RE: Any = ...
    NAME_RE: Any = ...
    def run(self, doc: Any) -> None: ...
    def assign_attrs(self, elem: Any, attrs: Any) -> None: ...
    def sanitize_name(self, name: Any): ...

class AttrListExtension(Extension):
    def extendMarkdown(self, md: Any) -> None: ...

def makeExtension(**kwargs: Any): ...
