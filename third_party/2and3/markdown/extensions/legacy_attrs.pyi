from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from typing import Any

ATTR_RE: Any

class LegacyAttrs(Treeprocessor):
    def run(self, doc: Any) -> None: ...
    def handleAttributes(self, el: Any, txt: Any): ...

class LegacyAttrExtension(Extension):
    def extendMarkdown(self, md: Any) -> None: ...

def makeExtension(**kwargs: Any): ...
