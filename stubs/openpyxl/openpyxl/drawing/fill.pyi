from _typeshed import Incomplete
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import Bool, MinMax, NoneSet, Set, Typed, _ConvertibleToBool, _ConvertibleToFloat
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

_PatternFillPropertiesPrst: TypeAlias = Literal[
    "pct5",
    "pct10",
    "pct20",
    "pct25",
    "pct30",
    "pct40",
    "pct50",
    "pct60",
    "pct70",
    "pct75",
    "pct80",
    "pct90",
    "horz",
    "vert",
    "ltHorz",
    "ltVert",
    "dkHorz",
    "dkVert",
    "narHorz",
    "narVert",
    "dashHorz",
    "dashVert",
    "cross",
    "dnDiag",
    "upDiag",
    "ltDnDiag",
    "ltUpDiag",
    "dkDnDiag",
    "dkUpDiag",
    "wdDnDiag",
    "wdUpDiag",
    "dashDnDiag",
    "dashUpDiag",
    "diagCross",
    "smCheck",
    "lgCheck",
    "smGrid",
    "lgGrid",
    "dotGrid",
    "smConfetti",
    "lgConfetti",
    "horzBrick",
    "diagBrick",
    "solidDmnd",
    "openDmnd",
    "dotDmnd",
    "plaid",
    "sphere",
    "weave",
    "divot",
    "shingle",
    "wave",
    "trellis",
    "zigZag",
]
_PropertiesFlip: TypeAlias = Literal["x", "y", "xy"]
_TileInfoPropertiesAlgn: TypeAlias = Literal["tl", "t", "tr", "l", "ctr", "r", "bl", "b", "br"]
_BlipCstate: TypeAlias = Literal["email", "screen", "print", "hqprint"]
_PathShadePropertiesPath: TypeAlias = Literal["shape", "circle", "rect"]

class PatternFillProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    prst: NoneSet[_PatternFillPropertiesPrst]
    preset: Incomplete
    fgClr: Typed[ColorChoice, Literal[True]]
    foreground: Incomplete
    bgClr: Typed[ColorChoice, Literal[True]]
    background: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        prst: _PatternFillPropertiesPrst | Literal["none"] | None = None,
        fgClr: ColorChoice | None = None,
        bgClr: ColorChoice | None = None,
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
    pos: MinMax[float, Literal[True]]
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
        pos: _ConvertibleToFloat | None = None,
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
    scaled: Bool[Literal[True]]
    def __init__(self, ang: Incomplete | None = None, scaled: _ConvertibleToBool | None = None) -> None: ...

class PathShadeProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    path: Set[_PathShadePropertiesPath]
    fillToRect: Typed[RelativeRect, Literal[True]]
    def __init__(self, path: _PathShadePropertiesPath, fillToRect: RelativeRect | None = None) -> None: ...

class GradientFillProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    flip: NoneSet[_PropertiesFlip]
    rotWithShape: Bool[Literal[True]]
    gsLst: Incomplete
    stop_list: Incomplete
    lin: Typed[LinearShadeProperties, Literal[True]]
    linear: Incomplete
    path: Typed[PathShadeProperties, Literal[True]]
    tileRect: Typed[RelativeRect, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        flip: _PropertiesFlip | Literal["none"] | None = None,
        rotWithShape: _ConvertibleToBool | None = None,
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
    cstate: NoneSet[_BlipCstate]
    embed: Incomplete
    link: Incomplete
    noGrp: Bool[Literal[True]]
    noSelect: Bool[Literal[True]]
    noRot: Bool[Literal[True]]
    noChangeAspect: Bool[Literal[True]]
    noMove: Bool[Literal[True]]
    noResize: Bool[Literal[True]]
    noEditPoints: Bool[Literal[True]]
    noAdjustHandles: Bool[Literal[True]]
    noChangeArrowheads: Bool[Literal[True]]
    noChangeShapeType: Bool[Literal[True]]
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
        cstate: _BlipCstate | Literal["none"] | None = None,
        embed: Incomplete | None = None,
        link: Incomplete | None = None,
        noGrp: _ConvertibleToBool | None = None,
        noSelect: _ConvertibleToBool | None = None,
        noRot: _ConvertibleToBool | None = None,
        noChangeAspect: _ConvertibleToBool | None = None,
        noMove: _ConvertibleToBool | None = None,
        noResize: _ConvertibleToBool | None = None,
        noEditPoints: _ConvertibleToBool | None = None,
        noAdjustHandles: _ConvertibleToBool | None = None,
        noChangeArrowheads: _ConvertibleToBool | None = None,
        noChangeShapeType: _ConvertibleToBool | None = None,
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
    flip: NoneSet[_PropertiesFlip]
    algn: Set[_TileInfoPropertiesAlgn]
    def __init__(
        self,
        tx: Incomplete | None,
        ty: Incomplete | None,
        sx: Incomplete | None,
        sy: Incomplete | None,
        flip: _PropertiesFlip | Literal["none"] | None,
        algn: _TileInfoPropertiesAlgn,
    ) -> None: ...

class BlipFillProperties(Serialisable):
    tagname: str
    dpi: Incomplete
    rotWithShape: Bool[Literal[True]]
    blip: Typed[Blip, Literal[True]]
    srcRect: Typed[RelativeRect, Literal[True]]
    tile: Typed[TileInfoProperties, Literal[True]]
    stretch: Typed[StretchInfoProperties, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        dpi: Incomplete | None = None,
        rotWithShape: _ConvertibleToBool | None = None,
        blip: Blip | None = None,
        tile: TileInfoProperties | None = None,
        stretch: StretchInfoProperties = ...,
        srcRect: RelativeRect | None = None,
    ) -> None: ...
