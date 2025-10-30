from _typeshed import SupportsWrite, Unused
from binascii import Incomplete
from collections.abc import Generator, Iterable
from contextlib import contextmanager
from typing import Final, Literal, NamedTuple, Protocol, runtime_checkable, type_check_only
from typing_extensions import Self, TypeAlias

from ._fonttools_shims import BasePen, _TTGlyphSet
from .drawing_primitives import (
    DeviceCMYK as DeviceCMYK,
    DeviceGray as DeviceGray,
    DeviceRGB as DeviceRGB,
    Number as Number,
    NumberClass as NumberClass,
    Point as Point,
    Transform as Transform,
    check_range as check_range,
    color_from_hex_string as color_from_hex_string,
    force_nodocument as force_nodocument,
    number_to_str as number_to_str,
)
from .enums import BlendMode, CompositingOperation, GradientSpreadMethod, GradientUnits, PathPaintRule
from .output import ResourceCatalog
from .pattern import Gradient
from .syntax import Name, Raw

@type_check_only
class _Serializable(Protocol):
    def serialize(self) -> str: ...

# Type check only type alias
_Primitive: TypeAlias = (
    _Serializable | str | bytes | bool | Number | list[_Primitive] | tuple[_Primitive, ...] | dict[Name, _Primitive] | None
)

def render_pdf_primitive(primitive: _Primitive) -> Raw: ...

class GradientPaint:
    __slots__ = ("gradient", "units", "gradient_transform", "apply_page_ctm", "skip_alpha", "spread_method")

    gradient: Gradient
    units: GradientUnits
    gradient_transform: Transform
    apply_page_ctm: bool
    skip_alpha: bool
    spread_method: GradientSpreadMethod

    def __init__(
        self,
        gradient: Gradient,
        units: GradientUnits | str = GradientUnits.USER_SPACE_ON_USE,
        gradient_transform: Transform | None = None,
        apply_page_ctm: bool = True,
        spread_method: GradientSpreadMethod | str | None = None,
    ) -> None: ...
    def emit_fill(self, resource_catalog, bbox: BoundingBox | None) -> str: ...
    def emit_stroke(self, resource_catalog, bbox: BoundingBox | None) -> str: ...
    def has_alpha(self) -> bool: ...

class BoundingBox(NamedTuple):
    x0: float
    y0: float
    x1: float
    y1: float

    @classmethod
    def empty(cls) -> Self: ...
    def is_valid(self) -> bool: ...
    @classmethod
    def from_points(cls, points: Iterable[Point]) -> Self: ...
    def merge(self, other: BoundingBox) -> BoundingBox: ...
    def transformed(self, tf: Transform) -> Self: ...
    def expanded(self, dx: float, dy: float | None = None) -> BoundingBox: ...
    def expanded_to_stroke(self, style: GraphicsStyle, row_norms: tuple[float, float] = (1.0, 1.0)) -> BoundingBox: ...
    def to_tuple(self) -> tuple[float, float, float, float]: ...
    def to_pdf_array(self) -> str: ...
    def corners(self) -> tuple[tuple[float, float], tuple[float, float], tuple[float, float], tuple[float, float]]: ...
    def project_interval_on_axis(self, x1: float, y1: float, x2: float, y2: float) -> tuple[float, float, float]: ...
    def max_distance_to_point(self, cx: float, cy: float) -> float: ...
    @property
    def width(self) -> float: ...
    @property
    def height(self) -> float: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class GraphicsStyle:
    ca: Incomplete
    BM: Incomplete
    CA: Incomplete
    SA: Incomplete
    LW: Incomplete
    LC: Incomplete
    LJ: Incomplete
    ML: Incomplete
    SMask: Incomplete

    INHERIT: Final[object]  # singleton value to indicate inheritance
    MERGE_PROPERTIES: Final[tuple[str, ...]]
    TRANSPARENCY_KEYS: Final[tuple[Name, ...]]
    PDF_STYLE_KEYS: Final[tuple[Name, ...]]

    @classmethod
    def merge(cls, parent: GraphicsStyle, child: GraphicsStyle) -> Self: ...
    def __init__(self) -> None: ...
    def __deepcopy__(self, memo: Unused) -> Self: ...
    @property
    def allow_transparency(self): ...
    @allow_transparency.setter
    def allow_transparency(self, new): ...
    @property
    def paint_rule(self): ...
    @paint_rule.setter
    def paint_rule(self, new) -> None: ...
    @property
    def auto_close(self): ...
    @auto_close.setter
    def auto_close(self, new) -> None: ...
    @property
    def intersection_rule(self): ...
    @intersection_rule.setter
    def intersection_rule(self, new) -> None: ...
    @property
    def fill_color(self): ...
    @fill_color.setter
    def fill_color(self, color) -> None: ...
    @property
    def fill_opacity(self): ...
    @fill_opacity.setter
    def fill_opacity(self, new) -> None: ...
    @property
    def stroke_color(self): ...
    @stroke_color.setter
    def stroke_color(self, color) -> None: ...
    @property
    def stroke_opacity(self): ...
    @stroke_opacity.setter
    def stroke_opacity(self, new) -> None: ...
    @property
    def blend_mode(self): ...
    @blend_mode.setter
    def blend_mode(self, value) -> None: ...
    @property
    def stroke_width(self): ...
    @stroke_width.setter
    def stroke_width(self, width) -> None: ...
    @property
    def stroke_cap_style(self): ...
    @stroke_cap_style.setter
    def stroke_cap_style(self, value) -> None: ...
    @property
    def stroke_join_style(self): ...
    @stroke_join_style.setter
    def stroke_join_style(self, value) -> None: ...
    @property
    def stroke_miter_limit(self): ...
    @stroke_miter_limit.setter
    def stroke_miter_limit(self, value) -> None: ...
    @property
    def stroke_dash_pattern(self): ...
    @stroke_dash_pattern.setter
    def stroke_dash_pattern(self, value) -> None: ...
    @property
    def stroke_dash_phase(self): ...
    @stroke_dash_phase.setter
    def stroke_dash_phase(self, value): ...
    @property
    def soft_mask(self): ...
    @soft_mask.setter
    def soft_mask(self, value) -> None: ...
    def serialize(self) -> Raw | None: ...
    def resolve_paint_rule(self) -> PathPaintRule: ...

@runtime_checkable
class Renderable(Protocol):
    def render(
        self, resource_registry: ResourceCatalog, style: GraphicsStyle, last_item: Renderable, initial_point: Point
    ) -> tuple[str, Renderable, Point]: ...
    def bounding_box(self, start: Point) -> tuple[BoundingBox, Point]: ...

class Move(NamedTuple):
    pt: Point
    @property
    def end_point(self) -> Point: ...
    def bounding_box(self, start: Unused) -> tuple[BoundingBox, Point]: ...
    def render(
        self, resource_registry: ResourceCatalog, style: GraphicsStyle, last_item: Renderable, initial_point: Point
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class RelativeMove(NamedTuple):
    pt: Point
    def bounding_box(self, start: Point) -> tuple[BoundingBox, Point]: ...
    def render(
        self, resource_registry: ResourceCatalog, style: GraphicsStyle, last_item: Renderable, initial_point: Point
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class Line(NamedTuple):
    pt: Point
    @property
    def end_point(self) -> Point: ...
    def bounding_box(self, start: Point) -> tuple[BoundingBox, Point]: ...
    def render(
        self, resource_registry: ResourceCatalog, style: GraphicsStyle, last_item: Renderable, initial_point: Point
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class RelativeLine(NamedTuple):
    pt: Point
    def bounding_box(self, start: Point) -> tuple[BoundingBox, Point]: ...
    def render(
        self, resource_registry: ResourceCatalog, style: GraphicsStyle, last_item: Renderable, initial_point: Point
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class HorizontalLine(NamedTuple):
    x: Number
    def bounding_box(self, start: Point) -> tuple[BoundingBox, Point]: ...
    def render(
        self, resource_registry: ResourceCatalog, style: GraphicsStyle, last_item: Renderable, initial_point: Point
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class RelativeHorizontalLine(NamedTuple):
    x: Number
    def bounding_box(self, start: Point) -> tuple[BoundingBox, Point]: ...
    def render(
        self, resource_registry: ResourceCatalog, style: GraphicsStyle, last_item: Renderable, initial_point: Point
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class VerticalLine(NamedTuple):
    y: Number
    def bounding_box(self, start: Point) -> tuple[BoundingBox, Point]: ...
    def render(
        self, resource_registry: ResourceCatalog, style: GraphicsStyle, last_item: Renderable, initial_point: Point
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class RelativeVerticalLine(NamedTuple):
    y: Number
    def bounding_box(self, start: Point) -> tuple[BoundingBox, Point]: ...
    def render(
        self, resource_registry: ResourceCatalog, style: GraphicsStyle, last_item: Renderable, initial_point: Point
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class BezierCurve(NamedTuple):
    c1: Point
    c2: Point
    end: Point
    @property
    def end_point(self): ...
    def bounding_box(self, start: Point) -> tuple[BoundingBox, Point]: ...
    def render(
        self, resource_registry: ResourceCatalog, style: GraphicsStyle, last_item: Renderable, initial_point: Point
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class RelativeBezierCurve(NamedTuple):
    c1: Point
    c2: Point
    end: Point
    def bounding_box(self, start: Point) -> tuple[BoundingBox, Point]: ...
    def render(
        self, resource_registry: ResourceCatalog, style: GraphicsStyle, last_item: Renderable, initial_point: Point
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class QuadraticBezierCurve(NamedTuple):
    ctrl: Point
    end: Point
    @property
    def end_point(self) -> Point: ...
    def to_cubic_curve(self, start_point: Point) -> BezierCurve: ...
    def bounding_box(self, start: Point) -> tuple[BoundingBox, Point]: ...
    def render(
        self, resource_registry: ResourceCatalog, style: GraphicsStyle, last_item: Renderable, initial_point: Point
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class RelativeQuadraticBezierCurve(NamedTuple):
    ctrl: Point
    end: Point
    def bounding_box(self, start: Point) -> tuple[BoundingBox, Point]: ...
    def render(
        self, resource_registry: ResourceCatalog, style: GraphicsStyle, last_item: Renderable, initial_point: Point
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class Arc(NamedTuple):
    radii: Point
    rotation: Number
    large: bool
    sweep: bool
    end: Point
    @staticmethod
    def subdivide_sweep(sweep_angle: float) -> Generator[tuple[Point, Point, Point]]: ...
    def bounding_box(self, start: Point) -> tuple[BoundingBox, Point]: ...
    def render(
        self, resource_registry: ResourceCatalog, style: GraphicsStyle, last_item: Renderable, initial_point: Point
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class RelativeArc(NamedTuple):
    radii: Point
    rotation: Number
    large: bool
    sweep: bool
    end: Point
    def bounding_box(self, start: Point) -> tuple[BoundingBox, Point]: ...
    def render(
        self, resource_registry: ResourceCatalog, style: GraphicsStyle, last_item: Renderable, initial_point: Point
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class Rectangle(NamedTuple):
    org: Point
    size: Point
    def bounding_box(self, start: Point | None = None) -> tuple[BoundingBox, Point]: ...
    def render(
        self, resource_registry: ResourceCatalog, style: GraphicsStyle, last_item: Renderable, initial_point: Point
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class RoundedRectangle(NamedTuple):
    org: Point
    size: Point
    corner_radii: Point
    def bounding_box(self, start: Point) -> tuple[BoundingBox, Point]: ...
    def render(
        self, resource_registry: ResourceCatalog, style: GraphicsStyle, last_item: Renderable, initial_point: Point
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class Ellipse(NamedTuple):
    radii: Point
    center: Point
    def bounding_box(self, start: Point) -> tuple[BoundingBox, Point]: ...
    def render(
        self, resource_registry: ResourceCatalog, style: GraphicsStyle, last_item: Renderable, initial_point: Point
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class TextRun(NamedTuple):
    text: str
    family: str
    emphasis: str
    size: float
    dx: float = 0.0
    dy: float = 0.0
    abs_x: float | None = None
    abs_y: float | None = None
    transform: Transform | None = None
    run_style: GraphicsStyle | None = None

class Text(NamedTuple):
    x: float
    y: float
    text_runs: tuple[TextRun, ...]
    text_anchor: Literal["start", "middle", "end"] = "start"
    def bounding_box(self, start: Point) -> tuple[BoundingBox, Point]: ...
    def render(
        self, resource_registry: ResourceCatalog, style: GraphicsStyle, last_item: Renderable, initial_point: Point
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class ImplicitClose(NamedTuple):
    def bounding_box(self, start: Point) -> tuple[BoundingBox, Point]: ...
    def render(
        self, resource_registry: ResourceCatalog, style: GraphicsStyle, last_item: Renderable, initial_point: Point
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class Close(NamedTuple):
    def bounding_box(self, start: Point) -> tuple[BoundingBox, Point]: ...
    def render(
        self, resource_registry: ResourceCatalog, style: GraphicsStyle, last_item: Renderable, initial_point: Point
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class DrawingContext:
    def __init__(self) -> None: ...
    def add_item(self, item: GraphicsContext | PaintedPath | PaintComposite, _copy: bool = True) -> None: ...
    def render(
        self, resource_registry: ResourceCatalog, first_point: Point, scale: float, height: float, starting_style: GraphicsStyle
    ) -> None: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        first_point: Point,
        scale: float,
        height: float,
        starting_style: GraphicsStyle,
        debug_stream: SupportsWrite[str],
    ) -> None: ...

class PaintedPath:
    def __init__(self, x: float = 0, y: float = 0) -> None: ...
    def __deepcopy__(self, memo) -> Self: ...
    @property
    def style(self) -> GraphicsStyle: ...
    @property
    def transform(self) -> Transform | None: ...
    @transform.setter
    def transform(self, tf: Transform) -> None: ...
    @property
    def auto_close(self) -> bool: ...
    @auto_close.setter
    def auto_close(self, should: bool) -> None: ...
    @property
    def paint_rule(self) -> PathPaintRule: ...
    @paint_rule.setter
    def paint_rule(self, style: PathPaintRule) -> None: ...
    @property
    def clipping_path(self): ...
    @clipping_path.setter
    def clipping_path(self, new_clipath) -> None: ...
    def get_graphics_context(self) -> GraphicsContext: ...
    @contextmanager
    def transform_group(self, transform: Transform) -> Generator[Self]: ...
    def add_path_element(self, item, _copy: bool = True) -> None: ...
    def remove_last_path_element(self) -> None: ...
    def rectangle(self, x: Number, y: Number, w: Number, h: Number, rx: Number = 0, ry: Number = 0) -> Self: ...
    def circle(self, cx: Number, cy: Number, r: Number) -> Self: ...
    def ellipse(self, cx: Number, cy: Number, rx: Number, ry: Number) -> Self: ...
    def move_to(self, x: Number, y: Number) -> Self: ...
    def move_relative(self, x: Number, y: Number) -> Self: ...
    def line_to(self, x: Number, y: Number) -> Self: ...
    def line_relative(self, dx: Number, dy: Number) -> Self: ...
    def horizontal_line_to(self, x: Number) -> Self: ...
    def horizontal_line_relative(self, dx: Number) -> Self: ...
    def vertical_line_to(self, y: Number) -> Self: ...
    def vertical_line_relative(self, dy: Number) -> Self: ...
    def curve_to(self, x1: Number, y1: Number, x2: Number, y2: Number, x3: Number, y3: Number) -> Self: ...
    def curve_relative(self, dx1: Number, dy1: Number, dx2: Number, dy2: Number, dx3: Number, dy3: Number) -> Self: ...
    def quadratic_curve_to(self, x1: Number, y1: Number, x2: Number, y2: Number) -> Self: ...
    def quadratic_curve_relative(self, dx1: Number, dy1: Number, dx2: Number, dy2: Number) -> Self: ...
    def arc_to(
        self, rx: Number, ry: Number, rotation: Number, large_arc: Number, positive_sweep: Number, x: Number, y: Number
    ) -> Self: ...
    def arc_relative(
        self, rx: Number, ry: Number, rotation: Number, large_arc: Number, positive_sweep: Number, dx: Number, dy: Number
    ) -> Self: ...
    def text(
        self,
        x: float,
        y: float,
        content: str,
        *,
        font_family: str = "helvetica",
        font_style: Literal["", "B", "I", "BI"] = "",
        font_size: float = 12.0,
        text_anchor: Literal["start", "middle", "end"] = "start",
    ) -> Self: ...
    def close(self) -> None: ...
    def bounding_box(self, start: Point, expand_for_stroke: bool = True) -> tuple[BoundingBox, Point]: ...
    def render(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str] | None = None,
        pfx: str | None = None,
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class ClippingPath(PaintedPath):
    paint_rule: PathPaintRule
    def __init__(self, x: float = 0, y: float = 0) -> None: ...
    def render(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str] | None = None,
        pfx: str | None = None,
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class GraphicsContext:
    style: GraphicsStyle
    path_items: list[Renderable]

    def __init__(self) -> None: ...
    def __deepcopy__(self, memo) -> Self: ...
    @property
    def transform(self) -> Transform | None: ...
    @transform.setter
    def transform(self, tf: Transform) -> None: ...
    @property
    def clipping_path(self) -> ClippingPath | None: ...
    @clipping_path.setter
    def clipping_path(self, new_clipath: ClippingPath) -> None: ...
    def add_item(self, item: Renderable, _copy: bool = True) -> None: ...
    def remove_last_item(self) -> None: ...
    def merge(self, other_context: GraphicsContext) -> None: ...
    def build_render_list(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str] | None = None,
        pfx: str | None = None,
        _push_stack: bool = True,
    ) -> tuple[list[str], Renderable, Point]: ...
    def bounding_box(
        self, start: Point, style: GraphicsStyle | None = None, expand_for_stroke: bool = True, transformed: bool = True
    ) -> tuple[BoundingBox, Point]: ...
    def render(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str] | None = None,
        pfx: str | None = None,
        _push_stack: bool = True,
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
        _push_stack: bool = True,
    ) -> tuple[str, Renderable, Point]: ...

class PaintSoftMask:
    __slots__ = ("mask_path", "invert", "resources", "use_luminosity", "object_id", "matrix")

    mask_path: PaintedPath | GraphicsContext
    invert: bool
    use_luminosity: bool
    resources: set[Incomplete]
    object_id: int
    matrix: Transform

    def __init__(
        self,
        mask_path: PaintedPath | GraphicsContext,
        invert: bool = False,
        use_luminosity: bool = False,
        matrix: Transform = ...,
    ) -> None: ...
    def serialize(self) -> str: ...
    def get_bounding_box(self) -> tuple[float, float, float, float]: ...
    def get_resource_dictionary(self, gfxstate_objs_per_name, pattern_objs_per_name) -> str: ...
    def render(self, resource_registry: ResourceCatalog) -> str: ...
    @staticmethod
    def coverage_white(node: PaintedPath | GraphicsContext) -> PaintedPath | GraphicsContext: ...
    @staticmethod
    def alpha_layers_from(node: PaintedPath | GraphicsContext) -> GraphicsContext | None: ...
    @classmethod
    def from_AB(
        cls,
        A: GraphicsContext | None,
        B: PaintedPath | GraphicsContext,
        invert: bool,
        registry,
        region_bbox: BoundingBox | None = None,
    ) -> Self: ...

def clone_structure(node): ...

class PaintComposite:
    backdrop: PaintedPath | GraphicsContext
    source: PaintedPath | GraphicsContext
    mode: CompositingOperation

    def __init__(
        self, backdrop: PaintedPath | GraphicsContext, source: PaintedPath | GraphicsContext, operation: CompositingOperation
    ) -> None: ...
    def render(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str] | None = None,
        pfx: str | None = None,
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class PaintBlendComposite:
    __slots__ = ("backdrop", "source", "blend_mode", "_form_index")

    backdrop: GraphicsContext | PaintedPath
    source: GraphicsContext | PaintedPath
    blend_mode: BlendMode
    _form_index: int | None

    def __init__(
        self, backdrop: GraphicsContext | PaintedPath, source: GraphicsContext | PaintedPath, blend_mode: BlendMode
    ) -> None: ...
    def render(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str] | None = None,
        pfx: str | None = None,
    ) -> tuple[str, Renderable, Point]: ...
    def render_debug(
        self,
        resource_registry: ResourceCatalog,
        style: GraphicsStyle,
        last_item: Renderable,
        initial_point: Point,
        debug_stream: SupportsWrite[str],
        pfx: str,
    ) -> tuple[str, Renderable, Point]: ...

class PathPen(BasePen):
    pdf_path: PaintedPath
    last_was_line_to: bool
    first_is_move: bool | None

    def __init__(self, pdf_path: PaintedPath, glyphSet: _TTGlyphSet | None = ...) -> None: ...
    def arcTo(self, rx, ry, rotation, arc, sweep, end) -> None: ...

class GlyphPathPen(PathPen): ...
