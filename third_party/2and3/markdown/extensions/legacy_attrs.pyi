from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from typing import Any

ATTR_RE: Any

class LegacyAttrs(Treeprocessor):
    def run(self, doc) -> None: ...
    def handleAttributes(self, el, txt): ...

class LegacyAttrExtension(Extension):
    def extendMarkdown(self, md) -> None: ...

def makeExtension(**kwargs): ...
