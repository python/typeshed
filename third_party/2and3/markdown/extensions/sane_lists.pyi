from . import Extension
from ..blockprocessors import OListProcessor, UListProcessor
from typing import Any

class SaneOListProcessor(OListProcessor):
    SIBLING_TAGS: Any
    LAZY_OL: bool = ...
    CHILD_RE: Any
    def __init__(self, parser) -> None: ...

class SaneUListProcessor(UListProcessor):
    SIBLING_TAGS: Any
    CHILD_RE: Any
    def __init__(self, parser) -> None: ...

class SaneListExtension(Extension):
    def extendMarkdown(self, md) -> None: ...

def makeExtension(**kwargs): ...
