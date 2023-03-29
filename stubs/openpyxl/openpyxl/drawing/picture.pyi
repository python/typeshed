from _typeshed import Incomplete, Unused
from typing_extensions import Literal

from openpyxl.chart.shapes import GraphicalProperties
from openpyxl.descriptors.base import Typed
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.drawing.fill import BlipFillProperties
from openpyxl.drawing.geometry import ShapeStyle
from openpyxl.drawing.properties import NonVisualDrawingProps

class PictureLocking(Serialisable):
    tagname: str
    namespace: Incomplete
    noCrop: Incomplete
    noGrp: Incomplete
    noSelect: Incomplete
    noRot: Incomplete
    noChangeAspect: Incomplete
    noMove: Incomplete
    noResize: Incomplete
    noEditPoints: Incomplete
    noAdjustHandles: Incomplete
    noChangeArrowheads: Incomplete
    noChangeShapeType: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        noCrop: Incomplete | None = None,
        noGrp: Incomplete | None = None,
        noSelect: Incomplete | None = None,
        noRot: Incomplete | None = None,
        noChangeAspect: Incomplete | None = None,
        noMove: Incomplete | None = None,
        noResize: Incomplete | None = None,
        noEditPoints: Incomplete | None = None,
        noAdjustHandles: Incomplete | None = None,
        noChangeArrowheads: Incomplete | None = None,
        noChangeShapeType: Incomplete | None = None,
        extLst: Unused = None,
    ) -> None: ...

class NonVisualPictureProperties(Serialisable):
    tagname: str
    preferRelativeResize: Incomplete
    picLocks: Typed[PictureLocking, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self, preferRelativeResize: Incomplete | None = None, picLocks: Incomplete | None = None, extLst: Unused = None
    ) -> None: ...

class PictureNonVisual(Serialisable):
    tagname: str
    cNvPr: Typed[NonVisualDrawingProps, Literal[False]]
    cNvPicPr: Typed[NonVisualPictureProperties, Literal[False]]
    __elements__: Incomplete
    def __init__(
        self, cNvPr: NonVisualDrawingProps | None = None, cNvPicPr: NonVisualPictureProperties | None = None
    ) -> None: ...

class PictureFrame(Serialisable):
    tagname: str
    macro: Incomplete
    fPublished: Incomplete
    nvPicPr: Typed[PictureNonVisual, Literal[False]]
    blipFill: Typed[BlipFillProperties, Literal[False]]
    spPr: Typed[GraphicalProperties, Literal[False]]
    graphicalProperties: Incomplete
    style: Typed[ShapeStyle, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        macro: Incomplete | None = None,
        fPublished: Incomplete | None = None,
        nvPicPr: PictureNonVisual | None = None,
        blipFill: BlipFillProperties | None = None,
        spPr: GraphicalProperties | None = None,
        style: ShapeStyle | None = None,
    ) -> None: ...
