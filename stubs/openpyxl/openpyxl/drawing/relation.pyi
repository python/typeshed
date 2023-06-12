from _typeshed import Incomplete
from typing import ClassVar

from openpyxl.descriptors.serialisable import Serialisable

class ChartRelation(Serialisable):
    tagname: ClassVar[str]
    namespace: Incomplete
    id: Incomplete
    def __init__(self, id) -> None: ...
