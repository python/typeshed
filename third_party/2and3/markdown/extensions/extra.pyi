from . import Extension
from typing import Any

extensions: Any

class ExtraExtension(Extension):
    config: Any
    def __init__(self, **kwargs) -> None: ...
    def extendMarkdown(self, md) -> None: ...

def makeExtension(**kwargs): ...
