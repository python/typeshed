from . import Extension
from typing import Any

extensions: Any

class ExtraExtension(Extension):
    config: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def extendMarkdown(self, md: Any) -> None: ...

def makeExtension(**kwargs: Any): ...
