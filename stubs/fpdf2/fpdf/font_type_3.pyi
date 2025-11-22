from _typeshed import Incomplete
from collections.abc import Iterable
from logging import Logger
from typing import Final, Literal

from fpdf.enums import BlendMode

from ._fonttools_shims import CompositeMode, Paint, PaintFormat, VarStoreInstancer
from .drawing import BoundingBox, DeviceRGB, GraphicsContext, PaintedPath, Transform
from .fonts import TTFFont
from .fpdf import FPDF

LOGGER: Logger

PAINT_VAR_MAPPING: Final[dict[PaintFormat, PaintFormat]]

class Type3FontGlyph:
    __slots__ = ("obj_id", "glyph_id", "unicode", "glyph_name", "glyph_width", "glyph", "_glyph_bounds")

    obj_id: int
    glyph_id: int
    unicode: tuple[Incomplete, ...]
    glyph_name: str
    glyph_width: int
    glyph: str
    _glyph_bounds: tuple[int, int, int, int]

    def __init__(self) -> None: ...
    def __hash__(self) -> int: ...

class Type3Font:
    i: int
    type: str
    fpdf: FPDF
    base_font: TTFFont
    upem: float
    scale: float
    images_used: set[Incomplete]
    graphics_style_used: set[Incomplete]
    patterns_used: set[Incomplete]
    glyphs: list[Type3FontGlyph]

    def __init__(self, fpdf: FPDF, base_font: TTFFont) -> None: ...
    def get_notdef_glyph(self, glyph_id: int) -> Type3FontGlyph: ...
    def get_space_glyph(self, glyph_id: int) -> Type3FontGlyph: ...
    def load_glyphs(self) -> None: ...
    def add_glyph(self, glyph_name: str, char_id: int) -> None: ...
    @classmethod
    def get_target_ppem(cls, font_size_pt: int) -> int: ...
    def load_glyph_image(self, glyph: Type3FontGlyph) -> None: ...
    def glyph_exists(self, glyph_name: str) -> bool: ...

class SVGColorFont(Type3Font): ...

class COLRFont(Type3Font):
    colrv0_glyphs: list[Incomplete]
    colrv1_glyphs: list[Incomplete]
    version: Incomplete
    colrv1_clip_boxes: dict[Incomplete, Incomplete]
    colr_var_instancer: Incomplete | None
    colr_var_index_map: Incomplete | None
    palette: Incomplete | None

    def __init__(self, fpdf: FPDF, base_font: TTFFont, palette_index: int = 0) -> None: ...
    def metric_bbox(self) -> BoundingBox: ...
    def get_color(self, color_index: int, alpha=1) -> DeviceRGB: ...
    def draw_glyph_colrv0(self, layers: Iterable[Incomplete]) -> GraphicsContext: ...
    def draw_glyph_colrv1(self, glyph_name: str) -> GraphicsContext: ...
    def draw_colrv1_paint(
        self,
        paint: Paint,
        parent: GraphicsContext,
        target_path: PaintedPath | None = None,
        ctm: Transform | None = None,
        visited_glyphs: set[Incomplete] | None = None,
    ) -> tuple[GraphicsContext, PaintedPath | None]: ...
    def get_paint_surface(self) -> PaintedPath: ...
    @classmethod
    def get_composite_mode(
        cls, composite_mode: CompositeMode
    ) -> tuple[Literal["Compositing"], CompositeMode] | tuple[Literal["Blend"], BlendMode]: ...

class VarTableWrapper:
    def __init__(self, wrapped, instancer: VarStoreInstancer, var_index_map=None, format_override: int | None = None) -> None: ...
    def __getattr__(self, attr_name: str): ...

class CBDTColorFont(Type3Font): ...

class SBIXColorFont(Type3Font):
    def get_strike_index(self) -> int: ...

def get_color_font_object(fpdf: FPDF, base_font: TTFFont, palette_index: int = 0) -> Type3Font | None: ...
