from typing import Any, Pattern

from markdown.blockprocessors import BlockProcessor
from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor

ABBR_REF_RE: Pattern

class AbbrExtension(Extension):
    def extendMarkdown(self, md) -> None: ...

class AbbrPreprocessor(BlockProcessor):
    def run(self, lines): ...

class AbbrInlineProcessor(InlineProcessor):
    title: Any
    def __init__(self, pattern, title) -> None: ...
    def handleMatch(self, m, data): ...  # type: ignore

def makeExtension(**kwargs): ...
