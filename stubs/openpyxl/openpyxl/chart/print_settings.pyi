from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import Alias, Typed
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.worksheet.header_footer import HeaderFooter
from openpyxl.worksheet.page import PrintPageSetup

class PageMargins(Serialisable):
    tagname: str
    l: Incomplete
    left: Alias
    r: Incomplete
    right: Alias
    t: Incomplete
    top: Alias
    b: Incomplete
    bottom: Alias
    header: Incomplete
    footer: Incomplete
    def __init__(
        self, l: float = 0.75, r: float = 0.75, t: int = 1, b: int = 1, header: float = 0.5, footer: float = 0.5
    ) -> None: ...

class PrintSettings(Serialisable):
    tagname: str
    headerFooter: Typed[HeaderFooter, Literal[True]]
    pageMargins: Typed[PageMargins, Literal[True]]
    pageSetup: Typed[PrintPageSetup, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        headerFooter: HeaderFooter | None = None,
        pageMargins: PageMargins | None = None,
        pageSetup: PrintPageSetup | None = None,
    ) -> None: ...
