from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.xml.functions import Element

class Related(Serialisable):
    id: Incomplete
    def __init__(self, id: Incomplete | None = None) -> None: ...
    def to_tree(self, tagname, idx: Incomplete | None = None) -> Element: ...  # type: ignore[override]
