from typing import Any

from ..treeprocessors import Treeprocessor
from . import Extension

def get_attrs(str): ...
def isheader(elem): ...

class AttrListTreeprocessor(Treeprocessor):
    BASE_RE: str = ...
    HEADER_RE: Any
    BLOCK_RE: Any
    INLINE_RE: Any
    NAME_RE: Any
    def run(self, doc) -> None: ...
    def assign_attrs(self, elem, attrs) -> None: ...
    def sanitize_name(self, name): ...

class AttrListExtension(Extension):
    def extendMarkdown(self, md) -> None: ...

def makeExtension(**kwargs): ...
