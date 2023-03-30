from _typeshed import Incomplete, Unused
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import NoneSet, Typed
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.drawing.geometry import GroupTransform2D, Scene3D
from openpyxl.drawing.text import Hyperlink

_GroupShapePropertiesBwMode: TypeAlias = Literal[
    "clr", "auto", "gray", "ltGray", "invGray", "grayWhite", "blackGray", "blackWhite", "black", "white", "hidden"
]

class GroupShapeProperties(Serialisable):
    tagname: str
    bwMode: NoneSet[_GroupShapePropertiesBwMode]
    xfrm: Typed[GroupTransform2D, Literal[True]]
    scene3d: Typed[Scene3D, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    def __init__(
        self,
        bwMode: _GroupShapePropertiesBwMode | Literal["none"] | None = None,
        xfrm: GroupTransform2D | None = None,
        scene3d: Scene3D | None = None,
        extLst: ExtensionList | None = None,
    ) -> None: ...

class GroupLocking(Serialisable):
    tagname: str
    namespace: Incomplete
    noGrp: Incomplete
    noUngrp: Incomplete
    noSelect: Incomplete
    noRot: Incomplete
    noChangeAspect: Incomplete
    noMove: Incomplete
    noResize: Incomplete
    noChangeArrowheads: Incomplete
    noEditPoints: Incomplete
    noAdjustHandles: Incomplete
    noChangeShapeType: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        noGrp: Incomplete | None = None,
        noUngrp: Incomplete | None = None,
        noSelect: Incomplete | None = None,
        noRot: Incomplete | None = None,
        noChangeAspect: Incomplete | None = None,
        noChangeArrowheads: Incomplete | None = None,
        noMove: Incomplete | None = None,
        noResize: Incomplete | None = None,
        noEditPoints: Incomplete | None = None,
        noAdjustHandles: Incomplete | None = None,
        noChangeShapeType: Incomplete | None = None,
        extLst: Unused = None,
    ) -> None: ...

class NonVisualGroupDrawingShapeProps(Serialisable):
    tagname: str
    grpSpLocks: Typed[GroupLocking, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(self, grpSpLocks: Incomplete | None = None, extLst: Unused = None) -> None: ...

class NonVisualDrawingShapeProps(Serialisable):
    tagname: str
    spLocks: Typed[GroupLocking, Literal[True]]
    txBax: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    txBox: Incomplete
    def __init__(self, spLocks: Incomplete | None = None, txBox: Incomplete | None = None, extLst: Unused = None) -> None: ...

class NonVisualDrawingProps(Serialisable):
    tagname: str
    id: Incomplete
    name: Incomplete
    descr: Incomplete
    hidden: Incomplete
    title: Incomplete
    hlinkClick: Typed[Hyperlink, Literal[True]]
    hlinkHover: Typed[Hyperlink, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        id: Incomplete | None = None,
        name: Incomplete | None = None,
        descr: Incomplete | None = None,
        hidden: Incomplete | None = None,
        title: Incomplete | None = None,
        hlinkClick: Hyperlink | None = None,
        hlinkHover: Hyperlink | None = None,
        extLst: ExtensionList | None = None,
    ) -> None: ...

class NonVisualGroupShape(Serialisable):
    tagname: str
    cNvPr: Typed[NonVisualDrawingProps, Literal[False]]
    cNvGrpSpPr: Typed[NonVisualGroupDrawingShapeProps, Literal[False]]
    __elements__: Incomplete
    def __init__(self, cNvPr: NonVisualDrawingProps, cNvGrpSpPr: NonVisualGroupDrawingShapeProps) -> None: ...
