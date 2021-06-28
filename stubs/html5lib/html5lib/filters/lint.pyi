from typing import Any

from ..constants import namespaces as namespaces, spaceCharacters as spaceCharacters, voidElements as voidElements
from . import base as base

class Filter(base.Filter):
    require_matching_tags: Any
    def __init__(self, source, require_matching_tags: bool = ...) -> None: ...
    def __iter__(self): ...
