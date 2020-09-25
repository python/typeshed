from . import Extension
from ..inlinepatterns import UnderscoreProcessor
from typing import Any

EMPHASIS_RE: str
STRONG_RE: str
STRONG_EM_RE: str

class LegacyUnderscoreProcessor(UnderscoreProcessor):
    PATTERNS: Any = ...

class LegacyEmExtension(Extension):
    def extendMarkdown(self, md: Any) -> None: ...

def makeExtension(**kwargs: Any): ...
