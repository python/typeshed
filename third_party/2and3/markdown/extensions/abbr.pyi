from . import Extension
from ..inlinepatterns import InlineProcessor
from ..preprocessors import Preprocessor
from typing import Any

ABBR_REF_RE: Any

class AbbrExtension(Extension):
    def extendMarkdown(self, md: Any) -> None: ...

class AbbrPreprocessor(Preprocessor):
    def run(self, lines: Any): ...

class AbbrInlineProcessor(InlineProcessor):
    title: Any = ...
    def __init__(self, pattern: Any, title: Any) -> None: ...
    def handleMatch(self, m: Any, data: Any): ...  # type: ignore

def makeExtension(**kwargs: Any): ...
