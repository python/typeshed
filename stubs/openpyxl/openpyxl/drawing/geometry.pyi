from _typeshed import Incomplete, Unused
from typing_extensions import Literal

from openpyxl.descriptors.base import Typed
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
    prst: Incomplete
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
    rig: Incomplete
    dir: Incomplete
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
    prst: Incomplete
    def __init__(self, w: Incomplete | None = None, h: Incomplete | None = None, prst: Incomplete | None = None) -> None: ...

class Shape3D(Serialisable):
    namespace: Incomplete
    z: Typed[Coordinate, Literal[True]]
    extrusionH: Incomplete
    contourW: Incomplete
    prstMaterial: Incomplete
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
    fill: Incomplete
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
    def __init__(self, name: Incomplete | None = None, fmla: Incomplete | None = None) -> None: ...

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
    prst: Incomplete
    avLst: Typed[GeomGuideList, Literal[True]]
    def __init__(self, prst: Incomplete | None = None, avLst: GeomGuideList | None = None) -> None: ...

class FontReference(Serialisable):
    idx: Incomplete
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
