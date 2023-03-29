from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import Set, Typed
from openpyxl.descriptors.excel import Coordinate, ExtensionList
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.drawing.effect import Color, EffectContainer, EffectList
from openpyxl.drawing.fill import BlipFillProperties, GradientFillProperties, PatternFillProperties
from openpyxl.drawing.geometry import Scene3D
from openpyxl.drawing.line import LineProperties

class EmbeddedWAVAudioFile(Serialisable):  # type: ignore[misc]
    name: Incomplete
    def __init__(self, name: Incomplete | None = None) -> None: ...

class Hyperlink(Serialisable):
    tagname: str
    namespace: Incomplete
    invalidUrl: Incomplete
    action: Incomplete
    tgtFrame: Incomplete
    tooltip: Incomplete
    history: Incomplete
    highlightClick: Incomplete
    endSnd: Incomplete
    snd: Typed[EmbeddedWAVAudioFile, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    id: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        invalidUrl: Incomplete | None = None,
        action: Incomplete | None = None,
        tgtFrame: Incomplete | None = None,
        tooltip: Incomplete | None = None,
        history: Incomplete | None = None,
        highlightClick: Incomplete | None = None,
        endSnd: Incomplete | None = None,
        snd: EmbeddedWAVAudioFile | None = None,
        extLst: ExtensionList | None = None,
        id: Incomplete | None = None,
    ) -> None: ...

class Font(Serialisable):
    tagname: str
    namespace: Incomplete
    typeface: Incomplete
    panose: Incomplete
    pitchFamily: Incomplete
    charset: Incomplete
    def __init__(
        self,
        typeface: Incomplete | None = None,
        panose: Incomplete | None = None,
        pitchFamily: Incomplete | None = None,
        charset: Incomplete | None = None,
    ) -> None: ...

class CharacterProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    kumimoji: Incomplete
    lang: Incomplete
    altLang: Incomplete
    sz: Incomplete
    b: Incomplete
    i: Incomplete
    u: Incomplete
    strike: Incomplete
    kern: Incomplete
    cap: Incomplete
    spc: Incomplete
    normalizeH: Incomplete
    baseline: Incomplete
    noProof: Incomplete
    dirty: Incomplete
    err: Incomplete
    smtClean: Incomplete
    smtId: Incomplete
    bmk: Incomplete
    ln: Typed[LineProperties, Literal[True]]
    highlight: Typed[Color, Literal[True]]
    latin: Typed[Font, Literal[True]]
    ea: Typed[Font, Literal[True]]
    cs: Typed[Font, Literal[True]]
    sym: Typed[Font, Literal[True]]
    hlinkClick: Typed[Hyperlink, Literal[True]]
    hlinkMouseOver: Typed[Hyperlink, Literal[True]]
    rtl: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    noFill: Incomplete
    solidFill: Incomplete
    gradFill: Typed[GradientFillProperties, Literal[True]]
    blipFill: Typed[BlipFillProperties, Literal[True]]
    pattFill: Typed[PatternFillProperties, Literal[True]]
    grpFill: Incomplete
    effectLst: Typed[EffectList, Literal[True]]
    effectDag: Typed[EffectContainer, Literal[True]]
    uLnTx: Incomplete
    uLn: Typed[LineProperties, Literal[True]]
    uFillTx: Incomplete
    uFill: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        kumimoji: Incomplete | None = None,
        lang: Incomplete | None = None,
        altLang: Incomplete | None = None,
        sz: Incomplete | None = None,
        b: Incomplete | None = None,
        i: Incomplete | None = None,
        u: Incomplete | None = None,
        strike: Incomplete | None = None,
        kern: Incomplete | None = None,
        cap: Incomplete | None = None,
        spc: Incomplete | None = None,
        normalizeH: Incomplete | None = None,
        baseline: Incomplete | None = None,
        noProof: Incomplete | None = None,
        dirty: Incomplete | None = None,
        err: Incomplete | None = None,
        smtClean: Incomplete | None = None,
        smtId: Incomplete | None = None,
        bmk: Incomplete | None = None,
        ln: LineProperties | None = None,
        highlight: Color | None = None,
        latin: Font | None = None,
        ea: Font | None = None,
        cs: Font | None = None,
        sym: Font | None = None,
        hlinkClick: Hyperlink | None = None,
        hlinkMouseOver: Hyperlink | None = None,
        rtl: Incomplete | None = None,
        extLst: ExtensionList | None = None,
        noFill: Incomplete | None = None,
        solidFill: Incomplete | None = None,
        gradFill: GradientFillProperties | None = None,
        blipFill: BlipFillProperties | None = None,
        pattFill: PatternFillProperties | None = None,
        grpFill: Incomplete | None = None,
        effectLst: EffectList | None = None,
        effectDag: EffectContainer | None = None,
        uLnTx: Incomplete | None = None,
        uLn: LineProperties | None = None,
        uFillTx: Incomplete | None = None,
        uFill: Incomplete | None = None,
    ) -> None: ...

class TabStop(Serialisable):  # type: ignore[misc]
    pos: Typed[Coordinate, Literal[True]]
    algn: Typed[Set, Literal[False]]
    def __init__(self, pos: Coordinate | None = None, algn: Set | None = None) -> None: ...

class TabStopList(Serialisable):  # type: ignore[misc]
    tab: Typed[TabStop, Literal[True]]
    def __init__(self, tab: Incomplete | None = None) -> None: ...

class Spacing(Serialisable):
    spcPct: Incomplete
    spcPts: Incomplete
    __elements__: Incomplete
    def __init__(self, spcPct: Incomplete | None = None, spcPts: Incomplete | None = None) -> None: ...

class AutonumberBullet(Serialisable):
    type: Incomplete
    startAt: Incomplete
    def __init__(self, type: Incomplete | None = None, startAt: Incomplete | None = None) -> None: ...

class ParagraphProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    marL: Incomplete
    marR: Incomplete
    lvl: Incomplete
    indent: Incomplete
    algn: Incomplete
    defTabSz: Incomplete
    rtl: Incomplete
    eaLnBrk: Incomplete
    fontAlgn: Incomplete
    latinLnBrk: Incomplete
    hangingPunct: Incomplete
    lnSpc: Typed[Spacing, Literal[True]]
    spcBef: Typed[Spacing, Literal[True]]
    spcAft: Typed[Spacing, Literal[True]]
    tabLst: Typed[TabStopList, Literal[True]]
    defRPr: Typed[CharacterProperties, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    buClrTx: Incomplete
    buClr: Typed[Color, Literal[True]]
    buSzTx: Incomplete
    buSzPct: Incomplete
    buSzPts: Incomplete
    buFontTx: Incomplete
    buFont: Typed[Font, Literal[True]]
    buNone: Incomplete
    buAutoNum: Incomplete
    buChar: Incomplete
    buBlip: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        marL: Incomplete | None = None,
        marR: Incomplete | None = None,
        lvl: Incomplete | None = None,
        indent: Incomplete | None = None,
        algn: Incomplete | None = None,
        defTabSz: Incomplete | None = None,
        rtl: Incomplete | None = None,
        eaLnBrk: Incomplete | None = None,
        fontAlgn: Incomplete | None = None,
        latinLnBrk: Incomplete | None = None,
        hangingPunct: Incomplete | None = None,
        lnSpc: Spacing | None = None,
        spcBef: Spacing | None = None,
        spcAft: Spacing | None = None,
        tabLst: TabStopList | None = None,
        defRPr: CharacterProperties | None = None,
        extLst: ExtensionList | None = None,
        buClrTx: Incomplete | None = None,
        buClr: Color | None = None,
        buSzTx: Incomplete | None = None,
        buSzPct: Incomplete | None = None,
        buSzPts: Incomplete | None = None,
        buFontTx: Incomplete | None = None,
        buFont: Font | None = None,
        buNone: Incomplete | None = None,
        buAutoNum: Incomplete | None = None,
        buChar: Incomplete | None = None,
        buBlip: Incomplete | None = None,
    ) -> None: ...

class ListStyle(Serialisable):
    tagname: str
    namespace: Incomplete
    defPPr: Typed[ParagraphProperties, Literal[True]]
    lvl1pPr: Typed[ParagraphProperties, Literal[True]]
    lvl2pPr: Typed[ParagraphProperties, Literal[True]]
    lvl3pPr: Typed[ParagraphProperties, Literal[True]]
    lvl4pPr: Typed[ParagraphProperties, Literal[True]]
    lvl5pPr: Typed[ParagraphProperties, Literal[True]]
    lvl6pPr: Typed[ParagraphProperties, Literal[True]]
    lvl7pPr: Typed[ParagraphProperties, Literal[True]]
    lvl8pPr: Typed[ParagraphProperties, Literal[True]]
    lvl9pPr: Typed[ParagraphProperties, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        defPPr: ParagraphProperties | None = None,
        lvl1pPr: ParagraphProperties | None = None,
        lvl2pPr: ParagraphProperties | None = None,
        lvl3pPr: ParagraphProperties | None = None,
        lvl4pPr: ParagraphProperties | None = None,
        lvl5pPr: ParagraphProperties | None = None,
        lvl6pPr: ParagraphProperties | None = None,
        lvl7pPr: ParagraphProperties | None = None,
        lvl8pPr: ParagraphProperties | None = None,
        lvl9pPr: ParagraphProperties | None = None,
        extLst: ParagraphProperties | None = None,
    ) -> None: ...

class RegularTextRun(Serialisable):
    tagname: str
    namespace: Incomplete
    rPr: Typed[CharacterProperties, Literal[True]]
    properties: Incomplete
    t: Incomplete
    value: Incomplete
    __elements__: Incomplete
    def __init__(self, rPr: CharacterProperties | None = None, t: str = "") -> None: ...

class LineBreak(Serialisable):
    tagname: str
    namespace: Incomplete
    rPr: Typed[CharacterProperties, Literal[True]]
    __elements__: Incomplete
    def __init__(self, rPr: CharacterProperties | None = None) -> None: ...

class TextField(Serialisable):
    id: Incomplete
    type: Incomplete
    rPr: Typed[CharacterProperties, Literal[True]]
    pPr: Typed[CharacterProperties, Literal[True]]
    t: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        id: Incomplete | None = None,
        type: Incomplete | None = None,
        rPr: CharacterProperties | None = None,
        pPr: CharacterProperties | None = None,
        t: Incomplete | None = None,
    ) -> None: ...

class Paragraph(Serialisable):
    tagname: str
    namespace: Incomplete
    pPr: Typed[ParagraphProperties, Literal[True]]
    properties: Incomplete
    endParaRPr: Typed[CharacterProperties, Literal[True]]
    r: Incomplete
    text: Incomplete
    br: Typed[LineBreak, Literal[True]]
    fld: Typed[TextField, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        pPr: ParagraphProperties | None = None,
        endParaRPr: CharacterProperties | None = None,
        r: Incomplete | None = None,
        br: LineBreak | None = None,
        fld: TextField | None = None,
    ) -> None: ...

class GeomGuide(Serialisable):
    name: Incomplete
    fmla: Incomplete
    def __init__(self, name: Incomplete | None = None, fmla: Incomplete | None = None) -> None: ...

class GeomGuideList(Serialisable):
    gd: Incomplete
    def __init__(self, gd: Incomplete | None = None) -> None: ...

class PresetTextShape(Serialisable):
    prst: Typed[Set, Literal[False]]
    avLst: Typed[GeomGuideList, Literal[True]]
    def __init__(self, prst: Set, avLst: GeomGuideList | None = None) -> None: ...

class TextNormalAutofit(Serialisable):
    fontScale: Incomplete
    lnSpcReduction: Incomplete
    def __init__(self, fontScale: Incomplete | None = None, lnSpcReduction: Incomplete | None = None) -> None: ...

class RichTextProperties(Serialisable):
    tagname: str
    namespace: Incomplete
    rot: Incomplete
    spcFirstLastPara: Incomplete
    vertOverflow: Incomplete
    horzOverflow: Incomplete
    vert: Incomplete
    wrap: Incomplete
    lIns: Incomplete
    tIns: Incomplete
    rIns: Incomplete
    bIns: Incomplete
    numCol: Incomplete
    spcCol: Incomplete
    rtlCol: Incomplete
    fromWordArt: Incomplete
    anchor: Incomplete
    anchorCtr: Incomplete
    forceAA: Incomplete
    upright: Incomplete
    compatLnSpc: Incomplete
    prstTxWarp: Typed[PresetTextShape, Literal[True]]
    scene3d: Typed[Scene3D, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    noAutofit: Incomplete
    normAutofit: Incomplete
    spAutoFit: Incomplete
    flatTx: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        rot: Incomplete | None = None,
        spcFirstLastPara: Incomplete | None = None,
        vertOverflow: Incomplete | None = None,
        horzOverflow: Incomplete | None = None,
        vert: Incomplete | None = None,
        wrap: Incomplete | None = None,
        lIns: Incomplete | None = None,
        tIns: Incomplete | None = None,
        rIns: Incomplete | None = None,
        bIns: Incomplete | None = None,
        numCol: Incomplete | None = None,
        spcCol: Incomplete | None = None,
        rtlCol: Incomplete | None = None,
        fromWordArt: Incomplete | None = None,
        anchor: Incomplete | None = None,
        anchorCtr: Incomplete | None = None,
        forceAA: Incomplete | None = None,
        upright: Incomplete | None = None,
        compatLnSpc: Incomplete | None = None,
        prstTxWarp: Incomplete | None = None,
        scene3d: Incomplete | None = None,
        extLst: Incomplete | None = None,
        noAutofit: Incomplete | None = None,
        normAutofit: Incomplete | None = None,
        spAutoFit: Incomplete | None = None,
        flatTx: Incomplete | None = None,
    ) -> None: ...
