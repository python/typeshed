from typing import Any

from . import Extension

BR_RE: str

class Nl2BrExtension(Extension):
    def extendMarkdown(self, md) -> None: ...

def makeExtension(**kwargs): ...
