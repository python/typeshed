from . import Extension
from typing import Any

BR_RE: str

class Nl2BrExtension(Extension):
    def extendMarkdown(self, md: Any) -> None: ...

def makeExtension(**kwargs: Any): ...
