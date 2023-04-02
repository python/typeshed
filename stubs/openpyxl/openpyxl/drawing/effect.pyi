from _typeshed import Incomplete
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import Bool, Float, Set, String, Typed, _ConvertibleToBool, _ConvertibleToFloat
from openpyxl.descriptors.serialisable import Serialisable

from .colors import ColorChoice

_FillOverlayEffectBlend: TypeAlias = Literal["over", "mult", "screen", "darken", "lighten"]
_EffectContainerType: TypeAlias = Literal["sib", "tree"]
_Algn: TypeAlias = Literal["tl", "t", "tr", "l", "ctr", "r", "bl", "b", "br"]
_PresetShadowEffectPrst: TypeAlias = Literal[
    "shdw1",
    "shdw2",
    "shdw3",
    "shdw4",
    "shdw5",
    "shdw6",
    "shdw7",
    "shdw8",
    "shdw9",
    "shdw10",
    "shdw11",
    "shdw12",
    "shdw13",
    "shdw14",
    "shdw15",
    "shdw16",
    "shdw17",
    "shdw18",
    "shdw19",
    "shdw20",
]

class TintEffect(Serialisable):
    tagname: str
    hue: Incomplete
    amt: Incomplete
    def __init__(self, hue: int = 0, amt: int = 0) -> None: ...

class LuminanceEffect(Serialisable):
    tagname: str
    bright: Incomplete
    contrast: Incomplete
    def __init__(self, bright: int = 0, contrast: int = 0) -> None: ...

class HSLEffect(Serialisable):
    hue: Incomplete
    sat: Incomplete
    lum: Incomplete
    def __init__(self, hue: Incomplete | None = None, sat: Incomplete | None = None, lum: Incomplete | None = None) -> None: ...

class GrayscaleEffect(Serialisable):
    tagname: str

class FillOverlayEffect(Serialisable):
    blend: Set[_FillOverlayEffectBlend]
    def __init__(self, blend: _FillOverlayEffectBlend) -> None: ...

class DuotoneEffect(Serialisable): ...
class ColorReplaceEffect(Serialisable): ...
class Color(Serialisable): ...

class ColorChangeEffect(Serialisable):
    useA: Bool[Literal[True]]
    clrFrom: Typed[Color, Literal[False]]
    clrTo: Typed[Color, Literal[False]]
    def __init__(self, useA: _ConvertibleToBool | None, clrFrom: Color, clrTo: Color) -> None: ...

class BlurEffect(Serialisable):
    rad: Float[Literal[False]]
    grow: Bool[Literal[True]]
    def __init__(self, rad: _ConvertibleToFloat, grow: _ConvertibleToBool | None = None) -> None: ...

class BiLevelEffect(Serialisable):
    thresh: Incomplete
    def __init__(self, thresh: Incomplete | None = None) -> None: ...

class AlphaReplaceEffect(Serialisable):
    a: Incomplete
    def __init__(self, a: Incomplete | None = None) -> None: ...

class AlphaModulateFixedEffect(Serialisable):
    amt: Incomplete
    def __init__(self, amt: Incomplete | None = None) -> None: ...

class EffectContainer(Serialisable):
    type: Set[_EffectContainerType]
    name: String[Literal[True]]
    def __init__(self, type: _EffectContainerType, name: str | None = None) -> None: ...

class AlphaModulateEffect(Serialisable):
    cont: Typed[EffectContainer, Literal[False]]
    def __init__(self, cont: EffectContainer) -> None: ...

class AlphaInverseEffect(Serialisable): ...
class AlphaFloorEffect(Serialisable): ...
class AlphaCeilingEffect(Serialisable): ...

class AlphaBiLevelEffect(Serialisable):
    thresh: Incomplete
    def __init__(self, thresh: Incomplete | None = None) -> None: ...

class GlowEffect(ColorChoice):
    rad: Float[Literal[False]]
    scrgbClr: Incomplete
    srgbClr: Incomplete
    hslClr: Incomplete
    sysClr: Incomplete
    schemeClr: Incomplete
    prstClr: Incomplete
    __elements__: Incomplete
    def __init__(self, rad: _ConvertibleToFloat, **kw) -> None: ...

class InnerShadowEffect(ColorChoice):
    blurRad: Float[Literal[False]]
    dist: Float[Literal[False]]
    dir: Incomplete
    scrgbClr: Incomplete
    srgbClr: Incomplete
    hslClr: Incomplete
    sysClr: Incomplete
    schemeClr: Incomplete
    prstClr: Incomplete
    __elements__: Incomplete
    def __init__(self, blurRad: _ConvertibleToFloat, dist: _ConvertibleToFloat, dir: Incomplete | None = None, **kw) -> None: ...

class OuterShadow(ColorChoice):
    tagname: str
    blurRad: Float[Literal[True]]
    dist: Float[Literal[True]]
    dir: Incomplete
    sx: Incomplete
    sy: Incomplete
    kx: Incomplete
    ky: Incomplete
    algn: Set[_Algn]
    rotWithShape: Bool[Literal[True]]
    scrgbClr: Incomplete
    srgbClr: Incomplete
    hslClr: Incomplete
    sysClr: Incomplete
    schemeClr: Incomplete
    prstClr: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        blurRad: _ConvertibleToFloat | None,
        dist: _ConvertibleToFloat | None,
        dir: Incomplete | None,
        sx: Incomplete | None,
        sy: Incomplete | None,
        kx: Incomplete | None,
        ky: Incomplete | None,
        algn: _Algn,
        rotWithShape: _ConvertibleToBool | None = None,
        **kw,
    ) -> None: ...

class PresetShadowEffect(ColorChoice):
    prst: Set[_PresetShadowEffectPrst]
    dist: Float[Literal[False]]
    dir: Incomplete
    scrgbClr: Incomplete
    srgbClr: Incomplete
    hslClr: Incomplete
    sysClr: Incomplete
    schemeClr: Incomplete
    prstClr: Incomplete
    __elements__: Incomplete
    def __init__(self, prst: _PresetShadowEffectPrst, dist: _ConvertibleToFloat, dir: Incomplete | None = None, **kw) -> None: ...

class ReflectionEffect(Serialisable):
    blurRad: Float[Literal[False]]
    stA: Incomplete
    stPos: Incomplete
    endA: Incomplete
    endPos: Incomplete
    dist: Float[Literal[False]]
    dir: Incomplete
    fadeDir: Incomplete
    sx: Incomplete
    sy: Incomplete
    kx: Incomplete
    ky: Incomplete
    algn: Set[_Algn]
    rotWithShape: Bool[Literal[True]]
    def __init__(
        self,
        blurRad: _ConvertibleToFloat,
        stA: Incomplete | None,
        stPos: Incomplete | None,
        endA: Incomplete | None,
        endPos: Incomplete | None,
        dist: _ConvertibleToFloat,
        dir: Incomplete | None,
        fadeDir: Incomplete | None,
        sx: Incomplete | None,
        sy: Incomplete | None,
        kx: Incomplete | None,
        ky: Incomplete | None,
        algn: _Algn,
        rotWithShape: _ConvertibleToBool | None = None,
    ) -> None: ...

class SoftEdgesEffect(Serialisable):
    rad: Float[Literal[False]]
    def __init__(self, rad: _ConvertibleToFloat) -> None: ...

class EffectList(Serialisable):
    blur: Typed[BlurEffect, Literal[True]]
    fillOverlay: Typed[FillOverlayEffect, Literal[True]]
    glow: Typed[GlowEffect, Literal[True]]
    innerShdw: Typed[InnerShadowEffect, Literal[True]]
    outerShdw: Typed[OuterShadow, Literal[True]]
    prstShdw: Typed[PresetShadowEffect, Literal[True]]
    reflection: Typed[ReflectionEffect, Literal[True]]
    softEdge: Typed[SoftEdgesEffect, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        blur: BlurEffect | None = None,
        fillOverlay: FillOverlayEffect | None = None,
        glow: GlowEffect | None = None,
        innerShdw: InnerShadowEffect | None = None,
        outerShdw: OuterShadow | None = None,
        prstShdw: PresetShadowEffect | None = None,
        reflection: ReflectionEffect | None = None,
        softEdge: SoftEdgesEffect | None = None,
    ) -> None: ...
