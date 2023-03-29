from _typeshed import Incomplete, Unused
from typing_extensions import Literal

from openpyxl.descriptors.base import NoneSet, Typed
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.drawing.fill import GradientFillProperties, PatternFillProperties

class LineEndProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    type: NoneSet(values=(["none", "triangle", "stealth", "diamond", "oval", "arrow"]))
    w: NoneSet(values=(["sm", "med", "lg"]))
    len: NoneSet(values=(["sm", "med", "lg"]))
    def __init__(self, type: Incomplete | None = None, w: Incomplete | None = None, len: Incomplete | None = None) -> None: ...

class DashStop(Serialisable):
    tagname: str
    namespace: Incomplete
    d: Incomplete
    length: Incomplete
    sp: Incomplete
    space: Incomplete
    def __init__(self, d: int = 0, sp: int = 0) -> None: ...

class DashStopList(Serialisable):
    ds: Incomplete
    def __init__(self, ds: Incomplete | None = None) -> None: ...

class LineProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    w: Incomplete
    width: Incomplete
    cap: NoneSet(values=(["rnd", "sq", "flat"]))
    cmpd: NoneSet(values=(["sng", "dbl", "thickThin", "thinThick", "tri"]))
    algn: NoneSet(values=(["ctr", "in"]))
    noFill: Incomplete
    solidFill: Incomplete
    gradFill: Typed[GradientFillProperties, Literal[True]]
    pattFill: Typed[PatternFillProperties, Literal[True]]
    prstDash: Incomplete
    dashStyle: Incomplete
    custDash: Typed[DashStop, Literal[True]]
    round: Incomplete
    bevel: Incomplete
    miter: Incomplete
    headEnd: Typed[LineEndProperties, Literal[True]]
    tailEnd: Typed[LineEndProperties, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        w: Incomplete | None = None,
        cap: Incomplete | None = None,
        cmpd: Incomplete | None = None,
        algn: Incomplete | None = None,
        noFill: Incomplete | None = None,
        solidFill: Incomplete | None = None,
        gradFill: GradientFillProperties | None = None,
        pattFill: PatternFillProperties | None = None,
        prstDash: Incomplete | None = None,
        custDash: DashStop | None = None,
        round: Incomplete | None = None,
        bevel: Incomplete | None = None,
        miter: Incomplete | None = None,
        headEnd: LineEndProperties | None = None,
        tailEnd: LineEndProperties | None = None,
        extLst: Unused = None,
    ) -> None: ...
