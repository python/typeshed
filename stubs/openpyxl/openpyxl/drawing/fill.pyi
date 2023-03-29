from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import Typed
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.drawing.colors import ColorChoice, HSLColor, RGBPercent, SchemeColor, SystemColor
from openpyxl.drawing.effect import (
    AlphaBiLevelEffect,
    AlphaCeilingEffect,
    AlphaFloorEffect,
    AlphaInverseEffect,
    AlphaModulateEffect,
    AlphaModulateFixedEffect,
    AlphaReplaceEffect,
    BiLevelEffect,
    BlurEffect,
    ColorChangeEffect,
    ColorReplaceEffect,
    DuotoneEffect,
    FillOverlayEffect,
    GrayscaleEffect,
    HSLEffect,
    LuminanceEffect,
    TintEffect,
)

class PatternFillProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    prst: Incomplete
    preset: Incomplete
    fgClr: Typed[ColorChoice, Literal[True]]
    foreground: Incomplete
    bgClr: Typed[ColorChoice, Literal[True]]
    background: Incomplete
    __elements__: Incomplete
    def __init__(
        self, prst: Incomplete | None = None, fgClr: ColorChoice | None = None, bgClr: ColorChoice | None = None
    ) -> None: ...

class RelativeRect(Serialisable):
    tagname: str
    namespace: Incomplete
    l: Incomplete
    left: Incomplete
    t: Incomplete
    top: Incomplete
    r: Incomplete
    right: Incomplete
    b: Incomplete
    bottom: Incomplete
    def __init__(
        self, l: Incomplete | None = None, t: Incomplete | None = None, r: Incomplete | None = None, b: Incomplete | None = None
    ) -> None: ...

class StretchInfoProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    fillRect: Typed[RelativeRect, Literal[True]]
    def __init__(self, fillRect: RelativeRect = ...) -> None: ...

class GradientStop(Serialisable):
    tagname: str
    namespace: Incomplete
    pos: Incomplete
    scrgbClr: Typed[RGBPercent, Literal[True]]
    RGBPercent: Incomplete
    srgbClr: Incomplete
    RGB: Incomplete
    hslClr: Typed[HSLColor, Literal[True]]
    sysClr: Typed[SystemColor, Literal[True]]
    schemeClr: Typed[SchemeColor, Literal[True]]
    prstClr: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        pos: Incomplete | None = None,
        scrgbClr: RGBPercent | None = None,
        srgbClr: Incomplete | None = None,
        hslClr: HSLColor | None = None,
        sysClr: SystemColor | None = None,
        schemeClr: SchemeColor | None = None,
        prstClr: Incomplete | None = None,
    ) -> None: ...

class LinearShadeProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    ang: Incomplete
    scaled: Incomplete
    def __init__(self, ang: Incomplete | None = None, scaled: Incomplete | None = None) -> None: ...

class PathShadeProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    path: Incomplete
    fillToRect: Typed[RelativeRect, Literal[True]]
    def __init__(self, path: Incomplete | None = None, fillToRect: RelativeRect | None = None) -> None: ...

class GradientFillProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    flip: Incomplete
    rotWithShape: Incomplete
    gsLst: Incomplete
    stop_list: Incomplete
    lin: Typed[LinearShadeProperties, Literal[True]]
    linear: Incomplete
    path: Typed[PathShadeProperties, Literal[True]]
    tileRect: Typed[RelativeRect, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        flip: Incomplete | None = None,
        rotWithShape: Incomplete | None = None,
        gsLst=(),
        lin: LinearShadeProperties | None = None,
        path: PathShadeProperties | None = None,
        tileRect: RelativeRect | None = None,
    ) -> None: ...

class SolidColorFillProperties(Serialisable):
    tagname: str
    scrgbClr: Typed[RGBPercent, Literal[True]]
    RGBPercent: Incomplete
    srgbClr: Incomplete
    RGB: Incomplete
    hslClr: Typed[HSLColor, Literal[True]]
    sysClr: Typed[SystemColor, Literal[True]]
    schemeClr: Typed[SchemeColor, Literal[True]]
    prstClr: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        scrgbClr: RGBPercent | None = None,
        srgbClr: Incomplete | None = None,
        hslClr: HSLColor | None = None,
        sysClr: SystemColor | None = None,
        schemeClr: SchemeColor | None = None,
        prstClr: Incomplete | None = None,
    ) -> None: ...

class Blip(Serialisable):
    tagname: str
    namespace: Incomplete
    cstate: Incomplete
    embed: Incomplete
    link: Incomplete
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
    alphaBiLevel: Typed[AlphaBiLevelEffect, Literal[True]]
    alphaCeiling: Typed[AlphaCeilingEffect, Literal[True]]
    alphaFloor: Typed[AlphaFloorEffect, Literal[True]]
    alphaInv: Typed[AlphaInverseEffect, Literal[True]]
    alphaMod: Typed[AlphaModulateEffect, Literal[True]]
    alphaModFix: Typed[AlphaModulateFixedEffect, Literal[True]]
    alphaRepl: Typed[AlphaReplaceEffect, Literal[True]]
    biLevel: Typed[BiLevelEffect, Literal[True]]
    blur: Typed[BlurEffect, Literal[True]]
    clrChange: Typed[ColorChangeEffect, Literal[True]]
    clrRepl: Typed[ColorReplaceEffect, Literal[True]]
    duotone: Typed[DuotoneEffect, Literal[True]]
    fillOverlay: Typed[FillOverlayEffect, Literal[True]]
    grayscl: Typed[GrayscaleEffect, Literal[True]]
    hsl: Typed[HSLEffect, Literal[True]]
    lum: Typed[LuminanceEffect, Literal[True]]
    tint: Typed[TintEffect, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        cstate: Incomplete | None = None,
        embed: Incomplete | None = None,
        link: Incomplete | None = None,
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
        extLst: ExtensionList | None = None,
        alphaBiLevel: AlphaBiLevelEffect | None = None,
        alphaCeiling: AlphaCeilingEffect | None = None,
        alphaFloor: AlphaFloorEffect | None = None,
        alphaInv: AlphaInverseEffect | None = None,
        alphaMod: AlphaModulateEffect | None = None,
        alphaModFix: AlphaModulateFixedEffect | None = None,
        alphaRepl: AlphaReplaceEffect | None = None,
        biLevel: BiLevelEffect | None = None,
        blur: BlurEffect | None = None,
        clrChange: ColorChangeEffect | None = None,
        clrRepl: ColorReplaceEffect | None = None,
        duotone: DuotoneEffect | None = None,
        fillOverlay: FillOverlayEffect | None = None,
        grayscl: GrayscaleEffect | None = None,
        hsl: HSLEffect | None = None,
        lum: LuminanceEffect | None = None,
        tint: TintEffect | None = None,
    ) -> None: ...

class TileInfoProperties(Serialisable):
    tx: Incomplete
    ty: Incomplete
    sx: Incomplete
    sy: Incomplete
    flip: Incomplete
    algn: Incomplete
    def __init__(
        self,
        tx: Incomplete | None = None,
        ty: Incomplete | None = None,
        sx: Incomplete | None = None,
        sy: Incomplete | None = None,
        flip: Incomplete | None = None,
        algn: Incomplete | None = None,
    ) -> None: ...

class BlipFillProperties(Serialisable):
    tagname: str
    dpi: Incomplete
    rotWithShape: Incomplete
    blip: Typed[Blip, Literal[True]]
    srcRect: Typed[RelativeRect, Literal[True]]
    tile: Typed[TileInfoProperties, Literal[True]]
    stretch: Typed[StretchInfoProperties, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        dpi: Incomplete | None = None,
        rotWithShape: Incomplete | None = None,
        blip: Blip | None = None,
        tile: TileInfoProperties | None = None,
        stretch: StretchInfoProperties = ...,
        srcRect: RelativeRect | None = None,
    ) -> None: ...
