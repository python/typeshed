from typing import Any

from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

class FencedCodeExtension(Extension):
    def extendMarkdown(self, md) -> None: ...

class FencedBlockPreprocessor(Preprocessor):
    FENCED_BLOCK_RE: Any
    CODE_WRAP: str = ...
    LANG_TAG: str = ...
    checked_for_codehilite: bool = ...
    codehilite_conf: Any
    def __init__(self, md) -> None: ...
    def run(self, lines): ...

def makeExtension(**kwargs): ...
