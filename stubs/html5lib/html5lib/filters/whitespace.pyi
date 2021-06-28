from typing import Any

from ..constants import rcdataElements as rcdataElements, spaceCharacters as spaceCharacters
from . import base as base

SPACES_REGEX: Any

class Filter(base.Filter):
    spacePreserveElements: Any
    def __iter__(self): ...

def collapse_spaces(text): ...
