from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import Bool, String, _ConvertibleToBool
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.worksheet.protection import _Protected

class ChartsheetProtection(Serialisable, _Protected):
    tagname: str
    algorithmName: String[Literal[True]]
    hashValue: Incomplete
    saltValue: Incomplete
    spinCount: Incomplete
    content: Bool[Literal[True]]
    objects: Bool[Literal[True]]
    __attrs__: Incomplete
    password: Incomplete
    def __init__(
        self,
        content: _ConvertibleToBool | None = None,
        objects: _ConvertibleToBool | None = None,
        hashValue: Incomplete | None = None,
        spinCount: Incomplete | None = None,
        saltValue: Incomplete | None = None,
        algorithmName: str | None = None,
        password: Incomplete | None = None,
    ) -> None: ...
