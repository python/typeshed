from _typeshed import Incomplete, Unused
from typing_extensions import Literal

from openpyxl.descriptors.base import NoneSet, Typed
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.drawing.fill import GradientFillProperties, PatternFillProperties
from openpyxl.drawing.geometry import CustomGeometry2D, PresetGeometry2D, Scene3D, Shape3D, Transform2D
from openpyxl.drawing.line import LineProperties

class GraphicalProperties(Serialisable):
    tagname: str
    bwMode: NoneSet(
        values=(["clr", "auto", "gray", "ltGray", "invGray", "grayWhite", "blackGray", "blackWhite", "black", "white", "hidden"])
    )
    xfrm: Typed[Transform2D, Literal[True]]
    transform: Incomplete
    custGeom: Typed[CustomGeometry2D, Literal[True]]
    prstGeom: Typed[PresetGeometry2D, Literal[True]]
    noFill: Incomplete
    solidFill: Incomplete
    gradFill: Typed[GradientFillProperties, Literal[True]]
    pattFill: Typed[PatternFillProperties, Literal[True]]
    ln: Typed[LineProperties, Literal[True]]
    line: Incomplete
    scene3d: Typed[Scene3D, Literal[True]]
    sp3d: Typed[Shape3D, Literal[True]]
    shape3D: Incomplete
    extLst: Typed[Incomplete, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        bwMode: Incomplete | None = None,
        xfrm: Transform2D | None = None,
        noFill: Incomplete | None = None,
        solidFill: Incomplete | None = None,
        gradFill: GradientFillProperties | None = None,
        pattFill: PatternFillProperties | None = None,
        ln: Incomplete | None = None,
        scene3d: Scene3D | None = None,
        custGeom: CustomGeometry2D | None = None,
        prstGeom: PresetGeometry2D | None = None,
        sp3d: Shape3D | None = None,
        extLst: Unused = None,
    ) -> None: ...
