from typing import Any

from openpyxl.descriptors.serialisable import Serialisable

class Related(Serialisable):
    id: Any
    def __init__(self, id: Any | None = ...) -> None: ...
    def to_tree(self, tagname, idx: Any | None = ...): ...
