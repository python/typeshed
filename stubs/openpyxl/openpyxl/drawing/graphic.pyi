from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import Typed
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.drawing.picture import PictureFrame
from openpyxl.drawing.properties import GroupShapeProperties, NonVisualGroupShape
from openpyxl.drawing.relation import ChartRelation
from openpyxl.drawing.xdr import XDRTransform2D

class GraphicFrameLocking(Serialisable):
    noGrp: Incomplete
    noDrilldown: Incomplete
    noSelect: Incomplete
    noChangeAspect: Incomplete
    noMove: Incomplete
    noResize: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    def __init__(
        self,
        noGrp: Incomplete | None = None,
        noDrilldown: Incomplete | None = None,
        noSelect: Incomplete | None = None,
        noChangeAspect: Incomplete | None = None,
        noMove: Incomplete | None = None,
        noResize: Incomplete | None = None,
        extLst: ExtensionList | None = None,
    ) -> None: ...

class NonVisualGraphicFrameProperties(Serialisable):
    tagname: str
    graphicFrameLocks: Typed[GraphicFrameLocking, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    def __init__(self, graphicFrameLocks: GraphicFrameLocking | None = None, extLst: ExtensionList | None = None) -> None: ...

class NonVisualGraphicFrame(Serialisable):
    tagname: str
    cNvPr: Typed[ExtensionList, Literal[False]]
    cNvGraphicFramePr: Typed[ExtensionList, Literal[False]]
    __elements__: Incomplete
    def __init__(self, cNvPr: Incomplete | None = None, cNvGraphicFramePr: Incomplete | None = None) -> None: ...

class GraphicData(Serialisable):
    tagname: str
    namespace: Incomplete
    uri: Incomplete
    chart: Typed[ChartRelation, Literal[True]]
    def __init__(self, uri: str = ..., chart: ChartRelation | None = None) -> None: ...

class GraphicObject(Serialisable):
    tagname: str
    namespace: Incomplete
    graphicData: Typed[GraphicData, Literal[False]]
    def __init__(self, graphicData: GraphicData | None = None) -> None: ...

class GraphicFrame(Serialisable):
    tagname: str
    nvGraphicFramePr: Typed[NonVisualGraphicFrame, Literal[False]]
    xfrm: Typed[XDRTransform2D, Literal[False]]
    graphic: Typed[GraphicObject, Literal[False]]
    macro: Incomplete
    fPublished: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        nvGraphicFramePr: NonVisualGraphicFrame | None = None,
        xfrm: XDRTransform2D | None = None,
        graphic: GraphicObject | None = None,
        macro: Incomplete | None = None,
        fPublished: Incomplete | None = None,
    ) -> None: ...

class GroupShape(Serialisable):
    nvGrpSpPr: Typed[NonVisualGroupShape, Literal[False]]
    nonVisualProperties: Incomplete
    grpSpPr: Typed[GroupShapeProperties, Literal[False]]
    visualProperties: Incomplete
    pic: Typed[PictureFrame, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self, nvGrpSpPr: NonVisualGroupShape, grpSpPr: GroupShapeProperties, pic: PictureFrame | None = None
    ) -> None: ...
