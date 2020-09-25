from typing import Any

from ..inlinepatterns import UnderscoreProcessor
from . import Extension

EMPHASIS_RE: str
STRONG_RE: str
STRONG_EM_RE: str

class LegacyUnderscoreProcessor(UnderscoreProcessor):
    PATTERNS: Any

class LegacyEmExtension(Extension):
    def extendMarkdown(self, md) -> None: ...

def makeExtension(**kwargs): ...
