from . import Extension
from ..inlinepatterns import InlineProcessor
from ..preprocessors import Preprocessor
from typing import Any

ABBR_REF_RE: Any

class AbbrExtension(Extension):
    def extendMarkdown(self, md) -> None: ...

class AbbrPreprocessor(Preprocessor):
    def run(self, lines): ...

class AbbrInlineProcessor(InlineProcessor):
    title: Any
    def __init__(self, pattern, title) -> None: ...
    def handleMatch(self, m, data): ...  # type: ignore

def makeExtension(**kwargs): ...
