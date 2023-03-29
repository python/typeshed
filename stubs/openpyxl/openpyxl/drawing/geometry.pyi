from _typeshed import Incomplete, Unused
from typing_extensions import Literal

from openpyxl.descriptors.base import NoneSet, Set, Typed
from openpyxl.descriptors.excel import Coordinate, ExtensionList, Percentage
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.styles.colors import Color

class Point2D(Serialisable):
    tagname: str
    namespace: Incomplete
    x: Incomplete
    y: Incomplete
    def __init__(self, x: Incomplete | None = None, y: Incomplete | None = None) -> None: ...

class PositiveSize2D(Serialisable):
    tagname: str
    namespace: Incomplete
    cx: Incomplete
    width: Incomplete
    cy: Incomplete
    height: Incomplete
    def __init__(self, cx: Incomplete | None = None, cy: Incomplete | None = None) -> None: ...

class Transform2D(Serialisable):
    tagname: str
    namespace: Incomplete
    rot: Incomplete
    flipH: Incomplete
    flipV: Incomplete
    off: Typed[Point2D, Literal[True]]
    ext: Typed[PositiveSize2D, Literal[True]]
    chOff: Typed[Point2D, Literal[True]]
    chExt: Typed[PositiveSize2D, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        rot: Incomplete | None = None,
        flipH: Incomplete | None = None,
        flipV: Incomplete | None = None,
        off: Point2D | None = None,
        ext: PositiveSize2D | None = None,
        chOff: Point2D | None = None,
        chExt: PositiveSize2D | None = None,
    ) -> None: ...

class GroupTransform2D(Serialisable):
    tagname: str
    namespace: Incomplete
    rot: Incomplete
    flipH: Incomplete
    flipV: Incomplete
    off = Typed(expected_type=Point2D, allow_none=True)
    ext = Typed(expected_type=PositiveSize2D, allow_none=True)
    chOff = Typed(expected_type=Point2D, allow_none=True)
    chExt = Typed(expected_type=PositiveSize2D, allow_none=True)
    __elements__: Incomplete
    def __init__(
        self,
        rot: int = 0,
        flipH: Incomplete | None = None,
        flipV: Incomplete | None = None,
        off: Point2D | None = None,
        ext: PositiveSize2D | None = None,
        chOff: Point2D | None = None,
        chExt: PositiveSize2D | None = None,
    ) -> None: ...

class SphereCoords(Serialisable):
    tagname: str
    lat: Incomplete
    lon: Incomplete
    rev: Incomplete
    def __init__(self, lat: Incomplete | None = None, lon: Incomplete | None = None, rev: Incomplete | None = None) -> None: ...

class Camera(Serialisable):
    tagname: str
    prst: Set(
        values=[
            "legacyObliqueTopLeft",
            "legacyObliqueTop",
            "legacyObliqueTopRight",
            "legacyObliqueLeft",
            "legacyObliqueFront",
            "legacyObliqueRight",
            "legacyObliqueBottomLeft",
            "legacyObliqueBottom",
            "legacyObliqueBottomRight",
            "legacyPerspectiveTopLeft",
            "legacyPerspectiveTop",
            "legacyPerspectiveTopRight",
            "legacyPerspectiveLeft",
            "legacyPerspectiveFront",
            "legacyPerspectiveRight",
            "legacyPerspectiveBottomLeft",
            "legacyPerspectiveBottom",
            "legacyPerspectiveBottomRight",
            "orthographicFront",
            "isometricTopUp",
            "isometricTopDown",
            "isometricBottomUp",
            "isometricBottomDown",
            "isometricLeftUp",
            "isometricLeftDown",
            "isometricRightUp",
            "isometricRightDown",
            "isometricOffAxis1Left",
            "isometricOffAxis1Right",
            "isometricOffAxis1Top",
            "isometricOffAxis2Left",
            "isometricOffAxis2Right",
            "isometricOffAxis2Top",
            "isometricOffAxis3Left",
            "isometricOffAxis3Right",
            "isometricOffAxis3Bottom",
            "isometricOffAxis4Left",
            "isometricOffAxis4Right",
            "isometricOffAxis4Bottom",
            "obliqueTopLeft",
            "obliqueTop",
            "obliqueTopRight",
            "obliqueLeft",
            "obliqueRight",
            "obliqueBottomLeft",
            "obliqueBottom",
            "obliqueBottomRight",
            "perspectiveFront",
            "perspectiveLeft",
            "perspectiveRight",
            "perspectiveAbove",
            "perspectiveBelow",
            "perspectiveAboveLeftFacing",
            "perspectiveAboveRightFacing",
            "perspectiveContrastingLeftFacing",
            "perspectiveContrastingRightFacing",
            "perspectiveHeroicLeftFacing",
            "perspectiveHeroicRightFacing",
            "perspectiveHeroicExtremeLeftFacing",
            "perspectiveHeroicExtremeRightFacing",
            "perspectiveRelaxed",
            "perspectiveRelaxedModerately",
        ]
    )
    fov: Incomplete
    zoom: Typed[Percentage, Literal[True]]
    rot: Typed[SphereCoords, Literal[True]]
    def __init__(
        self,
        prst: Incomplete | None = None,
        fov: Incomplete | None = None,
        zoom: Percentage | None = None,
        rot: SphereCoords | None = None,
    ) -> None: ...

class LightRig(Serialisable):
    tagname: str
    rig: Set(
        values=[
            "legacyFlat1",
            "legacyFlat2",
            "legacyFlat3",
            "legacyFlat4",
            "legacyNormal1",
            "legacyNormal2",
            "legacyNormal3",
            "legacyNormal4",
            "legacyHarsh1",
            "legacyHarsh2",
            "legacyHarsh3",
            "legacyHarsh4",
            "threePt",
            "balanced",
            "soft",
            "harsh",
            "flood",
            "contrasting",
            "morning",
            "sunrise",
            "sunset",
            "chilly",
            "freezing",
            "flat",
            "twoPt",
            "glow",
            "brightRoom",
        ]
    )
    dir: Set(values=(["tl", "t", "tr", "l", "r", "bl", "b", "br"]))
    rot: Typed[SphereCoords, Literal[True]]
    def __init__(self, rig: Incomplete | None = None, dir: Incomplete | None = None, rot: SphereCoords | None = None) -> None: ...

class Vector3D(Serialisable):
    tagname: str
    dx: Incomplete
    dy: Incomplete
    dz: Incomplete
    def __init__(self, dx: Incomplete | None = None, dy: Incomplete | None = None, dz: Incomplete | None = None) -> None: ...

class Point3D(Serialisable):
    tagname: str
    x: Incomplete
    y: Incomplete
    z: Incomplete
    def __init__(self, x: Incomplete | None = None, y: Incomplete | None = None, z: Incomplete | None = None) -> None: ...

class Backdrop(Serialisable):
    anchor: Typed[Point3D, Literal[False]]
    norm: Typed[Vector3D, Literal[False]]
    up: Typed[Vector3D, Literal[False]]
    extLst: Typed[ExtensionList, Literal[True]]
    def __init__(self, anchor: Point3D, norm: Vector3D, up: Vector3D, extLst: ExtensionList | None = None) -> None: ...

class Scene3D(Serialisable):
    camera: Typed[Camera, Literal[False]]
    lightRig: Typed[LightRig, Literal[False]]
    backdrop: Typed[Backdrop, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    def __init__(
        self, camera: Camera, lightRig: LightRig, backdrop: Backdrop | None = None, extLst: ExtensionList | None = None
    ) -> None: ...

class Bevel(Serialisable):
    tagname: str
    w: Incomplete
    h: Incomplete
    prst: NoneSet(
        values=[
            "relaxedInset",
            "circle",
            "slope",
            "cross",
            "angle",
            "softRound",
            "convex",
            "coolSlant",
            "divot",
            "riblet",
            "hardEdge",
            "artDeco",
        ]
    )
    def __init__(self, w: Incomplete | None = None, h: Incomplete | None = None, prst: Incomplete | None = None) -> None: ...

class Shape3D(Serialisable):
    namespace: Incomplete
    z: Typed[Coordinate, Literal[True]]
    extrusionH: Incomplete
    contourW: Incomplete
    prstMaterial: NoneSet(
        values=[
            "legacyMatte",
            "legacyPlastic",
            "legacyMetal",
            "legacyWireframe",
            "matte",
            "plastic",
            "metal",
            "warmMatte",
            "translucentPowder",
            "powder",
            "dkEdge",
            "softEdge",
            "clear",
            "flat",
            "softmetal",
        ]
    )
    bevelT: Typed[Bevel, Literal[True]]
    bevelB: Typed[Bevel, Literal[True]]
    extrusionClr: Typed[Color, Literal[True]]
    contourClr: Typed[Color, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    def __init__(
        self,
        z: Coordinate | None = None,
        extrusionH: Incomplete | None = None,
        contourW: Incomplete | None = None,
        prstMaterial: Incomplete | None = None,
        bevelT: Bevel | None = None,
        bevelB: Bevel | None = None,
        extrusionClr: Color | None = None,
        contourClr: Color | None = None,
        extLst: ExtensionList | None = None,
    ) -> None: ...

class Path2D(Serialisable):
    w: Incomplete
    h: Incomplete
    fill: NoneSet(values=(["norm", "lighten", "lightenLess", "darken", "darkenLess"]))
    stroke: Incomplete
    extrusionOk: Incomplete
    def __init__(
        self,
        w: Incomplete | None = None,
        h: Incomplete | None = None,
        fill: Incomplete | None = None,
        stroke: Incomplete | None = None,
        extrusionOk: Incomplete | None = None,
    ) -> None: ...

class Path2DList(Serialisable):
    path: Typed[Path2D, Literal[True]]
    def __init__(self, path: Path2D | None = None) -> None: ...

class GeomRect(Serialisable):
    l: Incomplete
    t: Incomplete
    r: Incomplete
    b: Incomplete
    def __init__(
        self, l: Incomplete | None = None, t: Incomplete | None = None, r: Incomplete | None = None, b: Incomplete | None = None
    ) -> None: ...

class AdjPoint2D(Serialisable):
    x: Incomplete
    y: Incomplete
    def __init__(self, x: Incomplete | None = None, y: Incomplete | None = None) -> None: ...

class ConnectionSite(Serialisable):
    ang: Incomplete
    pos: Typed[AdjPoint2D, Literal[False]]
    def __init__(self, ang: Incomplete | None, pos: AdjPoint2D) -> None: ...

class ConnectionSiteList(Serialisable):
    cxn: Typed[ConnectionSite, Literal[True]]
    def __init__(self, cxn: ConnectionSite | None = None) -> None: ...

class AdjustHandleList(Serialisable): ...

class GeomGuide(Serialisable):
    name: Incomplete
    fmla: Incomplete
    def __init__(self, name: str | None = None, fmla: Incomplete | None = None) -> None: ...

class GeomGuideList(Serialisable):
    gd: Typed[GeomGuide, Literal[True]]
    def __init__(self, gd: GeomGuide | None = None) -> None: ...

class CustomGeometry2D(Serialisable):
    avLst: Typed[GeomGuideList, Literal[True]]
    gdLst: Typed[GeomGuideList, Literal[True]]
    ahLst: Typed[AdjustHandleList, Literal[True]]
    cxnLst: Typed[ConnectionSiteList, Literal[True]]
    pathLst: Typed[Path2DList, Literal[False]]
    rect: GeomRect | None
    def __init__(
        self,
        avLst: GeomGuideList | None,
        gdLst: GeomGuideList | None,
        ahLst: AdjustHandleList | None,
        cxnLst: ConnectionSiteList | None,
        rect: Unused,
        pathLst: Path2DList,
    ) -> None: ...

class PresetGeometry2D(Serialisable):
    namespace: Incomplete
    prst: Set(
        values=(
            [
                "line",
                "lineInv",
                "triangle",
                "rtTriangle",
                "rect",
                "diamond",
                "parallelogram",
                "trapezoid",
                "nonIsoscelesTrapezoid",
                "pentagon",
                "hexagon",
                "heptagon",
                "octagon",
                "decagon",
                "dodecagon",
                "star4",
                "star5",
                "star6",
                "star7",
                "star8",
                "star10",
                "star12",
                "star16",
                "star24",
                "star32",
                "roundRect",
                "round1Rect",
                "round2SameRect",
                "round2DiagRect",
                "snipRoundRect",
                "snip1Rect",
                "snip2SameRect",
                "snip2DiagRect",
                "plaque",
                "ellipse",
                "teardrop",
                "homePlate",
                "chevron",
                "pieWedge",
                "pie",
                "blockArc",
                "donut",
                "noSmoking",
                "rightArrow",
                "leftArrow",
                "upArrow",
                "downArrow",
                "stripedRightArrow",
                "notchedRightArrow",
                "bentUpArrow",
                "leftRightArrow",
                "upDownArrow",
                "leftUpArrow",
                "leftRightUpArrow",
                "quadArrow",
                "leftArrowCallout",
                "rightArrowCallout",
                "upArrowCallout",
                "downArrowCallout",
                "leftRightArrowCallout",
                "upDownArrowCallout",
                "quadArrowCallout",
                "bentArrow",
                "uturnArrow",
                "circularArrow",
                "leftCircularArrow",
                "leftRightCircularArrow",
                "curvedRightArrow",
                "curvedLeftArrow",
                "curvedUpArrow",
                "curvedDownArrow",
                "swooshArrow",
                "cube",
                "can",
                "lightningBolt",
                "heart",
                "sun",
                "moon",
                "smileyFace",
                "irregularSeal1",
                "irregularSeal2",
                "foldedCorner",
                "bevel",
                "frame",
                "halfFrame",
                "corner",
                "diagStripe",
                "chord",
                "arc",
                "leftBracket",
                "rightBracket",
                "leftBrace",
                "rightBrace",
                "bracketPair",
                "bracePair",
                "straightConnector1",
                "bentConnector2",
                "bentConnector3",
                "bentConnector4",
                "bentConnector5",
                "curvedConnector2",
                "curvedConnector3",
                "curvedConnector4",
                "curvedConnector5",
                "callout1",
                "callout2",
                "callout3",
                "accentCallout1",
                "accentCallout2",
                "accentCallout3",
                "borderCallout1",
                "borderCallout2",
                "borderCallout3",
                "accentBorderCallout1",
                "accentBorderCallout2",
                "accentBorderCallout3",
                "wedgeRectCallout",
                "wedgeRoundRectCallout",
                "wedgeEllipseCallout",
                "cloudCallout",
                "cloud",
                "ribbon",
                "ribbon2",
                "ellipseRibbon",
                "ellipseRibbon2",
                "leftRightRibbon",
                "verticalScroll",
                "horizontalScroll",
                "wave",
                "doubleWave",
                "plus",
                "flowChartProcess",
                "flowChartDecision",
                "flowChartInputOutput",
                "flowChartPredefinedProcess",
                "flowChartInternalStorage",
                "flowChartDocument",
                "flowChartMultidocument",
                "flowChartTerminator",
                "flowChartPreparation",
                "flowChartManualInput",
                "flowChartManualOperation",
                "flowChartConnector",
                "flowChartPunchedCard",
                "flowChartPunchedTape",
                "flowChartSummingJunction",
                "flowChartOr",
                "flowChartCollate",
                "flowChartSort",
                "flowChartExtract",
                "flowChartMerge",
                "flowChartOfflineStorage",
                "flowChartOnlineStorage",
                "flowChartMagneticTape",
                "flowChartMagneticDisk",
                "flowChartMagneticDrum",
                "flowChartDisplay",
                "flowChartDelay",
                "flowChartAlternateProcess",
                "flowChartOffpageConnector",
                "actionButtonBlank",
                "actionButtonHome",
                "actionButtonHelp",
                "actionButtonInformation",
                "actionButtonForwardNext",
                "actionButtonBackPrevious",
                "actionButtonEnd",
                "actionButtonBeginning",
                "actionButtonReturn",
                "actionButtonDocument",
                "actionButtonSound",
                "actionButtonMovie",
                "gear6",
                "gear9",
                "funnel",
                "mathPlus",
                "mathMinus",
                "mathMultiply",
                "mathDivide",
                "mathEqual",
                "mathNotEqual",
                "cornerTabs",
                "squareTabs",
                "plaqueTabs",
                "chartX",
                "chartStar",
                "chartPlus",
            ]
        )
    )
    avLst: Typed[GeomGuideList, Literal[True]]
    def __init__(self, prst: Incomplete | None = None, avLst: GeomGuideList | None = None) -> None: ...

class FontReference(Serialisable):
    idx: NoneSet(values=(["major", "minor"]))
    def __init__(self, idx: Incomplete | None = None) -> None: ...

class StyleMatrixReference(Serialisable):
    idx: Incomplete
    def __init__(self, idx: Incomplete | None = None) -> None: ...

class ShapeStyle(Serialisable):
    lnRef: Typed[StyleMatrixReference, Literal[False]]
    fillRef: Typed[StyleMatrixReference, Literal[False]]
    effectRef: Typed[StyleMatrixReference, Literal[False]]
    fontRef: Typed[FontReference, Literal[False]]
    def __init__(
        self, lnRef: StyleMatrixReference, fillRef: StyleMatrixReference, effectRef: StyleMatrixReference, fontRef: FontReference
    ) -> None: ...
