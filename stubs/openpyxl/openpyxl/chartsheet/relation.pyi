from _typeshed import Incomplete

from openpyxl.descriptors.base import Alias
from openpyxl.descriptors.serialisable import Serialisable

class SheetBackgroundPicture(Serialisable):
    tagname: str
    id: Incomplete
    def __init__(self, id) -> None: ...

class DrawingHF(Serialisable):
    id: Incomplete
    lho: Incomplete
    leftHeaderOddPages: Alias
    lhe: Incomplete
    leftHeaderEvenPages: Alias
    lhf: Incomplete
    leftHeaderFirstPage: Alias
    cho: Incomplete
    centerHeaderOddPages: Alias
    che: Incomplete
    centerHeaderEvenPages: Alias
    chf: Incomplete
    centerHeaderFirstPage: Alias
    rho: Incomplete
    rightHeaderOddPages: Alias
    rhe: Incomplete
    rightHeaderEvenPages: Alias
    rhf: Incomplete
    rightHeaderFirstPage: Alias
    lfo: Incomplete
    leftFooterOddPages: Alias
    lfe: Incomplete
    leftFooterEvenPages: Alias
    lff: Incomplete
    leftFooterFirstPage: Alias
    cfo: Incomplete
    centerFooterOddPages: Alias
    cfe: Incomplete
    centerFooterEvenPages: Alias
    cff: Incomplete
    centerFooterFirstPage: Alias
    rfo: Incomplete
    rightFooterOddPages: Alias
    rfe: Incomplete
    rightFooterEvenPages: Alias
    rff: Incomplete
    rightFooterFirstPage: Alias
    def __init__(
        self,
        id: Incomplete | None = None,
        lho: Incomplete | None = None,
        lhe: Incomplete | None = None,
        lhf: Incomplete | None = None,
        cho: Incomplete | None = None,
        che: Incomplete | None = None,
        chf: Incomplete | None = None,
        rho: Incomplete | None = None,
        rhe: Incomplete | None = None,
        rhf: Incomplete | None = None,
        lfo: Incomplete | None = None,
        lfe: Incomplete | None = None,
        lff: Incomplete | None = None,
        cfo: Incomplete | None = None,
        cfe: Incomplete | None = None,
        cff: Incomplete | None = None,
        rfo: Incomplete | None = None,
        rfe: Incomplete | None = None,
        rff: Incomplete | None = None,
    ) -> None: ...
