from typing import Any

from ..preprocessors import Preprocessor
from . import Extension

log: Any
META_RE: Any
META_MORE_RE: Any
BEGIN_RE: Any
END_RE: Any

class MetaExtension(Extension):
    md: Any
    def extendMarkdown(self, md) -> None: ...
    def reset(self) -> None: ...

class MetaPreprocessor(Preprocessor):
    def run(self, lines): ...

def makeExtension(**kwargs): ...
