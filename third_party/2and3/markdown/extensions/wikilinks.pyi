from typing import Any

from ..inlinepatterns import InlineProcessor
from . import Extension

def build_url(label, base, end): ...

class WikiLinkExtension(Extension):
    config: Any
    def __init__(self, **kwargs) -> None: ...
    md: Any
    def extendMarkdown(self, md) -> None: ...

class WikiLinksInlineProcessor(InlineProcessor):
    config: Any
    def __init__(self, pattern, config) -> None: ...
    def handleMatch(self, m, data): ...  # type: ignore

def makeExtension(**kwargs): ...
