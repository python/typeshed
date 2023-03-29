from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import NoneSet, Typed
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.drawing.connector import Shape
from openpyxl.drawing.graphic import GraphicFrame, GroupShape
from openpyxl.drawing.picture import PictureFrame
from openpyxl.drawing.xdr import XDRPoint2D, XDRPositiveSize2D

class AnchorClientData(Serialisable):
    fLocksWithSheet: Incomplete
    fPrintsWithSheet: Incomplete
    def __init__(self, fLocksWithSheet: Incomplete | None = None, fPrintsWithSheet: Incomplete | None = None) -> None: ...

class AnchorMarker(Serialisable):
    tagname: str
    col: Incomplete
    colOff: Incomplete
    row: Incomplete
    rowOff: Incomplete
    def __init__(self, col: int = 0, colOff: int = 0, row: int = 0, rowOff: int = 0) -> None: ...

class _AnchorBase(Serialisable):
    sp: Typed[Shape, Literal[True]]
    shape: Incomplete
    grpSp: Typed[GroupShape, Literal[True]]
    groupShape: Incomplete
    graphicFrame: Typed[GraphicFrame, Literal[True]]
    cxnSp: Typed[Shape, Literal[True]]
    connectionShape: Incomplete
    pic: Typed[PictureFrame, Literal[True]]
    contentPart: Incomplete
    clientData: Typed[AnchorClientData, Literal[False]]
    __elements__: Incomplete
    def __init__(
        self,
        clientData: AnchorClientData | None = None,
        sp: Shape | None = None,
        grpSp: GroupShape | None = None,
        graphicFrame: GraphicFrame | None = None,
        cxnSp: Shape | None = None,
        pic: PictureFrame | None = None,
        contentPart: Incomplete | None = None,
    ) -> None: ...

class AbsoluteAnchor(_AnchorBase):
    tagname: str
    pos: Typed[XDRPoint2D, Literal[False]]
    ext: Typed[XDRPositiveSize2D, Literal[False]]
    sp: Incomplete
    grpSp: Incomplete
    graphicFrame: Incomplete
    cxnSp: Incomplete
    pic: Incomplete
    contentPart: Incomplete
    clientData: Incomplete
    __elements__: Incomplete
    def __init__(self, pos: XDRPoint2D | None = None, ext: XDRPositiveSize2D | None = None, **kw) -> None: ...

class OneCellAnchor(_AnchorBase):
    tagname: str
    ext: Typed[XDRPositiveSize2D, Literal[False]]
    sp: Incomplete
    grpSp: Incomplete
    graphicFrame: Incomplete
    cxnSp: Incomplete
    pic: Incomplete
    contentPart: Incomplete
    clientData: Incomplete
    __elements__: Incomplete
    def __init__(self, _from: AnchorMarker | None = None, ext: XDRPositiveSize2D | None = None, **kw) -> None: ...

class TwoCellAnchor(_AnchorBase):
    tagname: str
    editAs: NoneSet(values=(["twoCell", "oneCell", "absolute"]))
    to: Typed[AnchorMarker, Literal[False]]
    sp: Incomplete
    grpSp: Incomplete
    graphicFrame: Incomplete
    cxnSp: Incomplete
    pic: Incomplete
    contentPart: Incomplete
    clientData: Incomplete
    __elements__: Incomplete
    def __init__(
        self, editAs: Incomplete | None = None, _from: AnchorMarker | None = None, to: AnchorMarker | None = None, **kw
    ) -> None: ...

class SpreadsheetDrawing(Serialisable):
    tagname: str
    mime_type: str
    PartName: str
    twoCellAnchor: Incomplete
    oneCellAnchor: Incomplete
    absoluteAnchor: Incomplete
    __elements__: Incomplete
    charts: Incomplete
    images: Incomplete
    def __init__(self, twoCellAnchor=(), oneCellAnchor=(), absoluteAnchor=()) -> None: ...
    def __hash__(self) -> int: ...
    def __bool__(self) -> bool: ...
    @property
    def path(self): ...
