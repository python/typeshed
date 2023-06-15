from typing_extensions import Literal

from openpyxl.descriptors.base import Bool, _ConvertibleToBool
from openpyxl.descriptors.serialisable import Serialisable

class Protection(Serialisable):
    tagname: str
    locked: Bool[Literal[False]]
    hidden: Bool[Literal[False]]
    def __init__(self, locked: _ConvertibleToBool = True, hidden: _ConvertibleToBool = False) -> None: ...
