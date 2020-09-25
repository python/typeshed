from . import Extension
from ..blockprocessors import BlockProcessor, ListIndentProcessor
from typing import Any

class DefListProcessor(BlockProcessor):
    RE: Any
    NO_INDENT_RE: Any
    def test(self, parent, block): ...
    def run(self, parent, blocks): ...

class DefListIndentProcessor(ListIndentProcessor):
    ITEM_TYPES: Any
    LIST_TYPES: Any
    def create_item(self, parent, block) -> None: ...

class DefListExtension(Extension):
    def extendMarkdown(self, md) -> None: ...

def makeExtension(**kwargs): ...
