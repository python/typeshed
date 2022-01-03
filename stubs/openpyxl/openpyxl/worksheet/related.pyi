from typing import Any

from openpyxl.descriptors.excel import Relation as Relation
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class Related(Serialisable):
    id: Any
    def __init__(self, id: Any | None = ...) -> None: ...
    def to_tree(self, tagname, idx: Any | None = ...): ...
